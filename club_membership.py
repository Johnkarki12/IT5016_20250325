class club_membership:
    counter = 10000
    total_registered = 0
    total_approved = 0
    total_pending = 0

    def __init__(self, name):
        self.name = name
        self.member_id = self.generate_id()
        self.add_on =  {}
        self.total = 100
        self.approval = ""
        club_membership.total_registered += 1


    def generate_id(self):
        club_membership.counter += 1
        return club_membership.counter

    def request_add_on(self):
        num = int(input("How many add on you want: "))
        for i in range(num):
            add_on_name = input("Name of add on: ")
            price = float(input("Enter the price: "))
            self.add_on[add_on_name] = price
        self.total = sum(self.add_on.values()) + 100
        return self.total

    def approve(self, name):
        if self.total <= 1000:
            self.approval = "Approved"
            club_membership.total_approved += 1
        else:
            self.approval = "Pending"
            club_membership.total_pending += 1

    def display(self):
        print("Name: ", self.name)
        print("ID: ", self.member_id)
        print("Total: ", self.total)
        print("Status: ", self.approval)

        for add_on, price in self.add_on.items():
            print(add_on, ":", price)

name = input("Enter your name: ")
membership = club_membership(name)
membership.request_add_on()
membership.request_add_on()
membership.display()

print("Total registered: ",club_membership.total_registered )
print("Total approved:", club_membership.total_approved)
print("Total pending: ", club_membership.total_pending)



