# from string import printable as alph
# for x in alph[:19]:
#     num1=int(f'98{x}79641',19)
#     num2=int(f'36{x}14',19)
#     num3=int(f'73{x}4',19)
#     num=num1+num2+num3
#     if num%18==0:
#         print(x,num//18)
#     from string import printable
#
#     o = set()
#     for x in range(10, 67):
#         for y in range(0, x):
#             num1 = 7 * 67 ** 4 + 3 * 67 ** 3 + x * 67 ** 2 + 1 * 67 ** 1 + y
#             num2 = 4 * 67 ** 3 + 9 * 67 ** 2 + y * 67 ** 1 + 6
#             num = num1 + num2
#             o.add(num)
#     print(set(o))
#num1=2*2187**2020+729**2021-2*243**2022+81**2023-2*27**2024-6561
    # 1 sposob
    # K=0
    # for i in range(10,27):
    #     K+=d27.count(printable[i])
    # print(K)
    # 2 sposob
    # cnt_2=0
    # for i in d27:
    #     if int(i,27)>9:
    #         cnt_2+=1
    # print(cnt_2)
    # 3 sposob
    # cnt_1=0
    # for i in d27:
    #     if i in printable[10:27]:
    #         cnt_1+=1
    # print(cnt_1)
# cnt=0
# while num1:
#     if num1%27>9:
#         cnt+=1
#     num1//=27
# print(cnt)
