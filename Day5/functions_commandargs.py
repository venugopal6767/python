import sys
def test(num1, num2):
   add = num1 + num2
   print(add)
   return add
test(sys.args[1], sys.args[2])