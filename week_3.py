
num_list = list(range(1, 11))

# Input student info
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = int(input("Enter student grade: "))

student_info = {
    'name': name,
    'age': age,
    'grade': grade
}

index = 0
while index < len(num_list):
    print(num_list[index])
    index += 1

print("Student Information:")
for key, value in student_info.items():
    print(f"{key.capitalize()}: {value}")

if student_info['grade'] >= 80:
    print("Pass")
else:
    print("Fail")
