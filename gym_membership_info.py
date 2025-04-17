member_counter = 0  # Global counter to track membership IDs

def gym_member_info():
    global member_counter
    member_counter += 1  # Increment counter for a unique ID

    date = input("Enter registration date (YYYY-MM-DD): ")
    member_name = input("Enter member's full name: ")
    membership_id = f"GYM{member_counter:03d}"  # Generate unique Membership ID

    return {"Date": date, "Member Name": member_name, "Membership ID": membership_id}


def gym_membership_fees_total():
    member_info = gym_member_info()

    add_ons = {}  # Dictionary to store add-ons and their prices
    total_cost = 0

    while True:
        add_on = input("Enter membership add-on (or type 'done' to finish): ")
        if add_on.lower() == "done":
            break
        price = float(input(f"Enter price for {add_on}: $"))
        add_ons[add_on] = price
        total_cost += price

    member_info["Total Cost"] = total_cost
    member_info["Add-ons"] = add_ons
    return member_info


def gym_membership_approval():
    member_data = gym_membership_fees_total()
    total_cost = member_data["Total Cost"]

    # Default status
    member_data["Status"] = "Pending"

    if total_cost < 1000:
        member_id = member_data["Membership ID"]
        approval_ref = f"{member_id}{member_id[-3:]}"
        member_data["Status"] = "Approved"
        member_data["Approval Reference"] = approval_ref
    else:
        member_data["Status"] = "Pending"

    return member_data