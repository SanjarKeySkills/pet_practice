# squares = [1, 4, 9, 16]
# sum = 0
# for num in squares:
#     sum += num
# print(sum)

# ------------------

# colors = [ 'red', 'blue', 'green']
# print(colors[0])
# print(colors[2])
# print(len(colors))

# ------------------

# list = ['larry', 'curly', 'moe']
# if 'curly' in list:
#     print('yay')

# ------------------

# for i in range(9):
#     print(i)

# ------------------

# a = ['ivi', 'kiwi', 'study', 'buddy', 'heru', 'sheru', 'iten', 'biten', 'kozel', 'vasel']
# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 3

# -----------------

# card_num = "1234-5678-9012-3456"
# for x in card_num:
#     print(x)

# -----------------

# for x in range(1, 21):
#     if x == 13:
#         break
#     else:
#         print(x)

# -----------------------------------

# -----------------------------------

# i = 1
# while i < 11:
#     print(f" num {i}")
#     i += 1

# while True: #идет как тестер по условия правда или нет
#     user_input = input(str("add input 'sam' for finishing:"))
#     if user_input.lower() == 'sam':
#         break
#     print(f"you added {user_input}")

# i = 0
# while i < 4:
#     print(f"i = {i}")
#     i += 1

# count = 0
# while True:
#     print(f"num is {count}")
#     count += 1
#     if count >= 5:
#         break

# num_insert = int(input("please insert a number from 1 to 20 and we print only even num in this range: "))
# num = num_insert
# while num < 20:
#     num += 1
#     if num % 2 == 0:
#         continue
#     print(num)

# count = 0
# while count < 3:
#     print(f"count: {count}")
#     count +=1
# else:
#     print("loop is completed")
    
count = 0
while count < 9:
    if count == 6:
        break
    print(count)
    count += 1
else:
    print("this wll not be printed")