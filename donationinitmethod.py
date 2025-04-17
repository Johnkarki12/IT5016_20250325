class donationrequest:

    counter = 1000

    def __init__ (self, requester_name, project_name):
        self.requester_name = requester_name
        self.project_name = project_name
        self.requestID = self.generateID()
        self.list_of_items = {}
        self.total = 0
        self.priority = ""
        self.status = ""
        self.approval_ID = None

    def generateID(self):
        donationrequest.counter = donationrequest.counter + 1
        return donationrequest.counter

    def add_request_items(self):
        num = int(input("How many items are you requesting for? "))
        for i in range(num):
            item_name = input("Enter the name of item: ")
            price = float(input("Enter the price of item: "))

            self.list_of_items[item_name] = price
            self.total = sum(self.list_of_items.values())
            return self.total

    def approval(self):
        if "Family" in self.project_name:
            print("Hello")
            self.priority = "High"
            self.status = "Approved"
            self.approval_ID = str(self.requestID) + self.requester_name[-2:]
        else:
            self.priority = "Low"
            self.status = "Pending"

    def display_all_the_request(self):
        print ("Donation Details: ")
        print("Requester name: ", self.requester_name)
        print("Project name: ", self.project_name)
        print("Request ID", self.requestID)
        print("Total amount requested: ", self.total)
        print("Priority", self.priority)
        print("Status", self.status)
        if self.approval_ID:
            print("Approval ID: ", self.approval_ID)
        for k, v in self.list_of_items.items():
            print (f"{k}: {v}")
for i in range(20):
    rn = input("\nEnter requester name: ")
    pn = input("Enter the name of the project: ")

    request = donationrequest(rn, pn)
    request.add_request_items()
    request.approval()
    request.display_all_the_request()



