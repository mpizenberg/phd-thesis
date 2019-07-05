function timeNow() {
  return new Date().getTime();
}

function randomNumber() {
  return Math.random();
}

// Global variable.
lastname = "Doe";

function getFullName(firstname) {
  lastname = " " + lastname;
  return firstname + lastname;
}

console.log(getFullName("John")); // "John Doe"
console.log(getFullName("John")); // "John  Doe"
console.log(getFullName("John")); // "John   Doe"
