# a = 33
# b = 200
# if a < b:
	# print("b is bigger than a")
 
# ----------------------

# first = 10
# second = 20
# num = 180

# if first + second > num:
#     print("equation is not mine")

# -----------------------

from collections import Counter
sentence = str(input("Please insert your sentence:"))
print(sentence)

str = "If you want your classes to be reusable then you will find that different clients have different output requirements let the client not the class worry about the output side of things."

list = sentence.splite()

object = Counter(list)
x = dict(object)
print(x)
