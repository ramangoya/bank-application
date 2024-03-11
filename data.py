#prohject File Bank AApplication System (ATM system)
bank={}
head=["Name","Address","phone","Amount"]
data=[]
acn=101
while True:
    print("*"*20,"Welcome Apna Bank","*"*20) 
    print("1.Open Acount")
    print("2.Check Balance")
    print("3.Dopist Amount")
    print("4.Withdraw Amount")
    print("5.Exit")
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        n=input("Enter the name : ")
        data.append(n)
        a=input("Enter the Address : ")
        data.append(a)
        p=input("Enter the Phone : ")
        data.append(p)
        bal=int(input("Enter the Amount : "))
        data.append(bal)
        temp=dict(zip(head,data))
        bank[acn]=temp
        acn+=1
        data.clear()
        print(bank)
        print("*"*20,"Acount Opened","*"*20)
    elif ch==2:
        pin=int(input("Enter the Your Bank Pin Number : "))
        if pin in bank:
            print("your Current Bank Balance is : ")
            print(bank[pin]["Amount"])
        else:
            print("*"*20,"Your Pin Is Wrong ")
    elif ch==3:
        ac=int(input("Enter the Acount Number:"))
        if ac in bank:
            a=int(input("Enter the Amount :"))
            bank[ac]["Amount"]+=a
            print("*"*20,"Amount Add Sucessfully")
            print("Currect Balance :",bank[ac]["Amount"])
        else:
            print("*"*20,"Your Pin Is Wrong ")
               
    elif ch==4:
        ac=int(input("Enter the Acount Number:"))
        if ac in bank:
            a=int(input("Enter the Amount :"))
            bank[ac]["Amount"]-=a
            print("*"*20,"Amount withdraw Sucessfully")
            print("Currect Balance :",bank[ac]["Amount"])
        else:
            print("*"*20,"Your Pin Is Wrong ")
    elif ch==5:
        print("Tnakn You ")
        break
    else:
        print("Invalid Command")
