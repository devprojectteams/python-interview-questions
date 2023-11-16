# Answers to the interview questions

# Define a function to count the occurrences of each color
def count_colors(table):
    colors = {}
    for row in table.find_all('td')[1::2]:
        for color in row.text.split():
            colors[color] = colors.get(color, 0) + 1
    return colors

# Calculate the mean color
mean_color = sum(counts.values()) / len(counts)
print("Mean color:", mean_color)

# Find the color worn most
mostly_worn_color = max(counts, key=counts.get)
print("Color worn most:", mostly_worn_color)

# Find the median color
sorted_colors = sorted(counts.values())
if len(sorted_colors) % 2 == 0:
    median = (sorted_colors[len(sorted_colors) // 2 - 1] + sorted_colors[len(sorted_colors) // 2]) / 2
else:
    median = sorted_colors[len(sorted_colors) // 2]
print("Median color:", median)

# Calculate the variance of the colors
mean_color = sum(counts.values()) / len(counts)
variance = sum((color - mean_color) ** 2 for color in counts.values()) / len(counts)
print("Variance of colors:", variance)

# Calculate the probability of red
red_count = counts.get("RED", 0)
total_count = sum(counts.values())
red_probability = red_count / total_count
print("Probability of red:", red_probability)

# Save the colors and their frequencies to a PostgreSQL database
import psycopg2

conn = psycopg2.connect(
    database="bincom_colors", user="bincom_user", password="bincom_password", host="bincom_host", port="5432"
)

cursor = conn.cursor()

sql = "INSERT INTO colors (color, count) VALUES (%s, %s)"
for color, count in counts.items():
    cursor.execute(sql, (color, count))
conn.commit()

cursor.close()
conn.close()


# Recursive searching algorithm
def recursive_search(arr, target, start):
    if start >= len(arr):
        return -1
    if arr[start] == target:
        return start
    return recursive_search(arr, target, start + 1)

# Example usage
print(recursive_search([1, 2, 3, 4, 5], 3, 0))


# Generate random number
import random

def generate_random_number():
    digits = [0, 1]
    number = ""
    for I in range(4):
        number += str(random.choice(digits))
    return int(number)

# Example usage
print(generate_random_number())


# Sum of first 50 Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Calculate the sum of the first 50 Fibonacci numbers
sum = 0
for I in range(50):
    sum += fibonacci(i)
print("Sum of first 50 Fibonacci numbers:", sum)