numbers = {1, 2, 3, 4, 5,2,6}
unique_numbers = set(numbers)
print(unique_numbers)

fruits = set(["apple", "banana", "orange"])
print(fruits)
print(len(fruits))
print("banana" in fruits)
print("grape" in fruits)

fruits.add("grape")
print(fruits)
fruits.remove("banana")
print(fruits)

users = {"john", "jane", "bob"}
if "john" in users:
    print("Access granted.")
else:
    print("Access denied.")