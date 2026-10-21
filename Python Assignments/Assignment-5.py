# ============================================================
# LEVEL 1 — LOOP THINKING & range()
# ============================================================

# Q1. Predict the loop values
for i in range(2, 15, 3):
    print(i)


# Q2. Reverse range prediction
for i in range(15, 2, -3):
    print(i)


# Q3. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Q4. Print multiples of 3 from 3 to 18
for i in range(3, 19, 3):
    print(i)


# Q5. Print numbers from 20 down to 1
for i in range(20, 0, -1):
    print(i)


# Q6. Print all even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)


# Q7. Find the sum of numbers from start to end
start = int(input("Enter start: "))
end = int(input("Enter end: "))

total = 0
for i in range(start, end + 1):
    total += i

print("Sum =", total)


# Q8. Print the multiplication table of a number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Q9. Count numbers from 1 to N divisible by 3
n = int(input("Enter N: "))

count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1

print("Count =", count)


# Q10. Print squares from 1 to N
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i, "->", i * i)


# ============================================================
# LEVEL 2 — LOOP LOGIC
# ============================================================

# Q11. Find the factorial of a number
n = int(input("Enter a non-negative number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)


# Q12. Find the sum of the first N natural numbers
n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum =", total)


# Q13. Find the sum of even numbers from 1 to N
n = int(input("Enter N: "))

total = 0
for i in range(2, n + 1, 2):
    total += i

print("Sum of even numbers =", total)


# Q14. Find the sum of odd numbers from 1 to N
n = int(input("Enter N: "))

total = 0
for i in range(1, n + 1, 2):
    total += i

print("Sum of odd numbers =", total)


# Q15. Validate input and calculate factorial
n = int(input("Enter a non-negative number: "))

if n < 0:
    print("Invalid input")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print("Factorial =", factorial)


# Q16. Print all divisors of a positive integer
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


# Q17. Check whether a number is prime
n = int(input("Enter a number: "))

is_prime = n > 1

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")


# Q18. Count multiples of K up to N
n = int(input("Enter N: "))
k = int(input("Enter K: "))

count = 0

if k == 0:
    print("K cannot be zero")
else:
    for i in range(1, n + 1):
        if i % k == 0:
            count += 1

    print("Count =", count)


# Q19. Print even numbers up to N
n = int(input("Enter a positive number: "))

if n <= 0:
    print("Invalid input")
else:
    for i in range(2, n + 1, 2):
        print(i)


# Q20. Reverse a positive integer using arithmetic
num = int(input("Enter a positive integer: "))

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed number =", reversed_num)


# ============================================================
# LEVEL 3 — DIGIT-BASED QUESTIONS
# ============================================================

# Q21. Find the sum of digits
num = abs(int(input("Enter an integer: ")))

total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits =", total)


# Q22. Find the sum of factorials of digits
num = abs(int(input("Enter an integer: ")))

total = 0

if num == 0:
    total = 1
else:
    for _ in range(num):
        digit = num % 10

        digit_factorial = 1
        for i in range(1, digit + 1):
            digit_factorial *= i

        total += digit_factorial
        num //= 10

        if num == 0:
            break

print("Sum of digit factorials =", total)


# Q23. Count digits without converting the number to a string
num = abs(int(input("Enter an integer: ")))

count = 0

if num == 0:
    count = 1
else:
    for _ in range(num):
        count += 1
        num //= 10

        if num == 0:
            break

print("Digit count =", count)


# Q24. Find the product of digits
num = abs(int(input("Enter an integer: ")))

product = 1

if num == 0:
    product = 0
else:
    for _ in range(num):
        product *= num % 10
        num //= 10

        if num == 0:
            break

print("Product of digits =", product)


# Q25. Find the largest digit
num = abs(int(input("Enter an integer: ")))

largest = 0

for _ in range(max(1, num)):
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

    if num == 0:
        break

print("Largest digit =", largest)


# Q26. Find the smallest digit
num = abs(int(input("Enter an integer: ")))

smallest = 9

if num == 0:
    smallest = 0
else:
    for _ in range(num):
        digit = num % 10

        if digit < smallest:
            smallest = digit

        num //= 10

        if num == 0:
            break

print("Smallest digit =", smallest)


# Q27. Count even digits
num = abs(int(input("Enter an integer: ")))

count = 0

if num == 0:
    count = 1
else:
    for _ in range(num):
        if (num % 10) % 2 == 0:
            count += 1

        num //= 10

        if num == 0:
            break

print("Even digits =", count)


# Q28. Count odd digits
num = abs(int(input("Enter an integer: ")))

count = 0

while num > 0:
    if (num % 10) % 2 != 0:
        count += 1

    num //= 10

print("Odd digits =", count)


# Q29. Count digits divisible by 3
num = abs(int(input("Enter an integer: ")))

count = 0

while num > 0:
    if (num % 10) % 3 == 0:
        count += 1

    num //= 10

print("Digits divisible by 3 =", count)


# Q30. Check whether a number contains digit 5
num = abs(int(input("Enter an integer: ")))

found = False

while num > 0:
    if num % 10 == 5:
        found = True
        break

    num //= 10

print("Contains digit 5:", found)


# Q31. Count occurrences of a chosen digit
num = abs(int(input("Enter an integer: ")))
target = int(input("Enter digit to count (0-9): "))

count = 0

if num == 0 and target == 0:
    count = 1
else:
    while num > 0:
        if num % 10 == target:
            count += 1

        num //= 10

print("Occurrences =", count)


# Q32. Check whether a number is a palindrome
num = int(input("Enter a non-negative integer: "))

original = num
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

if original == reversed_num:
    print("Palindrome")
else:
    print("Not palindrome")


# Q33. Check whether a three-digit number is an Armstrong number
num = int(input("Enter a three-digit number: "))

original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit ** 3
    num //= 10

if total == original and 100 <= original <= 999:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# Q34. Print digits from right to left
num = abs(int(input("Enter an integer: ")))

if num == 0:
    print(0)
else:
    while num > 0:
        print(num % 10)
        num //= 10


# Q35. Find the difference between even-digit and odd-digit sums
num = abs(int(input("Enter an integer: ")))

even_sum = 0
odd_sum = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    num //= 10

print("Difference =", abs(even_sum - odd_sum))


# ============================================================
# LEVEL 4 — VALIDATION & NUMBER LOGIC
# ============================================================

# Q36. Check whether an integer is a three-digit number
num = int(input("Enter an integer: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")


# Q37. Print all factors of a number
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


# Q38. Find the HCF/GCD of two positive integers
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a <= 0 or b <= 0:
    print("Enter positive integers")
else:
    gcd = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    print("GCD =", gcd)


# Q39. Find the LCM of two positive integers
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a == 0 or b == 0:
    print("LCM = 0")
elif a < 0 or b < 0:
    print("Enter positive integers")
else:
    candidate = max(a, b)

    while candidate % a != 0 or candidate % b != 0:
        candidate += 1

    print("LCM =", candidate)


# Q40. Check whether a number is perfect
n = int(input("Enter a positive integer: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n and n > 0:
    print("Perfect number")
else:
    print("Not a perfect number")


# Q41. Find the first occurrence position of a digit from the right
num = abs(int(input("Enter an integer: ")))
target = int(input("Enter digit to find (0-9): "))

position = 1
found_position = -1

if num == 0 and target == 0:
    found_position = 1
else:
    while num > 0:
        if num % 10 == target:
            found_position = position
            break

        num //= 10
        position += 1

print("Position from right =", found_position)


# Q42. Check whether a number is a strong number
num = abs(int(input("Enter an integer: ")))

original = num
total = 0

if num == 0:
    total = 1

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    total += fact
    num //= 10

if total == original:
    print("Strong number")
else:
    print("Not a strong number")


# Q43. Reverse a number using arithmetic
num = abs(int(input("Enter an integer: ")))

reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print("Reversed number =", reversed_num)


# Q44. Check whether two numbers have the same digit sum
a = abs(int(input("Enter first integer: ")))
b = abs(int(input("Enter second integer: ")))

sum_a = 0
sum_b = 0

while a > 0:
    sum_a += a % 10
    a //= 10

while b > 0:
    sum_b += b % 10
    b //= 10

if sum_a == sum_b:
    print("Same digit sum")
else:
    print("Different digit sums")


# Q45. Print the first N Fibonacci numbers
n = int(input("How many Fibonacci numbers? "))

a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b


# ============================================================
# LEVEL 5 — STRING LOOPS
# ============================================================

# Q46. Count characters without using len()
text = input("Enter text: ")

count = 0

for char in text:
    count += 1

print("Character count =", count)


# Q47. Print the first and second halves of an even-length string
# without using slicing
text = input("Enter an even-length string: ")

length = 0
for char in text:
    length += 1

if length % 2 != 0:
    print("String length must be even")
else:
    first_half = ""
    second_half = ""
    index = 0

    for char in text:
        if index < length // 2:
            first_half += char
        else:
            second_half += char

        index += 1

    print("First half =", first_half)
    print("Second half =", second_half)


# Q48. Check whether a string is a palindrome
text = input("Enter text: ")

length = 0
for char in text:
    length += 1

is_palindrome = True

for i in range(length // 2):
    if text[i] != text[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")


# Q49. Print the first half of a string
text = input("Enter text: ")

length = 0
for char in text:
    length += 1

first_half = ""

for i in range(length // 2):
    first_half += text[i]

print(first_half)


# Q50. Count vowels in a string
text = input("Enter text: ")

count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Vowel count =", count)


# Q51. Count consonants in a string
text = input("Enter text: ")

count = 0

for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        count += 1

print("Consonant count =", count)


# Q52. Check whether the two halves of an even-length string match
text = input("Enter an even-length string: ")

length = 0
for char in text:
    length += 1

if length % 2 != 0:
    print("String length must be even")
else:
    same = True

    for i in range(length // 2):
        if text[i] != text[i + length // 2]:
            same = False
            break

    if same:
        print("Halves match")
    else:
        print("Halves do not match")


# Q53. Find the second-largest distinct digit
num = abs(int(input("Enter an integer: ")))

largest = -1
second_largest = -1

if num == 0:
    largest = 0
else:
    for _ in range(num):
        digit = num % 10

        if digit > largest:
            second_largest = largest
            largest = digit
        elif digit != largest and digit > second_largest:
            second_largest = digit

        num //= 10

        if num == 0:
            break

if second_largest == -1:
    print("No second-largest distinct digit")
else:
    print("Second-largest distinct digit =", second_largest)


# Q54. Count uppercase and lowercase letters
text = input("Enter text: ")

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Uppercase =", upper_count)
print("Lowercase =", lower_count)


# Q55. Count a chosen character and calculate frequency percentage
text = input("Enter text: ")
target = input("Enter a character: ")

count = 0
length = 0

for char in text:
    length += 1

    if char == target:
        count += 1

if length == 0:
    frequency = 0
else:
    frequency = round(count / length * 100, 2)

print(f"Count = {count}, Frequency = {frequency}%")


# ============================================================
# LEVEL 6 — STRING ANALYSIS
# ============================================================

# Q56. Remove spaces by building a new string
text = input("Enter text: ")

result = ""

for char in text:
    if char != " ":
        result += char

print(result)


# Q57. Count words in a sentence (single spaces between words)
text = input("Enter a sentence: ").strip()

if text == "":
    words = 0
else:
    words = 1

    for char in text:
        if char == " ":
            words += 1

print("Word count =", words)


# Q58. Check whether two strings are equal using one comparison loop
first = input("Enter first string: ")
second = input("Enter second string: ")

same = True

if len(first) != len(second):
    same = False
else:
    for i in range(len(first)):
        if first[i] != second[i]:
            same = False
            break

if same:
    print("Strings are equal")
else:
    print("Strings are not equal")


# Q59. Print i * (i + 1) for i from 1 to 5
for i in range(1, 6):
    print(i * (i + 1))


# Q60. Count how many times a loop runs
count = 0

for i in range(1, 6):
    count += 1

print("Loop runs", count, "times")


# Q61. Sum numbers from 1 to N
n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Total =", total)


# ============================================================
# LEVEL 7 — DATA ANALYSIS USING LOOPS
# ============================================================

# Q62. Expense analyzer: total, average, highest, and lowest
days = int(input("Enter number of days: "))

expenses = []

for i in range(days):
    expense = float(input(f"Expense for day {i + 1}: "))
    expenses.append(expense)

if days <= 0:
    print("Enter at least one day")
else:
    total = 0
    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:
        total += expense

        if expense > highest:
            highest = expense

        if expense < lowest:
            lowest = expense

    print("Total =", total)
    print("Average =", total / days)
    print("Highest =", highest)
    print("Lowest =", lowest)


# Q63. Count days where expense is above a given limit
days = int(input("Enter number of days: "))

expenses = []

for i in range(days):
    expense = float(input(f"Expense for day {i + 1}: "))
    expenses.append(expense)

limit = float(input("Enter expense limit: "))

count = 0

for expense in expenses:
    if expense > limit:
        count += 1

print("Days above limit =", count)


# Q64. Count pass and fail results (pass mark is 40)
n = int(input("Enter number of students: "))

pass_count = 0
fail_count = 0

for i in range(n):
    marks = float(input(f"Marks of student {i + 1}: "))

    if marks >= 40:
        pass_count += 1
    else:
        fail_count += 1

print("Passed =", pass_count)
print("Failed =", fail_count)


# Q65. Find the average of N marks
n = int(input("Enter number of students: "))

total = 0

for i in range(n):
    marks = float(input(f"Marks of student {i + 1}: "))
    total += marks

if n > 0:
    print("Average marks =", total / n)
else:
    print("No marks entered")


# Q66. Calculate total cost for a quantity and price per item
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = 0

for _ in range(quantity):
    total += price

print("Total cost =", total)


# Q67. Calculate success rate as a percentage
total_students = int(input("Enter total students: "))
successful = int(input("Enter number of successful students: "))

if total_students > 0:
    success_rate = successful / total_students * 100
    print("Success rate =", round(success_rate, 2), "%")
else:
    print("Total students must be greater than zero")


# ============================================================
# LEVEL 8 — ONE-LOOP CHALLENGES
# ============================================================

# Q68. Count digits, sum digits, and count even digits
num = abs(int(input("Enter an integer: ")))

digit_count = 0
digit_sum = 0
even_digit_count = 0

if num == 0:
    digit_count = 1
    even_digit_count = 1
else:
    for _ in range(num):
        digit = num % 10

        digit_count += 1
        digit_sum += digit

        if digit % 2 == 0:
            even_digit_count += 1

        num //= 10

        if num == 0:
            break

print("Digit count =", digit_count)
print("Digit sum =", digit_sum)
print("Even digit count =", even_digit_count)


# Q69. Count uppercase, lowercase, vowels, consonants,
# and characters at even indexes in one loop.
# Spaces count as characters for even-index counting.
text = input("Enter text: ")

uppercase = 0
lowercase = 0
vowels = 0
consonants = 0
even_index_chars = 0

for index, char in enumerate(text):
    if char.isupper():
        uppercase += 1

    if char.islower():
        lowercase += 1

    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

    if index % 2 == 0:
        even_index_chars += 1

print("Uppercase =", uppercase)
print("Lowercase =", lowercase)
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Characters at even indexes =", even_index_chars)