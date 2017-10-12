# coding: utf-8
from .github import Webhook
from qqbot.mysocketserver import Query

webhook = Webhook()

config = {'default_groups': [u'青铜王者']}
default_groups = config['default_groups']


@webhook.hook()
def on_push(data):
    # 发送一条群消息
    full_name = data['repository']['full_name']
    commit = data['head_commit']
    commit = commit['id'][-7:] + ': ' + commit['message']
    text = '\n'.join((full_name, commit))
    _config = config.get(full_name, {})
    for group in _config.get('groups', default_groups):
        Query('send', 'group', group, text)
    for friend in _config.get('friends', []):
        Query('send', 'buddy', friend, text)
