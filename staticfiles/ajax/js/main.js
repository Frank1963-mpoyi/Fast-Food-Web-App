const alertBox = document.getElementById('alert-box') // get the id of div in index.html and store it in the variable
const imgBox = document.getElementById('img-box')// store id of image in the variable
const form = document.getElementById('p-form')

const nam = document.getElementById('id_name')
const description = document.getElementById('id_description')
const image = document.getElementById('id_image')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const url =""

// =======This is Upload a Image
//image.addEventListener('change', ()=>{}) //on the change event we are going to execute something 
image.addEventListener('change', ()=>{
    const img_data = image.files[0] // varaiable to grab the image itself 
    const url = URL.createObjectURL(img_data) //create a block and put data
    imgBox.innerHTML =`<img src="${url}" width="100%" >`// take the object of image above and pass url to display it 
})

  //==============Send the data
form.addEventListener('submit', e=>{
    e.preventDefault() //we dont want the page to be reloaded
    const fd = new FormData() //store in the variable fd form data 
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('nam', nam.value)
    fd.append('description', description.value)
    fd.append('image', image.files[0])

    //we have all the field added or append to form data we need now Ajax
    $.ajax({
        type:'POST',
        url: url, 
        enctype:'multipart/form-data', //we sending the images in database we need to have this
        data: fd, //send the data itself is the fd we created
        success: function(response){// display what will happen in success
            console.log(response)

        },
        error: function(error){
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,
    })


})