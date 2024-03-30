#homework 1 

name = input("Please enter your name: ")

surname = input("Please enter your surname: ")

age = int(input("Please enter your age: "))

home = input("Please enter your home address: ")

### 

personal_information = []

personal_information.append(name)

personal_information.append(surname)

personal_information.append(age)

personal_information.append(home)

first = slice(0, 2)

second = slice(1, 3)

third = slice(0, 3)

fourth = slice(1, 4)

###

print("name and surname", personal_information[first])

print("surname and age", personal_information[second])

print("name, surname and age", personal_information[third])

print("surname, age and home address", personal_information[fourth])

#homework 2

num = int(input("Please enter your negative number: "))

negative_numbers = []

for i in range(num, 0):
    print(i)

#homework 3
    
info = (name, surname)

info1 = slice(0, 1)
info2 = slice(1, 3)

print("first - name:", info[info1])
print("second - surname:", info[info2])

#homework 4

five_favourite_movies = ["Trainspotting", "Venom", "MR.robot", "Requiem", "Alone"]

print(five_favourite_movies[1:3])  

print(five_favourite_movies[2:4]) 

print(five_favourite_movies[-4:-2]) 

print(five_favourite_movies[-3:-1]) 

#homework 5

academy = input("please enter the name of academy: ")

if academy[0:1] == "G":
    print("goa is the best choice")
else:
    print("you made the wrong choice")

