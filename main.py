from tracker import add_expense, read_expense, clear_all_expenses, category

while True:
    print("-----WELCOME TO EXPENCE TRACKER-----")
    print("1. Add expence")
    print("2. Check/View you expences")
    print("3. Check expenses of particular category ")
    print("4. Clear all expenses")
    print("5. Exit")
    a=input("Enter number(1,2,3...): ")
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
    
    else:
        print("Invalid Input. Try again!")