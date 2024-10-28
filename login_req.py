import json

def login_required(email,pas,login):
        if (email ==" " or pas ==" "):
            print("Login is most necessary(you forgot to enter your email or pass )")
        else:
            for ind,info in enumerate(login_li):
                emm=info["email"]
                pasword=info["pass"]
                if emm == email and pas == pasword :
                    facilities()
    
def facilities():
    print("Here are the features and facilities :\n1.Home delivery \n2.30 min sceme")     
def load_info():
    try:
        with open("login_info.txt","r") as file:
            return json.load(file)
    except:
        return []        

login_li=load_info()
count=0
def password_not_match():
    pas=input("Re-Enter your new password: ")
    conf_pass=input("Confirm your password: ")
    check_pas(pas,conf_pass)
def signup(login_li): 
    email=input("Enter your email: ")
    pas=input("New password: ")
    conf_pass=input("Confirm your password: ")
    check_pas(pas,conf_pass,email,login_li)
def check_pas(a,b,email,login_li):
    if a.lower() == b.lower() :
        login_li.append({"email":email,"pass":a})
        for ind,info in enumerate(login_li):
            emm=info["email"]
        if emm != email :
            print("You have successfully entered to our application: ")
            with open("login_info.txt","w") as file:
                json.dump(login_li,file)
        else:
            print("The gmail is already registered.")        
    else:
        password_not_match()   
 
def sign_in(email,pas,login_li):
    
        
    print("You have successfully logged into our server")
    return login_required(email,pas,login_li)

print("Welcome to your application: ")
greet=input("Is this your first timr visiting our app (yes or no) :") 
if greet.lower() == "yes" :
        signup(login_li)
elif greet.lower() == "no" :
    em=input("Enter your email: ")
    pa=input("Enter your password: ")
    
    sign_in(em, pa,login_li)





              
