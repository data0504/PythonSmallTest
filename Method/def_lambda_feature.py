test_number = 1

def square(x):
    return x * 2

# 一般使用方法
method_page_1 = square(test_number)
result = method_page_1
print(result)

# 隱匿韓式初階用法
method_page_2 = lambda x: x * 2  # 宣告 匿名函式
result = method_page_2(test_number)  # 結果
print(result)  # 顯示結果

# 隱匿韓式進階用法
if ((lambda x: x * 2)(test_number)) == 2:
    print(f'{((lambda x: x * 2)(test_number))}')