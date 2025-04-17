class Ticket:
    ticket_counter = 0
    tickets = []

    def __init__(self, date, employee_id, employee_name, issue_des):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.date = date
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.issue_des = issue_des
        self.status = "In Progress"
        self.priority = self.assign_priority()
        self.resolution_message = None
        if"password reset" in self.issue_des.lower():
            self.auto_password_reset()
        Ticket.tickets.append(self)

    def assign_priority(self):
        issues = ["system outage", "network failure"]
        for des in issues:
            if des in self.issue_des.lower():
                return "High"
        return "Low" 

    def auto_password_reset(self):
        password = self.employee_id[:-2] + self.employee_name[:-2]
        self.status = "Resolved"
        self.resolution_message = f"Password reset completed! Your new password {password}"
    @classmethod

    def ticket_statistics(self):
        total_submitted = len(Ticket.tickets)
        resloved_ticket = 0
        total_in_progress = 0
        total_closed = 0
        for each_ticket in Ticket.tickets:
            if each_ticket.status == "Resolved":
                resloved_ticket += 1
            elif each_ticket.status == "In progress":
                total_in_progress += 1
            elif each_ticket.status == "Closed":
                total_closed += 1

        print("\n----------Statistics-----------")
        print("Total tickets: ", total_submitted)
        print("Total in progress: ", total_in_progress)
        print("Total closed: ", total_closed)
        print("Total ticket Resolved: ", resloved_ticket)
    @classmethod

    def display_tickets(cls):
        for ticket in Ticket.tickets:
            print("Date: ", ticket.date)
            print("Ticket ID: ", ticket.ticket_id )
            print("Employee ID: ", ticket.employee_id)
            print("Name: ", ticket.employee_name)
            print("Issue: ", ticket.issue_des)
            print("Priority: ", ticket.priority)
            print("Status: ", ticket.status)
            print("Resolution: ", ticket.resolution_message)

num_tickets = int(input("How many tickets do you want to create? "))

# Use a for loop to collect the specified number of tickets
for _ in range(num_tickets):
    date = input("Enter ticket date (MM/DD/YYYY): ")
    employee_id = input("Enter employee ID: ")
    employee_name = input("Enter employee name: ")
    issue_des = input("Enter issue description: ")

    # Create a new ticket with the input values
    Ticket(date, employee_id, employee_name, issue_des)

Ticket.display_tickets()
Ticket.ticket_statistics()







