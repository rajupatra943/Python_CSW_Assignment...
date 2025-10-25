def highest_average_student():
    students = {}
    n = int(input("Enter number of students: "))

    print("\n👉 Example: For scores, enter like → 85, 90, 92")

    for _ in range(n):
        name = input("\nEnter student name: ")
        scores_input = input(f"Enter scores for {name} separated by commas: ")
        try:
            scores = [int(s.strip()) for s in scores_input.split(",") if s.strip()]
            students[name] = scores
        except ValueError:
            print("Invalid score input. Please enter integers only.")
            return

    highest_avg = 0
    top_student = ""

    print("\n📊 Average Scores:")
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        print(f"{name}: {avg:.2f}")
        if avg > highest_avg:
            highest_avg = avg
            top_student = name

    print(f"\n🏆 Top student based on average score: {top_student}")

# Run the function
highest_average_student()