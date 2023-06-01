let ul_itm = document.getElementById("html_body_cust_lst_itms__ul_class");
let lst_itm = ul_itm.getElementsByClassName("inst_optn");

for (i=0; i < lst_itm.length; i++){
    lst_itm[i].addEventListener("click", function()
    {
        var current = ul_itm.getElementsByClassName("active_ele");
        if (current.length == 0){
            this.className += " active_ele"
        }
        else{
            let last_selected_cls_str = current[0].className;
            current[0].className = last_selected_cls_str.replace("active_ele", "");
            this.className +=  " active_ele";
        }        
        let selected_instance = this.title.replaceAll('.', '');
        
        //get the exact table and change the display settings
        let selected_table_div_section = document.getElementsByClassName(selected_instance);
        let all_table_div_section = document.getElementsByClassName("html_body_sec_table_div");
        for (i=0; i < all_table_div_section.length; i++){
            all_table_div_section[i].style.display = "none";
        };
        selected_table_div_section[0].style.display = "block";
    });
    };