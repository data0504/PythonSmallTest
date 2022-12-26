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

print(f'{"groupby_itemgetter":=^50}')
for key, value in groupby(test_json_str, itemgetter('id')):
    print(key)
    for i in list(value):
        print(i["PasswordStr"])
        print(i["initToken"])
        print(i["initToken"])
        print(i["SignInTime"])
        print(i["SignInTime"])
        print(i["pay"])
        print(i["getCoin"])
        print(i["rebate"])


print(f'{"itemgetter":=^50}')
for row in test_json_str:
    print(str(itemgetter('id')(row)))

    print(str(itemgetter('PasswordStr')(row)))
    print(str(itemgetter('initToken')(row)))
    print(str(itemgetter('SignUpTime')(row)))
    print(str(itemgetter('SignInTime')(row)))
    print(str(itemgetter('pay')(row)))
    print(str(itemgetter('getCoin')(row)))
    print(str(itemgetter('rebate')(row)))