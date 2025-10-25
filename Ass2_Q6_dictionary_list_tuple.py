def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_dictionary(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, list):
            prime_sum = sum(x for x in value if is_prime(x))
            result[key] = prime_sum
        elif isinstance(value, tuple):
            product = 1
            has_odd = False
            for x in value:
                if x % 2 != 0:
                    product *= x
                    has_odd = True
            result[key] = product if has_odd else 0
        else:
            result[key] = None  # Handle unexpected types
    return result

# Example input
data = {
    "A": [2, 3, 4, 5, 10],
    "B": (1, 2, 3, 4, 5),
    "C": [7, 8, 9],
    "D": (6, 7, 8)
}

# Process and display result
processed = process_dictionary(data)
print("Processed Dictionary:")
for k, v in processed.items():
    print(f"{k}: {v}")

