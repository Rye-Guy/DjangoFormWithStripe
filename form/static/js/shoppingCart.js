shoppingCart = document.getElementById('shoppingCart')

boothType = null
numberOfBooths = 1
selectedDates = 0
boothOptions = null


allDatesCheckboxes = document.querySelectorAll('input.dates-select')
allBoothOptionsRadios = document.querySelectorAll('input.booth-options-select')
allAdditionalOptions = document.querySelectorAll('input.fair-options')
console.log(allAdditionalOptions)

additonalBoothsSelect = document.getElementById('id_additional_booth_option')
//numberOfBooths = parseInt(additonalBoothsSelect.value)

allDatesCheckboxes.forEach((input) =>{
    input.addEventListener('click', ()=>{
        if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
             cartItem.innerText = cartText
             shoppingCart.append(cartItem)
             selectedDates++

        }else if(!input.checked){
            findInputId = input.parentElement.innerText
            document.getElementById(findInputId).remove()
            selectedDates--
            console.log(numberOfBooths)
        }
    })
})

allBoothOptionsRadios.forEach((input) =>{

    input.addEventListener('click', ()=>{
        parentUl = input.parentElement.parentElement.parentElement.id
        cartItem = document.createElement('li')
        cartItemText = input.parentElement.innerText
        cartItem.innerText = cartItemText

        if(input.checked){
           if(parentUl == 'id_toronto_booth_options'){
              if(document.getElementById('torontoSingleCartItem')){
                 document.getElementById('torontoSingleCartItem').remove()
              }
              cartItem.id = 'torontoSingleCartItem'
              shoppingCart.append(cartItem)
           }
           if(parentUl == 'id_calgary_booth_options'){
              if(document.getElementById('calgarySingleCartItem')){
                 document.getElementById('calgarySingleCartItem').remove()
              }
              cartItem.id = 'calgarySingleCartItem'
              shoppingCart.append(cartItem)
           }
           if(parentUl == 'id_edmonton_booth_options'){
              if(document.getElementById('edmontonSingleCartItem')){
                 document.getElementById('edmontonSingleCartItem').remove()
              }
              cartItem.id = 'edmontonSingleCartItem'
              shoppingCart.append(cartItem)
           }
           if(parentUl == 'id_winnipeg_booth_options'){
              if(document.getElementById('winnipegSingleCartItem')){
                 document.getElementById('winnipegSingleCartItem').remove()
              }
              cartItem.id = 'winnipegSingleCartItem'
              shoppingCart.append(cartItem)
           }

           boothValue = parseInt(input.getAttribute('value'))
           boothType = boothValue
           calculateTotal(boothType, numberOfBooths, selectedDates, boothOptions)
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
            calculateTotal(boothType, numberOfBooths, selectedDates, boothOptions)

        }else if(!input.checked){
           findInputId = input.parentElement.innerText
           document.getElementById(findInputId).remove()
           calculateTotal(boothType, numberOfBooths, selectedDates, boothOptions)

        }
    })
})

function clearDiv(id){
    document.getElementById(id).innerHTML = ''

}



cartTotal = document.getElementById('cart-total')

function calculateTotal(boothType, numberOfBooths, selectedDates, boothOptions){
    roughTaxCalc = ((boothType * numberOfBooths) * selectedDates + boothOptions) * .13
    cartTotal.innerText = ((boothType * numberOfBooths) * selectedDates + boothOptions) + roughTaxCalc
    return ((boothType * numberOfBooths) * selectedDates + boothOptions) * .13
}


