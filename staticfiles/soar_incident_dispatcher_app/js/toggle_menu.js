var toggle_button = document.querySelectorAll(".security--toolbar__button");
var menu_nav = document.querySelector(".security--toolbar__panel");
var security_icon = document.querySelector(".security--toolbar__icon")
var backdrop = document.querySelector(".backdrop");
var settings_nav = document.querySelector(".security--toolbar__panel-settings");
var help_nav = document.querySelector(".security--toolbar__panel-help")


toggle_button[0].addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    security_icon.style.opacity=1;
    menu_nav.style.display = "block";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";

});

toggle_button[1].addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    security_icon.style.opacity=1;
    settings_nav.style.display = "block";
    backdrop.style.display = "block";
    menu_nav.style.display = "none";
    help_nav.style.display = "none";

});

toggle_button[2].addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    security_icon.style.opacity=1;
    help_nav.style.display = "block";
    backdrop.style.display = "block";
    menu_nav.style.display = "none";
    settings_nav.style.display = "none";

});

backdrop.addEventListener("click", function() {
    menu_nav.style.display = "none";
    settings_nav.style.display = "none";
    backdrop.style.display = "none";
    help_nav.style.display = "none";
});