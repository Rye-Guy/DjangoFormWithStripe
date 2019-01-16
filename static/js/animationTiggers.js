formSubmit = document.getElementById('formSubmit')

billingInfoBtn = document.getElementById('billingInfoTrigger')
billingInfoContainer = document.getElementById('billingInfoContainer')


allInputs = document.querySelectorAll("input[type='text']")
allUrlInputs = document.querySelectorAll("input[type='url']")
allEmailInputs = document.querySelectorAll("input[type='email']")

function helperTextCheck(input){
    input.addEventListener('blur', (ev)=>{
        if(input.value == "" || input.value.length < 0 || input.value == " "){
            console.log('leave helper text')
        }
        else{
            input.nextSibling.className = 'helperTextRemain'
            console.log('remove initial helper text style')
        }
    })
}
formSubmit.addEventListener('click', (ev)=>{

    if(billingInfoContainer.className == 'animated fadeOutLeft'){
        ev.preventDefault()
        billingInfoContainer.className = 'animated fadeInLeft'
    }
})

billingInfoBtn.addEventListener('click', (ev)=>{
    ev.preventDefault()
    console.log(ev)
    if(billingInfoContainer.className == 'animated fadeOutLeft'){
        billingInfoContainer.className = 'animated fadeInLeft'
        billingInfoBtn.value = 'Hide Billing Info'
    }else{
        billingInfoContainer.className = 'animated fadeOutLeft'
        billingInfoBtn.value = 'Fill Billing Info'
    }
})


allInputs.forEach((input)=>{
   helperTextCheck(input)
})

allUrlInputs.forEach((input)=>{
   helperTextCheck(input)
})

allEmailInputs.forEach((input)=>{
    helperTextCheck(input)
})



