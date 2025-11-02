# def main():
#     str = "Hello"
#     return str
# print(main())



from collections import Counter
sentence = str(input("Please insert your sentence"))

str = "If you want your classes to be reusable then you will find that different clients have different output requirements let the client not the class worry about the output side of things."

list = str.split()

object = Counter(list)
x = dict(object)
print(x)