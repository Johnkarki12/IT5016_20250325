counter = 0

def staff_info():
    global counter, staff_ID, staff_name, requisition_id, date
    date = input("Enter the date (dd/mm/yyyy): ")
    staff_ID = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
    requisition_id = 10000 + counter
    counter += 1

def requisitions_total():
    items = {}
    total = 0
    num = int(input("\nHow many items? "))
    for i in range(num):
        item = input("Enter item name: ")
        price = float(input("Enter price: "))
        items[item] = price
        total += price
    return total

def requisition_approval():
    global staff_ID, requisition_id, total, status, approval_ref
    total = requisitions_total()  # Get total from Task 2
    if total < 500:
        status = "Approved"
        approval_ref = staff_ID + str(requisition_id)[-3:]
    else:
        status = "Pending"
        approval_ref = "None"

def display_requisitions():
    print("\nPrinting Requisitions:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_ID)
    print("Staff Name:", staff_name)
    print("Total: $", total)  # Task 3 already calculates this
    print("Status:", status)  # Task 3 already determines this
    print("Approval Reference Number:", approval_ref)  # Task 3 already sets this

num = int(input("How many staff do you want to enter: "))
for i in range(num):
    print(f"\nEntering details for Staff {i + 1}:")
    staff_info()  # Task 1
    requisition_approval()  # Task 3 (includes Task 2)
    display_requisitions()  # Task 4 (just displaying)

print("\nAll staff entries completed!")
