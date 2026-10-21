# ============================================================
# LEVEL 1 — BASIC PATTERNS
# ============================================================

# Q1. Solid Square
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()


# Q2. Solid Rectangle
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()


# Q3. Increasing Star Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print("*" * i)


# Q4. Increasing Number Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q5. Repeated Number Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(str(i) * i)


# Q6. Repeated Alphabet Triangle
n = int(input("Enter size (maximum 26): "))
for i in range(n):
    print(chr(65 + i) * (i + 1))


# Q7. Alphabet Triangle
n = int(input("Enter size (maximum 26): "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# Q8. Continuous Number Triangle
n = int(input("Enter size: "))
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# Q9. Alternating 0–1 Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    for j in range(i):
        print(1 if (i + j) % 2 == 0 else 0, end=" ")
    print()


# Q10. Decreasing Star Triangle
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print("*" * i)


# Q11. Decreasing Number Triangle
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q12. Decreasing Alphabet Triangle
n = int(input("Enter size (maximum 26): "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# ============================================================
# LEVEL 2 — SPACES AND ALIGNMENT
# ============================================================

# Q13. Right-Aligned Half Pyramid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# Q14. Inverted Right-Aligned Half Pyramid
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)


# Q15. Star Pyramid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Q16. Inverted Star Pyramid
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Q17. Solid Diamond
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Q18. Rhombus
n = int(input("Enter size: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * n)


# Q19. Mirrored Number Pattern
n = int(input("Enter size: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print(" " * (2 * (n - i)), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()


# Q20. Centered Number Pyramid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Q21. Palindromic Number Pyramid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()


# Q22. Alphabet Palindrome Pyramid
n = int(input("Enter size (maximum 26): "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()


# Q23. Reverse-Starting Alphabet Triangle
n = int(input("Enter size (maximum 26): "))
for i in range(n):
    for j in range(n - i, n + 1):
        print(chr(64 + j), end=" ")
    print()


# ============================================================
# LEVEL 3 — MIXED LOGIC AND REPEATED SEQUENCES
# ============================================================

# Q24. Increasing and Decreasing Star Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)


# Q25. Number Hourglass
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(2, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q26. Alphabet Hourglass
n = int(input("Enter size (maximum 26): "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
for i in range(2, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


# Q27. Alternating Star and Hash Grid
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        print("*" if (i + j) % 2 == 0 else "#", end="")
    print()


# Q28. Binary Checkerboard
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        print(1 if (i + j) % 2 == 0 else 0, end="")
    print()


# Q29. Multiplication Grid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end=" ")
    print()


# Q30. Alternating-Direction Rows
n = int(input("Enter size: "))
for i in range(1, n + 1):
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(i, 0, -1):
            print(j, end="")
    print()


# Q31. Number Diamond
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()


# Q32. Concentric Number Square
n = int(input("Enter size: "))
width = 2 * n - 1
for i in range(width):
    for j in range(width):
        layer = min(i, j, width - 1 - i, width - 1 - j)
        print(n - layer, end=" ")
    print()


# ============================================================
# LEVEL 4 — HOLLOW PATTERNS AND CONDITIONS
# ============================================================

# Q33. Hollow Square
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q34. Hollow Rectangle
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q35. Hollow Number Square
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("1", end="")
        else:
            print("0", end="")
    print()


# Q36. Hollow Right-Angled Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q37. Hollow Inverted Triangle
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q38. Hollow Pyramid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q39. Hollow Diamond
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")


# Q40. X Pattern
n = int(input("Enter odd size: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q41. Cross Pattern
n = int(input("Enter odd size: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q42. Star Cross with Four Arms
n = int(input("Enter odd size: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# ============================================================
# LEVEL 5 — ADVANCED SHAPES AND CHALLENGES
# ============================================================

# Q43. Butterfly Pattern
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


# Q44. Hollow Hourglass
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
for i in range(2, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")


# Q45. Alphabet Diamond
n = int(input("Enter size (maximum 26): "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end="")
    print()


# Q46. Pascal's Triangle
n = int(input("Enter rows: "))
for i in range(n):
    print(" " * (n - i - 1), end="")
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i - j) // (j + 1)
    print()


# Q47. Heart Pattern
n = int(input("Enter size (minimum 4): "))
for i in range(n // 2, n + 1, 2):
    print(" " * ((n - i) // 2), end="")
    print("*" * i, end="")
    print(" " * (n - i), end="")
    print("*" * i)
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))


# Q48. Hollow Heart
n = int(input("Enter size (minimum 4): "))
for i in range(n // 2, n + 1, 2):
    print(" " * ((n - i) // 2), end="")
    for j in range(i):
        print("*" if j == 0 or j == i - 1 else " ", end="")
    print(" " * (n - i), end="")
    for j in range(i):
        print("*" if j == 0 or j == i - 1 else " ", end="")
    print()
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    if i == n:
        print("*" + " " * (2 * i - 2) + "*")
    elif i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 2) + "*")


# Q49. Star-and-Space Center Pattern
n = int(input("Enter odd size: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1 or i == n // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q50. Custom Symbol Square
n = int(input("Enter size: "))
symbol = input("Enter symbol: ")
for i in range(n):
    for j in range(n):
        print(symbol, end="")
    print()


# Q51. User-Sized Hollow Rectangle
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q52. Create Your Own Pattern — Increasing Symbol Triangle
n = int(input("Enter size: "))
symbol = input("Enter symbol: ")
for i in range(1, n + 1):
    print(symbol * i)


# ============================================================
# LEVEL 6 — ADDITIONAL PATTERNS
# ============================================================

# Q53. Number Increasing Reverse Pyramid
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Q54. Square Fill Pattern
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# Q55. Left Half Pyramid
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Q56. Reverse Right Half Pyramid
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print("*" * i)


# Q57. Left Half Pyramid — Increasing
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print("*" * i)


# Q58. Reverse Left Half Pyramid
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)


# Q59. Triangle Star Pattern
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# Q60. Mirror-Image Number Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print(" " * (i - 1), end="")
    for j in range(i, n + 1):
        print(j, end=" ")
    print()


# Q61. Hollow Reverse Triangle
n = int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if j == i or j == 0 or i == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Q62. Hollow Diamond Pyramid
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")


# Q63. Hollow Hourglass Pattern
n = int(input("Enter size: "))
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
for i in range(2, n + 1):
    print(" " * (n - i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")


# Q64. Right Pascal's Triangle
n = int(input("Enter size: "))
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)


# Q65. Pattern Size Challenge
# Run this program with N = 3, N = 5, and N = 7.
n = int(input("Enter size (try 3, 5, 7): "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# ============================================================
# PART 2 — STATEMENT-BASED LOGIC PRACTICE
# ============================================================

# Q66. Count Digits
n = abs(int(input("Enter integer: ")))
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print(count)


# Q67. Sum of Digits
n = abs(int(input("Enter integer: ")))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)


# Q68. Product of Digits
n = abs(int(input("Enter integer: ")))
product = 1
if n == 0:
    product = 0
else:
    while n > 0:
        product *= n % 10
        n //= 10
print(product)


# Q69. Reverse a Number
n = abs(int(input("Enter integer: ")))
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
print(reverse)


# Q70. Palindrome Number
n = int(input("Enter integer: "))
original = abs(n)
temp = original
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
print(original == reverse)


# Q71. Prime Number
n = int(input("Enter integer: "))
prime = n >= 2
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
print(prime)


# Q72. Primes from 1 to N
n = int(input("Enter N: "))
for num in range(2, n + 1):
    prime = True
    for j in range(2, num):
        if num % j == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()


# Q73. First N Fibonacci Numbers
n = int(input("Enter N: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# Q74. GCD of Two Numbers
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
while b != 0:
    a, b = b, a % b
print(a)


# Q75. LCM of Two Numbers
a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))
x, y = a, b
while y != 0:
    x, y = y, x % y
print(a * b // x)


# ============================================================
# LEVEL 2 — BASIC STRING LOGIC
# ============================================================

# Q76. Length of a String
s = input("Enter string: ")
length = 0
for ch in s:
    length += 1
print(length)


# Q77. Print Each Character
s = input("Enter string: ")
for ch in s:
    print(ch)


# Q78. Count Vowels
s = input("Enter string: ")
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)


# Q79. Count Consonants
s = input("Enter string: ")
count = 0
for ch in s:
    if ("a" <= ch <= "z" or "A" <= ch <= "Z") and ch not in "aeiouAEIOU":
        count += 1
print(count)


# Q80. Convert to Uppercase
s = input("Enter string: ")
print(s.upper())


# Q81. Convert to Lowercase
s = input("Enter string: ")
print(s.lower())


# Q82. Reverse a String
s = input("Enter string: ")
reverse = ""
for ch in s:
    reverse = ch + reverse
print(reverse)


# Q83. Palindrome String
s = input("Enter string: ")
reverse = ""
for ch in s:
    reverse = ch + reverse
print(s == reverse)


# Q84. Count a Specific Character
s = input("Enter string: ")
count = 0
for ch in s:
    if ch == "a" or ch == "A":
        count += 1
print(count)


# Q85. Remove All Spaces
s = input("Enter string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print(result)


# ============================================================
# LEVEL 3 — MORE STRING PRACTICE
# ============================================================

# Q86. Count Words
s = input("Enter sentence: ")
count = 0
inside_word = False
for ch in s:
    if ch != " " and not inside_word:
        count += 1
        inside_word = True
    elif ch == " ":
        inside_word = False
print(count)


# Q87. Replace All 'a' with 'e'
s = input("Enter string: ")
result = ""
for ch in s:
    if ch == "a":
        result += "e"
    else:
        result += ch
print(result)


# Q88. Check for a Character
s = input("Enter string: ")
ch = input("Enter character: ")
found = False
for c in s:
    if c == ch:
        found = True
        break
print(found)


# Q89. Compare Two Strings
first = input("Enter first string: ")
second = input("Enter second string: ")
print(first == second)


# Q90. Count Digits in a String
s = input("Enter string: ")
count = 0
for ch in s:
    if "0" <= ch <= "9":
        count += 1
print(count)


# Q91. Count Uppercase Letters
s = input("Enter string: ")
count = 0
for ch in s:
    if "A" <= ch <= "Z":
        count += 1
print(count)


# Q92. Count Lowercase Letters
s = input("Enter string: ")
count = 0
for ch in s:
    if "a" <= ch <= "z":
        count += 1
print(count)


# Q93. Remove All Vowels
s = input("Enter string: ")
result = ""
for ch in s:
    if ch not in "aeiouAEIOU":
        result += ch
print(result)


# Q94. Remove All Digits
s = input("Enter string: ")
result = ""
for ch in s:
    if not ("0" <= ch <= "9"):
        result += ch
print(result)


# Q95. Toggle Character Case
s = input("Enter string: ")
result = ""
for ch in s:
    if "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    elif "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    else:
        result += ch
print(result)


# ============================================================
# PART 3 — NESTED-LOOP THINKING
# ============================================================

# Q96. Multiplication Tables from 1 to N
n = int(input("Enter N: "))
k = int(input("Enter K: "))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        print(f"{i} x {j} = {i * j}")


# Q97. Number and Its Divisors
n = int(input("Enter N: "))
for i in range(1, n + 1):
    print(f"{i}:", end=" ")
    for j in range(1, i + 1):
        if i % j == 0:
            print(j, end=" ")
    print()


# Q98. Count Divisors for Every Number
n = int(input("Enter N: "))
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(f"{i}: {count}")


# Q99. Perfect Numbers in a Range
n = int(input("Enter N: "))
for i in range(2, n + 1):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    if total == i:
        print(i)


# Q100. Prime Numbers in a Range
n = int(input("Enter N: "))
for i in range(2, n + 1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i, end=" ")
print()


# ============================================================
# LEVEL 2 — COMPARE ITEMS AND FIND PAIRS
# ============================================================

# Q101. Pairs of Digits with a Target Sum
number = input("Enter positive integer: ")
target = int(input("Enter target sum: "))
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if int(number[i]) + int(number[j]) == target:
            print(number[i], number[j])


# Q102. Digit Pairs with a Fixed Difference
number = input("Enter positive integer: ")
d = int(input("Enter difference D: "))
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if abs(int(number[i]) - int(number[j])) == d:
            print(number[i], number[j])


# Q103. Repeated Digits in a Number
number = input("Enter number: ")
for i in range(len(number)):
    appeared_before = False
    for k in range(i):
        if number[k] == number[i]:
            appeared_before = True
            break
    if appeared_before:
        continue

    count = 0
    for j in range(len(number)):
        if number[j] == number[i]:
            count += 1
    if count > 1:
        print(number[i])


# Q104. Count Equal Digit Pairs
number = input("Enter number: ")
count = 0
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] == number[j]:
            count += 1
print(count)


# Q105. Common Characters in Two Strings
first = input("Enter first string: ")
second = input("Enter second string: ")
for i in range(len(first)):
    earlier = False
    for k in range(i):
        if first[k] == first[i]:
            earlier = True
            break
    if earlier:
        continue

    found = False
    for j in range(len(second)):
        if first[i] == second[j]:
            found = True
            break
    if found:
        print(first[i])


# Q106. Check Whether Two Strings Share a Character
first = input("Enter first string: ")
second = input("Enter second string: ")
found = False
for ch1 in first:
    for ch2 in second:
        if ch1 == ch2:
            found = True
            break
    if found:
        break
print(found)


# Q107. Seating Plan
rows = int(input("Enter rows: "))
seats = int(input("Enter seats per row: "))
for i in range(1, rows + 1):
    print(f"Row {i}:", end=" ")
    for j in range(1, seats + 1):
        print(j, end=" ")
    print()


# Q108. Student Marks and Class Total
students = int(input("Enter number of students: "))
tests = int(input("Enter number of tests: "))
class_total = 0
for i in range(1, students + 1):
    student_total = 0
    for j in range(1, tests + 1):
        mark = int(input(f"Student {i}, test {j}: "))
        student_total += mark
    class_total += student_total
    print(f"Student {i} total: {student_total}")
print(f"Class total: {class_total}")


# Q109. Daily Rainfall Summary
days = int(input("Enter days: "))
stations = int(input("Enter stations: "))
for i in range(1, days + 1):
    daily_total = 0
    for j in range(1, stations + 1):
        rainfall = int(input(f"Day {i}, station {j}: "))
        daily_total += rainfall
    print(f"Day {i} total: {daily_total}")


# Q110. Largest of Several Numbers in Each Group
groups = int(input("Enter number of groups: "))
k = int(input("Enter numbers per group: "))
for i in range(1, groups + 1):
    largest = int(input(f"Group {i}, number 1: "))
    for j in range(2, k + 1):
        value = int(input(f"Group {i}, number {j}: "))
        if value > largest:
            largest = value
    print(largest)


# Q111. Sum of Numbers by Group and Position
a = int(input("Group 1, number 1: "))
b = int(input("Group 1, number 2: "))
c = int(input("Group 1, number 3: "))
d = int(input("Group 2, number 1: "))
e = int(input("Group 2, number 2: "))
f = int(input("Group 2, number 3: "))
print("Group sums:", a + b + c, d + e + f)
print("Position sums:", a + d, b + e, c + f)


# Q112. Number Pair Comparison Table
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i + j, end=" ")
    print()


# Q113. Count Zeroes in a Number Sequence
n = int(input("Enter number of integers: "))
count = 0
for i in range(n):
    value = int(input("Enter integer: "))
    if value == 0:
        count += 1
print(count)


# Q114. Print Row and Column Coordinates
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    for j in range(cols):
        print(f"({i}, {j})", end=" ")
    print()


# Q115. Find Every Occurrence of a Substring
text = input("Enter text: ")
pattern = input("Enter pattern: ")
found = False
if len(pattern) > 0:
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            print(i, end=" ")
            found = True
print()


# Q116. Count Matching Character Pairs
s = input("Enter string: ")
count = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)


# Q117. Check Whether Two Strings Are Anagrams
first = input("Enter first string: ")
second = input("Enter second string: ")
anagram = len(first) == len(second)

if anagram:
    for i in range(len(first)):
        count1 = 0
        count2 = 0
        for j in range(len(first)):
            if first[j] == first[i]:
                count1 += 1
            if second[j] == first[i]:
                count2 += 1
        if count1 != count2:
            anagram = False
            break
print(anagram)


# Q118. Print Character Frequency Without a Dictionary
s = input("Enter string: ")
for i in range(len(s)):
    earlier = False
    for j in range(i):
        if s[j] == s[i]:
            earlier = True
            break
    if earlier:
        continue

    count = 0
    for ch in s:
        if ch == s[i]:
            count += 1
    print(f"{s[i]}: {count}")


# Q119. Find Repeated Adjacent Characters
s = input("Enter string: ")
i = 0
while i < len(s):
    ch = s[i]
    count = 1
    j = i + 1
    while j < len(s) and s[j] == ch:
        count += 1
        j += 1
    if count >= 2:
        print(f"{ch}: {count}")
    i = j


# Q120. Compare Two Words Position by Position
first = input("Enter first string: ")
second = input("Enter second string: ")
count = 0
for i in range(len(first)):
    if first[i] != second[i]:
        count += 1
print(count)


# ============================================================
# LEVEL 5 — CHALLENGE PROBLEMS
# ============================================================

# Q121. Print All Pythagorean Triples up to N
n = int(input("Enter N: "))
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        for c in range(b + 1, n + 1):
            if a * a + b * b == c * c:
                print(a, b, c)


# Q122. Numbers Equal to the Sum of Their Proper Divisors
n = int(input("Enter N: "))
for i in range(2, n + 1):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    if total == i:
        print(i)


# Q123. Print Unique Products in Increasing Factor Order
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        product = i * j
        appeared = False

        for a in range(1, n + 1):
            for b in range(a, n + 1):
                if a == i and b == j:
                    break
                if a * b == product:
                    appeared = True
                    break
            if appeared or (a == i and j >= i):
                break

        if not appeared:
            print(product, end=" ")
print()


# Q124. Find All Pairs of Prime Numbers with a Given Sum
n = int(input("Enter even integer greater than 2: "))
for a in range(2, n // 2 + 1):
    b = n - a

    prime_a = True
    for i in range(2, a):
        if a % i == 0:
            prime_a = False
            break

    prime_b = True
    for i in range(2, b):
        if b % i == 0:
            prime_b = False
            break

    if prime_a and prime_b:
        print(a, b)


# Q125. Check a Magic-Sum Pattern
n = int(input("Enter odd N: "))
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, n + 1):
        value = i + j
        print(value, end=" ")
        row_sum += value
    print()

print("Row sums:", end=" ")
for i in range(1, n + 1):
    print(n * i + n * (n + 1) // 2, end=" ")
print()


# Q126. Count Peaks in a Number Sequence
n = int(input("Enter number of values: "))
peaks = 0

if n >= 3:
    previous = int(input("Enter number 1: "))
    current = int(input("Enter number 2: "))

    for i in range(3, n + 1):
        following = int(input(f"Enter number {i}: "))
        if current > previous and current > following:
            peaks += 1
        previous = current
        current = following

print(peaks)


# Q127. Find Repeated Digit Sums
number = input("Enter number: ")
repeated = False

for i in range(len(number)):
    for j in range(i + 1, len(number)):
        target_sum = int(number[i]) + int(number[j])
        matches = 0

        for a in range(len(number)):
            for b in range(a + 1, len(number)):
                if int(number[a]) + int(number[b]) == target_sum:
                    matches += 1

        if matches > 1:
            repeated = True
            break
    if repeated:
        break

if repeated:
    print("Repeated pair sums exist")
else:
    print("No repeated pair sums")


# Q128. Number Pattern from Row and Column
n = int(input("Enter N: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(abs(i - j), end=" ")
    print()


# Q129. Compare Digits with Their Neighbours
number = input("Enter positive integer: ")
count = 0
for i in range(1, len(number) - 1):
    if number[i] > number[i - 1] and number[i] > number[i + 1]:
        count += 1
print(count)


# Q130. Count Increasing Digit Pairs
number = input("Enter number: ")
count = 0
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] < number[j]:
            count += 1
print(count)


# Q131. Character Frequency Compression Without a Dictionary
s = input("Enter string: ")
result = ""

for i in range(len(s)):
    earlier = False
    for j in range(i):
        if s[j] == s[i]:
            earlier = True
            break

    if earlier:
        continue

    count = 0
    for ch in s:
        if ch == s[i]:
            count += 1

    result += s[i] + str(count)

print(result)