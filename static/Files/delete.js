var itemdel=document.getElementById("delete")
itemdel.addEventListener('click',function(){
    var ids=this.dataset.blogid
    alert(ids)
    console.log(ids)
    deleting(ids);
})
function deleting(bid)
    {
        alert("request")
        var url='/delete'
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'blogid':bid})
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