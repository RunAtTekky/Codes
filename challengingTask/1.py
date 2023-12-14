def determine_health_status(weight, height):
    if 30 <= weight <= 45 and height == 150:
        return "Healthy"
    elif 46 <= weight <= 60 and height == 160:
        return "Average Health"
    elif 61 <= weight <= 100 and height == 175:
        return "Not Healthy"
    else:
        return "Invalid input"

num_student = 10
num_student = int(input())
for student in range(1,num_student+1):
    print(f"\nStudent{student}")
    weight = float(input("Enter weight (kg): "))
    height = int(input("Enter height (cm): "))

    health_status = determine_health_status(weight,height)
    print(f"Health status: {health_status}")
