def process_student_profiles():
    students = []
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\nStudent {i+1}:")

        # Input student info
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        info = (student_id, name)

        # Input marks
        marks_input = input("Enter marks separated by commas (e.g., 85,90,88): ")
        marks = [int(m.strip()) for m in marks_input.split(",") if m.strip()]

        # Input skills
        skills_input = input("Enter skills separated by commas (e.g., Python, Java): ")
        skills = {s.strip() for s in skills_input.split(",") if s.strip()}

        # Build student profile
        student = {
            "info": info,
            "marks": marks,
            "skills": skills
        }
        students.append(student)

    # Process data
    skill_counter = {}
    top_student = ""
    top_avg = 0.0

    print("\n📚 Student Averages:")
    for student in students:
        student_id, name = student["info"]
        marks = student["marks"]
        skills = student["skills"]

        avg = sum(marks) / len(marks)
        print(f"{name} (ID: {student_id}) → Average Marks: {avg:.2f}")

        if avg > top_avg:
            top_avg = avg
            top_student = name

        for skill in skills:
            skill_counter[skill] = skill_counter.get(skill, 0) + 1

    print("\n🛠️ Skill Frequency Across Students:")
    for skill, count in skill_counter.items():
        print(f"{skill}: {count}")

    print(f"\n🏆 Top-Performing Student: {top_student} with average {top_avg:.2f}")

# Run the program
process_student_profiles()