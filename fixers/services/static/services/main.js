document.querySelectorAll(".status-btn").forEach(button => {
    button.addEventListener("click",function(){
        const job_id = this.dataset.id;
        const status = this.dataset.status;
        fetch(`/services/status_update/${job_id}`,{
            method:"POST",
            headers:{
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body:JSON.stringify({
                status:status
            })

        })
              .then(response=>response.json())
              .then(data=>{
                if(data.success){
                   alert("updated");

            
                  this.parentElement.innerHTML= `Status: ${status}`;

                }
    });
    })

     
});
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}