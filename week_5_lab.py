def calculate_result(*marks):
    """
    This function accepts any number of student marks,
    calculates the average, and determines if the student has passed or failed.
    """

    # Check if any marks were passed in
    if len(marks) == 0:
        print("No marks provided.")
        return

    # Calculate the total of all marks using the sum() function
    total = sum(marks)

    # Calculate the average by dividing the total by the number of marks
    average = total / len(marks)

    # Print the average for the user
    print(f"Average mark: {average:.2f}")

    # Determine if the student has passed (pass mark is 50 or more)
    if average >= 50:
        print("Result: Passed")
    else:
        print("Result: Failed")


calculate_result(65, 70, 55, 80)  # Should print average and "Passed"
calculate_result(40, 45, 30)  # Should print average and "Failed"

import random  # Import the random module


def generate_unique_random_numbers():
    """
    This function generates random numbers from 1 to 20 without repetition.
    It returns the list of randomly ordered numbers.
    """

    numbers = random.sample(range(1, 21), 20)

    # Print the generated numbers
    print("Random numbers from 1 to 20 :")
    print(numbers)

    return numbers  # Return the list in case it's needed for other use


# Example usage
generate_unique_random_numbers()

def calculate_average_score(**subject_scores):
    """
    This function accepts subject scores using keyword arguments (**kwargs),
    calculates the average, and prints the result.
    """

    # Check if any scores were provided
    if not subject_scores:
        print("No scores provided.")
        return

    # Calculate the total score
    total_score = sum(subject_scores.values())

    # Count the number of subjects
    num_subjects = len(subject_scores)

    # Calculate the average
    average = total_score / num_subjects

    # Printing the subject scores
    print("Subject Scores:")
    for subject, score in subject_scores.items():
        print(f"{subject}: {score}")

    # Printing the average score
    print(f"\nAverage Score: {average:.2f}")

# Example usage with the given values
calculate_average_score(IT5014=60, IT7809=80, IT6798=50, IT5048=70)
