function enable(){
    $("#imp-btn").removeAttr("disabled");
    $('#imp-btn').removeClass('disabled');
}

function validatepassword() {
    
    var pass1 = document.getElementById("password").value;
    var pass2= document.getElementById("password1").value;
    var emsg = document.getElementById("error_msg");
    var element = document.getElementById("imp-btn");
    document.getElementById("imp-btn").disable=false;
    emsg.innerHTML = "";
    if(pass1=="" && pass2=="")
    {

    }
    else
    {
        if (pass1!=pass2) {
            emsg.innerHTML = "<font style='color:red;'>Password Not Matched  <i class='fa fa-ban'></i></font>";
        }
        else{
            emsg.innerHTML = "<font style='color:green;'>Password Matched <i class='fa fa-check-circle' aria-hidden='true'></i></font>";
                enable();
                $("#passinfo").hide();

        }
    }
}

function passcheck(){
    $("#passinfo").show();
    f1=0;f2=0;f3=0;
    var format = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
    var pass1 = document.getElementById("password").value;
    if(pass1.length>7)
    {
        f1=1;
        document.getElementById("first").innerHTML="<font style='color:green;'><i class='fa fa-check-circle' aria-hidden='true'></i></font>";
    }
    else{document.getElementById("first").innerHTML="<font style='color:red;'><i class='fa fa-ban'></i></font>";}
    var matches = pass1.match(/\d+/g);
    if (matches != null && format.test(pass1)) {f2=1;
        document.getElementById("second").innerHTML="<font style='color:green;'><i class='fa fa-check-circle' aria-hidden='true'></i></font>";
    }
    else{document.getElementById("second").innerHTML="<font style='color:red;'><i class='fa fa-ban'></i></font>";}
    format1=/[A-Z]+/;
    if(format1.test(pass1)){
        f3=1;
        document.getElementById("third").innerHTML="<font style='color:green;'><i class='fa fa-check-circle' aria-hidden='true'></i></font>";
    }
    else
    {document.getElementById("third").innerHTML="<font style='color:red;'><i class='fa fa-ban'></i></font>";}
   
  };