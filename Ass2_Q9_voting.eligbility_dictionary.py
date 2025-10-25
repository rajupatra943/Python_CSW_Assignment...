def check_voting_eligibility():
    voters = []
    n = int(input("Enter number of voters: "))

    for i in range(n):
        print(f"\nVoter {i+1}:")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        nationality = input("Enter nationality: ")
        voters.append((name, age, nationality))

    # a) Filter eligible voters
    eligible = list(filter(lambda v: v[1] >= 18 and v[2].lower() == "indian", voters))
    eligible_names = [v[0] for v in eligible]

    # b) Display count
    print("\n✅ Eligible:", eligible_names)
    print("🧮 Count:", len(eligible_names))

    # c) Dictionary comprehension
    result = {
        'Eligible': [v[0] for v in voters if v[1] >= 18 and v[2].lower() == "indian"],
        'Not Eligible': [v[0] for v in voters if not (v[1] >= 18 and v[2].lower() == "indian")]
    }

    print("\n📊 Eligibility Summary:")
    print(result)

# Run the program
check_voting_eligibility()

