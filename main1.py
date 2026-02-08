# lst = [1, 2, 3, "1234", ["abc", "def"]]
# #      0  1  2     3     4
# #      -5 -4 -3   -2    -1
# print(lst)
# lst[0] = "a"
# lst.pop(0)
# lst.remove("1234")
# print(lst)


# lst45qw = ["a", "bc", 100]
# for qwertyu in lst45qw:
#     print(qwertyu)

# a = [100, 20]
# for i in a:
#     i = i*2
#     print(i)

# a.append("1")
# a.insert(1, "q")
# print(a)

# string = "abc" # 不可变
# string_2 = string
# print(string_2 is string)
# string_2 = string_2.upper()
# print(string_2 is string)
# print(string)

# lst = ["a", "b", "c"] # 可变
# lst_2 = lst
# print(lst_2 is lst)
# lst_2.insert(0, "1")
# print(lst_2 is lst)
# print(lst)

# mylist = [1, "10", "abc", 2]
# mylist.pop(1) #[1,"abc",2]
# mylist.append(mylist) #[1, "abc", 2, [...]]
#                                       # -> [1, "abc", 2, [...]]

# a = mylist[0] # 1
# print(str(a) *mylist[-1][-1][-1][-1][-1][-1][-2])
# # "1" *mylist[-2]
# # "1" *2

# b = [1, 100, 99]
# b = sorted(b)
# print(b)

# c = ["https://baidu.com", ...]
# for url in c:
#     ...

# mydict = {
#     "a": [1, 2],
#     "b": 2,
#     "c": "3",
#     "d": 2,
# } # 
# print(mydict["a"])

# for k, v in mydict.items():
#     print(k)
#     print(v)

# mystr = "wwudyhyowboewuynw"
# need_to_search = "w"
# mydict = {}
# for i in mystr:
#     # 统计字符串各字符出现的数量
#     if i not in mydict:
#         mydict[i] = 0

#     mydict[i] = mydict[i] +1

# print(mydict)
# goodname2price = {}

# dict1 = {
#     "a": "a",
#     "b": 1
# }
# dict2 = dict1

# dict2["a"] = dict1["b"]
# print(dict1["a"])

# a, b, c = (1, "2", ["a", 5.0])

# d = int(b *2) // c[-1]  # 22 // 5.0
# e = c
# e.insert(0, d)  #[4.0,"a",5.0]

# f = {
#     "2": 0,
#     b: 1,
#     "b": 2,
#     "c": "b",  
#     #"sth": f[...]
# }

# f["sth"] = f

# print(e[0])  # 4.0
# print(f["2"])  # 1
# print(f["sth"]["sth"][f["c"]])  # 2