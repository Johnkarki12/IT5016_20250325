# Global counter for unique requisition ID
counter = 1


class RequisitionSystem:
    def __init__(self):
        global counter
        # Staff info
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.requisition_id = 10000 + counter
        counter += 1

        # Items details
        self.items = {}
        self.total = 0
        self.status = ""
        self.approval_reference_number = ""

    def staff_info(self):
        """Method for the staff to input their information"""
        self.date = input("\nEnter the date (DD/MM/YYYY): ")
        self.staff_id = input("Enter Staff ID: ")
        self.staff_name = input("Enter Staff name: ")

        print("\nPrinting Staff Information:")
        print("Date:", self.date)
        print("Staff ID:", self.staff_id.upper())
        print("Staff Name:", self.staff_name.capitalize())
        print("Requisition ID:", self.requisition_id)

    def requisition_details(self):
        """Accepts a list of requisition items and returns the total"""
        num = int(input("\nHow many items: "))
        for i in range(num):
            item = input(f"Name of item {i + 1}: ")
            price = float(input("Enter price for " + item + ": "))
            self.items[item] = price
            self.total += price

        print("\nItems details:")
        for item, price in self.items.items():
            print(item.capitalize(), price)

        return self.total

    def requisition_approval(self):
        """Checks if the requisition is approved based on the total"""
        self.requisition_details()  # get the total
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference_number = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference_number = "Not available"

        print("\nTotal: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference_number.upper())

    def respond_requisition(self):
        """Manager can approve or reject a pending requisition"""
        if self.status == "Pending":
            response = input("\nManager, do you approve this requisition? (yes/no): ").lower()
            if response == "yes":
                self.status = "Approved"
            elif response == "no":
                self.status = "Not approved"
            else:
                self.status = "Pending"
            print("\nUpdated Status:", self.status)

    def display_requisitions(self):
        """Displays all requisition details"""
        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id.upper())
        print("Staff Name:", self.staff_name.capitalize())
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference_number.upper())
        print(" ")  # Printing empty line for space

    def requisition_statistic(self, requisitions):
        approved_count = 0
        pending_count = 0
        not_approved_count = 0

        for requisition in requisitions:
            if requisition.status == "Approved":
                approved_count += 1
            elif requisition.status == "Pending":
                pending_count += 1
            else:
                not_approved_count += 1

        # Display statistics
        print("------Statistics------:")
        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", num)
        print("The total number of approved requisitions:", approved_count)
        print("The total number of pending requisitions:", pending_count)
        print("The total number of not approved requisitions:", not_approved_count)



def display_all_requisitions(requisitions):
    print("\nPrinting Requisitions:")
    for req in requisitions:
        req.display_requisitions()


# List to hold all requisition objects
requisitions = []

num = int(input("How many staff requisitions would you like to enter? "))


for i in range(num):
    print(f"\nEntering details for staff {i + 1}")
    req = RequisitionSystem()
    req.staff_info()
    req.requisition_approval()
    req.respond_requisition()
    requisitions.append(req)

display_all_requisitions(requisitions)

req.requisition_statistic(requisitions)
