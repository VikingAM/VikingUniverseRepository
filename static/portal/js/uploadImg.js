


// OTP code

const inputs = document.querySelectorAll("input.otp-box"),
    button = document.querySelector("button.otp-verify")

inputs.forEach((input, index1) => {

    input.addEventListener("keyup", (e) => {
        const currentInput = input,
                nextInput = input.nextElementSibling,
                prevInput = input.previousElementSibling;

                if(currentInput.value.length > 1) {
                    currentInput.value = "";
                    return;
                }

                if(nextInput && nextInput.hasAttribute("disabled") && currentInput.value !== "") {
                    nextInput.removeAttribute("disabled");
                    nextInput.focus();
                }


                if(e.key === "Backspace"){
                    inputs.forEach((input, index2) => {

                        if(index1 <= index2 && prevInput){
                            input.setAttribute("disabled", true);
                            input.value = ""; 
                            prevInput.focus();
                        }
                    });
                }

                if(!inputs[3].disabled && inputs[3].value !== ""){
                    button.classList.add("active");
                    return;
                }
                    button.classList.remove("active");
    });
});

window.addEventListener("load", () => inputs[0].focus());





// pop up toggle


function togglePopup(){

    document.getElementById("popup-1").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
 
    
}

function toggleSubmitTicket(){

    document.getElementById("popup-submit-ticket").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

    
}

function toggleTaskReOccurence(){

    document.getElementById("popup-choose-service").classList.remove("active");
    document.getElementById("popup-taskReOccurence").classList.toggle("active");

}   

function toggleTaskAddSuccess(){

    document.getElementById("popup-taskReOccurence").classList.remove("active");
    document.getElementById("popup-taskAddSuccess").classList.toggle("active");

}   

function toggleRevise(){

    document.getElementById("popup-revise-task").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

    
}

function toggleApproveTask(){

    document.getElementById("popup-approve-task").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

    
}

function toggleEditTaskSuccess(){

    document.getElementById("popup-editTask-success").classList.toggle("active");
    document.getElementById("popup-editTask").classList.remove("active");

    
}

function toggleRepeatTaskSuccess(){

    document.getElementById("popup-repeat-task-success").classList.toggle("active");
    document.getElementById("popup-repeatTask").classList.remove("active");

    
}

function toggleReviseSuccess(){
    document.getElementById("popup-revise-task").classList.remove("active");
    document.getElementById("popup-revise-task-success").classList.toggle("active");

    
}

function toggleApproveSuccess(){
    document.getElementById("popup-approve-task").classList.remove("active");
    document.getElementById("popup-approve-task-success").classList.toggle("active");

    
}

function togglePopupInvoice(){

    document.getElementById("popup-view-invoice").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
  
    
}

function toggleAddCredit(){

    document.getElementById("popup-add-credit").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

    
}

function togglePaymentMethod(){

    document.getElementById("popup-credit-payment-method").classList.toggle("active");
    document.getElementById("popup-add-credit").classList.toggle("active");
   
    
}

function toggleChooseService(){

    document.getElementById("popup-choose-service").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

   
    
}

function toggleCreditSuccess(){
    
    document.getElementById("popup-credit-payment-method").classList.toggle("active");
    document.getElementById("popup-credit-add-success").classList.toggle("active");
   
    
}

function toggleEditTaskSuccess(){
    document.getElementById("popup-editTask").classList.remove("active");
    document.getElementById("popup-editTask-success").classList.toggle("active");
}

function toggleCreditPlanConfirm(){
    
    document.getElementById("popup-management-plan-confirm").classList.toggle("active");
    document.getElementById("popup-management-plan").classList.remove("active");
   
    
}

function toggleCreditPlanSuccess(){
    
    document.getElementById("popup-management-plan-success").classList.toggle("active");
    document.getElementById("popup-management-plan-confirm").classList.remove("active");
   
    
}

function toggleCreditPlan(){
    
    document.getElementById("popup-management-plan").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
   
    
}

function togglePwMngr(){
    
    document.getElementById("popup-pw-mngr").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
   
    
}

function toggleEditTask(){
    
    document.getElementById("popup-editTask").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
   
    
}

function toggleRepeatTask(){
    
    document.getElementById("popup-repeatTask").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
   
    
}

function toggleRepeatTaskSuccess(){
    
    document.getElementById("popup-repeatTask").classList.remove("active");
    document.getElementById("popup-repeatTask-success").classList.toggle("active");
   
    
}

function toggleAccountFAQ(){
    
    document.getElementById("popup-account-faqs").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");
    
}

function toggleCancelPaymentMethod(){

    document.getElementById("popup-credit-payment-method").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCancelTask(){

    document.getElementById("popup-editTask").classList.remove("active");
    document.getElementById("popup-repeatTask").classList.remove("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCancelAddCredit(){

    document.getElementById("popup-add-credit").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCancelNewTask(){

    document.getElementById("popup-choose-service").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

}

function toggleCancelInvoice(){

    document.getElementById("popup-view-invoice").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCloseEditPw(){

    document.getElementById("popup-pw-mngr").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

}

function toggleCloseViewTask(){

    document.getElementById("popup-revise-task").classList.remove("active");
    document.getElementById("popup-approve-task").classList.remove("active");
    document.getElementById("popup-editTask").classList.remove("active");
    document.getElementById("popup-repeatTask").classList.remove("active");
    document.getElementById("popup-approve-task-success").classList.remove("active");
    document.getElementById("popup-revise-task-success").classList.remove("active");
    document.getElementById("popup-editTask-success").classList.remove("active");
    document.getElementById("popup-repeatTask-success").classList.remove("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCloseService(){

    document.getElementById("popup-choose-service").classList.remove("active");
    document.getElementById("popup-taskReOccurence").classList.remove("active");
    document.getElementById("popup-taskAddSuccess").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

}

function toggleOverlayInvoice(){

    document.getElementById("popup-view-invoice").classList.toggle("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleOverlayPwMngr(){

    document.getElementById("popup-pw-mngr").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

}

function toggleOverlayCredit(){
    document.getElementById("popup-credit-payment-method").classList.remove("active");
    document.getElementById("popup-add-credit").classList.remove("active");
    document.getElementById("popup-credit-add-success").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

   
}

function toggleOverlayCreditPlan(){
    document.getElementById("popup-management-plan").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");
    document.getElementById("popup-management-plan-confirm").classList.remove("active");
    document.getElementById("popup-management-plan-success").classList.remove("active");
   
}

function toggleOverlayFAQ(){

    document.getElementById("popup-account-faqs").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

}

function openNavSettings(){
    
    var filterNav = document.getElementById("navSettings");

    if (filterNav.style.display === "none") {
        filterNav.style.display = "block";
      } else {
        filterNav.style.display = "none";
      }
}

function closeNavSettings(){

    document.getElementById("navSettings").style.display = "none";
    document.getElementById("openNav").style.display = "none";
    document.getElementById("closeNav").style.display = "block";
}

function openFilter(){

    var filterNav = document.getElementById("openNavFilter");

    if (filterNav.style.display === "none") {
        filterNav.style.display = "block";
      } else {
        filterNav.style.display = "none";
      }
}

function openNotifs(){

    var filterNotifTab = document.getElementById("notifTab");

    if (filterNotifTab.style.display === "none") {
        filterNotifTab.style.display = "block";
      } else {
        filterNotifTab.style.display = "none";
      }

}

function closeNotifs(){

    document.getElementById("notifTab").style.display = "none";
    document.getElementById("notifTabOne").style.display = "block";
    document.getElementById("notifTabTwo").style.display = "none";
}

// pop up to otp success
function toggleSuccess(){
    document.getElementById("popup-1").classList.toggle("active");
    document.getElementById("popup-2").classList.toggle("active");
}

function togglePwSaveToDb(){
    document.getElementById("popup-3").classList.toggle("active");
    document.getElementById("popup-2").classList.remove("active");
}

function toggleCancel(){

    document.getElementById("popup-1").classList.remove("active");
    document.getElementById("popup-2").classList.remove("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCloseFAQs(){
    document.getElementById("popup-account-faqs").classList.remove("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleCloseTickets(){
    document.getElementById("popup-1").classList.remove("active");
    document.getElementById("popup-submit-ticket").classList.remove("active");
    document.getElementById("overlay_id").classList.toggle("active");

}

function toggleOverlay(){
    
    document.getElementById("popup-1").classList.remove("active");
    document.getElementById("popup-2").classList.remove("active");
    document.getElementById("popup-3").classList.remove("active");
    document.getElementById("overlay_id").classList.remove("active");

}

//file name upload

// let inFile = document.getElementById('img');
// let outFile = document.getElementById('outputImg');

// inFile.addEventListener("input", ()=> {

//     if(inFile.files.length){
//         let outputN = inFile.files[0].name;
//         outFile.innerHTML =  outputN;
//     }
//     else{
//         outFile.innerHTML = "";
//     }
// })

// uncheck radio buttons

function uncheck() {
    //add credit popup
    document.getElementById("option1").checked = false;
    document.getElementById("option2").checked = false;
    document.getElementById("option3").checked = false;
    document.getElementById("option4").checked = false;
    
   
    const resetBtn = document.getElementById('credit-reset-btn');
    const creditResetField = document.getElementById('creditReset');

    const resetBtn2 = document.getElementById('confirmPayment_reset');
    const cardName = document.getElementById('cardholder_name');
    const cardNumber = document.getElementById('card_number');
    const expDate = document.getElementById('exp_date');
    const cardCCV = document.getElementById('card_ccv');

    resetBtn2.addEventListener('click', function() {
        cardCCV.value = '';
      });

    resetBtn.addEventListener('click', function() {
        creditResetField.value = '';
        cardName.value = '';
        cardNumber.value = '';
        expDate.value = '';
        cardCCV.value = '';
      });

    //confirm payment method popup
    document.getElementById("payment_option1").checked = false;
    document.getElementById("payment_option2").checked = false;
    document.getElementById("payment_option3").checked = false;
    document.getElementById("payment_option4").checked = false;
  }
  














const slidePage = document.querySelector(".slidePage");
const firstNextBtn = document.querySelector(".nextBtn");
const prevBtnSec = document.querySelector(".prev-1");
const nextBtnSec = document.querySelector(".next-1");
const prevBtnThird = document.querySelector(".prev-2");
const nextBtnThird = document.querySelector(".next-2");
const prevBtnFourth = document.querySelector(".prev-3");
const submitBtn = document.querySelector(".submit");
const progressTexts = document.querySelectorAll(".step p");
const progressChecks = document.querySelectorAll(".check");
const bullets = document.querySelectorAll(".bullet");

let max=4;
let current = 1;

firstNextBtn.addEventListener("click",()=>{
  slidePage.style.marginLeft="-25%";

  bullets[current-1].classList.add("active");
  animation = getComputedStyle(document.querySelectorAll('.bullet')[0], '::after').getPropertyValue('animation');
   console.log(animation);
  progressTexts[current-1].classList.add("active");
  progressChecks[current-1].classList.add("active");
  current +=1;
})

nextBtnSec.addEventListener("click",()=>{
  slidePage.style.marginLeft="-50%";
  bullets[current-1].classList.add("active");
  progressTexts[current-1].classList.add("active");
  progressChecks[current-1].classList.add("active"); 
  current +=1;
})
nextBtnThird.addEventListener("click",()=>{
  slidePage.style.marginLeft="-75%";
  bullets[current-1].classList.add("active");
  progressTexts[current-1].classList.add("active");
  progressChecks[current-1].classList.add("active"); 
  current +=1;
})

submitBtn.addEventListener("click",()=>{
  slidePage.style.marginLeft="-75%";
  bullets[current-1].classList.add("active");
  progressTexts[current-1].classList.add("active");
  progressChecks[current-1].classList.add("active"); 
  current +=1;
  setTimeout(() => {
    alert("fuck yeahh");
    location.reload();
  }, 800);
})





prevBtnSec.addEventListener("click",()=>{
  slidePage.style.marginLeft="0%";
  bullets[current-2].classList.remove("active");
  progressTexts[current-2].classList.remove("active");
  progressChecks[current-2].classList.remove("active"); 
  current -=1;
})
prevBtnThird.addEventListener("click",()=>{
  slidePage.style.marginLeft="-25%";
  bullets[current-2].classList.remove("active");
  progressTexts[current-2].classList.remove("active");
  progressChecks[current-2].classList.remove("active"); 
  current -=1;

})
prevBtnFourth.addEventListener("click",()=>{
  slidePage.style.marginLeft="-50%";
  bullets[current-2].classList.remove("active");
  progressTexts[current-2].classList.remove("active");
  progressChecks[current-2].classList.remove("active"); 
  current -=1;
})




function filterData() {
    const status = document.getElementById('filterSelect').value;
    const dataDiv = document.getElementById('data');
    const dataItems = dataDiv.children;
    
    // Loop through each data item and show/hide based on status
    for (let i = 0; i < dataItems.length; i++) {
      const item = dataItems[i];
      
      if (status === 'all') {
        // Show all data items
        item.classList.remove("hidden");
  
      } else if (item.classList.contains(status)) {
        // Show only data items with matching status
        item.classList.remove("hidden");
  
      } else {
        // Hide data items that don't match the status
        item.classList.add("hidden");
  
      }
    }
  }
  
