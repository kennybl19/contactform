function validateForm(){
    //track validation
    let isValid = false
    //clear error messages
    const errors = document.querySelectorAll('.error');
    const inputs = document.querySelectorAll('input');
    inputs.forEach((input)=> input.classList.remove('invalid'));
    errors.forEach((error)=> error.textContent = "");

    //firstname validation
    const firstname = document.querySelector("#firstname");
    const firstname_err = document.querySelector(".firstname-err");

    if(firstname.value == ""){
        firstname_err.textContent = "This field is required";
        firstname.classList.add("invalid");
        isValid = true
    }

    //lastname validation
    const lastname = document.querySelector("#lastname");
    const lastname_err = document.querySelector(".lastname-err");

    if (lastname.value == ""){
        lastname_err.textContent = "This field is required";
        lastname.classList.add("invalid");
        isValid = true;
    }
    
    if(!isValid){
        alert("Form submitted successfully");
    }
}

document.querySelector("#form").addEventListener("submit", (event) => {
    event.preventDefault()
    validateForm()
});