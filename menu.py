

def MiniDosaCorner():
    print("NAME:DILIP V.PRAJAPATI.\n")
    print(" ")
    print("SUBJECT: PYTHON\n")
    print(" ")
    print("TOPIC: MINI PROJECT(MINIDOSA CORNER)")
    print(" ")









    print("$"*40,"WELCOME TO DP MINIDOSACORNER","$"*40)
    print(" ")
    print("$"*40,"SELECT YOUR FAVOURATE AND YUMMY DOSA.........!!!!!!!!!","$"*40)
    print(" ")

    print("1-->SADA DOSA @ Rs.50")
    print("2-->CHEESE DOSA @ Rs.180")
    print("3-->SECHEZWAN DOSA @ Rs.150")
    print("4-->MASALA DOSA @ Rs.90")
    print("5-->PASTA DOSA @ Rs.120")
    print("6-->SWEET CORN DOSA @ Rs.190")
    print("7-->CHEESE MASALA DOSA (BHAJI SEPERATE)@ Rs.200")
    Subtotal=0
    cgst=0
    sgst=0
    total=0
    print(" ")

    ch=int(input("enter your choice:"))
    print(" ")
    if ch==1:
        SD=int(input("enter quantity:"))
        subtotal=SD*50
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==2:
        CD=int(input("enter quantity:"))
        subtotal=CD*180
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==3:
        SWD=int(input("enter quantity:"))
        subtotal=SWD*150
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==4:
        MD=int(input("enter quantity:"))
        subtotal=MD*90
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==5:
        PD=int(input("enter quantity:"))
        subtotal=PD*120
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==6:
        SCD=int(input("enter quantity:"))
        subtotal=SCD*190
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    elif ch==7:
        CMD=int(input("enter quantity:"))
        subtotal=CMD*200
        cgst=subtotal*0.05
        sgst=subtotal*0.05
    else:
        print("ENTERED CHOICE NOT AVAILABLE!!! TRY AGAIN")
        MiniDosaCorner()    
    total=subtotal+cgst+sgst
    print()
    print("##"*20,"RECEIPT","##"*20)
    print("subtotal:",subtotal)
    print("total:",total)
    print("cgst:",cgst)
    print("sgst:",sgst)
#    print("~"*40,"VISIT AGAIN","~"*40)

        
def cashback():
    print("#"*40,"DO YOU WANT CASHBACK OFFER??? IF YES THEN CHOOSE OPTION","#"*40)
    print("select your opinion")
    print ("a-->YES THROUGH PAYTM APP")
    print("b-->YES THROUGH PHONEPE APP")
    print("c-->YES THROUGH FUTURE PAY APP")
    print("d-->NO....I DON'T WANT CASHBACK")
    print(" ")
    C=input("select your option:")
    
    total=0
    if C=="a":
        print("WOW!!!YOU HAVE ACHIVED A CASHBACK OFFER OF RS.500")
    elif C=="b":
        print("WOW!!!YOU HAVE ACHIVED A CASHBACK OFFER OF RS.700")
    elif C=="c":
        print("WOW!!!YOU HAVE ACHIVED A CASHBACK OFFER OF RS.450")
    elif C=="d":
            print("OOPS!! SORRY YOU DONT HAVE CASHBACK")
    else:
        print("PLEASE TRY AGAIN")
##    if total>1000:
##        print("CASHBACK")






def feedback():
   # print("~"*38)
    print("#"*40,"GIVE YOUR FEEDBACK","#"*40)
    print("select your opinion")
    print ("a-->execellent service")
    print("b-->good service")
    print("c-->can do better")
    print("d-->bad service")
    ch=input("ENTER YOUR OPINION:")
    if ch=="a":
        print("execellent service")
    elif ch=="b":
        print("good service")
    elif ch=="c":
        print("can do better")
    elif ch=="d":
        print("bad services")
    else:
        print("PLEASE TRY AGAIN")

    print("~"*40,"THANK YOU VISIT AGAIN.WE HOPE YOU ENJOYED...","~"*40)    
MiniDosaCorner()    
cashback()
feedback()          

