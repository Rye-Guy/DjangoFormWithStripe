console.log('Animation Hello')

billingInfoBtn = document.getElementById('sideTrigger')
billingInfoContainer = document.getElementById('billingInfoContainer')

billingInfoContainer.className = 'animated fadeInLeft'

allInputs = document.querySelectorAll("input[type='text']")
allUrlInputs = document.querySelectorAll("input[type='url']")
allEmailInputs = document.querySelectorAll("input[type='email']")

function helperTextCheck(input){
    input.addEventListener('blur', (ev)=>{
        console.log(input, ev)
        if(input.value == "" || input.value.length < 0){
            console.log('leave helper text')
        }
        else{
            console.log(input.nextSibling)
            input.nextSibling.className = 'helperTextRemain'
            console.log('remove initial helper text style')
        }
    })
}

allInputs.forEach((input)=>{
   helperTextCheck(input)
})

allUrlInputs.forEach((input)=>{
   helperTextCheck(input)
})

allEmailInputs.forEach((input)=>{
    helperTextCheck(input)
})

