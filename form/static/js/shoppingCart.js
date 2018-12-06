shoppingCart = document.getElementById('shoppingCart')

//first value is dates selected, next is booth option value, next is number of booths, finally is an array for additional booth options.
torontoCart = [0, 0, 0, []]

winnipegCart = [0, 0, 0, []]

calgaryCart = [0, 0, 0, []]

edmontonCart = [0, 0, 0, []]



allDatesCheckboxes = document.querySelectorAll('input.dates-select')
allBoothOptionsRadios = document.querySelectorAll('input.booth-options-select')
allAdditionalOptions = document.querySelectorAll('input.fair-options')




allDatesCheckboxes.forEach((input) =>{
    input.addEventListener('click', ()=>{
    parentUl = input.parentElement.parentElement.parentElement.id
        if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
             cartItem.innerText = cartText
             shoppingCart.append(cartItem)
             if(parentUl == 'id_toronto_dates'){
                torontoCart[0]++
             }if(parentUl == 'id_calgary_dates'){
                calgaryCart[0]++
             }if(parentUl == 'id_edmonton_dates'){
                edmontonCart[0]++
             }if(parentUl ==  'id_winnipeg_dates'){
                winnipegCart[0]++
             }


        }else if(!input.checked){
            findInputId = input.parentElement.innerText
            document.getElementById(findInputId).remove()
            if(parentUl == 'id_toronto_dates'){
                torontoCart[0]--
            }if(parentUl == 'id_calgary_dates'){
                calgaryCart[0]--
            }if(parentUl == 'id_edmonton_dates'){
             edmontonCart[0]--
            }if(parentUl =  'id_winnipeg)_dates'){
             winnipegCart[0]--
             }

        }
    })
})

allBoothOptionsRadios.forEach((input) =>{
    input.addEventListener('click', ()=>{
        parentUl = input.parentElement.parentElement.parentElement.id
        cartItem = document.createElement('li')
        cartItemText = input.parentElement.innerText
        cartItem.innerText = cartItemText
        boothValue = parseInt(input.getAttribute('value'))
        if(input.checked){
           if(parentUl == 'id_toronto_booth_options'){
              if(document.getElementById('torontoSingleCartItem')){
                 document.getElementById('torontoSingleCartItem').remove()
              }
              cartItem.id = 'torontoSingleCartItem'
              shoppingCart.append(cartItem)
              torontoCart[1] = boothValue
              amountSpent = calculateTotal('toronto', torontoCart)
              document.getElementById('torontoCartNumber').innerText = amountSpent
              calculateGrandTotal()
           }
           if(parentUl == 'id_calgary_booth_options'){
              if(document.getElementById('calgarySingleCartItem')){
                 document.getElementById('calgarySingleCartItem').remove()
              }
              cartItem.id = 'calgarySingleCartItem'
              shoppingCart.append(cartItem)
              calgaryCart[1] = boothValue
              amountSpent = calculateTotal('calgary', calgaryCart)
              document.getElementById('calgaryCartNumber').innerText = amountSpent
              calculateGrandTotal()
           }
           if(parentUl == 'id_edmonton_booth_options'){
              if(document.getElementById('edmontonSingleCartItem')){
                 document.getElementById('edmontonSingleCartItem').remove()
              }
              cartItem.id = 'edmontonSingleCartItem'
              shoppingCart.append(cartItem)
              edmontonCart[1] = boothValue
              amountSpent = calculateTotal('edmonton', edmontonCart)
              document.getElementById('edmontonCartNumber').innerText = amountSpent
              calculateGrandTotal()

           }
           if(parentUl == 'id_winnipeg_booth_options'){
              if(document.getElementById('winnipegSingleCartItem')){
                 document.getElementById('winnipegSingleCartItem').remove()
              }
              cartItem.id = 'winnipegSingleCartItem'
              shoppingCart.append(cartItem)
              winnipegCart[1] = boothValue
              amountSpent = calculateTotal('winnipeg', winnipegCart)
              document.getElementById('winnipegCartNumber').innerText = amountSpent
              calculateGrandTotal()
           }
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

function calculateTotal(boothZone, cartName){
            cartName[2] = parseInt(document.getElementById(`id_${boothZone}_additional_booth_option`).value) + 1
            return parseInt(cartName[0] * (cartName[1] * cartName[2]) + cartName[3])
}

function calculateGrandTotal(){
       value1 = calculateTotal('toronto', torontoCart)
       value2 = calculateTotal('winnipeg', winnipegCart)
       value3 = calculateTotal('calgary', calgaryCart)
       value4 = calculateTotal('edmonton', edmontonCart)
       grandTotal = value1 + value2 + value3 + value4
       roughTaxCal = grandTotal * .13
       overallTotalWithTax = grandTotal + roughTaxCal
       document.getElementById('cart-total').innerText = overallTotalWithTax
       return overallTotalWithTax
}

cartTotal = document.getElementById('cart-total')


