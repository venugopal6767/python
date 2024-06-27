# a tuple is a collection of items, which are immutable which cannot be changed once it is created
# It is defined with ()
# example tuple = ("venu", "admin","devops")
#we cannot append or remove data once tuple is created.

my_tuple = (1, 2, 'apple', 'banana')
print(my_tuple)
first_element = my_tuple[0]  # Access the first element (1)
print(first_element)
tuple_length = len(my_tuple)  # Length of the tuple (4)
print(tuple_length)

coordinates = (3, 4)
x, y = coordinates  # Unpack the tuple into x and y (x=3, y=4)
print(x, y)
