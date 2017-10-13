# encoding: utf-8

import requests

url = "http://127.0.0.1:8888/postreceive"

payload = '{"ref": "refs/heads/master", "user_id": 38, "object_kind": "push", "repository": {"git_ssh_url": "git@git.hypers.com:hfa/adtracker.git", "name": "adtracker", "url": "git@git.hypers.com:hfa/adtracker.git", "git_http_url": "https://git.hypers.com/hfa/adtracker.git", "visibility_level": 0, "homepage": "https://git.hypers.com/hfa/adtracker", "description": "adtracker"}, "event_name": "push", "commits": [{"added": [], "author": {"name": "jejayhe", "email": "hjjscofield@163.com"}, "url": "https://git.hypers.com/hfa/adtracker/commit/98ca62e0c42c09351d632dc7102b52073b90dab9", "timestamp": "2017-10-12T18:43:43+08:00", "message": "fix: \\u5bfc\\u5165\\u521b\\u610f\\u81ea\\u5b9a\\u4e49\\u5c5e\\u6027bug\\n", "removed": [], "modified": ["apps/campaigns/views/batch_import.py"], "id": "98ca62e0c42c09351d632dc7102b52073b90dab9"}, {"added": [], "author": {"name": "drinks", "email": "drinksober@foxmail.com"}, "url": "https://git.hypers.com/hfa/adtracker/commit/55ba1052a4fb984ee292cda8f678c1cdc94541be", "timestamp": "2017-10-10T15:03:56+08:00", "message": "Merge branch \'hotfix/v2.1.9\'\\n", "removed": [], "modified": ["apps/api4custom/dmp_api.py"], "id": "55ba1052a4fb984ee292cda8f678c1cdc94541be"}, {"added": [], "author": {"name": "drinks", "email": "drinksober@foxmail.com"}, "url": "https://git.hypers.com/hfa/adtracker/commit/048ec02297a5d58d8354ca583768ca8ce8b6cfc3", "timestamp": "2017-10-10T15:03:46+08:00", "message": "fix: \\u4fee\\u590ddmp\\u63a5\\u53e3\\n", "removed": [], "modified": ["apps/api4custom/dmp_api.py"], "id": "048ec02297a5d58d8354ca583768ca8ce8b6cfc3"}], "after": "98ca62e0c42c09351d632dc7102b52073b90dab9", "project": {"git_ssh_url": "git@git.hypers.com:hfa/adtracker.git", "description": "adtracker", "default_branch": "master", "web_url": "https://git.hypers.com/hfa/adtracker", "ssh_url": "git@git.hypers.com:hfa/adtracker.git", "visibility_level": 0, "name": "adtracker", "url": "git@git.hypers.com:hfa/adtracker.git", "namespace": "hfa", "git_http_url": "https://git.hypers.com/hfa/adtracker.git", "avatar_url": null, "http_url": "https://git.hypers.com/hfa/adtracker.git", "path_with_namespace": "hfa/adtracker", "homepage": "https://git.hypers.com/hfa/adtracker"}, "checkout_sha": "98ca62e0c42c09351d632dc7102b52073b90dab9", "total_commits_count": 3, "user_avatar": "https://secure.gravatar.com/avatar/51de8a9d2e55eeae730e24339101e9df?s=80&d=identicon", "message": null, "project_id": 366, "user_name": "drinks", "user_email": "drinks.huang@hypers.com", "before": "048ec02297a5d58d8354ca583768ca8ce8b6cfc3"}'

headers = {
    'content-type': "application/json",
    'x-gitlab-event': "push",
    'x-github-delivery': "845da0f6-af61-11e7-9409-20c02a1b0517",
    'cache-control': "no-cache",
    'postman-token': "9d6f88ea-44f0-aa1d-6b83-31acf4c0ccae"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
