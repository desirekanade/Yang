def test(s):
    # 将字符串转换为小写并移除空格
    s = s.replace(" ", "").lower()
    # 检查字符串与其反转是否相等
    return s == s[::-1]

# test
print(test("A man a plan a canal Panama"))
print(test("Hello, World!"))