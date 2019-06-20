// x and y are global variables
x = 42;
y = 14;

// Let's open an inner block scope
{
  // The "var" keyword has a function scope
  // so it will erase the global value 42.
  var x = 14;

  // The "let" keyword has a block scope
  // so it will not replace the global y.
  let y = 0;

  // The "const" keyword has a block scope.
  // It prevents reassignment of the variable.
  const z = 3;
  // z = 4; TypeError: Assignment to a constant variable
}

// x: 14
console.log("x: " + x.toString());

// y: 14
console.log("y: " + y.toString());
