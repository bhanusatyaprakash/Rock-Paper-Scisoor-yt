print("Welcome to ABC Bank !!")
pin=1234
chances= 3
balance=50000
while chances !=0:
    user_pin=int(input("Please enter the four digit pin : "))
    if user_pin !=pin:
        chances -=1
        print("Wrong pin number")
        print(f"you have {chances} chances lef")

    else:
        user_choice=input("B : balance , D : deposite, W : withdraw")
        if user_choice == "B" :
            print(f"your total balance is Rs.{balance}")

        if user_choice=="D":
            deposite_user= int(input("Enter the amount that you would like to deposite !!"))
            total_balance= deposite_user + balance
            print(f"you have deposited Rs.{deposite_user}")
            print(f"your total balance is {total_balance} ")

        if user_choice=="W":
            withdraw_user= int(input("Enter the amount you want to withdraw"))
            total_balance=balance - withdraw_user
            print(f"you have withdrawn Rs.{total_balance}")
            print(f"your toal balance is Rs.{total_balance}")
    user_exit=input("would you like to exit ? Yes/No")
    if user_exit == "Yes":
        print("Thnakyou for using ABC bank !!")
        break
    else:
        continue
        

                                     
