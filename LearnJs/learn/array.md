Here are **10 array-related interview questions** in JavaScript categorized by difficulty: **easy, medium, hard, and algorithmic (hots)**.

---

### **Easy Questions**:
1. **What is an array in JavaScript?**
   - An array is a list-like object that allows you to store multiple values in a single variable. Arrays are defined using square brackets `[]` and accessed using indices.
   ```javascript
   const fruits = ['apple', 'banana', 'cherry'];
   console.log(fruits[1]); // 'banana'
   ```

2. **How do you add or remove elements from an array?**
   - You can use methods like:
     - `push()` to add an element at the end.
     - `pop()` to remove the last element.
     - `shift()` to remove the first element.
     - `unshift()` to add an element at the beginning.
   ```javascript
   fruits.push('orange'); // Adds 'orange'
   fruits.pop();          // Removes 'cherry'
   ```

3. **What is the difference between `slice()` and `splice()`?**
   - `slice()` returns a shallow copy of a portion of an array without modifying the original array. `splice()` changes the contents of an array by removing or replacing existing elements and/or adding new elements.
   ```javascript
   const sliced = fruits.slice(1, 3); // ['banana', 'cherry']
   fruits.splice(1, 1, 'kiwi');        // Replaces 'banana' with 'kiwi'
   ```

4. **How do you iterate over an array?**
   - You can iterate using:
     - `for` loop
     - `forEach()`
     - `map()`
   ```javascript
   fruits.forEach(fruit => console.log(fruit));
   ```

5. **How do you find the length of an array?**
   - Use the `length` property.
   ```javascript
   console.log(fruits.length); // Number of elements in the array
   ```

6. **What is the `map()` function in arrays?**
   - `map()` creates a new array populated with the results of calling a provided function on every element in the calling array.
   ```javascript
   const lengths = fruits.map(fruit => fruit.length); // [5, 4, 6]
   ```

7. **How do you convert an array to a string in JavaScript?**
   - Use `join()` or `toString()`.
   ```javascript
   const str = fruits.join(', '); // 'apple, kiwi, cherry'
   ```

8. **What is the `filter()` function in arrays?**
   - `filter()` creates a new array with all elements that pass the test implemented by the provided function.
   ```javascript
   const longFruits = fruits.filter(fruit => fruit.length > 5); // ['banana']
   ```

9. **How do you check if an element exists in an array?**
   - Use `indexOf()` or `includes()`.
   ```javascript
   console.log(fruits.includes('banana')); // true
   ```

10. **What is the difference between an array and an object in JavaScript?**
    - Arrays are ordered collections of values, while objects are unordered collections of key-value pairs. Arrays have numerical indices, while objects use strings as keys.

---

### **Medium Questions**:
1. **How does `reduce()` work in arrays?**
   - `reduce()` executes a reducer function on each element of the array, resulting in a single output value.
   ```javascript
   const total = [1, 2, 3].reduce((acc, curr) => acc + curr, 0); // 6
   ```

2. **What is array destructuring in JavaScript?**
   - Array destructuring allows unpacking values from arrays into distinct variables.
   ```javascript
   const [first, second] = fruits; // first = 'apple', second = 'kiwi'
   ```

3. **What is the difference between shallow copy and deep copy for arrays?**
   - A shallow copy duplicates the top-level elements, while a deep copy duplicates all levels of nested elements.
   ```javascript
   const shallowCopy = fruits.slice(); // Shallow copy
   const deepCopy = JSON.parse(JSON.stringify(fruits)); // Deep copy
   ```

4. **How do you remove duplicates from an array?**
   - Use `Set()` or `filter()`.
   ```javascript
   const uniqueFruits = [...new Set(fruits)]; // Using Set
   ```

5. **Explain how to sort an array in JavaScript.**
   - Use `sort()` with a compare function for custom sorting.
   ```javascript
   const sortedFruits = fruits.sort(); // Alphabetical order
   ```

6. **What is the `find()` function in arrays?**
   - `find()` returns the value of the first element that satisfies the provided testing function.
   ```javascript
   const found = fruits.find(fruit => fruit.startsWith('b')); // 'banana'
   ```

7. **How do you reverse an array?**
   - Use the `reverse()` method, which modifies the original array.
   ```javascript
   fruits.reverse(); // Reverses the order of elements
   ```

8. **What is `Array.prototype.every()` and `Array.prototype.some()`?**
   - `every()` tests whether all elements pass the test implemented by the provided function, while `some()` tests whether at least one element passes the test.
   ```javascript
   const allLong = fruits.every(fruit => fruit.length > 3); // false
   const someLong = fruits.some(fruit => fruit.length > 5); // true
   ```

9. **How do you merge two arrays?**
   - Use `concat()` or the spread operator (`...`).
   ```javascript
   const merged = fruits.concat(['grape', 'melon']); // Using concat
   const mergedSpread = [...fruits, 'grape', 'melon']; // Using spread operator
   ```

10. **How do you flatten a multidimensional array?**
    - Use recursion or the `flat()` method.
    ```javascript
    const nested = [1, [2, [3, 4]]];
    const flatArray = nested.flat(2); // [1, 2, 3, 4]
    ```

---

### **Hard Questions**:
1. **Explain the difference between pass-by-reference and pass-by-value for arrays.**
   - In JavaScript, arrays are objects and are passed by reference. Modifying an array inside a function affects the original array.
   ```javascript
   function modifyArray(arr) {
       arr.push(4);
   }
   const nums = [1, 2, 3];
   modifyArray(nums); // nums is now [1, 2, 3, 4]
   ```

2. **How do you create a deep copy of an array containing objects?**
   - Solutions include using `JSON.parse(JSON.stringify())` or recursive methods.
   ```javascript
   const deepCopy = JSON.parse(JSON.stringify(originalArray));
   ```

3. **What is the time complexity of common array operations (e.g., push, pop, shift, unshift)?**
   - `push`: O(1), `pop`: O(1), `shift`: O(n), `unshift`: O(n).

4. **How do you implement a custom `map()` function for arrays?**
   - Write a polyfill for `Array.prototype.map()`.
   ```javascript
   Array.prototype.myMap = function(callback) {
       const result = [];
       for (let i = 0; i < this.length; i++) {
           if (this[i] !== undefined) {
               result.push(callback(this[i], i, this));
           }
       }
       return result;
   };
   ```

5. **What are sparse arrays, and how are they different from normal arrays?**
   - Sparse arrays have "holes" (undefined elements) and do not have contiguous indices.
   ```javascript
   const sparse = [1, , 3]; // Index 1 is empty
   console.log(sparse.length); // 3
   ```

6. **How do you remove falsy values from an array?**
   - Use `filter()` to create a new array with only truthy values.
   ```javascript
   const cleaned = [0, 1, false, 2, '', 3].filter(Boolean); // [1, 2, 3]
   ```

7. **What is the `reduceRight()` function in arrays?**
   - `reduceRight()` works similarly to `reduce()`, but it processes elements from right to left.
   ```javascript
   const reversed = [1, 2, 3].reduceRight((acc, curr) => acc + curr, ''); // '321'
   ```

8. **How do you partition an array into two parts based on a condition?**
   - Use `reduce()` or `filter()` to separate elements.
   ```javascript
   const partition = (arr, predicate) => {
       return arr.reduce(([pass, fail], element) => {
           predicate(element) ? pass.push(element) : fail.push(element);
           return [pass, fail];
       }, [[], []]);
   };
   ```

9. **How does the `flatMap()` method work in arrays?**
   - `flatMap()` first maps each element using a mapping function, then flattens the result into a new array.
   ```javascript
   const arr = [1, 2, 3];
   const flatMapped = arr.flatMap(x => [x, x * 2]); // [1, 2, 2, 4, 3, 6]
   ```

10. **How do you implement an efficient search for an element in a sorted array?**
    - Implement binary search.
    ```javascript
    function binarySearch(arr, target) {
        let left = 0;
        let right = arr.length - 1;
        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] === target) return mid;
            if (arr[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1; // Not found
    }
    ```

---

### **Algorithmic Questions (Hot/Advanced)**:
1. **Write a function to find the intersection of two arrays.**
   - Return elements that appear in both arrays.
   ```javascript
   function intersection(arr1, arr2) {
       return arr1.filter(value => arr2.includes(value));
   }
   ```

2. **Implement a function to rotate an array by `k` positions.**
   - Example with both left and right rotations.
   ```javascript
   function rotateArray(arr, k) {
       k = k % arr.length; // Handle rotations greater than array length
       return arr.slice(-k).concat(arr.slice(0, arr.length - k));
   }
   ```

3. **Write a function to find the maximum sum of a contiguous subarray (Kadane’s Algorithm).**
   - Example of solving the maximum subarray problem.
   ```javascript
   function maxSubArray(nums) {
       let maxSum = nums[0];
       let currentSum = nums[0];
       for (let i = 1; i < nums.length; i++) {
           currentSum = Math.max(nums[i], currentSum + nums[i]);
           maxSum = Math.max(maxSum, currentSum);
       }
       return maxSum;
   }
   ```

4. **How do you find the kth largest element in an unsorted array?**
   - Solution using sorting or a heap.
   ```javascript
   function findKthLargest(nums, k) {
       return nums.sort((a, b) => b - a)[k - 1];
   }
   ```

5. **Write a function to remove duplicates from a sorted array in place.**
   - Optimize the algorithm to use constant extra space.
   ```javascript
   function removeDuplicates(nums) {
       let i = 0;
       for (let j = 1; j < nums.length; j++) {
           if (nums[i] !== nums[j]) {
               i++;
               nums[i] = nums[j];
           }
       }
       return i + 1; // New length
   }
   ```

6. **Implement a function to merge two sorted arrays into a single sorted array.**
   - Ensure the final array is sorted without using extra space.
   ```javascript
   function mergeSortedArrays(arr1, arr2) {
       let i = 0, j = 0, merged = [];
       while (i < arr1.length && j < arr2.length) {
           if (arr1[i] < arr2[j]) {
               merged.push(arr1[i++]);
           } else {
               merged.push(arr2[j++]);
           }
       }
       return merged.concat(arr1.slice(i)).concat(arr2.slice(j));
   }
   ```

7. **How do you find the missing number in an array of integers from 1 to n?**
   - Example using sum formulas or XOR to find the missing number.
   ```javascript
   function findMissingNumber(nums) {
       const n = nums.length + 1;
       const expectedSum = (n * (n + 1)) / 2;
       const actualSum = nums.reduce((acc, num) => acc + num, 0);
       return expectedSum - actualSum;
   }
   ```

8. **Write a function to find all pairs in an array whose sum equals a given target.**
   - Optimize using a hash map.
   ```javascript
   function twoSum(nums, target) {
       const map = new Map();
       for (let i = 0; i < nums.length; i++) {
           const complement = target - nums[i];
           if (map.has(complement)) {
               return [map.get(complement), i];
           }
           map.set(nums[i], i);
       }
       return [];
   }
   ```

9. **Implement a function to group anagrams from an array of strings.**
   - Sort each string and use it as a key in a hash map.
   ```javascript
   function groupAnagrams(strs) {
       const map = {};
       for (const str of strs) {
           const sorted = str.split('').sort().join('');
           if (!map[sorted]) map[sorted] = [];
           map[sorted].push(str);
       }
       return Object.values(map);
   }
   ```

10. **Write a function to move all zeroes to the end of an array while maintaining the order of non-zero elements.**
    - Solution with two-pointer technique.
    ```javascript
    function moveZeroes(nums) {
        let lastNonZeroIndex = 0;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] !== 0) {
                nums[lastNonZeroIndex++] = nums[i];
            }
        }
        for (let i = lastNonZeroIndex; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
    ```

---

This comprehensive list covers a range of topics related to arrays in JavaScript, suitable for various levels of expertise.