def main():
    print("Hello World!")



from collections import Counter
str = "If you want your classes to be reusable then you will find that different clients have different output requirements let the client not the class worry about the output side of things."

list = str.split()
print(list)

object = Counter(list)
x = dict(object)
print(x)