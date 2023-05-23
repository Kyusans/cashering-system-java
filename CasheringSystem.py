# --------IMPORTANT _NOTE_: ang \n sa mga code kay pang break og line para spacing lang na para limpyo og chuy
# --------IMPORTANT _NOTE_: str() pang convert og non-string nga variables to string
# --------IMPORTANT _NOTE_: kaning import os, para lang ni maka access tag mga functions or commands sa operating system...sa atong case kay ang 'cls' nga command para pang clear lang sa terminal
import os
# username og password ni boe jiden
username = ["boe"]
password = ["jiden"]
# burger list nato:
#              0                1                  2                   3
burger = ["Cheese burger", "Nut burger", "Deep-fried burger", "Regular Joe burger"]
# price sa burger.... kani nga list kay puros int
foodPrice = [69, 45, 30, 25]

# para ma show nato ang gi order ni user
# empty pa siya for now kay wa paman nag order si user
orderList = []
orderListQuantity = []
amount = []

totalAmount = 0

# function pang limpyo sa terminal
def clear():
    # ang os.system('cls') kay pang clear rana sa terminal para limpyo tan awon / cls means clear screen
    os.system('cls')

clear()

def home():
    print("Welcome to Joe's burger!")
    # mangutana ta if gusto ba siya mag signup(S), mag login(L) or eh shutdown ang app(Q)
    command = input("\nType S: to signup\nType L: to login\nType Q: to shutdown\n\nCommand: ").lower()
    clear()
    if command == "s":  
        signup()
    elif command == "l":
        login()
    elif command == "q":
        print("\nShutting down...")
        exit()    
    else:
        print("Invalid command! Please try again")
        home()
   
# function pang login
def login():
    #-------------------------------diri mag login si user-------------------------------
    while True:
        print("Login: ")

        getUsername = input("\nEnter username: ").lower()
        getPassword = input("Enter password: ")

        for index in range(len(username)):
            # validation if sakto ang username og password
            # index = 0
            # username = ["boe", "joe"]
            # password = ["jiden", "trump"]
            if getUsername == "" or getPassword == "":
                # pang continue lang ni sa for loop
                continue
            elif getUsername == username[index] and getPassword == password[index]:
                clear()
                print("Welcome " + username[index].capitalize() + "! What burger do you want to order?\n")
                getUserOrder()
            else:
                continue
        # if nahuman na ang for loop, execute dayun ni (Meaning mali ang username or password ang gi enter ni user)
        else:
            clear()
            # if naay mali sa duha (username or password) then print ni tapos balik enter og username og password
            print("\nIncorrect username or password")

            # mangutana ta if magpadayun ba siyag login or mag signup nalang siya if wala siyay account
            while True:
                command = input("\nDon't have an account?\nType Y: to signup\nType N: continue to login\n\nCommand: ").lower()
                clear()
                if command == "y":
                    signup()
                elif command == "n":
                    break
                else:
                    print("Invalid command! Please try again")

# function pang signup
def signup():
    while True:
        print("Signup:")
        setUsername = input("\nEnter username: ").lower()
        setPassword = input("Enter password: ")
        clear()

        # if ang setUsername og ang setPassword kay empty
        if setUsername == "" and setPassword == "":
            print("Username and password cannot be empty! Please try again ")
        # if ang setUsername lang ang empty
        elif setUsername == "":
            print("Username cannot be empty! Please try again")
        # if ang gi enter ni user nga username, kay existing na. Dapat wala juy magkaparehog username
        elif setUsername in username:
            print("A user with this username already exists! Please enter a different username")
        # if ang setPassword lang ang empty
        elif setPassword == "":
            print("Password cannot be empty! Please try again")
        # if ang gi enter ni user nga password kay less than or equal to 4 characters lang
        elif len(setPassword) <= 4:
            print("Your password must be atleast 5 characters! Please try again")
        # if goods na tanan kani ang eh execute
        else:
            # list.append() kaning append() nga method, kay pang add lang ni sa list example: username.append("joe")
            username.append(setUsername)
            password.append(setPassword)
            print("Success!\n")
            break
        
    home()

# function pang logout
def logout():
    global orderList,orderListQuantity,amount,totalAmount

    clear()
    # since mag logout naman ang user, gi empty nato tanan order, quantity, amount og totalAmount
    orderList = []
    orderListQuantity = []
    amount = []
    totalAmount = 0

    print("Logging off...\n")
    home()

# kani nga function kay pang kuha sa order ni user
def getUserOrder():
    global totalAmount,burgerNumber,addAmount

    #-------------------------------ipa enter og number si user kung unsa iyang gusto nga burger-------------------------------
    while True:
        # kaning try and except...para catch lang ni og error....like kung alphabets ang gi enter ni user, eh execute tanan code sa except ValueError:
        try:      
            # Pang show lang ni sa atong mga baligya (mga burger nato) og ang mga price nila
            for index in range(len(burger)):
                print("Type "+ str(index) + " for " + burger[index] + " for only: ₱" + str(foodPrice[index]))  

            burgerNumber = int(input("\nEnter burger number: "))

            # validation if valid ang gi type ni user
            if burgerNumber > 3 or burgerNumber < 0:
                # if nag pili siyag greater than or equal to 4 o kaya nag pili siyag less than 0 then print ni tapos balik enter burger number
                print("\nInvalid input!")
            else:
                break
        # kung naay error like nag type si user og alpabet, eh stop tanan sa try: tapos eh execute tanan code sa except ValueError:    
        except ValueError:
            clear()
            print("Invalid input! Please try again\n")

    #-------------------------------mo enter og number si user kung pila ka burger iyang paliton------------------------------
    while True:   
        try:
            quantity = int(input("\nHow many " + burger[burgerNumber] + " do you want? : "))

            if quantity <= 0:
            # if nag pili siyag less than or equal to 0 then print niya ni tapos balik enter how many burgers do you want
                print("\nInvalid input!")
            else:
                #   50                25                  2
                addAmount = foodPrice[burgerNumber] * quantity
                
                # if empty ang orderlist...gi add nato diritso ang gi order niya
                if orderList == []:
                    # remember nga ang .append() nga method kay pang add lang na og items sa list
                    orderList.append(burger[burgerNumber])
                    amount.append(addAmount)
                    orderListQuantity.append(quantity)
                # diri if dili empty ang orderList...orderList ha katong gi order ni user
                else:
                    # gi loop nato ang orderlist para makita ba nato kung nag order na ba siyag specific nga burger para eh update lang nato ang quantity og ang cost
                    indexItem = 0

                    for items in orderList:
                        # indexItem = 1
                        # amount = [300]
                        # quantity = [12]
                        # orderList = ["Regular joe burger"]

                        # pang update lang ni sa existing item
                        # if nag order na siyag, lets say "Regular Joe burger", gi update lang nato ang existing amount og ang existing quantity(orderListQuantity) nga iyang gi enter last time
                        if burger[burgerNumber] in items:

                            updatedAmount = amount[indexItem] + addAmount
                            updatedQuantity = orderListQuantity[indexItem] + quantity

                            # ing ani pag update og specific value sa list example { name[0] = "Joe" } meaning ani, ang name[0] kay "Joe" na
                            amount[indexItem] = updatedAmount
                            orderListQuantity[indexItem] = updatedQuantity
                            clear()
                            break
                        # kung wala juy duplicate nga burger nga iyang gi order
                        else:
                            indexItem += 1
                            continue

                    else:
                        if burger[burgerNumber] not in items:
                            orderList.append(burger[burgerNumber])
                            orderListQuantity.append(quantity)    
                            amount.append(addAmount)                                   
                totalAmount += addAmount
                addAmount = 0
                clear()
                break               
        except ValueError:
            clear()
            print("\nInvalid input! Please try again")

    purchase()

# kani nga function kay pang display lang sa gi order ni user
def showOrderList():
    print("\nYour order:")
    # diri gipakita tanan gi order ni user
    # index = 1
    for index in range(len(orderList)):
        print(str(index + 1)+ ".) " + str(orderListQuantity[index]) + "x " + orderList[index] + " = ₱" + str(amount[index]))

# kani nga function kay pang remove sa item nga gi order ni user
def removeItemList():
    global subtractMoney
    clear()
    while True:
        try:
            showOrderList()
            removeIndex = int(input("\nEnter the number of the item you want to remove: "))
            clear()
            # if nag enter siyag number sa list unya wala man diay na nga number sa iyang list eh excute dayun ni
            if removeIndex > len(orderList) or removeIndex <= 0:         
                print("There is no number " + str(removeIndex) + " in your list! Please try again")
            # if sakto iyang pag enter og number sa iyang list, execute dayun ni
            else:
                # minus 1 kay ang eh enter man ni user kay list # 1, 2, 3 or 4 raman ang ma enter ni user
                # para makuha ang sakto nga index sa list since ang una nga number sa list kay always 0 baya
                    #                   0                   1
                # orderList = ["regular joe burger", "cheeseburger"]
                removeIndex -= 1

                subtractMoney = amount[removeIndex]   
                # .pop() kay pang remove og specific index sa list
                orderList.pop(removeIndex)
                orderListQuantity.pop(removeIndex)
                amount.pop(removeIndex)

                print("\nItem successfully removed!")
                break              
        except ValueError:
            print("Invalid input! Please try again")

# function kung mag purchase na si user or mag add pa ba siya or something
def purchase():
    global totalAmount,addAmount,orderListQuantity,amount,orderList
    
    #-------------------------------mangutana ta if naa pa siyay gusto eh add or eh remove sa order niya-----------------------------------------
    while True:
        # check if empty ang iyang order list
        if orderList == []:
            print("\nYour order list is empty")
        # if naa siyay gi order, kani ang ma execute
        else:
            showOrderList()
            print("\nTotal amount: ₱" + str(totalAmount))
        
        command = input("\nType C: to confirm everything\nType A: to add something in your list\nType R: to remove something in your list\nType E: to exit \n\nCommand: ").lower()
        clear()
        # if naa siyay gusto eh add sa iyang list
        if command == "a":
            getUserOrder()
        # if goods na tanan og ready na si user mag bayad
        elif command == "c":
            # validation if nag confirm siya tapos wala man diay siyay gi order
            if orderList == []:
                print("\nYou didn't order anything! Please try again")
            else:
                break
        # if naay gusto eh remove si user sa iyang list
        elif command == "r":
            # validation if naa ba siyay ma remove nga item sa iyang list
            # [] = meaning kay empty na nga list
            if orderList == []:
                print("\nYou don't have something to remove! Please try again")
            else:
                removeItemList()
                totalAmount -= subtractMoney
        elif command == "e":
            logout()
        else:
            print("\nInvalid command! Please try again")

    #-------------------------------mo enter og number si user kung pila iyang eh bayad-------------------------------
    while True:
        try:
            showOrderList()
            print("\nTotal amount: ₱" + str(totalAmount))

            userMoney = int(input("Enter your money: "))
            clear()
            change = userMoney - totalAmount

            if change < 0:
            #   if kulang iyang bayad, print ni tapos balik enter your money nga input
                print("\nInsufficient Fund!")
            else:
                break
        except ValueError:
            print("Invalid input! Please try again")

    #-------------------------------gi display ang iyang sukli-------------------------------
    showOrderList()
    print("\nTotal amount: ₱" + str(totalAmount)+"\n\nYou paid: ₱" + str(userMoney))

    print("\nYour order will be delivered shortly and your change is: ₱" + str(change))
    print("Thank you for your order! Please come again")

    # mangutana ta if mag order pa siyag another(Y) or dili na(N)
    while True:
        command = input("\nDo you want to order again?\n\nType Y: to order again\nType N: to exit\n\nCommand: ").lower()

        if command == "y":
            clear()
            orderList = []
            orderListQuantity = []
            amount = []
            totalAmount = 0
            getUserOrder()
        elif command == "n":
            logout()
        else:
            print("Invalid command! Please try again")

home()