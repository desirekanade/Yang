def filter_strings(lambda_func, string_array):
    return list(filter(lambda_func, string_array))

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

filtered_no_spaces = filter_strings(lambda x: ' ' not in x, strings)
print("no spaces", filtered_no_spaces)

# 排除以字母 'a' 开头的字符串
filtered_no_a = filter_strings(lambda x: not x.startswith('a'), strings)
print("no a", filtered_no_a)

# 排除长度小于5的字符串
filtered_min_length = filter_strings(lambda x: len(x) >= 5, strings)
print("min 5", filtered_min_length)