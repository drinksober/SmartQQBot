# coding: utf-8
from .base import Webhook
from qqbot.mysocketserver import Query

webhook = Webhook()

config = {
    'default_groups': [],
    'default_friends': [u'398869368'],
    'hfa/adtracker': {'groups': ['666188124']},
    'hfa/adtracker-fe': {'groups': ['666188124']},
    'BronzeKing/ssrd': {'groups': ['656991593']},
    'BronzeKing/ssrd-fe': {'groups': ['656991593']},
    'BronzeKing/ssrd-prototye': {'groups': ['656991593']},
}
default_groups = config['default_groups']
default_friends = config['default_friends']


@webhook.hook()
def on_push(data):
    # 发送一条群消息
    if not isinstance(data, dict):
        import json
        data = json.loads(data)
    if 'head_commit' in data:  # github
        full_name = data['repository']['full_name']
        commits = data['commits']
    else:
        full_name = data['project']['path_with_namespace']
        commits = data['commits']
    commit = '\n'.join(commit['id'][-7:] + ': ' + commit['message'] for commit in commits)
    full_name = '[{}] {}个新的提交'.format(full_name, len(commits))
    author = commits[0]['author']['name']
    text = '\n'.join((author, full_name, commit))
    name = '/'.join(full_name.split('/')[1:])   # project name
    _config = config.get(full_name, {}) or config.get(name, {})
    for group in _config.get('groups', default_groups):
        command = u'send group {} {}'.format(group, text).encode('utf8')
        Query('127.0.0.1', '8188', command)
    for friend in _config.get('friends', default_friends):
        command = u'send buddy {} {}'.format(friend, text).encode('utf8')
        Query('127.0.0.1', '8188', command)
