formSubmit = document.getElementById('formSubmit')
viewCartBtn = document.getElementById('viewCartBtn')
priceBreakdown = document.getElementById('priceBreakdown')
viewRepTools = document.getElementById('viewRepTools')
repToolsContainer = document.getElementById('repTools')
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
            if(input.parentNode.className == 'billingInfoLabels'){
                 input.nextSibling.className = 'helperTextRemain'
                 console.log('remove initial helper text style')
                }
        }
    })
}

viewCartBtn.addEventListener('click', (ev)=>{
    ev.preventDefault()
    if(priceBreakdown.className == 'animated fadeInRight'){
        priceBreakdown.className = 'animated fadeOutRight';
    }else{
        priceBreakdown.className = 'animated fadeInRight';
        priceBreakdown.style.display = 'block'
    }
    
})


viewRepTools.addEventListener('click', (ev)=>{
    if(repTools.className == 'animated fadeInLeft'){
        viewRepTools.value = 'View Tools'
        repTools.className = 'animated fadeOutLeft';
    }
    else if(repTools.className == 'animated' || repTools.className == 'animated fadeOutLeft'){
        viewRepTools.value = 'Hide Tools'
        repTools.className = 'animated fadeInLeft';
    }


})

formSubmit.addEventListener('click', (ev)=>{
    
    if(billingInfoContainer.className == 'animated fadeOutLeft'){
        ev.preventDefault()
        document.getElementById('priceBreakdown').style.display = 'block'
        billingInfoContainer.className = 'animated fadeInLeft'
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



