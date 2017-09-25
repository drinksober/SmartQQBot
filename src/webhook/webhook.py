# coding: utf-8
from smart_qq_bot.httpserver import webhook

config = {"baxterthehacker/public-repo": {'groups': [u"锄禾日当午"], 'friends': ['746058508']}}
groupById = {}
friendById = {}


@webhook.hook()
def on_push(data):
    from smart_qq_bot.app import bot
    # 发送一条群消息
    global groupById
    global friendById
    if not groupById:
        groupById = bot.get_group_list_with_group_code()
        groupById = {x['name']: x['gid'] for x in groupById}
    if not friendById:
        friendById = {y['account']: x for x, y in bot.friend_uin_list.items()}
    full_name = data['repository']['full_name']
    commit = data['head_commit']
    commit = commit['id'][-7:] + ': ' + commit['message']
    text = '\n'.join((full_name, commit))
    _config = config[full_name]
    for group in _config.get('groups', []):
        bot.send_group_msg(text, groupById[group], 1)
    for friend in _config.get('friends', []):
        bot.send_friend_msg(text, friendById[friend], 1)
