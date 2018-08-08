# improved-youbike-web
Adjust some elements at youbike.com.tw to improve UI and UX.


## Normal Login Page
Log in multiple accounts more efficiently: 
```js
javascript:
if (window.location.href.includes("ntpc.youbike.com.tw/login")) {
    
    //Put your YouBike IDs in the array (usually phone numbers)
    var ids = ["09XXXXXXXX", "09XXXXXXXX", "09XXXXXXXX"];

    //Put your password
    var pw = ["XXXXXXXXX", "XXXXXXXXXXX", "XXXXXXXXXXX"]; 
    
    var br = document.createElement("br");
    var idSelect = document.createElement("SELECT");
    idSelect.name = "account";
    idSelect.innerHTML = '<option value="-1">請選擇帳號</option>';
    ids.forEach(function(e, i) {
        idSelect.innerHTML += '<option value="' + i + 1 + '">' + e + '</option>';
    });
    
    var form = document.querySelector("form");
    var img = document.getElementById("verify_image");
    form.childNodes[5].insertBefore(br, img);
    form.insertBefore(idSelect, form.childNodes[5]);
    img.style.width = "407px";
    form.querySelectorAll("input")[0].type = "hidden";
    form.querySelectorAll("input")[1].type = "hidden";

    var inputVerify = document.getElementById("login-verify");

    inputVerify.addEventListener("keyup", function() {
        var choice = idSelect.options[idSelect.selectedIndex].text;
        if (this.value.length == 4) {
            document.getElementById("account").value = choice;
            document.getElementById("password").value = pw[idSelect.selectedIndex - 1];
            login.dataSend();
        }
    });

    document.querySelector("select[name=account]").addEventListener("change", function() {
        inputVerify.select();
    });
} else {
    window.location.href = "https://ntpc.youbike.com.tw/login/";
}
```
