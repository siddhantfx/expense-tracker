# This python file is used to get input of expense and store the value in .txt form.

def add_expense():
    f=open("expense.txt","a")
    entries= int(input('Enter number of entries: '))
    
    # Using loops to input data and store for further use.
    for i in range(entries):
        category=input("In which category you want to add?: ")
        amount=float(input("Enter amount you've spent: "))
        a=input("Want to give any description?(yes/no): ")
        if a.lower()=="yes":
            description=input("Enter description of this expence: ")
        else:
            description = "None"
            
    # Generating a dictionary to store items.
        expense_dict = { "category": category,
                "amount": amount,
                "description": description }
        line = f"{expense_dict['category']}|{expense_dict['amount']}|{expense_dict['description']}\n"
        f.write(line)
        print("Expense saved!\n")
            
    f.close
    
def read_expense():
    try:
        f=open("expense.txt","r")
        total_amount=0
        for line in f:
            part=line.strip().split('|')
            category= part[0]
            amount= float(part[1])
            description= part[2]
            print(f"{category}: {amount} ({description})")
            total_amount= total_amount+ amount
        print("total spent: ",total_amount)
    
    except FileNotFoundError:
        print("Please add entries!")
    
    f.close()
    
def clear_all_expenses():
    option =input("Do you want to clear all the previous data and write new one?(yes/no): ")
    if option.lower()== "yes":
        with open("expense.txt","w") as f:
            pass
        print("All data has been cleared!")
    
    else:
        print("Previous data will remain.")
        
# This function is used when we want to check expense of particular category
def category():
    choice=input("Enter category whose data you want: ")
    f= open("expense.txt","r")
    for line in f:
        part=line.strip().split('|')
        category= part[0]
        amount= part[1]
        description= part[2]
        if category== choice:
            print(f"{category}: {amount} {description}")
        
        else:
            continue
    f.close()
