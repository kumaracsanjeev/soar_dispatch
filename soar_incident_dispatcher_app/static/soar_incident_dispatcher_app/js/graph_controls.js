var graph_1 = document.querySelector(".graph_1_controls_zoom");
var graph_2 = document.querySelector(".graph_2_controls_zoom");
var graph_3 = document.querySelector(".graph_3_controls_zoom");
var graph_4 = document.querySelector(".graph_4_controls_zoom");
var graph_5 = document.querySelector(".graph_5_controls_zoom");
var graph_6 = document.querySelector(".graph_6_controls_zoom");

//Graph Download Icon Links
var graph_1_download = document.querySelector(".graph_1_controls_download");
var graph_2_download = document.querySelector(".graph_2_controls_download");
var graph_3_download = document.querySelector(".graph_3_controls_download");
var graph_4_download = document.querySelector(".graph_4_controls_download");
var graph_5_download = document.querySelector(".graph_5_controls_download");
var graph_6_download = document.querySelector(".graph_6_controls_download");

var graph_1_canvas = document.getElementById("myPieChart_1")
var graph_2_canvas = document.getElementById("myPieChart_2")
var graph_3_canvas = document.getElementById("myBarChart")
var graph_4_canvas = document.getElementById("myLineChart")
var graph_5_canvas = document.getElementById("myPolarChart")
var graph_6_canvas = document.getElementById("myRadarChart")

var menu_nav = document.querySelector(".security--toolbar__panel");
var security_icon = document.querySelector(".security--toolbar__icon")
var backdrop = document.querySelector(".back-drop");
var settings_nav = document.querySelector(".security--toolbar__panel-settings");
var help_nav = document.querySelector(".security--toolbar__panel-help");
var graph_chart_1 = document.querySelector(".chart-container-pie_1");
var graph_chart_2 = document.querySelector(".chart-container-pie_2");
var graph_chart_3 = document.querySelector(".chart-container-bar");
var graph_chart_4 = document.querySelector(".chart-container-line");
var graph_chart_5 = document.querySelector(".chart-container-polar");
var graph_chart_6 = document.querySelector(".chart-container-radar");


graph_1_download.addEventListener("click", function(){
    var url_base64jp = graph_1_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_1_download.querySelector(".download_icon");
    a.href = url_base64jp
});

graph_1_download.addEventListener("click", function(){
    var url_base64jp = graph_1_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_1_download.querySelector(".download_icon");
    a.href = url_base64jp
});
graph_2_download.addEventListener("click", function(){
    var url_base64jp = graph_2_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_2_download.querySelector(".download_icon");
    a.href = url_base64jp
});
graph_3_download.addEventListener("click", function(){
    var url_base64jp = graph_3_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_3_download.querySelector(".download_icon");
    a.href = url_base64jp
});
graph_4_download.addEventListener("click", function(){
    var url_base64jp = graph_4_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_4_download.querySelector(".download_icon");
    a.href = url_base64jp
});
graph_5_download.addEventListener("click", function(){
    var url_base64jp = graph_5_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_5_download.querySelector(".download_icon");
    a.href = url_base64jp
});
graph_6_download.addEventListener("click", function(){
    var url_base64jp = graph_6_canvas.toDataURL("image/jpg", "1.0");
    var a = graph_6_download.querySelector(".download_icon");
    a.href = url_base64jp
});
graph_1.addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    menu_nav.style.display = "none";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";
    security_icon.style.opacity=1;
    graph_chart_1.style.zIndex="8002";
    graph_chart_1.style.margin= "2.5rem 5rem 2.5rem 5rem";
    graph_chart_1.style.background="#292929";
    graph_chart_1.style.width="80vw";
    graph_chart_1.style.height="80vh";
    graph_chart_1.style.borderRadius="2rem";
    graph_chart_1.style.boxShadow="4px 4px 15px 0px #626161";
    graph_chart_1.style.position="fixed";
    graph_chart_1.style.top="4rem";
    
});

graph_2.addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    menu_nav.style.display = "none";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";
    security_icon.style.opacity=1;
    graph_chart_2.style.zIndex="8002";
    graph_chart_2.style.margin= "2.5rem 5rem 2.5rem 5rem";
    graph_chart_2.style.background="#292929";
    graph_chart_2.style.width="80vw";
    graph_chart_2.style.height="80vh";
    graph_chart_2.style.borderRadius="2rem";
    graph_chart_2.style.boxShadow="4px 4px 15px 0px #626161";
    graph_chart_2.style.position="fixed";
    graph_chart_2.style.top="4rem";
    graph_chart_1.style.display = "none";
    
});

graph_3.addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    menu_nav.style.display = "none";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";
    security_icon.style.opacity=1;
    graph_chart_3.style.zIndex="8002";
    graph_chart_3.style.margin= "2.5rem 5rem 2.5rem 5rem";
    graph_chart_3.style.background="#292929";
    graph_chart_3.style.width="80vw";
    graph_chart_3.style.height="80vh";
    graph_chart_3.style.borderRadius="2rem";
    graph_chart_3.style.boxShadow="4px 4px 15px 0px #626161";
    graph_chart_3.style.position="fixed";
    graph_chart_3.style.top="4rem";
    
});

graph_4.addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    menu_nav.style.display = "none";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";
    security_icon.style.opacity=1;
    graph_chart_4.style.zIndex="8002";
    graph_chart_4.style.margin= "2.5rem 5rem 2.5rem 5rem";
    graph_chart_4.style.background="#292929";
    graph_chart_4.style.width="80vw";
    graph_chart_4.style.height="80vh";
    graph_chart_4.style.borderRadius="2rem";
    graph_chart_4.style.boxShadow="4px 4px 15px 0px #626161";
    graph_chart_4.style.position="fixed";
    graph_chart_4.style.top="4rem";
    graph_chart_3.style.display = "none";
    
});


graph_5.addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    menu_nav.style.display = "none";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";
    security_icon.style.opacity=1;
    graph_chart_5.style.zIndex="8002";
    graph_chart_5.style.margin= "2.5rem 5rem 2.5rem 5rem";
    graph_chart_5.style.background="#292929";
    graph_chart_5.style.width="80vw";
    graph_chart_5.style.height="80vh";
    graph_chart_5.style.borderRadius="2rem";
    graph_chart_5.style.boxShadow="4px 4px 15px 0px #626161";
    graph_chart_5.style.position="fixed";
    graph_chart_5.style.top="4rem";
    
});

graph_6.addEventListener("click", function() {
    //toggle_button.innerHTML = '<svg focusable="false" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" fill="currentColor" aria-hidden="true" style="will-change: transform;" width="20" height="20" viewBox="0 0 32 32" class="security--icon security--toolbar__icon"><path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path></svg>';
    menu_nav.style.display = "none";
    backdrop.style.display = "block";
    settings_nav.style.display = "none";
    help_nav.style.display = "none";
    security_icon.style.opacity=1;
    graph_chart_6.style.zIndex="8002";
    graph_chart_6.style.margin= "2.5rem 5rem 2.5rem 5rem";
    graph_chart_6.style.background="#292929";
    graph_chart_6.style.width="80vw";
    graph_chart_6.style.height="80vh";
    graph_chart_6.style.borderRadius="2rem";
    graph_chart_6.style.boxShadow="4px 4px 15px 0px #626161";
    graph_chart_6.style.position="fixed";
    graph_chart_6.style.top="4rem";
    graph_chart_5.style.display = "none";
    
});

backdrop.addEventListener("click", function() {
    menu_nav.style.display = "none";
    settings_nav.style.display = "none";
    backdrop.style.display = "none";
    help_nav.style.display = "none";
    graph_chart_1.style.zIndex="";
    graph_chart_1.style.margin= "";
    graph_chart_1.style.background="#292929";
    graph_chart_1.style.width="46.5vw";
    graph_chart_1.style.height="55vh";
    graph_chart_1.style.borderRadius="";
    graph_chart_1.style.boxShadow="";
    graph_chart_1.style.position="";
    graph_chart_1.style.top="";

    graph_chart_2.style.zIndex="";
    graph_chart_2.style.margin= "";
    graph_chart_2.style.background="#292929";
    graph_chart_2.style.width="46.5vw";
    graph_chart_2.style.height="55vh";
    graph_chart_2.style.borderRadius="";
    graph_chart_2.style.boxShadow="";
    graph_chart_1.style.display = "block";
    graph_chart_2.style.position="";
    graph_chart_2.style.top="";

    graph_chart_3.style.zIndex="";
    graph_chart_3.style.margin= "";
    graph_chart_3.style.background="#292929";
    graph_chart_3.style.width="46.5vw";
    graph_chart_3.style.height="55vh";
    graph_chart_3.style.borderRadius="";
    graph_chart_3.style.boxShadow="";
    graph_chart_3.style.position="";
    graph_chart_3.style.top="";

    graph_chart_4.style.zIndex="";
    graph_chart_4.style.margin= "";
    graph_chart_4.style.background="#292929";
    graph_chart_4.style.width="46.5vw";
    graph_chart_4.style.height="55vh";
    graph_chart_4.style.borderRadius="";
    graph_chart_4.style.boxShadow="";
    graph_chart_3.style.display="block";
    graph_chart_4.style.position="";
    graph_chart_4.style.top="";

    graph_chart_5.style.zIndex="";
    graph_chart_5.style.margin= "";
    graph_chart_5.style.background="#292929";
    graph_chart_5.style.width="46.5vw";
    graph_chart_5.style.height="55vh";
    graph_chart_5.style.borderRadius="";
    graph_chart_5.style.boxShadow="";
    graph_chart_5.style.position="";
    graph_chart_5.style.top="";


    graph_chart_6.style.zIndex="";
    graph_chart_6.style.margin= "";
    graph_chart_6.style.background="#292929";
    graph_chart_6.style.width="46.5vw";
    graph_chart_6.style.height="55vh";
    graph_chart_6.style.borderRadius="";
    graph_chart_6.style.boxShadow="";
    graph_chart_5.style.display="block";
    graph_chart_6.style.position="";
    graph_chart_6.style.top="";
    
});