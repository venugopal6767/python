import re

print("Hello World!")

# datatypes
# string

str = "I am venugopal"
str1 = "venu"
str2 = "gopal"
str3 = "    I am going    "

#length
length = len(str)
print(length)

#concat
full = str1 + str2
print(full)

#split
text = str.split()
print(text)

#upper & lower
Upper = str.upper()
print(Upper)

Lower = str.lower()
print(Lower)

#Replace
Replace = str.replace("venugopal" , "Moka")
print(Replace)

#strip
print(str3)
Strip = str3.strip()
print(Strip)

#substring
substring = "am"
if substring in str:
    print("the substring is present")


#integer
num1 = 15
num2 = -10
num = num1 * num2

print(abs(num)) # the abs value is always positive

#flaot
num3 =10.254
num4 =12.3654

Num = num3 +num4
print(Num)
Rounded = round(Num, 2)
print(Rounded)

#Regular expressions

#findall and Search
str6 = "the sky is blue"
pattern = r"is"
Search = re.search(pattern, str6)
if Search:
    print("pattern found:", Search.group())
else:
    print("no pattern found")
       
#match
pattern = r"the"
Search = re.search(pattern, str6)
if Search:
    print("pattern found:" , Search.group())
else:
    print("No match found")
    
#Replace for replace we use re.sub   
pattern = r"blue"
Replacement = "Black"
Search = re.sub(pattern, Replacement, str6)
print(Search)

#Split
pattern = r" "
Split = re.split(pattern, str6)
print(Split)