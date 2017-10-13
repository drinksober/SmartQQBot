# coding: utf-8
from .base import Webhook
from qqbot.mysocketserver import Query

webhook = Webhook()

config = {
    'default_groups': [],
    'default_friends': [u'398869368'],
    'hfa/adtracker': {'group': ['666188124']},
    'hfa/adtracker-fe': {'group': ['666188124']},
    'BronzeKing/ssrd': {'group': ['656991593']},
    'BronzeKing/ssrd-fe': {'group': ['656991593']},
    'BronzeKing/ssrd-prototye': {'group': ['656991593']},
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
        commit = data['head_commit']
        commit = commit['id'][-7:] + ': ' + commit['message']
        text = '\n'.join((full_name, commit))
    else:
        full_name = data['project']['path_with_namespace']
        commit = data['commits'][0]
        commit = commit['id'][-7:] + ': ' + commit['message']
        text = '\n'.join((full_name, commit))
    name = '/'.join(full_name.split('/')[1:])   # project name
    _config = config.get(full_name, {}) or config.get(name, {})
    for group in _config.get('groups', default_groups):
        command = u'send group {} {}'.format(group, text).encode('utf8')
        Query('127.0.0.1', '8188', command)
    for friend in _config.get('friends', default_friends):
        command = u'send buddy {} {}'.format(friend, text).encode('utf8')
        Query('127.0.0.1', '8188', command)
