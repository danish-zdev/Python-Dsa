//  Primitive-(use stack )

//  7 types : String, Number, Boolearn, null, undefined, Symbol, BigInt

const score = 100
const scoreValue = 100.3

const isLoggedIn = false
const outsideTemp = null
let userEmail;

const id = Symbol('123')
const anotherId = Symbol('123')

console.log(id === anotherId);

// const bigNumber = 3456543576654356754n



// Reference (Non primitive) -use Heap

// Array, Objects, Functions

const heros = ["shaktiman", "naagraj", "doga"];
let myObj = {
    name: "hitesh",
    age: 22,
}

const myFunction = function(){
    console.log("Hello world");
}

console.log(typeof anotherId);

// https://262.ecma-international.org/5.1/#sec-11.4.3




// Return type of variables in JavaScript
// 1) Primitive Datatypes
//        Number => number
//        String  => string
//        Boolean  => boolean
//        null  => object
//        undefined  =>  undefined
//        Symbol  =>  symbol
//        BigInt  =>  bigint

// 2) Non-primitive Datatypes
//        Arrays  =>  object
//        Function  =>  function
//        Object  =>  object



// Summary
// Primitives
//  (like numbers, strings, booleans) are copied by value, meaning a copy of the value is created. Changes to the copy do not affect the original.
// Non-primitives
//  (like objects and arrays) can be copied either by shallow copy or deep copy, affecting how changes to the copied object influence the original.
// Use shallow copies when you



// Shallow Copy:
// Stack: Holds references to primitives and the top-level object.
// Heap: Contains the top-level object and shared references to nested objects.

// Deep Copy:
// Stack: Holds references to primitives.
// Heap: Contains completely new instances of both the top-level object and all nested objects.