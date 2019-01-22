//shoppingCart = document.getElementById('shoppingCart')

//first value is dates selected, next is booth option value, next is number of extra booths, finally is additional options total if their is additional options at the venue. Extra booths are under this on the front but for the cost calculation they serve a different purpose.
torontoCart = [0, 0, 0, 0]

winnipegCart = [0, 0, 0, 0]

calgaryCart = [0, 0, 0, 0]

edmontonCart = [0, 0, 0, 0]


//query selectors that create arrays of relevent input elements for each section of the form. These are used later in the code with forEach loops to add custom behaviour depending on which form is being filled.
allDatesCheckboxes = document.querySelectorAll('input.dates-select')
allBoothOptionsRadios = document.querySelectorAll('input.booth-options-select')
allAdditionalOptions = document.querySelectorAll('input.fair-options')
if(document.getElementById('discountCheckbox')){
    document.getElementById('discountCheckbox').checked = true
}
function createOptions(elem){
    for(i = 0; i <= 5; i++){
        createOption = document.createElement('option')
        createOption.innerText = i
        createOption.value = i
        elem.append(createOption)
    }
}

function findAndDeleteDate(relatedElement, elemToDelete){
    if(relatedElement.checked === false){
        if(elemToDelete){
            elemToDelete.remove()
        }
    }
}

function dateCheck(input){
  //parent elements will contain our ID for making sure we are editing the appropriate Cart.
  parentUl = input.parentElement.parentElement.parentElement.id
  console.log('yes')
  if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
             cartItem.innerText = cartText
             shoppingCart.append(cartItem)
             additionalBoothOption = document.createElement('select')
             additionalLunchOption = document.createElement('select')
             additionalBreakfastOption = document.createElement('select')
             dietRequest = document.createElement('input')
             dietRequest.setAttribute('type', 'text')
             dietRequestLabel = document.createElement('label')
             dietRequestLabel.innerText = 'Diet Request: '
             breakfastLabel = document.createElement('label')
             breakfastLabel.innerText = ' Extra Breakfast: '
             lunchLabel = document.createElement('label')
             lunchLabel.innerText = ' Extra Lunch: '
             selectLabel = document.createElement('label')
             selectLabel.innerText = ' Extra Booth: '
             //our conditional checks to update our cart with a date selection.
             if(parentUl == 'id_toronto_dates'){
                additionalBoothOption.setAttribute('name', 'additional_booth_option_toronto_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_toronto_' + cartText
                createOptions(additionalBoothOption)
                selectLabel.append(additionalBoothOption)
                input.parentElement.append(document.createElement('br'), selectLabel)
                cartItem.innerHTML += '<br>' + selectLabel.innerText + ' ' + `<span id='extraBoothValue_${cartText}'>` + additionalBoothOption.value + '</span>'
                cartItem.innerHTML += `<h5>Toronto Career Fair <br>${cartText}</h5>`
                torontoCart[0]++
             }else if(parentUl == 'id_calgary_dates'){
                additionalBoothOption.setAttribute('name', 'additional_booth_option_calgary_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_calgary_' + cartText
                createOptions(additionalBoothOption)
                additionalLunchOption.setAttribute('name', 'additional_lunch_option_calgary_'+cartText)
                additionalLunchOption.id ='additional_lunch_option_calgary_'+cartText
                createOptions(additionalLunchOption)
                selectLabel.append(additionalBoothOption)
                lunchLabel.append(additionalLunchOption)
                dietRequestLabel.append(dietRequest)
                dietRequest.setAttribute('name', 'diet_request_for_calgary_'+cartText)
                input.parentElement.append(document.createElement('br'), selectLabel, document.createElement('br'), lunchLabel, document.createElement('br'), dietRequestLabel)
                cartItem.innerHTML += `<br>${selectLabel.innerText} <span id='extraBoothValue_${cartText}'>${additionalBoothOption.value}</span><br>${lunchLabel.innerText}<span id='extraLunchValue_${cartText}'>${additionalLunchOption.value}</span><br>`
                cartItem.innerHTML += `<h5>Calgary Career Fair <br>${cartText}</h5>`
                calgaryCart[0]++
             }else if(parentUl == 'id_edmonton_dates'){
                additionalBoothOption.setAttribute('name', 'additional_booth_option_edmonton_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_edmonton_' + cartText
                createOptions(additionalBoothOption)
                additionalLunchOption.setAttribute('name', 'additional_lunch_option_edmonton_'+cartText)
                additionalLunchOption.id ='additional_lunch_option_edmonton_'+cartText
                createOptions(additionalLunchOption)
                additionalBreakfastOption.setAttribute('name', 'additional_breakfast_option_edmonton_'+cartText)
                additionalBreakfastOption.id ='additional_breakfast_option_edmonton_'+cartText
                createOptions(additionalBreakfastOption)
                selectLabel.append(additionalBoothOption)
                lunchLabel.append(additionalLunchOption)
                breakfastLabel.append(additionalBreakfastOption)
                dietRequestLabel.append(dietRequest)
                dietRequest.setAttribute('name', 'diet_request_for_edmonton_'+cartText)
                input.parentElement.append(document.createElement('br'), selectLabel, document.createElement('br'), lunchLabel, document.createElement('br'), breakfastLabel, document.createElement('br'), dietRequestLabel)
                cartItem.innerHTML += `<br>${selectLabel.innerText} <span id='extraBoothValue_${cartText}'>${additionalBoothOption.value}</span><br>${lunchLabel.innerText}<span id='extraLunchValue_${cartText}'>${additionalLunchOption.value}</span><br>${breakfastLabel.innerText}<span id='extraBreakfastValue_${cartText}'>${additionalBreakfastOption.value}</span>`
                cartItem.innerHTML += `<h5>Edmonton Career Fair <br>${cartText}</h5>`
                edmontonCart[0]++
            }else if(parentUl ==  'id_winnipeg_dates'){
                additionalBoothOption.setAttribute('name', 'additional_booth_option_winnipeg_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_winnipeg_' + cartText
                createOptions(additionalBoothOption)
                additionalLunchOption.setAttribute('name', 'additional_lunch_option_winnipeg_'+cartText)
                additionalLunchOption.id ='additional_lunch_option_winnipeg_'+cartText
                createOptions(additionalLunchOption)
                selectLabel.append(additionalBoothOption)
                lunchLabel.append(additionalLunchOption)
                dietRequestLabel.append(dietRequest)
                dietRequest.setAttribute('name', 'diet_request_for_winnipeg_'+cartText)
                input.parentElement.append(document.createElement('br'), selectLabel, document.createElement('br'), lunchLabel, document.createElement('br'), dietRequestLabel)
                cartItem.innerHTML += `<br>${selectLabel.innerText} <span id='extraBoothValue_${cartText}'>${additionalBoothOption.value}</span><br>${lunchLabel.innerText}<span id='extraLunchValue_${cartText}'>${additionalLunchOption.value}</span><br>`
                cartItem.innerHTML += `<h5>Winnipeg Career Fair <br>${cartText}</h5>`
                winnipegCart[0]++
             }
            //The other side of our statement is to remove items from the cart as the user unchecks them if they want to edit their purchase.
        }else if(!input.checked){
            findAndDeleteDate(document.getElementById('id_toronto_dates_0'), document.getElementById('April 24th, 2018'))
            findAndDeleteDate(document.getElementById('id_toronto_dates_1'), document.getElementById('September 17th, 2019'))
            findAndDeleteDate(document.getElementById('id_winnipeg_dates_0'), document.getElementById('April 2nd, 2019'))
            findAndDeleteDate(document.getElementById('id_winnipeg_dates_1'), document.getElementById('July 10th, 2019'))
            findAndDeleteDate(document.getElementById('id_winnipeg_dates_2'), document.getElementById('July 23rd, 2019'))
            findAndDeleteDate(document.getElementById('id_calgary_dates_0'), document.getElementById('March 12th, 2019'))
            findAndDeleteDate(document.getElementById('id_calgary_dates_1'), document.getElementById('June 26th, 2019'))
            findAndDeleteDate(document.getElementById('id_calgary_dates_2'), document.getElementById('October 22nd, 2019'))
            findAndDeleteDate(document.getElementById('id_edmonton_dates_0'), document.getElementById('January 29th, 2019'))
            findAndDeleteDate(document.getElementById('id_edmonton_dates_1'), document.getElementById('May 28th, 2019'))
            findAndDeleteDate(document.getElementById('id_edmonton_dates_2'), document.getElementById('August 13th, 2019'))
            findAndDeleteDate(document.getElementById('id_edmonton_dates_3'), document.getElementById('November 19th, 2019'))
        }
}


//Keeps track of selected dates and add event listeners for click events and run our conditionals to make sure the proper card receives the relevant selection.
allDatesCheckboxes.forEach((input)=>{
    input.addEventListener('click', ()=>{
        dateCheck(input)
        if(!input.checked){
            console.log(input)
            if(!input.checked && input.nextElementSibling){
                while(input.nextElementSibling){
                    input.nextElementSibling.remove()
                }
            }
        //find the input id witch will match the id that we added to the LI cart item. remove it from the UL and go check its parent UL and find out what cart it belongs to and substract it from the cart value at its index.
            if(document.getElementById('shoppingCart').childNodes.length > 9){
                    findInputId = input.parentElement.innerText
                if(document.getElementById(findInputId)){
                    document.getElementById(findInputId).remove()
                }
            }
            if(parentUl == 'id_toronto_dates'){
                torontoCart[0]--
            }if(parentUl == 'id_calgary_dates'){
                calgaryCart[0]--
            }if(parentUl == 'id_edmonton_dates'){
             edmontonCart[0]--
            }if(parentUl ==  'id_winnipeg_dates'){
             winnipegCart[0]--
             }
        }
    })
   for(i = document.getElementById('shoppingCart').childNodes.length; i >= 9; i--){
       if(document.getElementById('shoppingCart').childNodes.length > 9){
           document.getElementById('shoppingCart').childNodes[i].remove()
       }
   }
    dateCheck(input)
})
function boothOptionCheck(input){
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
              amountSpent = calculateTotal(torontoCart)
           }
           if(parentUl == 'id_calgary_booth_options'){
              if(document.getElementById('calgarySingleCartItem')){
                 document.getElementById('calgarySingleCartItem').remove()
              }
              cartItem.id = 'calgarySingleCartItem'
              shoppingCart.append(cartItem)
              calgaryCart[1] = boothValue
              amountSpent = calculateTotal(calgaryCart)
           }
           if(parentUl == 'id_edmonton_booth_options'){
              if(document.getElementById('edmontonSingleCartItem')){
                 document.getElementById('edmontonSingleCartItem').remove()
              }
              cartItem.id = 'edmontonSingleCartItem'
              shoppingCart.append(cartItem)
              edmontonCart[1] = boothValue
              amountSpent = calculateTotal(edmontonCart)
           }
           if(parentUl == 'id_winnipeg_booth_options'){
              if(document.getElementById('winnipegSingleCartItem')){
                 document.getElementById('winnipegSingleCartItem').remove()
              }
              cartItem.id = 'winnipegSingleCartItem'
              shoppingCart.append(cartItem)
              winnipegCart[1] = boothValue
              amountSpent = calculateTotal(winnipegCart)
           }
    }
}

//forEach loop that adds the functionality for booth options. Similar logic as the dates with the main difference is we are capturing the inputs 'value' attribute and assigning the value of that to our booth value. Then we find the right cart and update it. Also I had to add a check that will remove other booths form the cart Ul that the users sees unlike our dates where you can select multiple, they can only have one booth option.

allBoothOptionsRadios.forEach((input) =>{
    input.addEventListener('click', ()=>{
        boothOptionCheck(input)
    })
    boothOptionCheck(input)
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

function additionalCartItems(cityName, fairDate, cart){
    //check for the existence of additional booths. If they do calculate the value and add it to our cart.
    if(document.getElementById(`additional_booth_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`extraBoothValue_${fairDate}`)){
            document.getElementById(`extraBoothValue_${fairDate}`).innerText = document.getElementById(`additional_booth_option_${cityName}_${fairDate}`).value
        }
        additionalBooths = parseInt(document.getElementById(`additional_booth_option_${cityName}_${fairDate}`).value) * 995
        cart[3] += additionalBooths
    }
    //check for additional lunches
    if(document.getElementById(`additional_lunch_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`extraLunchValue_${fairDate}`)){
            document.getElementById(`extraLunchValue_${fairDate}`).innerText = document.getElementById(`additional_lunch_option_${cityName}_${fairDate}`).value
        }
        additionalLunchOption = parseInt(document.getElementById(`additional_lunch_option_${cityName}_${fairDate}`).value) * 25
        cart[3] += additionalLunchOption
    }
    //check for additional breakfast
    if(document.getElementById(`additional_breakfast_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`extraBreakfastValue_${fairDate}`)){
            document.getElementById(`extraBreakfastValue_${fairDate}`).innerText = document.getElementById(`additional_breakfast_option_${cityName}_${fairDate}`).value
        }
        additionalBreakfastOption = parseInt(document.getElementById(`additional_breakfast_option_${cityName}_${fairDate}`).value) * 23
        cart[3] += additionalBreakfastOption
    }

}

function calculateTotal(cartName){
    return parseInt(cartName[0] * cartName[1]) + (cartName[0] * cartName[2]) + cartName[3]
}

function applyDiscount(grandTotal, typeOfDiscount){
    discountAmount = document.getElementById('id_discount_amount').value
    parseInt(discountAmount)
    if(typeOfDiscount.checked){
        document.getElementById('discountType').innerText = '%'
        document.getElementById('discountPercentHiddenInput').value = `%${discountAmount}`
        decimalNum = '.' + discountAmount
        parseFloat(decimalNum)
        takeAway = grandTotal * decimalNum
    }else{
        document.getElementById('discountType').innerText = '$'
        document.getElementById('discountHiddenInput').value = '$'
        takeAway = discountAmount
    }
    return takeAway
}

function calculateGrandTotal(){
       torontoCart[3] = 0
       winnipegCart[3] = 0
       edmontonCart[3] = 0
       calgaryCart[3] = 0
       additionalCartItems('toronto', 'April 24th, 2018', torontoCart)
       additionalCartItems('toronto', 'September 17th, 2019', torontoCart)
       additionalCartItems('winnipeg', 'July 10th, 2019', winnipegCart)
       additionalCartItems('winnipeg', 'April 2nd, 2019', winnipegCart)
       additionalCartItems('winnipeg', 'July 23rd, 2019', winnipegCart)
       additionalCartItems('calgary', 'March 12th, 2019', calgaryCart)
       additionalCartItems('calgary', 'June 26th, 2019', calgaryCart)
       additionalCartItems('calgary', 'October 22nd, 2019', calgaryCart)
       additionalCartItems('edmonton', 'January 29th, 2019', edmontonCart)
       additionalCartItems('edmonton', 'May 28th, 2019', edmontonCart)
       additionalCartItems('edmonton', 'August 13th, 2019', edmontonCart)
       additionalCartItems('edmonton', 'November 19th, 2019', edmontonCart)
       value1 = calculateTotal(torontoCart)
       value2 = calculateTotal(winnipegCart)
       value3 = calculateTotal(calgaryCart)
       value4 = calculateTotal(edmontonCart)
       grandTotal = value1 + value2 + value3 + value4
       typeOfDiscount = document.getElementById('discountCheckbox')
       amountToDiscount = applyDiscount(grandTotal, typeOfDiscount)
       totalAfterDiscount = grandTotal - amountToDiscount
       console.log(grandTotal, amountToDiscount, totalAfterDiscount)
       typeOfTax = document.getElementById('id_province').value
       switch(typeOfTax) {
            case '-':
                typeOfTax = 0;
                break;
            case 'Ontario':
                typeOfTax = 0.13
                break;  
            case 'New Brunswick': 
                typeOfTax = 0.15
                break;
            case 'Newfoundland and Labrador':
                typeOfTax = 0.15
                break;
            case 'Nova Scotia':
                typeOfTax = 0.15
                break;
            case 'Prince Edward Island':
                typeOfTax = 0.15
                break;
            case 'Alberta':
                typeOfTax = 0.05;
                break;    
            case 'British Columbia':
                typeOfTax = 0.05;
                break;
            case 'Manitoba':
                typeOfTax = 0.05;
                break;
            case 'Quebec':
                typeOfTax = 0.05;
                break;
            case 'Saskatchewan':
                typeOfTax = 0.05;
                break;
            case 'Northwest Territories':
                typeOfTax = 0.05;
                break;
            case 'Nunavut':
                typeOfTax = 0.05;
                break;
            case 'Yukon':
                typeOfTax = 0.05;
                break;
       }
       console.log(typeOfTax)
       parseInt(typeOfTax, totalAfterDiscount)
       taxToCharge = typeOfTax * totalAfterDiscount
       console.log(taxToCharge)
       document.getElementById('priceValue').innerText = grandTotal
       document.getElementById('discountValue').innerText = amountToDiscount
       document.getElementById('discountHiddenInput').value = `$${amountToDiscount}`
       document.getElementById('taxValue').innerText = parseFloat(taxToCharge).toFixed(2) 
       overallTotalWithTax = totalAfterDiscount + taxToCharge
       document.getElementById('totalValue').innerText = parseFloat(overallTotalWithTax).toFixed(2)
    // document.getElementById('cart-total').innerText = overallTotalWithTax
       document.getElementById('priceInput').value = overallTotalWithTax
       return overallTotalWithTax
}

cartTotal = document.getElementById('cart-total')
setInterval(calculateGrandTotal, 100)