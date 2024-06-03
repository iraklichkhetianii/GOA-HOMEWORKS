#dictionary
person = {
            'Name': "Irakli"
            'Surname': "Chkhetiani"
            'Age': "15"
            'Gender': "Male"
            }
      

#1
def user_contacts(data):
    stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }
    return {user[0]: user[1] 
        if len(user) > 1
        else None
        for user in data}


#2
def fillable(stock, merch, n):
    try: return stock[merch] >= n
    except: return False
