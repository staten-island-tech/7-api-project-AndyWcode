userinfo = []

def validinfo(email, password):
    if isinstance(email,str) != True:
        return "valid email has to be string"
    if "@" not in email:
        return "not valid email"
    if type(password) != str: 
        return "password not a string"
    if len(password) <= 7: 
        return "not enough characters (8!!)"
    numbers = 0
    for char in password:
        if char.isdigit == True:
            number+=1
    if numbers < 0:
        return "Password needs a number"
    if char.islower() == True:
        return "Password needs a capital letter"
    return {"email":email, "password":password}

print(validinfo("ANDYWENG@Gmail.com", "Weng!@#123"))