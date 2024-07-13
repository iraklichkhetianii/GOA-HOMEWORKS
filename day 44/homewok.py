#PYTHON SYNTAXS

print("Hello World!")

username = input("Please Enter Your  Username:")

#its single-line comment
'''its multi-line comment 
its very nice haha'''

name = 'irakli'
 
if name == 'irakli':
    print('Logging on to Facebook...')
else:
    print('retype the name.')
print('All set !')

for item in Iterable: # type: ignore
    if some_condition: # type: ignore
        break



#PYTHON COMMENTS


x = input("please enter you're name here: ") #In this code I ask the user to enter their name

password = input("Please enter your password: ") #In this code I ask the user to enter their password
repeat_password = input("Please enter your password again: ") #in this code i ask the user to enter their password again

if password == repeat_password:  #If the customer repeated the password correctly then the password is created
     print("password created!")
else:
     print("Invalid Passwords!") #if the customer repeated the password wrongly then the password didnt created

passcode = input("please enter you're password here to enter: ")  #in this code i ask the user to enter their password to get accsess for account
if passcode == passcode:
     print ("accsess granted")  #if password entered correctly user gets acsess to account


#python variables

print("assigning values of different datatypes")
a, b, c, d = 4, "geeks", 3.14, True
print(a)
print(b)
print(c)
print(d)



x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

