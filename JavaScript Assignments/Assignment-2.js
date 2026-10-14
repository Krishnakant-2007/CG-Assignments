// -------------------------SECTION-A----------------------------

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



// ---------------------------------SECTION-B-------------------------------

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
var user = "Krishna";
var user = "Rahul";
console.log(user);

let user = "Krishna";
let user = "Rahul";



// Question 8
var x = 10;
let y = 20;
const z = 30;

x = 100;
y = 200;


console.log(x);
console.log(y);
console.log(z);



// ---------------------------------SECTION-C---------------------------------

// Question 9
var x = 10;

if (true) {
    var x = 20;
    let y = 30;
    const z = 40;
}

console.log(x);



// Question 10
const name2 = "Krishna";

let age2 = 20;
age2 = 25;

let country = "India";

if (true) {
    var city2 = "Delhi";
}

console.log(name2);
console.log(age2);
console.log(city2);
console.log(country);

let score2 = 50;
score2 = 80;

console.log(score2);



// --------------------------------SECTION-D-----------------------------------

// Question-11
console.log(a); // undefined
console.log(b); // ReferenceError
console.log(c); // ReferenceError

var a = 10;
let b = 20;
const c = 30;



//Question-12
var u = "Hello";
let v = "World";
const w = "!";

console.log(u);
console.log(v);
console.log(w);

console.log(u + " " + v + w);



// --------------------------------SECTION-E-----------------------------------

// Question-1
let a = 10;
console.log(a, typeof a); // 10 number



// Question-2
let q = 10.5;
console.log(q, typeof q); // 10.5 number



// Question-3
let a = "Hello World";
console.log(a, typeof a); // Hello World string



// Question-4
let d = true;
console.log(d, typeof d); // true boolean



// --------------------------------SECTION-F-----------------------------------

// Question-5
let a = Symbol("id");
let m = Symbol("id");

console.log(a === m); // false

let user = {
    [a]: "User One",
    [m]: "User Two"
};

console.log(user[a]); // User One
console.log(user[m]); // User Two



// Question-6
let a = 9007199254740991;

console.log(a + 1); // 9007199254740992
console.log(a + 2); // 9007199254740992
console.log(a + 3); // 9007199254740994

let l = 9007199254740991n;

console.log(l + 1n); // 9007199254740992n
console.log(l + 2n); // 9007199254740993n
console.log(l + 3n); // 9007199254740994n\



// Question-7
let id = Symbol("id");
let bigNumber = 9007199254740993n;
let a;
let x = null;



// --------------------------------SECTION-G-----------------------------------

// Question-8
let a;
let r = null;
let t = 42;
let p = "Hello";
let e = true;
let f = Symbol("key");
let g = 123n;

console.log(typeof a, a); // undefined undefined
console.log(typeof r, r); // object null
console.log(typeof t, t); // number 42
console.log(typeof p, p); // string Hello
console.log(typeof e, e); // boolean true
console.log(typeof f, f); // symbol Symbol(key)
console.log(typeof g, g); // bigint 123n



// Question-9
let num = 10;
let text = "Hello";
let flag = true;
let emp;
let nothing = null;
let unique = Symbol("id");
let big = 9007199254740991n;

console.log(num, text, flag, emp, nothing, unique, big);        //10 Hello true undefined null Symbol(id) 9007199254740991n



// Question-10

//-----------------------------------Part-A-----------------------------------
// What is the main difference between Primitive and Non-Primitive data types?

//-----------------------------------ANSWER-----------------------------------
// Primitive data types represent a single value.
// Non-primitive data types can group multiple values or provide more complex structures.

// Example of a primitive:  let age = 18;

// Example of a non-primitive:  let student = {
//                                              name: "Rahul",
//                                              age: 18
//                                            };


//-----------------------------------Part-B-----------------------------------
// Why are Numbers, Strings, Booleans, Undefined, Null, Symbol, and BigInt called Primitive?

//-----------------------------------ANSWER-----------------------------------
// They are called primitive types because they are JavaScript's basic value types rather than objects.
// They represent values such as numbers, text, logical states, or the absence of a value.

// Examples:  let num = 10;            // Number
//            let text = "Hello";      // String
//            let flag = true;         // Boolean
//            let a;                   // Undefined
//            let b = null;            // Null
//            let id = Symbol("id");   // Symbol
//            let big = 100n;          // BigInt


//----------------------------------Part-C----------------------------------
// Give one example of a Non-Primitive data type and explain why it is considered Non-Primitive.

//----------------------------------ANSWER-----------------------------------
// An object is a non-primitive data type because it can store multiple related values as properties.
// Exapmle:         let student = {
//                  name: "Rahul",
//                  age: 18,
//                  passed: true
//              };
                
//              console.log(student.name);   // Rahul
//              console.log(student.age);    // 18
//              console.log(student.passed); // true
                
//              console.log(typeof student); // object

// The object stores a name, an age, and a Boolean value together in one structure.

// Arrays and functions are also non-primitive types in JavaScript.
// Arrays are a kind of object, while functions are callable objects.



// --------------------------------SECTION-H------------------------------------

// Question 1. Creating an Object
let student = {
    name: "Riya",
    age: 18,
    isEnrolled: true
};

console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.isEnrolled);



// Question 2. Working with Arrays
let scores = [85, 92, 78, 90];

let mixedData = [25, "Hello", true, null];

console.log(scores);
console.log(mixedData);

console.log(scores[0]); // First element
console.log(scores[3]); // Last element


// Question 3. Declaring and Call a Function
function calculateArea(length, width) {
    return length * width;
}

console.log(calculateArea(10, 5));
console.log(calculateArea(8, 4));


// Question 4. Checking Types with typeof
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



// ---------------------------------SECTION-I------------------------------

// Question 5. Valid vs Invalid Variable Names
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



// Question 6. Apply Best Practices
const length = 10;
const width = 5;
const area = length * width;
const MAX_VALUE = 100;

console.log(area);
console.log(MAX_VALUE);



// Question 7. Declaration & Assignment
// let age;
// age = 18;

// let city = "Delhi";

// const country = "India";

// console.log(age);
// console.log(city);
// console.log(country);



// ----------------------------SECTION-J---------------------------

// Question 8. Predict the Output
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



// Question 9. Fix the Program
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


// Question 10. Concept Questions
/*
--------------------------PART-A------------------------

Object vs Array

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



-----------------------------PART-B-----------------------------

Why does typeof null return "object"?

typeof null returns "object" because of an old historical
behavior in JavaScript.

null means the intentional absence of a value.

Example:
let data = null;

null is NOT actually an object.



-----------------------------PART-C------------------------------

Why is it recommended to keep arrays with a single data type?

Keeping the same type makes arrays easier to understand,
process, and maintain.

Example:

let scores = [85, 90, 78, 92];

All values are numbers.

A mixed array can be confusing:

let data = [85, "Hello", true, null];



-----------------------------PART-D----------------------------------

When should you use const and let?

Use const when the variable should not be reassigned.

Example:
const pi = 3.14;

Use let when the variable's value needs to change.

Example:
let score = 50;
score = 80;
*/