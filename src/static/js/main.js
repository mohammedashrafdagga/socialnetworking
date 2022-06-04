$.ajax({
    type:'GET',
    url : '/post-json/',
    success: function(response){
        // get a data
        const data = JSON.parse(response.data)
        // select post
        const post = document.getElementById('post')
        setTimeout(()=>{
            data.forEach(el => {
                post.innerHTML += `<div>${el.fields.body}</div>`
                post.innerHTML += ` <hr class='bg-white'/>`
            })
            document.getElementById('spinner').classList.add('non-visable')
        }, 1000)
        
      
    },
    error: function(error){
        console.log(error)
    }
})