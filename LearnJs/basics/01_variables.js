// - **`var`:** It is function-scoped and can be re-declared and updated. It's hoisted to the top of its scope and initialized with `undefined`.
  
// - **`let`:** It is block-scoped and cannot be re-declared within the same block, but it can be updated. Unlike `var`, it is not initialized, so referencing it before the declaration results in a `ReferenceError`.

// - **`const`:** It is also block-scoped like `let`, but it cannot be updated or re-declared. It’s used to define variables that are constants (cannot be reassigned).



// var and let create variables that can be reassigned another value.
// const creates "constant" variables that cannot be reassigned another value.
// developers shouldn't use var anymore. They should use let or const instead.
// if you're not going to change the value of a variable, it is good practice to use const.



function testVarLetConst() {
    if (true) {
        var a = 1;
        let b = 2;
        const c = 3;
        // b = 4; // OK, because 'b' is declared with let and can be updated
        // c = 5; // Error: Assignment to constant variable.
    }
    console.log(a); // 1 (var is function-scoped)
    // console.log(b); // ReferenceError: b is not defined (let is block-scoped)
    // console.log(c); // ReferenceError: c is not defined (const is block-scoped)
}

testVarLetConst();



const accountId = 144553
let accountEmail = "h@google.com"
var accountPassword = "12345"
accountCity = "Jaipur"
let accountState;

// accountId = 2 // not allowed


accountEmail = "hc@hc.com"
accountPassword = "21212121"
accountCity = "Bengaluru"

console.log(accountId);

/*
Prefer not to use var
because of issue in block scope and functional scope
*/


console.table([accountId, accountEmail, accountPassword, accountCity, accountState])