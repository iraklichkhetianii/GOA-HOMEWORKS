s
registered_password = "irakli1234"
authorized = "irakli12"

while authorized != True:
    user_input = input("Please enter your password: ")
    
    if user_input == registered_password:
        print("Acces Granted")
        authorized = True 
        
    else: 
        print("Password is incorrect please try again") 



        
      
