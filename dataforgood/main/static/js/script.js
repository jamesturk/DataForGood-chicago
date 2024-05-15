function showDiv(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    console.log('Form submitted');
    var div = document.getElementById('myDiv');
    if (div) {
        console.log('Div found');
        div.classList.remove('hidden'); // Remove the hidden class to display the div
    } else {
        console.log('Div not found');
    }
}
