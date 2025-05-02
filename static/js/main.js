// Dropzone.autoDiscover=false;
// const myDropzone= new Dropzone('#my-dropzone',{
//     url:'upload/',
//     maxFiles:5,
//     maxFilesize:2,
//     acceptedFiles:'.jpg',
// })
{/* <script src="https://cdnjs.cloudflare.com/ajax/libs/dropzone/5.9.3/min/dropzone.min.js"></script> */}
console.log("main js loaded")

function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function(){
        const output = document.getElementById('image-preview');
        output.src = reader.result;
        output.classList.remove('hidden');
    };
    reader.readAsDataURL(event.target.files[0]);
}



