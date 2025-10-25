import math

# Helper functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return int(math.sqrt(n)) ** 2 == n

def is_perfect_cube(n):
    return round(n ** (1/3)) ** 3 == n

# Classification function
def classify_numbers(numbers):
    classification = {
        "Prime": [],
        "Composite": [],
        "Perfect Squares": [],
        "Perfect Cubes": []
    }

    for num in numbers:
        if is_prime(num):
            classification["Prime"].append(num)
        elif num > 1:
            classification["Composite"].append(num)

        if is_perfect_square(num):
            classification["Perfect Squares"].append(num)

        if is_perfect_cube(num):
            classification["Perfect Cubes"].append(num)

    return classification

# Take user input with validation
try:
    user_input = input("Enter a list of integers separated by commas: ").strip()
    if not user_input:
        raise ValueError("Empty input")
    
    # Convert input to list of integers, ignoring empty entries
    input_list = [int(x.strip()) for x in user_input.split(",") if x.strip()]
    
    # Classify and display results
    result = classify_numbers(input_list)
    print("\nClassification Result:")
    for category, values in result.items():
        print(f"{category}: {values}")

except ValueError:
    print("Invalid input. Please enter only integers separated by commas.")