// Basic JavaScript for the website

document.addEventListener("DOMContentLoaded", function () {

    // Find the form on the page
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function (event) {

            // Get all input fields
            const inputs = form.querySelectorAll("input");

            let valid = true;

            inputs.forEach(function (input) {
                if (input.hasAttribute("required") && input.value.trim() === "") {
                    valid = false;
                    input.style.border = "2px solid red";
                } else {
                    input.style.border = "";
                }
            });

            if (!valid) {
                event.preventDefault();
                alert("Please fill in all required fields.");
            }
        });
    }

    // Simple button click message
    const buttons = document.querySelectorAll("button");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            console.log("Button clicked: " + button.textContent);
        });
    });
});