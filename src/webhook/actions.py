# coding: utf-8
from .base import Webhook
from qqbot.mysocketserver import Query

webhook = Webhook()

config = {
    'default_groups': [],
    'default_friends': [u'398869368'],
    'hfa/adtracker': ['666188124'],
    'hfa/adtracker-fe': ['666188124'],
    'BronzeKing/ssrd': ['656991593'],
    'BronzeKing/ssrd-fe': ['656991593'],
    'BronzeKing/ssrd-prototype': ['656991593'],
}
default_groups = config['default_groups']
default_friends = config['default_friends']


@webhook.hook()
def on_push(data):
    # 发送一条群消息
    if not isinstance(data, dict):
        import json
        data = json.loads(data)
    full_name = data['repository']['full_name']
    name = '/'.join(full_name.split('/')[1:])
    commit = data['head_commit']
    commit = commit['id'][-7:] + ': ' + commit['message']
    text = '\n'.join((full_name, commit))
    _config = config.get(full_name, {}) or config.get(name, {})
    for group in _config.get('groups', default_groups):
        command = u'send group {} {}'.format(group, text).encode('utf8')
        Query('127.0.0.1', '8188', command)
    for friend in _config.get('friends', default_friends):
        command = u'send buddy {} {}'.format(friend, text).encode('utf8')
        Query('127.0.0.1', '8188', command)
