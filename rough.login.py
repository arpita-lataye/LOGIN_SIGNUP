import json
import os
import re


def strong_password(password1):
    if len(password1)>6 and len(password1)<16:
        if re.findall("[!@#$%&'*+-.^_`|~:]", password1):
            if re.findall("[0-9]",password1):
                if re.findall("[a-zA-Z]",password1):
                   return True
                else:
                    print("password1 must contain at least one alpha character")
                    password1=input('enter password:')
                    strong_password(password1)
            else:
                print("password1 must contain at least one digit")   
                password1=input('enter password:')
                strong_password(password1) 
        else:
            print("password1 must contain at least one special character")
            password1=input('enter password:')
            strong_password(password1)
    else:
        print("password1 length must be greater than 6 and less than 16")
        password1=input('enter password:')
        strong_password(password1)
        
    
def check_password(password1,password2):
    if password1==password2:
        print("account created")
    else:
        print('password do not match')
        password2=input("enter password:")
        # check_password(password1,password2)

print("welcome to login sign_up page:") 
regestration=input("what do you wants to do=> 1.sign_up, 2.login:")
file=os.path.exists("user.json")
if file==False:
    if regestration=="1":
        user_name=input('enter user name:')
        password1=input('enter password:')
        strong_password(password1)
        password2=input("confirm your password:")
        check_password(password1,password2)
        print("congratulations",user_name,"you are sign_up successfully")
        DOB=input('enter your date of birth:')
        description=input('enter description:')
        hobbies=input('enter hobbies:')
        gender=input('enter gender:')

        my_list=[]
        dic={}
        list1=['user_name','password1','DOB','description','hobbies','gender']
        list2=[user_name,password1,DOB,description,hobbies,gender]
        for i in range(len(list1)):
            dic.update({list1[i]:list2[i]})
        my_list.append(dic)
        with open ("user.json","a") as file:
            json.dump(my_list,file,indent=4)

elif file==True:
    if regestration=="1":
        user_name=input('enter user name:')
        password1=input('enter password:')
        strong_password(password1)
        password2=input('confirm your password:')
        # check_password(password1,password2)

        m=open("user.json","r")
        username=m.read()
        if user_name in username:
            # print('this account is already exists')
            if password1 in username:
                print("password match this account is already exits")
            else:
                print("invalid password or user name")
            
        else:
            print('congrats',user_name,"you are signup successfully")
            DOB=input('enter your date of birth:')
            description=input('enter description:')
            hobbies=input('enter hobbies:')
            gender=input('enter gender:')

            dic={}
            list1=['user_name','password1','DOB','description','hobbies','gender']
            list2=[user_name,password1,DOB,description,hobbies,gender]
            for i in range(len(list1)):
                dic.update({list1[i]:list2[i]})
            with open ("user.json","r") as file:
                data=json.load(file)
                data.append(dic)
                with open("user.json","w") as file:
                    json.dump(data,file,indent=4)
                
    elif regestration=="2":
        login_id=input('enter user name:') 
        login_password=input('enter password:')
        with open ("user.json","r") as file :
            data=json.load(file)
            for i in data:
                if i['user_name']==login_id:
                    if i["password1"]==login_password:
                        print("you are login successfully")

                        for x,y in i.items():
                            print("your",x,"is",y )
                        break
                    else:
                        print('invalid password')
                        break
            else:
                print('invalid account')