/* 
//Enable button
const inputField1 = document.getElementById('cur_pass');
const inputField2 = document.getElementById('new_pass');
const inputField3 = document.getElementById('curnew_pass');
const myButton = document.getElementById('pw_btn');

inputField1.addEventListener('input', checkInputs);
inputField2.addEventListener('input', checkInputs);
inputField3.addEventListener('input', checkInputs);

// Function to check if all input fields are not empty
function checkInputs() {
    if (inputField1.value.trim() !== '' &&
        inputField2.value.trim() !== '' &&
        inputField3.value.trim() !== '') {
      myButton.disabled = false;
    } else {
      myButton.disabled = true;
    }
  }

  */