# Student scores list
scores = [85, 92, 78, 64, 99, 73, 88, 91, 67, 76]

# i. Calculate and display the average score
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")

# ii. Find and display the minimum and maximum scores
min_score = min(scores)
max_score = max(scores)
print(f"Minimum score: {min_score}")
print(f"Maximum score: {max_score}")

# iii. Display all scores above the average
above_average = [score for score in scores if score > average]
print("Scores above average:", above_average)

# iv. Sort the list in descending order
sorted_desc = sorted(scores, reverse=True)
print("Scores in descending order:", sorted_desc)

# v. Replace the three lowest scores with zero
# Make a copy to preserve the original list
modified_scores = scores.copy()
for _ in range(3):
    min_val = min(modified_scores)
    min_index = modified_scores.index(min_val)
    modified_scores[min_index] = 0

print("Scores after replacing three lowest with 0:", modified_scores)