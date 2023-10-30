import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3306",
  user="root",
  password="test@123",
  database="Bank_Database"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Customer (id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Address VARCHAR(255), City VARCHAR(255), Pincode VARCHAR(255))")
# mycursor.execute("CREATE TABLE Branch (id INT AUTO_INCREMENT PRIMARY KEY, branch_name VARCHAR(255), branch_city VARCHAR(255), assets VARCHAR(255))")
# mycursor.execute("CREATE TABLE Account (id INT AUTO_INCREMENT PRIMARY KEY, account_no VARCHAR(255), branch_name VARCHAR(255), balance VARCHAR(255))")
# mycursor.execute("CREATE TABLE Depositor (id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(255), account_no VARCHAR(255))")

def insert_customer_table():
    customer_details = input("Enter Customer Details (Name,Address,City,Pincode): ")
    x = customer_details.split(",")
    sql = "INSERT INTO Customer (Name, Address, City, Pincode) VALUES (%s, %s, %s, %s)"
    val = (x[0], x[1], x[2], x[3])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")

def delete_customer_table():
    display_customer_table()
    customer_name = input("Enter Customer Name: ")
    sql = "DELETE FROM Customer WHERE Name = '%s'" % (customer_name)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def display_customer_table():
    mycursor.execute("SELECT * FROM Customer")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x) 

def insert_branch_table():
    branch_details = input("Enter Branch Details (Branch Name,Branch City,Assets): ")
    x = branch_details.split(",")
    sql = "INSERT INTO Branch (branch_name, branch_city, assets) VALUES (%s, %s, %s)"
    val = (x[0], x[1], x[2])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")

def delete_branch_table():
    display_branch_table()
    branch_name = input("Enter Branch Name: ")
    branch_city = input("Enter Branch City: ")
    sql = "DELETE FROM Branch WHERE branch_name = '%s' and branch_city = '%s'" % (branch_name, branch_city)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def display_branch_table():
    mycursor.execute("SELECT * FROM Branch")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x) 

def insert_account_table():
    account_details = input("Enter Account Details (Account No.,Branch Name,Balance): ")
    x = account_details.split(",")
    sql = "INSERT INTO Account (account_no, branch_name, balance) VALUES (%s, %s, %s)"
    val = (x[0], x[1], x[2])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")

def delete_account_table():
    display_account_table()
    account_no = input("Enter Account Number: ")
    sql = "DELETE FROM Account WHERE account_no = '%s'" % (account_no)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")


def display_account_table():
    mycursor.execute("SELECT * FROM Account")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def insert_depositor_table():
    depositor_details = input("Enter Depositor Details (Customer Name,Account_No): ")
    x = depositor_details.split(",")
    sql = "INSERT INTO Depositor (customer_name, account_no) VALUES (%s, %s)"
    val = (x[0], x[1])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) inserted.")

def delete_depositor_table():
    display_depositor_table()
    customer_name = input("Enter Customer Name: ")
    account_no = input("Enter Account Number: ")
    sql = "DELETE FROM Depositor WHERE customer_name = '%s' and account_no = '%s'" % (customer_name, account_no)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def display_depositor_table():
    mycursor.execute("SELECT * FROM Depositor")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main_menu():   
    while (True):
        print("Banking Menu Options")
        print("1. Customer Menu")
        print("2. Branch Menu")
        print("3. Account Menu")
        print("4. Depositor Menu")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_menu()
        elif choice == '2':
            branch_menu()
        elif choice == '3':
            account_menu()   
        elif choice == '4':
            depositor_menu()
        elif choice == '5':
            break
        else:
            print("Invalid Choice. Please try again.")

def customer_menu():
    while(True):
        print("Customer Table Menu Options")
        print("1. Insert Record into Customer Table")
        print("2. Delete Record from Customer Table")
        print("3. Display Customer Table")
        print("4. Back to Main Menu")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            insert_customer_table()
        elif choice == '2':
            delete_customer_table()
        elif choice == '3':
            display_customer_table()
        elif choice == '4':
            break
        else:
            print("Invalid Choice. Please Try Again.")

def branch_menu():
    while(True):
        print("Branch Table Menu Options")
        print("1. Insert Record into Branch Table")
        print("2. Delete Record from Branch Table")
        print("3. Display Branch Table")
        print("4. Back to Main Menu")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            insert_branch_table()
        elif choice == '2':
            delete_branch_table()
        elif choice == '3':
            display_branch_table()
        elif choice == '4':
            break
        else:
            print("Invalid Choice. Please Try Again.")

def account_menu():
    while(True):
        print("Account Table Menu Options")
        print("1. Insert Record into Account Table")
        print("2. Delete Record from Account Table")
        print("3. Display Account Table")
        print("4. Back to Main Menu")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            insert_account_table()
        elif choice == '2':
            delete_account_table()
        elif choice == '3':
            display_account_table()
        elif choice == '4':
            break
        else:
            print("Invalid Choice. Please Try Again.")

def depositor_menu():
    while(True):
        print("Depositor Table Menu Options")
        print("1. Insert Record into Depositor Table")
        print("2. Delete Record from Depositor Table")
        print("3. Display Depositor Table")
        print("4. Back to Main Menu")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            insert_depositor_table()
        elif choice == '2':
            delete_depositor_table()
        elif choice == '3':
            display_depositor_table()
        elif choice == '4':
            break
        else:
            print("Invalid Choice. Please Try Again.")

if __name__ == "__main__":
    main_menu()