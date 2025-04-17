counter = 1

def staff_info():
    global counter, date, staff_name, staff_id, requisition_id
    date = input("\nEnter the date (DD/MM/YYYY): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff name: ")
    requisition_id = 10000 + counter
    counter += 1
    print("\nPrinting Staff Information: ")
    print("\nDate: ", date)
    print("Staff ID: ", staff_id.upper())
    print("Staff Name: ", staff_name.capitalize())
    print("Requisition ID: ", requisition_id)

def requisition_total():
    items = {}
    total = 0

    num = int(input("\nHow many items: "))
    for i in range(num):
        item = input(f"\nName of the item {i + 1}: ")
        price = float(input("Enter the price: "))
        items[item] = price
        total += price
    print("\nWhat you bought: ")
    for item_name, item_price in items.items():
        print(item_name.capitalize(), item_price)
    print("Total: ", total)
    return total

def requisition_approval():
    global total, status, approval_reference_number
    total = requisition_total()
    if total < 500:
        status = "Approved"
        approval_reference_number = staff_id + str(requisition_id)[-3:]
    else:
        status = "Pending"
        approval_reference_number = "Not Available "
    print("\nTotal: ", total)
    print("Status: ", status)
    print("Approval Reference Number: ", approval_reference_number.upper())

def display_requisition():
    global total, status, approval_reference_number
    print("\nPrinting Requisitions:")
    print("\nDate:", date)
    print("Requisition ID: ", requisition_id)
    print("Staff ID:", staff_id.upper())
    print("Staff name:", staff_name.capitalize())
    print("Total:", total)
    print("Status:", status)
    print("Approval Reference Number:", approval_reference_number.upper())

num = int(input("How many Staff details wolud you like to put? "))
for i in range(num):
    print(f"\nEnter the details of staff {i + 1}: ")
    staff_info()
    requisition_approval()
    display_requisition()

