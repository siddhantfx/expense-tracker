# Importing all the functions from tracker.py to run on main.py and combining both of them.
from tracker import add_expense, read_expense, clear_all_expenses, category

while True:
    print("-----WELCOME TO EXPENCE TRACKER-----")
    print("1. Add expence")
    print("2. Check/View you expences")
    print("3. Check expenses of particular category ")
    print("4. Clear all expenses")
    print("5. Exit")
    a=input("Enter number(1,2,3...): ")
    # will check the input and based on that runs the function and at last gives the output.
    if a=="1":
        add_expense()
        
    elif a=="2":
        read_expense()
    
    elif a=="3":
        category()
        
    elif a=="4":
        clear_all_expenses()
        
    elif a=="5":
        print("Thank you...Have a nice Day!")
        break

    # error handeling
    else:
        print("Invalid Input. Try again!")
