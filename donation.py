counter = 1000
def id_generator():
    global counter
    id = counter + 1
    return id

def make_request():
    name = input("Enter your name: ")
    project = input("Please! Provide the name of the project: ")
    amount = int(input("Donation Amount: "))
    id = id_generator()
    return name,project,amount,id

for i in range(2):
    print(make_request)

def donation_details():
    detail = {}
    num = int(input("How many items are you packing: "))

    for i in range(num):
        item = input("Enter item name: ")
        price = int(input("Enter the price: "))
        detail [item] = price
    total = 0
    for price in detail.values():
        total = total + price
    return total

def decision():
    priority = ""
    status = ""
    name, project, amount, id = make_request()
    approval_id = ""

    if "Family" in project:
        priority = "High"
        status = "Approved"
        new_id = str(id)
        approval_id = new_id + name[-2:]
    return name, project, priority, status, approval_id
print(decision())












