// Question 1


var name = "Krishna";
let age = 20;
const city = "Delhi";

console.log(name);
console.log(age);
console.log(city);



// Question 2


let score = 50;

score = 80;

console.log(score);



// Question 3


const PI = 3.14;

console.log(PI);



// Question 4


var num1;
let num2;

console.log(num1);
console.log(num2);

num1 = 10;
num2 = 20;

console.log(num1);
console.log(num2);



// Question 5


const studentName = "Krishna";
let marks = 70;
const schoolName = "ABC School";

marks = 85;

console.log(studentName);
console.log(marks);
console.log(schoolName);



// Question 6

if (true) {
    var a = 10;
    let b = 20;
    const c = 30;
}

console.log(a);

// console.log(b); // ReferenceError
// console.log(c); // ReferenceError



// Question 7


// Using var
var user = "Krishna";
var user = "Rahul";

console.log(user);


// Using let
// let user = "Krishna";
// let user = "Rahul";
// Error: Identifier 'user' has already been declared



// Question 8


var x = 10;
let y = 20;
const z = 30;

x = 100;
y = 200;

// z = 300; // TypeError: Assignment to constant variable.

console.log(x);
console.log(y);
console.log(z);



// Question 9


var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);

// console.log(y); // ReferenceError
// console.log(z); // ReferenceError



// Question 10


// const name2 = "Krishna";

// let age2 = 20;
// age2 = 25;

// let country = "India";

// if (true) {
//     var city2 = "Delhi";
// }

// console.log(name2);
// console.log(age2);
// console.log(city2);
// console.log(country);

// let score2 = 50;
// score2 = 80;

// console.log(score2);




// 1. Create an Object

let student = {
    name: "Riya",
    age: 18,
    isEnrolled: true
};

console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.isEnrolled);


// 2. Work with Arrays

let scores = [85, 92, 78, 90];

let mixedData = [25, "Hello", true, null];

console.log(scores);
console.log(mixedData);

console.log(scores[0]); // First element
console.log(scores[3]); // Last element


// 3. Declare and Call a Function

function calculateArea(length, width) {
    return length * width;
}

console.log(calculateArea(10, 5));
console.log(calculateArea(8, 4));


// 4. Check Types with typeof

let numberValue = 25;
let stringValue = "Hello";
let booleanValue = true;
let nullValue = null;
let objectValue = { name: "Riya" };
let arrayValue = [1, 2, 3];
let functionValue = function () {
    console.log("Hello");
};

console.log(numberValue, typeof numberValue);
console.log(stringValue, typeof stringValue);
console.log(booleanValue, typeof booleanValue);
console.log(nullValue, typeof nullValue);
console.log(objectValue, typeof objectValue);
console.log(arrayValue, typeof arrayValue);
console.log(functionValue, typeof functionValue);

/*
Surprising results:

typeof null      -> "object"
typeof array     -> "object"
typeof function  -> "function"
*/


// 5. Valid vs Invalid Variable Names

// Valid:
// userName
// _privateData
// $price
// totalCount

// Invalid:
// 2ndPlace  -> Cannot start with a number
// my-age     -> Hyphen (-) is not allowed
// function   -> Reserved keyword
// const      -> Reserved keyword


// 6. Apply Best Practices

const length = 10;
const width = 5;
const area = length * width;
const MAX_VALUE = 100;

console.log(area);
console.log(MAX_VALUE);


// 7. Declaration & Assignment

// let age;
// age = 18;

// let city = "Delhi";

// const country = "India";

// console.log(age);
// console.log(city);
// console.log(country);


// 8. Predict the Output

let person = {
    name: "Amit",
    age: 22
};

let colors = ["red", "green", "blue"];

function sayHi() {
    return "Hi!";
}

let empty = null;

console.log(typeof person);   // object
console.log(typeof colors);   // object
console.log(typeof sayHi);    // function
console.log(typeof empty);    // object
console.log(person.name);     // Amit
console.log(colors[1]);       // green
console.log(sayHi());         // Hi!

/*
Reasoning:

typeof person -> "object"
Objects have the type "object".

typeof colors -> "object"
Arrays are technically objects in JavaScript.

typeof sayHi -> "function"
Functions have the special typeof result "function".

typeof empty -> "object"
This is a historical JavaScript behavior.
null itself means "no value", but typeof null returns "object".
*/


// 9. Fix the Program

let student1 = {
    name: "Neha",
    age: 19
};

let scores2 = [90, 85, 88];

function greet(name) {
    return "Hello " + name;
}

const maxScore = 100;

console.log(student1.name);
console.log(scores2[0]);
console.log(greet("Neha"));


// 10. Concept Questions

/*
a) Object vs Array

Object stores data using key-value pairs.

Example:
let person = {
    name: "Amit",
    age: 22
};

Array stores multiple values using indexes.

Example:
let colors = ["red", "green", "blue"];

Object:
person.name

Array:
colors[0]


b) Why does typeof null return "object"?

typeof null returns "object" because of an old historical
behavior in JavaScript.

null means the intentional absence of a value.

Example:
let data = null;

null is NOT actually an object.


c) Why is it recommended to keep arrays with a single data type?

Keeping the same type makes arrays easier to understand,
process, and maintain.

Example:

let scores = [85, 90, 78, 92];

All values are numbers.

A mixed array can be confusing:

let data = [85, "Hello", true, null];


d) When should you use const and let?

Use const when the variable should not be reassigned.

Example:
const pi = 3.14;

Use let when the variable's value needs to change.

Example:
let score = 50;
score = 80;
*/