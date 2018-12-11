shoppingCart = document.getElementById('shoppingCart')

//first value is dates selected, next is booth option value, next is number of booths, finally is additional options total if their is additonal options at the venue. Extra booths are under this on the front but for the cost calculation they serve a different purpose.
torontoCart = [0, 0, 0, 0]

winnipegCart = [0, 0, 0, 0]

calgaryCart = [0, 0, 0, 0]

edmontonCart = [0, 0, 0, 0]


//query selectors that create arrays of relevent input elements for each section of the form. These are used later in the code with forEach loops to add custom behaviour depending on which form is being filled.
allDatesCheckboxes = document.querySelectorAll('input.dates-select')
allBoothOptionsRadios = document.querySelectorAll('input.booth-options-select')
allAdditionalOptions = document.querySelectorAll('input.fair-options')



//Keeps track of selected dates and add event listeners for click events and run our conditionals to make sure the proper card receives the relevant selection.
allDatesCheckboxes.forEach((input) =>{
    input.addEventListener('click', ()=>{
    //parent elements will contain our ID for making sure we are editing the appropriate Cart.
    parentUl = input.parentElement.parentElement.parentElement.id
        //for now I created an LI item for the cart UL and append it just to see what has been selected. This will be updated at some point with a cleaner looking cart for clients
        if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
             cartItem.innerText = cartText
             shoppingCart.append(cartItem)
             //our conditional checks to update our cart with a date selection.
             if(parentUl == 'id_toronto_dates'){
                console.log('date added')
                torontoCart[0]++
             }else if(parentUl == 'id_calgary_dates'){
                calgaryCart[0]++
             }else if(parentUl == 'id_edmonton_dates'){
                edmontonCart[0]++
             }else if(parentUl ==  'id_winnipeg_dates'){
                winnipegCart[0]++
             }
            //The other side of our statement is to remove items from the cart as the user unchecks them if they want to edit their purchase.
        }else if(!input.checked){
        //find the input id witch will match the id that we added to the LI cart item. remove it from the UL and go check its parent UL and if out what cart it belongs to and substract it from the cart.
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

//forEach loop that adds the functionality for booth options. Similar logic as the dates with the main difference is we are capturing the inputs 'value' attribute and assigning the value of that to our booth value. Then we find the right cart and update it. Also I had to add a check that will remove other booths form the cart Ul that the users sees unlike our dates where you can select multiple, they can only have one booth option.
allBoothOptionsRadios.forEach((input) =>{
    input.addEventListener('click', ()=>{
        parentUl = input.parentElement.parentElement.parentElement.id
        cartItem = document.createElement('li')
        cartItemText = input.parentElement.innerText
        cartItem.innerText = cartItemText
        boothValue = parseInt(input.getAttribute('value'))
        //double up if statements for every input check to what booth option was click and if the cartItem exists in the cart go remove it so we can add a new one and show to the user that their selection change is reflected in the cart.
        if(input.checked){
           if(parentUl == 'id_toronto_booth_options'){
              if(document.getElementById('torontoSingleCartItem')){
                 document.getElementById('torontoSingleCartItem').remove()
              }
              cartItem.id = 'torontoSingleCartItem'
              shoppingCart.append(cartItem)
              torontoCart[1] = boothValue
              amountSpent = calculateTotal('toronto', torontoCart)
              torontoCart[2] = parseInt(document.getElementById('id_toronto_additional_booth_option').value) * 995
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

            totalBreakfastCostEdmonton = parseInt(document.getElementById('id_edmonton_additional_breakfast_option').value) * 23
            totalLunchCostEdmonton = parseInt(document.getElementById('id_edmonton_additional_lunch_option').value) * 29
            edmontonCart[3] = totalBreakfastCostEdmonton + totalLunchCostEdmonton
            totalLunchCostCostCalgary = parseInt(document.getElementById('id_calgary_additional_lunch_option').value) * 29
            calgaryCart[3] = totalLunchCostCostCalgary
            totalWinnipegLunchCost = parseInt(document.getElementById('id_winnipeg_additional_lunch_option').value) * 25
            winnipegCart[3] = totalWinnipegLunchCost
            return parseInt(cartName[0] * cartName[1]) + (cartName[0] * cartName[2]) + cartName[3]
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


