// const inputs=document.querySelectorAll('otp-input');
// for inputs.forEach((input,index)=>{
//     input.addEventListener("keydown",
//         (event)=>{
//             console.log(event.key==="Backspace",input.value==='')
//             if (event.key==="Backspace" && input.value===''){
//                 inputs[index-1].focus();
//             }
//         });
// });
// function next_field(currentField,nextFieldId){
//     if(currentField.value.length==1 && nextFieldId){
//         document.getElementById(nextFieldId).focus();
//         console.log(nextFieldId)
//     }
// }

const inputs=document.querySelectorAll('.otp-container input');
const button=document.querySelector('#id_submit');
inputs.forEach(input => {
    let lastInputStatus=0
    input.onkeyup=(e)=>{
        const currentElement=e.target
        const nextElement=input.nextElementSibling
        const prevElement=input.previousElementSibling


        if(prevElement && e.keyCode ===8){
            if (lastInputStatus===1){
                prevElement.value=''
                prevElement.focus()
            }
            button.setAttribute('disabled',true)
            lastInputStatus=1
        }else{
            if (currentElement.value){
                if(nextElement){
                    nextElement.focus()
                }else{
                    button.removeAttribute('disabled')
                    lastInputStatus=0
                }
            }
        }
    }
})