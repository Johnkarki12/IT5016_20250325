import uuid  # For generating unique request IDs


def capture_request_info():
    """
    Captures the requester's name and project name.
    Generates a unique request ID.
    """
    requester_name = input("Enter the requester's name: ")
    project_name = input("Enter the project name: ")
    request_id = str(uuid.uuid4())[:8]  # Generate a short unique ID
    return requester_name, project_name, request_id



def capture_items_and_total():

    requester_name, project_name, request_id = capture_request_info()
    items = {}
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for {item_name}: $"))
            items[item_name] = price
        except ValueError:
            print("Invalid price. Please enter a number.")

    total_value = sum(items.values())
    return requester_name, project_name, request_id, items, total_value


def process_approval():
    """
    Determines approval status based on project name and total requested value.
    """
    requester_name, project_name, request_id, items, total_value = capture_items_and_total()
    status = "Pending"
    priority = "Low"
    approval_id = None

    if "family" in project_name.lower():
        priority = "High"
        status = "Approved"
        approval_id = request_id + requester_name[-2:]
    elif total_value < 500:
        priority = "Medium"
        status = "Approved"
        approval_id = request_id + requester_name[:2]

    return {
        "requester_name": requester_name,
        "project_name": project_name,
        "request_id": request_id,
        "items": items,
        "total_value": total_value,
        "status": status,
        "priority": priority,
        "approval_id": approval_id
    }


def display_request_summary():
    """
    Displays the full summary of the donation request.
    """
    result = process_approval()

    print("\n--- Donation Request Summary ---")
    print(f"Requester Name: {result['requester_name']}")
    print(f"Project Name: {result['project_name']}")
    print(f"Request ID: {result['request_id']}")
    print("Requested Items:")
    for item, price in result['items'].items():
        print(f"  - {item}: ${price:.2f}")
    print(f"Total Requested: ${result['total_value']:.2f}")
    print(f"Request Status: {result['status']}")
    print(f"Priority Level: {result['priority']}")
    if result['approval_id']:
        print(f"Approval ID: {result['approval_id']}")
    else:
        print("Approval ID: Not generated (Pending approval)")


# Run the full process
display_request_summary()
