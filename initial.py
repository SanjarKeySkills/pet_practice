# words = ["level", "word", "radar", "python", "code", "madam", "rsinfr"]
# result = 0
# def check_fn(words):
# 	count = 0
# 	for word in words:
# 		if word[0] == word[-1]:
# 			count += 1
# 	return count
# check_fn(words)
# result = check_fn(words)
# print(result)
# 
# ----------------------------------------------

words = ["level", "word", "radar", "python", "code", "madam", "rsinfr"]
result = 0
def check_fn(words):
	count = 0
	for word in words:
			count += 1
	return count
check_fn(words)
result = check_fn(words)
print(result)

# --------------------------------------------------------------
# The first attempt of the unittest
# def cube(n):
#     return n ** 3
# def triangle(base, height):
#     return base * height / 2

# def evenodd(i):
#     if i % 2 == 0:
#         return 'even'
#     else:
#           return 'odd'

# import unittest

# class MyTest(unittest.TestCase):
#     def test_cube(self):
#         self.assertEqual( insert, expect)
# insert = cube(5)
# expect = 125
        # self.assertEqual( cube(10), 1000)
        # self.assertEqual( cube(0), 0)
    # def test_triangle(self):
    #     self.assertEqual( triangle(10, 10), 50)
    #     self.assertEqual( triangle(0, 0), 0)
    #     self.assertEqual( triangle(5, 10), 25)
    # def test_evenodd(self):
    #     self.assertEqual( evenodd(1), 'odd')
    #     self.assertEqual( evenodd(-2), 'even')
    #     self.assertEqual( evenodd(0), 'even')
# if insert == expect:
#     prefix = "Ok"
# else:
# 	prefix = "X"
# print('%s got: %d expected: %d' % (prefix, insert, expect))

# if __name__ == '__main__':
#    unittest.main()

# -------------------------------------------------------------
# Second way to execute expression Unittest
# def main(a, b):
#     return a + b
# import unittest
# class addTest(unittest.TestCase):
#     def test_add(self):
#         insert = cube(5)
# 		expect = 125
# 		render(main, insert, expect)
# 	if insert == expect:
# 		prefix = ' OK '
# 	else:
# 		prefix = '  X '
# 	print('%s got: %s expected: %s' %(prefix, repr(got), repr(expected)))

# ------------------------------------------------------------------------------

# def main()
# # words = ["level", "word", "radar", "python", "code", "madam", "rsinfr"]
# # result = 0
# # def check_fn(words):
# # 	count = 0
# # 	for word in words:
# # 		if word[0] == word[-1]:
# # 			count += 1
# # 	return count
# # check_fn(words)
# # result = check_fn(words)
# # print(result)

# ---------------------------------------------------
# def add(a, b):
#     return a + b

# def multi(a, b):
#     result = add(a, b)
#     return result * 3
# print(multi(3, 3))


# --------------Bill task------------
# name = str(input("Enter your name, please."))
# bill = None
# while bill is None:
#     try:
#         bill=float(input('enter the bill'))
#     except ValueError:
#         print("Error")
# tipsPercent=bill/10
# total =  bill + tipsPercent

# print("Hello, %s, your total bill: %.2f. Bill: %.2f. Tips: %.2f" % (name, total, bill, tipsPercent))

# -----------------------------

# Calls the above functions with interesting inputs

# match-end
# words = ['aba', 'xyz', 'aa', 'x', 'bbb']
# words = ['', 'x', 'xy', 'xyx', 'xx']
# words = ['aaa', 'be', 'abc', 'hello']

# 'front_x'
# words = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
# words = ['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
# words = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

# 'sort_last'
# words = [(1, 3), (3, 2), (2, 1)]

# stage of sort last
# def sort_last(words):
#     for word in words:
        



# matching stage Match_end
# def match_end(words):
#     count = 0
#     for word in words:
#         if len(word) >= 3 and word[0] == word[-1]:
#             count += 1
#     return count
    # # return sum(1 for word in words if len(word) >= 3 and word[0] == word[-1])


# matching stage Front_x
# def front_x(words):
#     listX = []
#     list = []
    
#     for word in words:
#         if word[0] == 'x':
#             listX.append(word)
#         else:
#             list.append(word)
#     words = listX + list
#     print(words)
#     return words
# front_x(words)


# testing stage
# def test(got, expected):
#     if got == expected:
#         print(f"Test passed: Got is {got}, Expected {expected}")
#     else:
#         print(f"Test is not passed: Got is {got}, Expected {expected}")

# input stage
# def main():
    # test(match_end(words), 3)
    # test(match_end(words), 2)
    # test(match_end(words), 1)
    # test(front_x(words), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    # test(front_x(words), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    # test(front_x(words), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    # test(sort_last(words), [(2, 1), (3, 2), (1, 3)])
    # test(sort_last(words), [(3, 1), (1, 2), (2, 3)])
    # test(sort_last(words), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
# main()

# ------------------------------------------------
from collections import Counter
str = "If you want your classes to be reusable then you will find that different clients have different output requirements let the client not the class worry about the output side of things."

list = str.split()
print(list)

object = Counter(list)
x = dict(object)
print(x)

# ------------------
a = 90
b = 160
c = a + b
print(c)