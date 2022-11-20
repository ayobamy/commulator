const container = document.querySelector(".container");
const signUpBtn = document.querySelector(".bkg button");

signUpBtn.addEventListener("click", () => {
    container.classList.toggle("change");
});