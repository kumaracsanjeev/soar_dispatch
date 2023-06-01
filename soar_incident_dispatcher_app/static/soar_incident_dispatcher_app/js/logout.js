var logout_btn = document.querySelector(".main_header-bar__logout-action");
var logout_section = document.querySelector(".main_header-bar--logout-section");
var backdrop = document.querySelector(".backdrop");

logout_btn.addEventListener("click", function() {
    logout_section.style.display = "block";
    backdrop.style.display = "block";
});


backdrop.addEventListener("click", function() {
    logout_section.style.display = "none";
    backdrop.style.display = "none";
});