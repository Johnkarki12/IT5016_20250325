def capture_donation_request():
    requester_name = input("Enter your name: ")
    project_name = input("Enter the project name: ")
    request_id = requester_name[:3] + project_name[:3]

    return requester_name, project_name, request_id


def collect_request_items():

    requester_name, project_name, request_id = capture_donation_request()

    total_requested = 0
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        price = float(input(f"Enter price for {item_name}: "))
        total_requested += price

    return requester_name, project_name, request_id, total_requested


def approve_request():
    requester_name, project_name, request_id, total_requested = collect_request_items()

    if "Family" in project_name:
        priority = "High"
        approval_status = "Approved"
        approval_id = request_id + requester_name[-2:]
    elif total_requested < 500:
        priority = "Medium"
        approval_status = "Approved"
        approval_id = request_id + requester_name[:2]
    else:
        priority = "Low"
        approval_status = "Pending"
        approval_id = "N/A"

    print("\nDonation Request Summary:")
    print(f"Requester Name: {requester_name}")
    print(f"Project Name: {project_name}")
    print(f"Request ID: {request_id}")
    print(f"Total Amount Requested: ${total_requested}")
    print(f"Priority Level: {priority}")
    print(f"Approval Status: {approval_status}")
    print(f"Approval ID: {approval_id}")

approve_request()






























