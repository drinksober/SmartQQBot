# encoding: utf-8
from __future__ import division, unicode_literals

import json
import hmac
import hashlib
import collections
import logging
import six
from flask import abort, request

logger = logging.getLogger('webhook')
logger.setLevel('DEBUG')
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
fh = logging.FileHandler('log')
fh.setFormatter(formatter)
logger.addHandler(fh)


class Webhook(object):
    def __init__(self, secret=None):
        self._hooks = collections.defaultdict(list)
        if secret is not None and not isinstance(secret, six.binary_type):
            secret = secret.encode('utf-8')
        self.logger = logger
        self._secret = secret

    def hook(self, event_type='push'):
        """
        Registers a function as a hook. Multiple hooks can be registered for a given type, but the
        order in which they are invoke is unspecified.

        :param event_type: The event type this hook will be invoked for.
        """

        def decorator(func):
            self._hooks[event_type].append(func)
            return func

        return decorator

    def _format_event(self, event_type, data):
        try:
            return EVENT_DESCRIPTIONS[event_type].format(**data)
        except KeyError:
            return event_type

    def _get_digest(self):
        """Return message digest if a secret key was provided"""

        return hmac.new(self._secret, request.data,
                        hashlib.sha1).hexdigest() if self._secret else None

    def view(self):
        """Callback from Flask"""

        digest = self._get_digest()
        event = request.headers.get('X-Gitlab-Event') or request.headers.get(
            'X-Github-Event')
        if not event:
            abort(400, 'Missing header: ' + 'X-Github-Event')

        if digest is not None:
            sig_parts = _get_header('X-Hub-Signature').split('=', 1)
            if not isinstance(digest, six.text_type):
                digest = six.text_type(digest)

            if (len(sig_parts) < 2 or sig_parts[0] != 'sha1'
                    or not hmac.compare_digest(sig_parts[1], digest)):
                abort(400, 'Invalid signature')

        data = request.json or json.loads(request.form['payload'])
        logger.debug(data)

        if data is None:
            abort(400, 'Request body must contain json')

        for hook in self._hooks.get(event, []):
            hook(data)

        return '', 204


EVENT_DESCRIPTIONS = {
    'commit_comment':
    '{comment[user][login]} commented on '
    '{comment[commit_id]} in {repository[full_name]}',
    'create':
    '{sender[login]} created {ref_type} ({ref}) in '
    '{repository[full_name]}',
    'delete':
    '{sender[login]} deleted {ref_type} ({ref}) in '
    '{repository[full_name]}',
    'deployment':
    '{sender[login]} deployed {deployment[ref]} to '
    '{deployment[environment]} in {repository[full_name]}',
    'deployment_status':
    'deployment of {deployement[ref]} to '
    '{deployment[environment]} '
    '{deployment_status[state]} in '
    '{repository[full_name]}',
    'fork':
    '{forkee[owner][login]} forked {forkee[name]}',
    'gollum':
    '{sender[login]} edited wiki pages in {repository[full_name]}',
    'issue_comment':
    '{sender[login]} commented on issue #{issue[number]} '
    'in {repository[full_name]}',
    'issues':
    '{sender[login]} {action} issue #{issue[number]} in '
    '{repository[full_name]}',
    'member':
    '{sender[login]} {action} member {member[login]} in '
    '{repository[full_name]}',
    'membership':
    '{sender[login]} {action} member {member[login]} to team '
    '{team[name]} in {repository[full_name]}',
    'page_build':
    '{sender[login]} built pages in {repository[full_name]}',
    'ping':
    'ping from {sender[login]}',
    'public':
    '{sender[login]} publicized {repository[full_name]}',
    'pull_request':
    '{sender[login]} {action} pull #{pull_request[number]} in '
    '{repository[full_name]}',
    'pull_request_review':
    '{sender[login]} {action} {review[state]} review on pull #{pull_request[number]} in '
    '{repository[full_name]}',
    'pull_request_review_comment':
    '{comment[user][login]} {action} comment '
    'on pull #{pull_request[number]} in '
    '{repository[full_name]}',
    'push':
    '{pusher[name]} pushed {ref} in {repository[full_name]}',
    'release':
    '{release[author][login]} {action} {release[tag_name]} in '
    '{repository[full_name]}',
    'repository':
    '{sender[login]} {action} repository '
    '{repository[full_name]}',
    'status':
    '{sender[login]} set {sha} status to {state} in '
    '{repository[full_name]}',
    'team_add':
    '{sender[login]} added repository {repository[full_name]} to '
    'team {team[name]}',
    'watch':
    '{sender[login]} {action} watch in repository '
    '{repository[full_name]}'
}
