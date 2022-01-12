def validatePass(pd):
    pdLength = len(pd)
    invalidCharCount = 0  
    lowerCaseCount = 0
    upperCaseCount = 0
    digitCount = 0
    specialCharCount = 0
    flag = True            
    specialChar = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

    for c in pd:                    
        if c in specialChar:
            specialCharCount+=1
        elif c>='0' and c<='9':
            digitCount+=1
        elif c>='a' and c<='z':
            lowerCaseCount+=1
        elif c>='A' and c<='Z':
            upperCaseCount+=1
        else:
            invalidCharCount+=1

    if pdLength<6 or pdLength>16:  
        flag = False        
        print("Password should have min len 6 and max 16")
    if lowerCaseCount == 0:
        flag = False
        print("Password should contain atleast one lower case character (a-z)")
    if upperCaseCount == 0:
        flag = False
        print("Password should contain atleast one upper case character (A-Z)")
    if digitCount == 0:
        flag = False
        print("Password should contain atleast one digit (0-9)")
    if invalidCharCount > 0:
        flag = False
        print("You have provided an invalid chracter")
    
    return "Valid Password" if flag else "Invalid Password"


pd = input("Enter a password :\n")
print(validatePass(pd))
    

