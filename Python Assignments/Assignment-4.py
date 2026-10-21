#---------------------------------------------------------------Topic-1---------------------------------------------------------------

# Q1. Positive Number
num = int(input("Enter an integer: "))

if num > 0:
    print("Positive Number")


# Q2. Voting Eligibility Check
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to Vote")


# Q3. Temperature Warning
temperature = float(input("Enter temperature: "))

if temperature > 40:
    print("High Temperature")


# Q4. Divisible by 5
num = int(input("Enter an integer: "))

if num % 5 == 0:
    print("Divisible by 5")


# Q5. Free Delivery
amount = float(input("Enter order amount: "))

if amount >= 1000:
    print("Free Delivery")


# Q6. Character Check
ch = input("Enter a character: ")

if ch == "A":
    print("You entered A")


# Q7. Password Length Check
password = input("Enter password: ")

if len(password) >= 8:
    print("Strong Length")


# Q8. Number of Digits
num = int(input("Enter an integer: "))

if 100 <= num <= 999:
    print("Three Digit Number")



#---------------------------------------------------------------Topic-2---------------------------------------------------------------

# Q9. Even or Odd
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q10. Pass or Fail
marks = float(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q11. Adult or Minor
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q12. Number Sign
num = int(input("Enter an integer: "))

if num > 0:
    print("Positive")
else:
    print("Non-Positive")


# Q13. Divisible by 3
num = int(input("Enter an integer: "))

if num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")


# Q14. Login Password
correct_password = "python123"
password = input("Enter password: ")

if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")


# Q15. Username Check
username = input("Enter username: ")

if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")


# Q16. Greater Between Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")


# Q17. Hot or Comfortable
temperature = float(input("Enter temperature: "))

if temperature > 30:
    print("Hot")
else:
    print("Comfortable")


# Q18. Shopping Discount Eligibility
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")



#---------------------------------------------------------------Topic-3---------------------------------------------------------------

# Q19. Grade Calculator
marks = float(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")


# Q20. Temperature Category
temperature = float(input("Enter temperature: "))

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")


# Q21. Traffic Signal
signal = input("Enter signal color: ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


# Q22. Electricity Usage Category
units = float(input("Enter electricity units: "))

if units < 0:
    print("Invalid Units")
elif units <= 100:
    print("Low Usage")
elif units <= 300:
    print("Medium Usage")
elif units <= 500:
    print("High Usage")
else:
    print("Very High Usage")


# Q23. Movie Ticket Category
age = int(input("Enter age: "))

if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")


# Q24. BMI Category
bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# Q25. Month Days
month = int(input("Enter month number: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 Days")
elif month in (4, 6, 9, 11):
    print("30 Days")
elif month == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")


# Q26. Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0:
        print("Cannot divide by zero")
    else:
        print(a / b)
else:
    print("Invalid Operator")


# Q27. Day Number
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")


# Q28. Performance Level
score = float(input("Enter score (0-100): "))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Average")
else:
    print("Needs Improvement")



#---------------------------------------------------------------Topic-4---------------------------------------------------------------

# Q29. College Admission Eligibility
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")


# Q30. Scholarship Eligibility
marks = float(input("Enter marks: "))
income = float(input("Enter family income: "))

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")


# Q31. Weekend Check
day = input("Enter day name: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# Q32. Online Exam Access
username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")


# Q33. Delivery Availability
city = input("Enter city: ")

if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")


# Q34. Number Range Check
num = int(input("Enter an integer: "))

if 10 <= num <= 50:
    print("Inside Range")
else:
    print("Outside Range")


# Q35. Secure Transaction
amount = float(input("Enter transaction amount: "))
otp = input("Enter OTP: ")

if amount <= 50000 and otp == "1234" and amount > 0:
    print("Transaction Approved")
else:
    print("Transaction Declined")



#---------------------------------------------------------------Topic-5---------------------------------------------------------------

# Q36. Login with Role
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# Q37. Driving License Eligibility
age = int(input("Enter age: "))
status = input("Enter test status: ")

if age >= 18:
    if status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")


# Q38. ATM Withdrawal
balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance:
    if amount % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")


# Q39. Exam Result with Attendance
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")


# Q40. Bank Account Verification
account_type = input("Enter account type: ")
balance = float(input("Enter balance: "))

if account_type == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")


# Q41. Online Shopping Eligibility
amount = float(input("Enter order amount: "))

if amount >= 500:
    payment = input("Enter payment method: ")

    if payment == "card":
        print("Card Payment Accepted")
    elif payment == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


# Q42. Hostel Room Allocation
year = int(input("Enter year of study: "))

if year >= 2 and year <= 4:
    attendance = float(input("Enter attendance: "))

    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")


# Q43. Internet Plan Upgrade
plan = input("Enter current plan: ")

if plan == "basic":
    usage = float(input("Enter monthly usage in GB: "))

    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")



#---------------------------------------------------------------Topic-6---------------------------------------------------------------

# Q44. Greatest of Three Numbers
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a == b and b == c:
    print("All are Equal")
elif a == b and a > c:
    print("A and B are Equal and Greatest")
elif a == c and a > b:
    print("A and C are Equal and Greatest")
elif b == c and b > a:
    print("B and C are Equal and Greatest")
elif a > b and a > c:
    print("A is Greatest")
elif b > a and b > c:
    print("B is Greatest")
else:
    print("C is Greatest")


# Q45. Student Result with Grade
marks = float(input("Enter marks: "))
attendance = float(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


# Q46. Employee Bonus
salary = float(input("Enter salary: "))
rating = int(input("Enter performance rating: "))

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")


# Q47. Bus Ticket Category
age = int(input("Enter age: "))
distance = float(input("Enter distance in km: "))

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")


# Q48. Product Purchase Validation
stock = int(input("Enter stock quantity: "))

if stock > 0:
    payment = input("Enter payment status: ")

    if payment == "paid":
        print("Order Confirmed")
    elif payment == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


# Q49. Travel Ticket Validation
age = int(input("Enter age: "))

if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    ticket = input("Enter ticket type: ")

    if ticket == "AC":
        print("AC Ticket")
    elif ticket == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")



#---------------------------------------------------------------Topic-7---------------------------------------------------------------

# Q50. Basic Menu
choice = int(input("Enter menu number: "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")


# Q51. Day Name
day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")


# Q52. Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print(a / b)
    case _:
        print("Invalid Operator")


# Q53. Traffic Signal
signal = input("Enter signal color: ")

match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")


# Q54. Grade Message
grade = input("Enter grade: ")

match grade:
    case "A":
        print("Excellent Performance")
    case "B":
        print("Very Good Performance")
    case "C":
        print("Good Performance")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid Grade")


# Q55. Mobile Service Menu
service = int(input("Enter service code: "))

match service:
    case 1:
        print("Check Balance")
    case 2:
        print("Recharge")
    case 3:
        print("Data Usage")
    case 4:
        print("Customer Support")
    case _:
        print("Invalid Service")


# Q56. Month Name
month = int(input("Enter month number: "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")


# Q57. File Type Detector
extension = input("Enter file extension: ")

match extension:
    case "py":
        print("Python File")
    case "txt":
        print("Text File")
    case "pdf":
        print("PDF File")
    case "jpg":
        print("Image File")
    case _:
        print("Unknown File Type")



#---------------------------------------------------------------Topic-8---------------------------------------------------------------

# Q58. Student ID Validation
student_id = input("Enter student ID: ")
parts = student_id.split("-")

if len(parts) == 4:
    degree = parts[0]
    batch = parts[1]
    branch = parts[2]
    roll_number = parts[3]

    if branch == "CSE":
        print("CSE Student")
    else:
        print("Non-CSE Student")
else:
    print("Invalid Student ID")


# Q59. Email Domain Checker
email = input("Enter email: ")
parts = email.split("@")

if len(parts) == 2:
    domain = parts[1]

    if domain == "gmail.com":
        print("Gmail User")
    else:
        print("Other Email Provider")
else:
    print("Invalid Email")


# Q60. Username Generator Validation
full_name = input("Enter full name (three words): ")
parts = full_name.split()

if len(parts) == 3:
    username = parts[0] + "." + parts[2]

    if "." in username:
        print("Valid Username Format")
    else:
        print("Invalid Username Format")
else:
    print("Enter exactly three words")


# Q61. Number Digit Analyzer
num = int(input("Enter a positive integer: "))

if num < 0:
    print("Invalid Number")
elif num <= 9:
    print("One Digit")
elif num <= 99:
    print("Two Digits")
elif num <= 999:
    print("Three Digits")
else:
    print("Four or More Digits")


# Q62. Shopping Bill Category
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2000:
    discount_percent = 10
else:
    discount_percent = 0

discount = subtotal * discount_percent / 100
final_amount = subtotal - discount

print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount_percent}%")
print(f"Final: {final_amount:.2f}")


# Q63. Electricity Bill Category
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid Units")
else:
    if units <= 100:
        rate = 5
    elif units <= 300:
        rate = 7
    else:
        rate = 10

    bill = units * rate

    print(f"Units: {units:g}")
    print(f"Rate: ₹{rate}")
    print(f"Bill: ₹{bill:.2f}")


# Q64. ATM Menu
balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print(f"Balance: {balance}")
    case 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit Successful")
            print(f"Balance: {balance:g}")
        else:
            print("Invalid Amount")
    case 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0:
            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print(f"Balance: {balance:g}")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Amount")
    case 4:
        print("Exit")
    case _:
        print("Invalid Choice")


# Q65. Restaurant Ordering System
print("1. Pizza - ₹250")
print("2. Burger - ₹150")
print("3. Pasta - ₹200")
print("4. Sandwich - ₹120")

choice = int(input("Enter item number: "))
quantity = int(input("Enter quantity: "))

match choice:
    case 1:
        item = "Pizza"
        price = 250
    case 2:
        item = "Burger"
        price = 150
    case 3:
        item = "Pasta"
        price = 200
    case 4:
        item = "Sandwich"
        price = 120
    case _:
        item = "Invalid"
        price = 0

if price == 0:
    print("Invalid Choice")
elif quantity <= 0:
    print("Invalid Quantity")
else:
    total = price * quantity

    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print(f"Item: {item}")
    print(f"Total: {total:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final: {final_amount:.2f}")


# Q66. Exam Result Analyzer
m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))
attendance = float(input("Enter attendance: "))

total = m1 + m2 + m3
average = total / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


# Q67. Cab Fare Calculator
distance = float(input("Enter distance in km: "))
ride_type = input("Enter ride type (normal/premium): ")

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0

if distance <= 0:
    print("Invalid Distance")
elif rate == 0:
    print("Invalid Ride Type")
else:
    fare = distance * rate

    if distance > 20:
        fare = fare * 1.10

    print(f"Fare: {fare:.2f}")


# Q68. College Admission System
score = float(input("Enter entrance score: "))
percentage = float(input("Enter 12th percentage: "))
category = input("Enter category (general/obc/sc): ")

match category:
    case "general":
        if score >= 80:
            if percentage >= 75:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case "obc":
        if score >= 70:
            if percentage >= 70:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case "sc":
        if score >= 60:
            if percentage >= 60:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case _:
        print("Invalid Category")



#---------------------------------------------------------------Topic-9---------------------------------------------------------------

# Q69. Debug the Condition

# ERROR: input() returns a string.
# Comparing a string directly with integer 18 causes a TypeError.
# CORRECTION: Convert input to int.

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Q70. Debug the Nested Condition

# ERROR: Marks from 40 to 74 do not produce any output.
# The outer if is true, but neither inner condition matches.
# CORRECTION: Add an else inside the outer if for passing marks.

marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")



#---------------------------------------------------------------Topic-10-----------------------------------------------------------

# Q71. Condition Order
# Predict the output before running.

marks = 85

if marks >= 40:
    print("Pass")
elif marks >= 75:
    print("Very Good")
else:
    print("Fail")

# Output: Pass
# Explanation: The first condition is already true.
# Therefore, the elif condition is never checked.


# Q72. Correct Condition Order
# Predict the output for each marks value.

marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# Expected outputs:
# 95 -> A
# 85 -> B
# 50 -> Pass
# 30 -> Fail
# Explanation: Higher grade conditions are checked first,
# so a student receives the highest applicable grade.


# Q73. Nested if Execution Flow

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")

# Output: Entry Allowed

# If age = 20 and has_id = False:
# Output: ID Required

# If age = 16 and has_id = True:
# Output: Underage


# Q74. match-case and Default Case

choice = 5

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")

# Expected outputs:
# 1 -> Add
# 3 -> Delete
# 5 -> Invalid Choice
# Explanation: case _ is the default case. It matches
# when none of the preceding cases match.


# Q75. Final Execution Challenge

marks = 82
attendance = 80

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")

# Expected outputs:
# 82 80 -> Grade B
# 92 80 -> Grade A
# 55 80 -> Pass
# 92 60 -> Not Eligible

# Explanation: Attendance is checked first because
# the student must meet the attendance requirement
# before the marks-based grade can be determined.



#---------------------------------------------------------------Challenges-----------------------------------------------------------

#Challenge-1(Question-62)

# Q62. Shopping Bill with validation

price = float(input("Enter product price (₹): "))
quantity = int(input("Enter quantity: "))

# Validate input values before calculating the bill.
if price < 0 or quantity <= 0:
    print("Invalid price or quantity")
else:
    subtotal = price * quantity

    # Select the discount according to the subtotal.
    if subtotal >= 5000:
        discount_percent = 20
    elif subtotal >= 2000:
        discount_percent = 10
    else:
        discount_percent = 0

    discount = subtotal * discount_percent / 100
    final_amount = subtotal - discount

    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Discount Amount: ₹{discount:.2f}")
    print(f"Final Amount: ₹{final_amount:.2f}")

# Additional tests:
# Price 1000, quantity 5 -> Final Amount: ₹4000.00
# Price 400, quantity 5 -> Final Amount: ₹1800.00
# Price 500, quantity 4 -> Final Amount: ₹2000.00



#Challenge-2(Question-65)

# Q65. Restaurant Ordering with validation

print("1. Pizza - ₹250")
print("2. Burger - ₹150")
print("3. Pasta - ₹200")
print("4. Sandwich - ₹120")

choice = int(input("Choose item (1-4): "))
quantity = int(input("Enter quantity: "))

# Identify the selected food and its price.
match choice:
    case 1:
        item = "Pizza"
        price = 250
    case 2:
        item = "Burger"
        price = 150
    case 3:
        item = "Pasta"
        price = 200
    case 4:
        item = "Sandwich"
        price = 120
    case _:
        item = ""
        price = 0

# Validate selection and quantity before billing.
if price == 0:
    print("Invalid Choice")
elif quantity <= 0:
    print("Invalid Quantity")
else:
    total = price * quantity

    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Total: ₹{total:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Final Amount: ₹{final_amount:.2f}")

# Additional tests:
# Choice 1, quantity 1 -> Final Amount: ₹250.00
# Choice 2, quantity 4 -> Final Amount: ₹540.00
# Choice 4, quantity 5 -> Final Amount: ₹540.00



#Challenge-3(Question-67)

# Q67. Cab Fare with validation

distance = float(input("Enter distance in km: "))
ride_type = input("Enter ride type (normal/premium): ").lower()

# Select the fare rate using match-case.
match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0

# Validate distance and ride type.
if distance <= 0:
    print("Invalid Distance")
elif rate == 0:
    print("Invalid Ride Type")
else:
    fare = distance * rate

    # Apply a 10% surcharge only for trips above 20 km.
    if distance > 20:
        fare = fare * 1.10

    print(f"Distance: {distance:.2f} km")
    print(f"Ride Type: {ride_type}")
    print(f"Final Fare: ₹{fare:.2f}")

# Additional tests:
# 20 normal -> Fare: ₹300.00
# 21 normal -> Fare: ₹346.50
# 25 premium -> Fare: ₹687.50