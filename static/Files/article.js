

var test_form=document.getElementById("check")
        test_form.addEventListener("click",function(){
            var bid=this.dataset.blogid;
            var text_area=document.getElementById("blog").value;
            change(bid,text_area)

        })
        function change(bid,text_area)
            {
                var url='/update_con'
                fetch(url,{
                    method:'POST',
                    headers:{
                        'Content-Type':'application/json',
                        'X-CSRFToken':csrftoken,
                    },
                    body:JSON.stringify({'blogid':bid,'textdata':text_area})
                })
                .then((response)=>{
                    return response.json()
                })

                .then((data)=>{
                    alert(data)
                    location.reload(true);
                    console.log("value:",data)
                    
                })
            }

function openForm() {
    document.getElementById("blogcontent").style.display = "block";
    }
    function closeForm() {
        document.getElementById("blogcontent").style.display = "none";
    }
    function openform1()
    {
        document.getElementById("blogimage").style.display = "block";
    }
    function closeform1()
    {
        document.getElementById("blogimage").style.display = "none";
    }
    function openform2()
    {
        document.getElementById("blogtheme").style.display = "block";
    }
    function closeform2()
    {
        document.getElementById("blogtheme").style.display = "none";
    }


