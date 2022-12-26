from itertools import groupby
from operator import itemgetter

test_json_str = [{
    "id": "111",
    "PasswordStr": "111",
    "initToken": 0,
    "SignUpTime": 1667704450.4023623,
    "SignInTime": 1667704483.0912616,
    "pay": 400,
    "getCoin": 900,
    "rebate": 5.0
}]

for key, value in groupby(test_json_str, itemgetter('id')):
    print(key)
    for i in list(value):
        print(i["PasswordStr"])
        print(i["initToken"])
        print(i["SignUpTime"])
        print(i["SignInTime"])
        print(i["pay"])
        print(i["getCoin"])
        print(i["rebate"])