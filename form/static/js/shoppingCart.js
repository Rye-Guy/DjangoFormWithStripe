console.log('Im in the shopping cart js file :D')
torontoDatesList = document.getElementById('id_toronto_dates')
console.log(torontoDatesList)

shoppingCart = document.getElementById('shoppingCart')

boothType = null
numberOfBooths = 0
selectedDates = 0
boothOptions = null


allDatesCheckboxes = document.querySelectorAll('input.dates-select')
allBoothOptionsCheckboxes = document.querySelectorAll('input.booth-options-select')
allAdditionalOptions = document.querySelectorAll('input.fair-options')
console.log(allAdditionalOptions)

additonalBoothsSelect = document.getElementById('id_additional_booth_option')

allDatesCheckboxes.forEach((input) =>{
    input.addEventListener('click', ()=>{
        if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
             cartItem.innerText = cartText
             shoppingCart.append(cartItem)
             numberOfBooths++
             console.log(numberOfBooths)
             console.log(additonalBoothsSelect.value)
        }else if(!input.checked){
            findInputId = input.parentElement.innerText
            document.getElementById(findInputId).remove()
            numberOfBooths--
            console.log(numberOfBooths)
        }
    })
})

allBoothOptionsCheckboxes.forEach((input) =>{
    input.addEventListener('click', ()=>{
        if(input.checked){
           cartItemText = input.parentElement.innerText
           cartItem = document.createElement('li')
           cartItem.id = cartItemText
           cartItem.innerText = cartItemText
           boothValue = parseInt(input.getAttribute('value'))
           boothType += boothValue
           shoppingCart.append(cartItem)
           console.log(boothType)
        }else if(!input.checked){
           boothValue = parseInt(input.getAttribute('value'))
           boothType -= boothValue
           findInputId = input.parentElement.innerText
           document.getElementById(findInputId).remove()
           console.log(boothType)
        }
    })
})

allAdditionalOptions.forEach((input)=>{
    input.addEventListener('click', ()=>{
        if(input.checked){
            cartItemText = input.parentElement.innerText
            cartItem = document.createElement('li')
            cartItem.id = cartItemText
            cartItem.innerText = cartItemText
            shoppingCart.append(cartItem)
        }else if(!input.checked){
           findInputId = input.parentElement.innerText
           document.getElementById(findInputId).remove()
        }
    })
})

function clearDiv(id){
    document.getElementById(id).innerHTML = ''

}


console.log(selectedDates)
function gatherInputData(){


    function calculateTotal(boothType, numberOfBooths, selectedDates, boothOptions){

    }
}

gatherInputData()


