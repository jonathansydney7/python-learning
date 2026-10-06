def double(x):
    return x*2
print(double(2))

double = lambda x:x*2

students = [('Amy', 85),('ben',72),('cara',65)]
print(students.sort(key=lambda pair: pair[1]))


students = [("Amy", 85), ("Ben", 72), ("Cara", 91)]
students.sort(key=lambda pair: pair[1])
print(students)



if x >= 60:
    result = "Pass"
else:
    result = "Fail"


(lambda x:"pass" if x>=60 else "fail")