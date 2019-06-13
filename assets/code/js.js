// Global counter to keep track of the clicks.
let count = 0;

// Function creating a paragraph element containing
// only the number given in parameter.
function makeParagraph(n) {
  let node = document.createElement("p");
  let text = document.createTextNode(n.toString());
  node.appendChild(text);
  return node;
}

// Create a reference to the button in the HTML document.
let theButton = document.getElementById("the-button");

// Attach an event triggering on clicks on the button.
// When clicking we add a paragraph containing
// the number of times we clicked on the button.
theButton.addEventListener("click", function() {
  count = count + 1;
  let newParagraph = makeParagraph(count);
  document.body.appendChild(newParagraph);
});
