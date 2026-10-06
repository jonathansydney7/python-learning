def print_sydney(text):
    print(text)
    print(text)
print_sydney("make money")

def check_weather(temp):
    if temp > 30:
        print("it's hot")
    else:
        print("it's cold")
check_weather(35)
check_weather(25)

def greet(name):
    print(f"hi,{name}")
greet("Alice")

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet_user("Bob", 30)

def create_profile(name, age, city):
    profile = {
        'name': name,
        'age': age,
        'city': city
    }
    return profile

profile = create_profile("Charlie", 35, "New York")
print(profile)

def add_print(a,b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}.")
    return result
add_print(5, 10) 

def room_area(length, width):
    area = length * width
    print(f"The area of the room is {area} square units.")
    return area
room_area(5, 10)
