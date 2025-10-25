def process_numbers():
    # Step a: Accept input from user
    user_input = input("Enter a list of integers separated by commas: ")
    numbers = [int(x.strip()) for x in user_input.split(",") if x.strip()]

    # Step b: Remove duplicates using set comprehension
    unique_numbers = {x for x in numbers}

    # Step c: Frequency dictionary using dictionary comprehension
    freq_dict = {x: numbers.count(x) for x in unique_numbers}

    # Step d: Sort numbers by descending frequency using lambda
    sorted_by_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

    # Display results
    print("\n✅ Unique Numbers (Set):", unique_numbers)
    print("📊 Frequency Dictionary:", freq_dict)
    print("🔽 Numbers Sorted by Frequency (High to Low):")
    for num, freq in sorted_by_freq:
        print(f"{num} → {freq} times")

# Run the program
process_numbers()