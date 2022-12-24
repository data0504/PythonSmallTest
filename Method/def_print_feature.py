test_str = 'test'

# 一般顯示
print(f'{test_str}')

# 字串總為50個，可自定義 符號
# 物件放置最左邊，剩餘 自定義符號 填滿。
print(f'{test_str:#<50}')

# 物件放置最右邊，剩餘 自定義符號 填滿。
print(f'{test_str:_>50}')

# 物件放置中間，剩餘 自定義符號 填滿。
print(f'{test_str:.^50}')

# 物件放置中間，剩餘 自定義符號 填滿。
print(f'{test_str:=^50}')