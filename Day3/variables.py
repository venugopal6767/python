#define a variable
my_variable = "venugopal"

print(my_variable)


#local variable
def test():
    a = "one"
    b = "two"
    print(a + " " + b)
test()

#Global varialbles
a = "one"
b = "two"
def test():
    print(a + " " + b)
test()

name = "venugopal"
age = 27
study = "Btech"

profile = f"I am {name} and i am {age} old and I completed my {study}"
print(profile)