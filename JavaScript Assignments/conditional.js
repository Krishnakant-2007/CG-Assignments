// //------------------------------------------------------Part-A (if Statement)-----------------------------------------------------


// // Question-1
// let num1 = 25;

// if (num1 % 5 === 0) {
//     console.log("Divisible by 5");
// }



// // Question-2
// let age = 65;

// if (age >= 60) {
//     console.log("Senior Citizen");
// }



// // Question-3
// let num2 = 150;

// if (num2 > 100) {
//     console.log("Big Number");
// }



// // Question-4
// let temperature = 5;

// if (temperature < 10) {
//     console.log("Very Cold");
// }



// // Question-5
// let marks1 = 100;

// if (marks1 === 100) {
//     console.log("Perfect Score");
// }



// // Question-6
// let num3 = -10;

// if (num3 < 0) {
//     console.log("Negative Number");
// }



// // Question-7
// let userInput = "";

// if (userInput === "") {
//     console.log("No input provided");
// }



// // Question-8
// let year = 2000;

// if (year % 100 === 0) {
//     console.log("Century Year");
// }



// // Question-9
// let num4 = 8;

// if (num4 > 0 && num4 % 2 === 0) {
//     console.log("Positive Even Number");
// }



// // Question-10
// let marks = 75;

// if (marks >= 35 && marks <= 100) {
//     console.log("Valid Marks");
// }


// //--------------------------------------------------Part-B (if...else Statement)--------------------------------------------------


// // Question-1 
// let num1 = 7;

// if (num1 % 2 === 0) {
//     console.log("Even");
// } else {
//     console.log("Odd");
// }



// // Question-2 
// let age = 20;

// if (age >= 18) {
//     console.log("Eligible");
// } else {
//     console.log("Not Eligible");
// }



// // Question-3 
// let num2 = -5;

// if (num2 >= 0) {
//     console.log("Positive");
// } else {
//     console.log("Negative");
// }



// // Question-4 
// let marks = 32;

// if (marks >= 35) {
//     console.log("Passed");
// } else {
//     console.log("Failed");
// }



// // Question-5 
// let ch = "A";

// if (ch >= "A" && ch <= "Z") {
//     console.log("Uppercase Letter");
// } else {
//     console.log("Not an Uppercase Letter");
// }



// // Question-6
// let num3 = 12;

// if (num3 % 3 === 0) {
//     console.log("Divisible by 3");
// } else {
//     console.log("Not Divisible by 3");
// }



// // Question-7
// let password = prompt("Enter your password:");

// if (password === "admin123") {
//     console.log("Login Successful");
// } else {
//     console.log("Incorrect Password");
// }



// // Question-8
// let year = 2024;

// if (year % 4 === 0) {
//     console.log("Leap Year");
// } else {
//     console.log("Not a Leap Year");
// }



// // Question-9
// let a = 25;
// let b = 40;

// if (a > b) {
//     console.log(a + " is greater");
// } else {
//     console.log(b + " is greater");
// }



// // Question-10
// let num4 = 0;

// if (num4 > 0) {
//     console.log("Positive");
// } else if (num4 < 0) {
//     console.log("Negative");
// } else {
//     console.log("Zero");
// }



//--------------------------------------------------Part-C (if...else if...else Statement)---------------------------------


//Question-1
// let month = Number(prompt("Enter month number (1-12):"));

// if (month === 12 || month === 1 || month === 2) {
//     console.log("Winter");
// } else if (month >= 3 && month <= 5) {
//     console.log("Summer");
// } else if (month >= 6 && month <= 8) {
//     console.log("Monsoon");
// } else if (month >= 9 && month <= 11) {
//     console.log("Autumn");
// } else {
//     console.log("Invalid month number");
// }



//Question-2
// let income = Number(prompt("Enter your annual income:"));
// let tax;

// if (income < 300000) {
//     tax = 0;
// } else if (income <= 700000) {
//     tax = income * 0.05;
// } else if (income <= 1000000) {
//     tax = income * 0.10;
// } else {
//     tax = income * 0.15;
// }

// console.log("Tax amount: ₹" + tax);



//Question-3
// let score = Number(prompt("Enter student score:"));

// if (score >= 90) {
//     console.log("Outstanding");
// } else if (score >= 70) {
//     console.log("Good");
// } else if (score >= 40) {
//     console.log("Average");
// } else {
//     console.log("Needs Improvement");
// }



//Question-4
// let speed = Number(prompt("Enter vehicle speed:"));

// if (speed < 40) {
//     console.log("Slow");
// } else if (speed <= 80) {
//     console.log("Normal");
// } else {
//     console.log("Fast");
// }



//Question-5
// let height = Number(prompt("Enter height in cm:"));

// if (height < 150) {
//     console.log("Short");
// } else if (height <= 170) {
//     console.log("Average");
// } else {
//     console.log("Tall");
// }



//Question-6
// let day = Number(prompt("Enter day number (1-7):"));

// if (day >= 1 && day <= 5) {
//     console.log("Weekday");
// } else if (day === 6 || day === 7) {
//     console.log("Weekend");
// } else {
//     console.log("Invalid day number");
// }



//Question-7
// let units = Number(prompt("Enter electricity units:"));
// let bill;

// if (units < 0) {
//     console.log("Invalid units");
// } else if (units <= 50) {
//     bill = units * 2;
//     console.log("Total bill: ₹" + bill);
// } else if (units <= 150) {
//     bill = units * 4;
//     console.log("Total bill: ₹" + bill);
// } else {
//     bill = units * 6;
//     console.log("Total bill: ₹" + bill);
// }



//Question-8
// let attendance = Number(prompt("Enter attendance percentage:"));

// if (attendance >= 90) {
//     console.log("Excellent");
// } else if (attendance >= 75) {
//     console.log("Good");
// } else if (attendance >= 50) {
//     console.log("Satisfactory");
// } else {
//     console.log("Poor");
// }



//Question-9
// let m1 = Number(prompt("Enter first subject marks:"));
// let m2 = Number(prompt("Enter second subject marks:"));
// let m3 = Number(prompt("Enter third subject marks:"));

// if (m1 >= m2 && m1 >= m3) {
//     console.log("Highest mark: " + m1);
// } else if (m2 >= m1 && m2 >= m3) {
//     console.log("Highest mark: " + m2);
// } else {
//     console.log("Highest mark: " + m3);
// }



//Question-10
// let num = Number(prompt("Enter a number:"));

// if (num === 0) {
//     console.log("Zero");
// } else if (num > 0 && num % 2 === 0) {
//     console.log("Positive Even");
// } else if (num > 0 && num % 2 !== 0) {
//     console.log("Positive Odd");
// } else if (num < 0 && num % 2 === 0) {
//     console.log("Negative Even");
// } else {
//     console.log("Negative Odd");
// }



//--------------------------------------------------Part-D (Nested if Statement)------------------------------------------- 


//Question-1
// let num = Number(prompt("Enter a number:"));

// if (num > 10) {
//     if (num % 3 === 0) {
//         console.log("Greater than 10 and divisible by 3");
//     } else {
//         console.log("Greater than 10 but not divisible by 3");
//     }
// } else {
//     console.log("Number is not greater than 10");
// }



//Question-2
// let age = Number(prompt("Enter your age:"));
// let voterID = prompt("Do you have a voter ID? (yes/no)");

// if (age >= 18) {
//     if (voterID === "yes") {
//         console.log("Can Vote");
//     } else {
//         console.log("Voter ID required");
//     }
// } else {
//     console.log("Underage");
// }



//Question-3
// let marks = Number(prompt("Enter your marks:"));

// if (marks >= 40) {
//     if (marks >= 80) {
//         console.log("Passed with Distinction");
//     } else {
//         console.log("Passed");
//     }
// } else {
//     console.log("Failed");
// }



//Question-4
// let pin = Number(prompt("Enter your PIN:"));
// let balance = 10000;
// let amount = Number(prompt("Enter withdrawal amount:"));

// if (pin === 1234) {
//     if (amount > 0 && balance >= amount) {
//         balance = balance - amount;
//         console.log("Withdrawal Successful");
//         console.log("Remaining Balance: ₹" + balance);
//     } else {
//         console.log("Insufficient balance or invalid amount");
//     }
// } else {
//     console.log("Incorrect PIN");
// }



//Question-5
// let year = Number(prompt("Enter a year:"));

// if (year % 4 === 0) {
//     if (year % 100 === 0) {
//         if (year % 400 === 0) {
//             console.log("Leap Year");
//         } else {
//             console.log("Not a Leap Year");
//         }
//     } else {
//         console.log("Leap Year");
//     }
// } else {
//     console.log("Not a Leap Year");
// }



//Question-6
// let email = prompt("Enter your email:");

// if (email.includes("@")) {
//     if (email.endsWith(".com")) {
//         if (email.length > 10) {
//             console.log("Valid Email");
//         } else {
//             console.log("Email length must be greater than 10");
//         }
//     } else {
//         console.log("Email must end with .com");
//     }
// } else {
//     console.log("Email must contain @");
// }



//Question-7
// let cartTotal = Number(prompt("Enter cart total:"));
// let premium = prompt("Are you a premium member? (yes/no)");
// let discount = 0;

// if (cartTotal >= 1000) {
//     if (premium === "yes") {
//         discount = 0.20;
//     } else {
//         discount = 0.10;
//     }
// } else {
//     discount = 0;
// }

// let finalAmount = cartTotal - (cartTotal * discount);

// console.log("Discount: " + (discount * 100) + "%");
// console.log("Final Amount: ₹" + finalAmount);



//Question-8
// let num = Number(prompt("Enter a number:"));

// if (num > 0) {
//     if (num % 2 === 0) {
//         if (num % 4 === 0) {
//             console.log("Positive Even and Divisible by 4");
//         } else {
//             console.log("Positive Even but not divisible by 4");
//         }
//     } else {
//         console.log("Positive Odd");
//     }
// } else {
//     console.log("Number is not positive");
// }



//Question-9
// let age = Number(prompt("Enter your age:"));
// let degree = prompt("Do you have a graduation degree? (yes/no)");
// let experience = Number(prompt("Enter years of experience:"));

// if (age >= 21 && age <= 30) {
//     if (degree === "yes") {
//         if (experience >= 2) {
//             console.log("Eligible for Interview");
//         } else {
//             console.log("Insufficient Experience");
//         }
//     } else {
//         console.log("Graduation Degree Required");
//     }
// } else {
//     console.log("Age Criteria Not Met");
// }



//Question-10
// let present = prompt("Is the student present? (yes/no)");
// let internal = Number(prompt("Enter internal marks:"));
// let external = Number(prompt("Enter external marks:"));

// if (present === "yes") {
//     if (internal >= 30) {
//         if (external >= 35) {
//             console.log("Eligible for Final Exam");
//         } else {
//             console.log("External Marks Insufficient");
//         }
//     } else {
//         console.log("Internal Marks Insufficient");
//     }
// } else {
//     console.log("Student is Absent");
// }



//---------------------------------------------------Part-E (switch Statement)--------------------------------------------- 


//Question-1
// let month = Number(prompt("Enter month number (1-12):"));

// switch (month) {
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:
//     case 10:
//     case 12:
//         console.log("31 days");
//         break;

//     case 4:
//     case 6:
//     case 9:
//     case 11:
//         console.log("30 days");
//         break;

//     case 2:
//         console.log("28 days");
//         break;

//     default:
//         console.log("Invalid month number");
// }



//Question-2
// let ch = prompt("Enter a character:").toLowerCase();

// switch (ch) {
//     case "a":
//     case "e":
//     case "i":
//     case "o":
//     case "u":
//         console.log("Vowel");
//         break;

//     default:
//         if (ch.length === 1 && ch >= "a" && ch <= "z") {
//             console.log("Consonant");
//         } else {
//             console.log("Invalid character");
//         }
// }



//Question-3
// let num = Number(prompt("Enter a number (1-4):"));

// switch (num) {
//     case 1:
//     case 2:
//         console.log("Winter");
//         break;

//     case 3:
//     case 4:
//         console.log("Summer");
//         break;

//     default:
//         console.log("Invalid number");
// }



//Question-4
// let marks = Number(prompt("Enter marks:"));

// switch (true) {
//     case (marks >= 75):
//         console.log("Distinction");
//         break;

//     case (marks >= 60):
//         console.log("1st class");
//         break;

//     case (marks >= 50):
//         console.log("2nd class");
//         break;

//     case (marks >= 35):
//         console.log("3rd class");
//         break;

//     default:
//         console.log("Failed");
// }



//Question-5
// let role = prompt("Enter role (admin/user)").toLowerCase();

// switch (role) {
//     case "admin": {
//         let action = prompt(
//             "Enter action (create/edit/delete)"
//         ).toLowerCase();

//         switch (action) {
//             case "create":
//                 console.log("Create action performed");
//                 break;

//             case "edit":
//                 console.log("Edit action performed");
//                 break;

//             case "delete":
//                 console.log("Delete action performed");
//                 break;

//             default:
//                 console.log("Invalid action");
//         }
//         break;
//     }

//     case "user":
//         console.log("Limited Access");
//         break;

//     default:
//         console.log("Invalid role");
// }



//Question-6
// Mango is yellow
// Banana is yellow
// Unknown fruit



//Question-7
// let values = [0, "0", false, null, undefined];

// values.forEach((value) => {
//     switch (value) {
//         case 0:
//             console.log("Number zero");
//             break;

//         case "0":
//             console.log("String zero");
//             break;

//         case false:
//             console.log("Boolean false");
//             break;

//         case null:
//             console.log("Null value");
//             break;

//         case undefined:
//             console.log("Undefined value");
//             break;

//         default:
//             console.log("Unknown value");
//     }
// });



//Question-8
// let a = Number(prompt("Enter first number:"));
// let operator = prompt("Enter operator (+, -, *, /, %, **):");
// let b = Number(prompt("Enter second number:"));

// switch (operator) {
//     case "+":
//         console.log("Result:", a + b);
//         break;

//     case "-":
//         console.log("Result:", a - b);
//         break;

//     case "*":
//         console.log("Result:", a * b);
//         break;

//     case "/":
//         if (b === 0) {
//             console.log("Error: Division by zero");
//         } else {
//             console.log("Result:", a / b);
//         }
//         break;

//     case "%":
//         if (b === 0) {
//             console.log("Error: Modulo by zero");
//         } else {
//             console.log("Result:", a % b);
//         }
//         break;

//     case "**":
//         console.log("Result:", a ** b);
//         break;

//     default:
//         console.log("Invalid operator");
// }



//Question-9
// let day = Number(prompt("Enter day of the month (1-31):"));

// switch (true) {
//     case (day >= 1 && day <= 10):
//         console.log("Beginning of the month");
//         break;

//     case (day >= 11 && day <= 20):
//         console.log("Middle of the month");
//         break;

//     case (day >= 21 && day <= 31):
//         console.log("End of the month");
//         break;

//     default:
//         console.log("Invalid day");
// }



//Question-10
// let category = prompt("Enter category (veg/nonveg)").toLowerCase();
// let item = "";
// let size = "";
// let price = 0;

// switch (category) {
//     case "veg":
//         item = prompt("Choose item (paneer/biryani)").toLowerCase();

//         switch (item) {
//             case "paneer":
//                 size = prompt("Choose size (half/full)").toLowerCase();

//                 switch (size) {
//                     case "half":
//                         price = 120;
//                         break;

//                     case "full":
//                         price = 220;
//                         break;

//                     default:
//                         console.log("Invalid size");
//                 }
//                 break;

//             case "biryani":
//                 size = prompt("Choose size (half/full)").toLowerCase();

//                 switch (size) {
//                     case "half":
//                         price = 100;
//                         break;

//                     case "full":
//                         price = 180;
//                         break;

//                     default:
//                         console.log("Invalid size");
//                 }
//                 break;

//             default:
//                 console.log("Invalid veg item");
//         }
//         break;

//     case "nonveg":
//         item = prompt("Choose item (chicken/biryani)").toLowerCase();

//         switch (item) {
//             case "chicken":
//                 size = prompt("Choose size (half/full)").toLowerCase();

//                 switch (size) {
//                     case "half":
//                         price = 160;
//                         break;

//                     case "full":
//                         price = 280;
//                         break;

//                     default:
//                         console.log("Invalid size");
//                 }
//                 break;

//             case "biryani":
//                 size = prompt("Choose size (half/full)").toLowerCase();

//                 switch (size) {
//                     case "half":
//                         price = 140;
//                         break;

//                     case "full":
//                         price = 240;
//                         break;

//                     default:
//                         console.log("Invalid size");
//                 }
//                 break;

//             default:
//                 console.log("Invalid nonveg item");
//         }
//         break;

//     default:
//         console.log("Invalid category");
// }

// if (price > 0) {
//     console.log("----- Order Summary -----");
//     console.log("Category:", category);
//     console.log("Item:", item);
//     console.log("Size:", size);
//     console.log("Final Price: ₹" + price);
// }



//---------------------------------------------------Part-F (Ternary Operator)---------------------------------------------


//Question-1
// let num = Number(prompt("Enter a number:"));

// let result = num % 7 === 0
//     ? "Divisible by 7"
//     : "Not Divisible by 7";

// console.log(result);



//Question-2
// let temperature = Number(prompt("Enter temperature:"));

// let result = temperature >= 30
//     ? "Hot Day"
//     : "Pleasant Day";

// console.log(result);



//Question-3
// let str = prompt("Enter a string:");

// let result = str === ""
//     ? "Empty String"
//     : "String has content";

// console.log(result);



//Question-4
// let age = Number(prompt("Enter your age:"));

// let result = age < 13
//     ? "Child"
//     : age <= 19
//         ? "Teenager"
//         : "Adult";

// console.log(result);



//Question-5
// let a = Number(prompt("Enter a:"));
// let b = Number(prompt("Enter b:"));
// let c = Number(prompt("Enter c:"));

// let greatest = a >= b
//     ? (a >= c ? a : c)
//     : (b >= c ? b : c);

// console.log("Greatest number:", greatest);



//Question-6
// let marks = Number(prompt("Enter marks:"));

// let result = marks >= 75
//     ? "Distinction"
//     : marks >= 60
//         ? "First Class"
//         : marks >= 50
//             ? "Second Class"
//             : marks >= 35
//                 ? "Pass"
//                 : "Fail";

// console.log(result);



//Question-7
// let num = Number(prompt("Enter a number:"));

// let result = num === 0
//     ? "Zero"
//     : num > 0
//         ? (num % 2 === 0 ? "Positive Even" : "Positive Odd")
//         : (num % 2 === 0 ? "Negative Even" : "Negative Odd");

// console.log(result);



//Question-8
// let year = Number(prompt("Enter a year:"));

// let result = year % 4 === 0
//     ? (year % 100 === 0
//         ? (year % 400 === 0 ? "Leap Year" : "Not a Leap Year")
//         : "Leap Year")
//     : "Not a Leap Year";

// console.log(result);



//Question-9
// let role = prompt("Enter role (admin/user):");
// let action = prompt("Enter action:");

// let result = role === "admin"
//     ? (action === "delete"
//         ? "Admin Delete"
//         : action === "edit"
//             ? "Admin Edit"
//             : "Admin Other")
//     : role === "user"
//         ? (action === "view"
//             ? "User View"
//             : "User Restricted")
//         : "Invalid Role";

// console.log(result);



//Question-10
// let cartTotal = Number(prompt("Enter cart total:"));

// let result = cartTotal >= 5000
//     ? { discount: "20%", finalAmount: cartTotal * 0.80 }
//     : cartTotal >= 2000
//         ? { discount: "10%", finalAmount: cartTotal * 0.90 }
//         : cartTotal >= 1000
//             ? { discount: "5%", finalAmount: cartTotal * 0.95 }
//             : { discount: "0%", finalAmount: cartTotal };

// console.log("Discount:", result.discount);
// console.log("Final Amount: ₹" + result.finalAmount);