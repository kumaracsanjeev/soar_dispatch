// Block for Enabling Incident Assignment to Logged In User
let assigned_checkbox_itm = document.getElementsByClassName("assigne_checkbox_class");
for (i=0; i < assigned_checkbox_itm.length; i++){
    assigned_checkbox_itm[i].addEventListener("change", function(){
    if (this.checked == true){
        const url = "https://soardispatchernew-sanjeev-dev.apps.sandbox.x8i5.p1.openshiftapps.com/update";
        const data = { inc_id: this.id, user: $('.main_header-bar--logout').data('url'), checked: true};
        fetch(
            url,
            {
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
                method: "POST"
            }
        )
        .then(data => data.json())
        .then((json) => {
            //alert("Assigned to: "+$('.main_header-bar--logout').data('url'));
            this.nextElementSibling.innerText = $('.main_header-bar--logout').data('url');
        });
        console.info("checked incidentID "+ this.id + "LoggedIn user "+ $('.main_header-bar--logout').data('url'));
        
    }
    else
    {
        const url = "https://soardispatchernew-sanjeev-dev.apps.sandbox.x8i5.p1.openshiftapps.com/update";
        const data = { inc_id: this.id, user: $('.main_header-bar--logout').data('url'), checked: false};
        fetch(
            url,
            {
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data),
                method: "POST"
            }
        )
        .then(data => data.json())
        .then((json) => {
            //alert("Un assigned :"+ $('.main_header-bar--logout').data('url'));
            this.nextElementSibling.innerText = "";
        });
        console.info("Unchecked incidentID "+ this.id + "LoggedIn user "+ $('.main_header-bar--logout').data('url'));
    };
    })
}