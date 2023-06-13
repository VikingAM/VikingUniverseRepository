
  // Multi Step Form
  const prevBtns = document.querySelectorAll(".btn-prev");
  const nextBtns = document.querySelectorAll(".btn-next");
  const prwBtns = document.querySelectorAll(".btn-prw");

  const progress = document.getElementById("progress");
  const formSteps = document.querySelectorAll(".form-step");
  const progressSteps = document.querySelectorAll(".progress-step");
  
  let formStepsNum = 0;
  
  nextBtns.forEach((btn) => {
    btn.addEventListener("click", () => {

      formStepsNum++;
      updateFormSteps();
      updateProgressbar();
    });
  });
  
  prwBtns.forEach((btn) => {
    btn.addEventListener("click", () => {

      formStepsNum = 0;

      let barTitle = document.getElementById("barTitle");
      let prBtn = document.getElementById("prBtn");
      let submitFormBtn = document.getElementById("submitFormBtn");

      barTitle.innerHTML = "Preview of New Task";
      prBtn.style.display = "none";
      submitFormBtn.style.display = "block";

      updateFormSteps();
      updateProgressbar();
    });
  });

  prevBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      formStepsNum--;
      updateFormSteps();
      updateProgressbar();
    });
  });
  
  function updateFormSteps() {
    formSteps.forEach((formStep) => {
      formStep.classList.contains("form-step-active") &&
        formStep.classList.remove("form-step-active");
    });
  
    formSteps[formStepsNum].classList.add("form-step-active");
  }
  
  function updateProgressbar() {
    progressSteps.forEach((progressStep, idx) => {
      if (idx < formStepsNum + 1) {
        progressStep.classList.add("progress-step-active");
      } else {
        progressStep.classList.remove("progress-step-active");
      }
    });
  
    
  }