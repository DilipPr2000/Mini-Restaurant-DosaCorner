def MiniDosaCorner():
    Subtotal= 0
    cgst    = 0
    sgst    = 0
    total   = 0

    print("NAME:DILIP V.PRAJAPATI.\n")
    print("SUBJECT: PYTHON\n")
    print("TOPIC: MINI PROJECT(MINIDOSA CORNER)\n\n")
    
    print("$*"*7,"WELCOME TO DP MINIDOSA CORNER","$*"*7,end='\n\n')
    print("-*"*5,"SELECT YOUR FAVOURATE AND YUMMY DOSA !! ","*-"*5,end='\n\n')

    menu =  [{"item":"SADA DOSA",          "price": 50},
             {"item":"CHEESE DOSA",        "price": 180},
             {"item":"SECHEZWAN DOSA",     "price": 150},
             {"item":"MASALA DOSA",        "price": 90},
             {"item":"PASTA DOSA",         "price": 120},
             {"item":"SWEETCORN DOSA",     "price": 190},
             {"item":"CHEESE-MASALA DOSA", "price": 200}]

    for idx in range(len(menu)):
        print(f"{idx+1}--> {menu[idx]['item']} @ {menu[idx]['price']}")

    choice  = int(input("enter your choice:"))
    qty     = int(input("enter quantity:"))

    if choice>len(menu) or choice<0:
        print("ENTERED CHOICE NOT AVAILABLE!!! TRY AGAIN")
        MiniDosaCorner()    
    else:
        subtotal = qty*menu[choice-1]['price']

    cgst  = subtotal*0.05
    sgst  = subtotal*0.05
    total = subtotal + cgst + sgst

    print()
    print("##"*20,"RECEIPT","##"*20)
    print("subtotal:",subtotal)
    print("total:",total)
    print("cgst:",cgst)
    print("sgst:",sgst)


        
def cashback():
    print("*-"*5,"DO YOU WANT CASHBACK OFFER??? ","*-"*5,end='\n\n')
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
        cashback()

def feedback():
    print('\n\n')
    print("#"*40,"GIVE YOUR FEEDBACK","#"*40)
    print("Rate the Service")
    
    rating = ["excellent service",
              "good service",
              "acceptable service",
              "can do better",
              "bad service"]

    for idx in range(len(rating)):
        print(f"{chr(97+idx)}--> {rating[idx]}")

    ch=ord(input("\nENTER YOUR OPINION:"))

    if ch<97 or ch>102:
        print("PLEASE TRY AGAIN")
        feedback()
    else:
        print("You have Rated: ",rating[ch-97])

    print("~"*10,"THANK YOU VISIT AGAIN.WE HOPE YOU ENJOYED...","~"*10)    


if __name__=="__main__":    
    MiniDosaCorner()    
    cashback()
    feedback()