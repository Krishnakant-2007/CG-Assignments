# ============================================================
# TYPE 1: OUTPUT GUESSING — WHILE LOOPS
# Q1–Q20
# ============================================================

# Q1. Simple Counting
# Output:
# 1
# 2
# 3
# 4


# Q2. Counting by Two
# Output:
# 2 4 6 8


# Q3. Reverse Counting
# Output:
# 5 4 3 2 1


# Q4. The Condition Is Initially False
# Output:
# Finished


# Q5. Update Before Printing
# Output:
# 2 3 4 5


# Q6. Print After the Loop
# Output:
# 1 2 3
# Done


# Q7. Two Updates in One Iteration
# Output:
# 1 4 7


# Q8. Change the Variable Before Checking Again
# Output:
# 7 4 1 -2


# Q9. Add the Counter Values
# Output:
# 10


# Q10. Multiply During Each Iteration
# Output:
# 16


# Q11. Use the Remainder Operator
# Output:
# 2 1 0


# Q12. Integer Division
# Output:
# 58 5 0


# Q13. Print Only When a Condition Is True
# Output:
# 2 4 6


# Q14. A Conditional Expression Inside a Loop
# Output:
# Odd Even Odd Even Odd


# Q15. The Condition Changes Inside the Loop
# Output:
# 1 2 4 8


# Q16. A Tricky Starting Value
# Output:
# 5 3 1
# Stop: -1


# Q17. Build a String Repeatedly
# Output:
# A
# AA
# AAA
# AAAA


# Q18. A String Variable Changes Each Time
# Output:
# PY
# PYT
# PYTT
# PYTTT


# Q19. Does the Loop Run at All?
# Output:
# 3


# Q20. Find the Problem
# Answer: B
# It prints 1, 0, -1, -2, ... indefinitely because i decreases
# and therefore i <= 4 remains true.


# ============================================================
# TYPE 2: BASIC WHILE LOOP PROBLEMS
# Q21–Q40
# Run each question's code separately.
# ============================================================

# Q21. Print Numbers from 1 to N
n = int(input())
i = 1

while i <= n:
    print(i)
    i += 1


# Q22. Print Numbers from N to 1
n = int(input())
while n >= 1:
    print(n)
    n -= 1


# Q23. Print Even Numbers up to N
n = int(input())
i = 2

while i <= n:
    print(i)
    i += 2


# Q24. Print Odd Numbers up to N
n = int(input())
i = 1

while i <= n:
    print(i)
    i += 2


# Q25. Print Multiples of a Number
k = int(input())
n = int(input())
i = k

while i <= n:
    print(i)
    i += k


# Q26. Multiplication Table
n = int(input())
i = 1

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1


# Q27. Count by a Given Step
start = int(input())
step = int(input())
i = 1
value = start

while i <= 5:
    print(value)
    value += step
    i += 1


# Q28. Sum of Numbers from 1 to N
n = int(input())
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print(total)


# Q29. Sum of Even Numbers up to N
n = int(input())
i = 2
total = 0

while i <= n:
    total += i
    i += 2

print(total)


# Q30. Sum of Odd Numbers up to N
n = int(input())
i = 1
total = 0

while i <= n:
    total += i
    i += 2

print(total)


# Q31. Calculate the Total Cost
price = int(input())
quantity = int(input())
i = 1
total = 0

while i <= quantity:
    total += price
    i += 1

print(total)


# Q32. Calculate Total Savings
daily_saving = int(input())
days = int(input())
i = 1
total = 0

while i <= days:
    total += daily_saving
    i += 1

print(total)


# Q33. Calculate a Number Raised to a Power
base = int(input())
power = int(input())
i = 1
result = 1

while i <= power:
    result *= base
    i += 1

print(result)


# Q34. Calculate Factorial
n = int(input())
i = 1
factorial = 1

while i <= n:
    factorial *= i
    i += 1

print(factorial)


# Q35. Find the Sum from START to END
start = int(input())
end = int(input())
total = 0

while start <= end:
    total += start
    start += 1

print(total)


# Q36. Count Down by Two
n = int(input())

while n >= 2:
    print(n)
    n -= 2


# Q37. Repeatedly Divide by Two
n = int(input())

while n > 0:
    n //= 2
    print(n)


# Q38. Count How Many Steps Are Needed
n = int(input())
steps = 0

while n > 0:
    n -= 3
    steps += 1

print(steps)


# Q39. Save Until the Target Is Reached
saved = int(input())
daily_amount = int(input())
target = int(input())
days = 0

while saved < target:
    saved += daily_amount
    days += 1

print(days)


# Q40. Print a Number Sequence in Reverse Steps
start = int(input())
step = int(input())

while start >= 0:
    print(start)
    start -= step


# ============================================================
# TYPE 3: FACTORIAL AND NUMBER & DIGIT LOGIC
# Q41–Q58
# Use one while loop per question.
# Run each question's code separately.
# ============================================================

# Q41. Count the Digits
n = int(input())
count = 0

while n > 0:
    count += 1
    n //= 10

if count == 0:
    count = 1

print(count)


# Q42. Find the Sum of Digits
n = int(input())
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(total)


# Q43. Reverse a Number
n = int(input())
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print(reverse)


# Q44. Find the Product of Digits
n = int(input())
product = 1

if n == 0:
    product = 0

while n > 0:
    product *= n % 10
    n //= 10

print(product)


# Q45. Print Digits from Right to Left
n = int(input())

if n == 0:
    print(0)

while n > 0:
    print(n % 10)
    n //= 10


# Q46. Find the First and Last Digit
n = int(input())
last_digit = n % 10

while n >= 10:
    n //= 10

first_digit = n

print("First digit:", first_digit)
print("Last digit:", last_digit)


# Q47. Count Even Digits
n = int(input())
count = 0

if n == 0:
    count = 1

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        count += 1

    n //= 10

print(count)


# Q48. Count Odd Digits
n = int(input())
count = 0

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        count += 1

    n //= 10

print(count)


# Q49. Find the Sum of Even Digits
n = int(input())
total = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        total += digit

    n //= 10

print(total)


# Q50. Find the Largest Digit
n = int(input())
largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n //= 10

print(largest)


# Q51. Find the Smallest Digit
n = int(input())
smallest = 9

if n == 0:
    smallest = 0

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n //= 10

print(smallest)


# Q52. Check Whether a Number Is a Palindrome
n = int(input())
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Q53. Count How Many Times a Digit Appears
n = int(input())
d = int(input())
count = 0

if n == 0 and d == 0:
    count = 1

while n > 0:
    if n % 10 == d:
        count += 1

    n //= 10

print(count)


# Q54. Check Whether All Digits Are the Same
n = int(input())
first_digit = n % 10
same = True

while n > 0:
    if n % 10 != first_digit:
        same = False
        break

    n //= 10

if same:
    print("Yes")
else:
    print("No")


# Q55. Compare First/Last Digits Sum with Middle Digits Sum
n = int(input())
last_digit = n % 10
n //= 10
middle_sum = 0

while n >= 10:
    middle_sum += n % 10
    n //= 10

first_digit = n

print("First and last digits sum:", first_digit + last_digit)
print("Middle digits sum:", middle_sum)


# Q56. Print Factorial Values from 1! to N!
n = int(input())
i = 1
factorial = 1

while i <= n:
    factorial *= i
    print(factorial)
    i += 1


# Q57. Check Whether a Number Is a Factorial Value
n = int(input())
i = 1
factorial = 1
found = False

while factorial <= n:
    if factorial == n:
        found = True
        break

    i += 1
    factorial *= i

if found:
    print("Yes")
else:
    print("No")


# Q58. Find the Largest Factorial Not Greater Than N
n = int(input())
i = 1
factorial = 1
largest = 1

while factorial <= n:
    largest = factorial
    i += 1
    factorial *= i

print(largest)


# ============================================================
# TYPE 4: OUTPUT GUESSING — NESTED WHILE LOOPS,
# BREAK AND CONTINUE
# Q59–Q78
# ============================================================

# Q59. Two Loops, Two Values
# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3


# Q60. Print Values on the Same Line
# Output:
# 1 2
# 1 2
# 1 2


# Q61. Different Inner Loop Limits
# Output:
# *
# * *
# * * *


# Q62. Outer Value Changes the Inner Starting Point
# Output:
# 1 2 3
# 2 3
# 3


# Q63. Print After the Inner Loop
# Output:
# 1 2 End
# 1 2 End
# 1 2 End


# Q64. Print After Both Loops
# Output:
# 2
# 3
# 3
# 4
# Finished


# Q65. Two Separate while Loops
# Output:
# A 1
# A 2
# B 1
# B 2
# B 3


# Q66. Inner Counter Is Not Reset
# Output:
# 1 1
# 1 2


# Q67. Update the Outer Variable After the Inner Loop
# Output:
# 11
# 33


# Q68. Inner Loop Depends on the Outer Variable
# Output:
# X
# 1 X
# 1 2 X


# Q69. Break the Inner Loop
# Output:
# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# Q70. Break After Printing a Value
# Output:
# 1 2 |
# 1 2 |


# Q71. Break Condition Is Never Reached
# Output:
# 1 1
# 1 2
# 2 1
# 2 2


# Q72. break Does Not Stop the Outer Loop
# Output:
# 1 1
# Next row
# 2 1
# Next row
# 3 1
# Next row


# Q73. Skip One Inner-Loop Value
# Output:
# 1 1
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4


# Q74. Continue After Updating the Counter
# Output:
# 2 4 5 6


# Q75. Continue in the Inner Loop
# Output:
# 1 3 Row
# 1 3 Row
# 1 3 Row


# Q76. continue Does Not Skip the Whole Outer Loop
# Output:
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2


# Q77. Skip One Value, Then Break
# Output:
# 1 1
# 1 3
# 2 1
# 2 3


# Q78. Predict the Complete Output
# Output:
# 1 3 4 End
# 2 6 8 End
# 3 9 End
# Done