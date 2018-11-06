' Use filter '


def is_palindrome(n):
    s = list(str(n))
    # 0 = -1, 1 = -2, 2 = -3
    i = 0
    while i < len(s)/2:
        # print(s[i], s[-(i+1)])
        if s[i] != s[-(i+1)]:
            return False
        i += 1

    return True


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# print(is_palindrome(123))
# print(is_palindrome(12321))
