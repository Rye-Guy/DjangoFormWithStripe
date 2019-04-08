//shoppingCart = document.getElementById('shoppingCart')

//first value is dates selected, next is booth option value, next is number of extra booths, finally is additional options total if their is additional options at the venue. Extra booths are under this on the front but for the cost calculation they serve a different purpose.
torontoCart = [0, 0, 0, 0]
winnipegCart = [0, 0, 0, 0]
calgaryCart = [0, 0, 0, 0]
edmontonCart = [0, 0, 0, 0]


//query selectors that create arrays of relevent input elements for each section of the form. These are used later in the code with forEach loops to add custom behaviour depending on which form is being filled.
allDatesCheckboxes = document.querySelectorAll('input.dates-select')
allBoothOptionsRadios = document.querySelectorAll('.booth-options-select')
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

function createAdditionalBoothOptions(elem){
    for(i = 0; i<= 4; i++){
        switch(i){
            case 0:
                createOption = document.createElement('option')
                createOption.innerText = 'Bronze'
                createOption.value = 1495
                elem.append(createOption)
                break
            case 1:
                createOption = document.createElement('option')
                createOption.innerText = 'Silver'
                createOption.value = 1995
                elem.append(createOption)
                break
            case 2:
                createOption = document.createElement('option')
                createOption.innerText = 'Gold'
                createOption.value = 2495
                elem.append(createOption)
                break
           case 3:
                createOption = document.createElement('option')
                createOption.innerText = 'Platinum'
                createOption.value = 2995
                elem.append(createOption)
                break

         }
    }
}

function findAndDeleteDate(relatedElement, elemToDelete){
    if(relatedElement.checked === false){

        if(elemToDelete){

            elemToDelete.remove()
        }
    }
}

function fixBugWithFairsThatWontDelete(fairInput, cartItem) {
    console.log(fairInput.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.childNodes[0])
    if(fairInput.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.childNodes[1].childNodes[0].checked == false){
        fairInput.remove()
        if(cartItem){
            cartItem.remove()
        }
    }
}

function dateCheck(input){
  //parent elements will contain our ID for making sure we are editing the appropriate Cart.
  parentUl = input.parentElement.parentElement.parentElement.id

  if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
            shoppingCart.append(cartItem)
             boothOptionSelect = document.createElement('select')
             boothOptionLabel = document.createElement('label')
             boothOptionLabel.innerText = 'Booth Options:'
             additionalBoothOption = document.createElement('select')
             additionalLunchOption = document.createElement('select')
             additionalBreakfastOption = document.createElement('select')
             wifiPerDeviceOption = document.createElement('select')

             lunchLabel = document.createElement('label')
             lunchLabel.innerText = ' Extra Lunch: '
             selectLabel = document.createElement('label')
             selectLabel.innerText = ' Extra Booth: '
             wifiLabel = document.createElement('label')
             wifiLabel.innerText = ' Wifi Per Device: '

             //to fix bug we are going to put generate elements in a div we can easily remove instead of naviagting through the dom tree and delete specifc nodes related to a parent
            deleteMeDiv = document.createElement('div')
            deleteMeDiv.className = 'deleteMe'

             //our conditional checks to update our cart with a date selection.
             if(parentUl == 'id_toronto_dates'){
                //Booth type select
                boothOptionSelect.setAttribute('name', 'booth_option_toronto_'+cartText)
                boothOptionSelect.id = 'booth_option_toronto_'+cartText
                //create options and append select w/ options to label
                createAdditionalBoothOptions(boothOptionSelect)
                boothOptionLabel.append(boothOptionSelect)
                //additional booth option select
                additionalBoothOption.setAttribute('name', 'additional_booth_option_toronto_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_toronto_' + cartText
                //create options and append select w/ options to label
                createOptions(additionalBoothOption)
                selectLabel.append(additionalBoothOption)
                 deleteMeDiv.append(document.createElement('br'), selectLabel, boothOptionLabel)
                 //now create the cart item to display to the user and append all inputs controlling cart options to the date input parent(<LABEL>)
                input.parentElement.append(deleteMeDiv)
                 if(window.createTextArea){
                     deleteMeDiv.append(createTextArea(cartText, 'toronto'))
                 }
                cartItem.innerHTML += `<li class="cartItemHeading">${cartText}</li>Booth Option: <span id="boothOption_${cartText}">${boothOptionSelect.value}</span><br>Extra Booth: <span id="extraBoothValue_${cartText}">${additionalBoothOption.value}</span><br><h5>Toronto Fair Breakdown for ${cartText}</h5>`
                torontoCart[0]++
             }else if(parentUl == 'id_calgary_dates'){
                //create electricity option and maybe a better way to insert html instead of my usual modus operandi.
                 let venueOpts = document.createElement('div')
                 venueOpts.id = 'venueOptions'
                 venueOpts.innerHTML += `<p><label><input name='electricity_option_calgary_${cartText}' id='electricity_option_calgary_${cartText}' type=checkbox /><span>Electricity</span></label></p>`

                //Booth type select
                boothOptionSelect.setAttribute('name', 'booth_option_calgary_'+cartText)
                boothOptionSelect.id = 'booth_option_calgary_'+cartText
                //create options and append select w/ options to label
                createAdditionalBoothOptions(boothOptionSelect)
                boothOptionLabel.append(boothOptionSelect)
                //additional booth option select
                additionalBoothOption.setAttribute('name', 'additional_booth_option_calgary_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_calgary_' + cartText
                //create options and append select w/ options to label
                createOptions(additionalBoothOption)
                selectLabel.append(additionalBoothOption)
                //create lunch options select
                additionalLunchOption.setAttribute('name', 'additional_lunch_option_calgary_'+cartText)
                additionalLunchOption.id ='additional_lunch_option_calgary_'+cartText
                //Harrison has decided 3 months in WIFI is no longer boolean and now needs to be a select with a list of options... what a guy.
                createOptions(wifiPerDeviceOption)
                wifiLabel.append(wifiPerDeviceOption)
                wifiPerDeviceOption.setAttribute('name', 'wifi_per_device_for_calgary_'+cartText)
                wifiPerDeviceOption.id = 'wifi_per_device_for_calgary_'+cartText

                //create options and append select w/ options to label
                createOptions(additionalLunchOption)
                lunchLabel.append(additionalLunchOption)

                //now create the cart item to display to the user and append all inputs controlling cart options to the date input parent(<LABEL>)
                 input.parentElement.append(document.createElement('br'), boothOptionLabel, document.createElement('br'), selectLabel, document.createElement('br'), lunchLabel, document.createElement('br'), wifiLabel, document.createElement('br'), document.createElement('br'),  venueOpts, document.createElement('br'))
                 if(window.createTextArea){
                     input.parentElement.append(createTextArea(cartText, 'calgary'))
                 }
                 cartItem.innerHTML += `<li class="cartItemHeading">${cartText}</li>Booth Option: <span id="boothOption_${cartText}">${boothOptionSelect.value}</span><br>Extra Booth: <span id="extraBoothValue_${cartText}">${additionalBoothOption.value}</span><br>Extra Lunch: <span id="extraLunchValue_${cartText}">${additionalLunchOption.value}</span><h5>Calgary Fair Breakdown for ${cartText}</h5>`
                calgaryCart[0]++
             }else if(parentUl == 'id_edmonton_dates'){
                 //Create Venue Options
                 let venueOpts = document.createElement('div')
                 venueOpts.id = 'venueOptions'
                 venueOpts.innerHTML += `<p><label><input name='electricity_option_edmonton_${cartText}' id='electricity_option_edmonton_${cartText}' type=checkbox /><span>Electricity</span></label></p>`
                //Booth type select
                //Booth type select
                boothOptionSelect.setAttribute('name', 'booth_option_edmonton_'+cartText)
                boothOptionSelect.id = 'booth_option_edmonton_'+cartText
                //create options and append select w/ options to label
                createAdditionalBoothOptions(boothOptionSelect)
                boothOptionLabel.append(boothOptionSelect)
                //additional booth option select
                additionalBoothOption.setAttribute('name', 'additional_booth_option_edmonton_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_edmonton_' + cartText
                //create options and append select w/ options to label
                createOptions(additionalBoothOption)
                selectLabel.append(additionalBoothOption)
                //create lunch options select
                additionalLunchOption.setAttribute('name', 'additional_lunch_option_edmonton_'+cartText)
                additionalLunchOption.id ='additional_lunch_option_edmonton_'+cartText
                //create options and append select w/ options to label
                createOptions(additionalLunchOption)
                lunchLabel.append(additionalLunchOption)
                createOptions(wifiPerDeviceOption)
                wifiLabel.append(wifiPerDeviceOption)
                wifiPerDeviceOption.setAttribute('name', 'wifi_per_device_for_edmonton_'+cartText)
                wifiPerDeviceOption.id = 'wifi_per_device_for_edmonton_'+cartText


                //now create the rest of our cart item to display to the user and populated the date selection ul
                input.parentElement.append(document.createElement('br'), boothOptionLabel, document.createElement('br'), selectLabel, document.createElement('br'), lunchLabel, document.createElement('br'), wifiLabel, document.createElement('br'), venueOpts)
                 if(window.createTextArea){
                     input.parentElement.append(createTextArea(cartText, 'edmonton'))
                 }
                 cartItem.innerHTML += `<div><li class="cartItemHeading">${cartText}</li>Booth Option: <span id="boothOption_${cartText}">${boothOptionSelect.value}</span><br>Extra Booth: <span id="extraBoothValue_${cartText}">${additionalBoothOption.value}</span><br>Extra Lunch: <span id="extraLunchValue_${cartText}">${additionalLunchOption.value}</span><h5>Edmonton Fair Breakdown for ${cartText}</h5>`
                edmontonCart[0]++
            }else if(parentUl ==  'id_winnipeg_dates'){
                //Booth type select
                boothOptionSelect.setAttribute('name', 'booth_option_winnipeg_'+cartText)
                boothOptionSelect.id = 'booth_option_winnipeg_'+cartText
                //create options and append select w/ options to label
                createAdditionalBoothOptions(boothOptionSelect)
                boothOptionLabel.append(boothOptionSelect)
                //additional booth option select
                additionalBoothOption.setAttribute('name', 'additional_booth_option_winnipeg_'+cartText)
                additionalBoothOption.id = 'additional_booth_option_winnipeg_' + cartText
                //create options and append select w/ options to label
                createOptions(additionalBoothOption)
                selectLabel.append(additionalBoothOption)
                //create lunch options select
                additionalLunchOption.setAttribute('name', 'additional_lunch_option_winnipeg_'+cartText)
                additionalLunchOption.id ='additional_lunch_option_winnipeg_'+cartText
                //create options and append select w/ options to label
                createOptions(additionalLunchOption)
                lunchLabel.append(additionalLunchOption)
                //create Diet Request and set up attributes for capturing data out of form.
                //now create the rest of our cart item to display to the user and populated the date selection ul
                 input.parentElement.append(document.createElement('br'), boothOptionLabel, document.createElement('br'), selectLabel, document.createElement('br'), lunchLabel, document.createElement('br'))
                 if(window.createTextArea){
                     input.parentElement.append(createTextArea(cartText, 'winnipeg'))
                 }
                 cartItem.innerHTML += `<li class="cartItemHeading">${cartText}</li>Booth Option: <span id="boothOption_${cartText}">${boothOptionSelect.value}</span><br>Extra Booth: <span id="extraBoothValue_${cartText}">${additionalBoothOption.value}</span><br>Extra Lunch: <span id="extraLunchValue_${cartText}">${additionalLunchOption.value}</span><h5>Winnipeg Fair Breakdown for ${cartText}</h5>`
                winnipegCart[0]++
             }
            //The other side of our statement is to remove items from the cart as the user unchecks them if they want to edit their purchase.
        }else if(!input.checked){
            findAndDeleteDate(document.getElementById('id_toronto_dates_0'), document.getElementById('April 24th, 2019'))
            findAndDeleteDate(document.getElementById('id_toronto_dates_1'), document.getElementById('September 17th, 2019'))
            findAndDeleteDate(document.getElementById('id_winnipeg_dates_0'), document.getElementById('April 2nd, 2019'))
            findAndDeleteDate(document.getElementById('id_winnipeg_dates_1'), document.getElementById('July 23rd, 2019'))
            findAndDeleteDate(document.getElementById('id_calgary_dates_0'), document.getElementById('March 12th, 2019'))
            findAndDeleteDate(document.getElementById('id_calgary_dates_1'), document.getElementById('June 25th, 2019'))
            findAndDeleteDate(document.getElementById('id_calgary_dates_2'), document.getElementById('October 23nd, 2019'))
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
    singleFairCostObj = {
        city: cityName,
        fair_date: fairDate,
    }
    if(document.getElementById(`booth_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`boothOption_${fairDate}`)){
              document.getElementById(`boothOption_${fairDate}`).innerText = document.getElementById(`booth_option_${cityName}_${fairDate}`).value
        }
        boothOption = parseInt(document.getElementById(`booth_option_${cityName}_${fairDate}`).value)
        singleFairCostObj.booth_option = boothOption
        cart[1] += boothOption

    }
    //check for the existence of additional booths. If they do calculate the value and add it to our cart.
    if(document.getElementById(`additional_booth_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`extraBoothValue_${fairDate}`)){
            document.getElementById(`extraBoothValue_${fairDate}`).innerText = document.getElementById(`additional_booth_option_${cityName}_${fairDate}`).value
        }
        additionalBoothsAmount = parseInt(document.getElementById(`additional_booth_option_${cityName}_${fairDate}`).value)
        additionalCost = additionalBoothsAmount * 995
        singleFairCostObj.additional_booths = {
            number_of_booths: additionalBoothsAmount,
            cost_of_booths: additionalCost
        }
        cart[3] += additionalCost
    }
    //check for additional lunches
    if(document.getElementById(`additional_lunch_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`extraLunchValue_${fairDate}`)){
            document.getElementById(`extraLunchValue_${fairDate}`).innerText = document.getElementById(`additional_lunch_option_${cityName}_${fairDate}`).value
        }
        numOfadditionalLunchOption = parseInt(document.getElementById(`additional_lunch_option_${cityName}_${fairDate}`).value)
        costOfadditionalLunchOption = numOfadditionalLunchOption * 25
        singleFairCostObj.additional_lunch = {
            number_of_lunches: numOfadditionalLunchOption,
            cost_of_lunch: costOfadditionalLunchOption
        }
        cart[3] += costOfadditionalLunchOption
    }
    if(document.getElementById(`wifi_per_device_for_${cityName}_${fairDate}`)){
        var wifi_num = document.getElementById(`wifi_per_device_for_${cityName}_${fairDate}`).value
        costofadditional_wifi = wifi_num * 50;
        singleFairCostObj.wifi_devices = {
            number_of_wifi_devices: wifi_num,
            cost_of_wifi:  costofadditional_wifi
        }
        cart[3] +=  costofadditional_wifi;
    }
    //check for additional breakfast
    if(document.getElementById(`electricity_option_${cityName}_${fairDate}`)){
        if(document.getElementById(`electricity_option_${cityName}_${fairDate}`).checked){
            singleFairCostObj.electricity = true
            cart[3] += 129
        }
    }
        calculateIndividualFair(singleFairCostObj)
    return singleFairCostObj
}

function calculateIndividualFair(fairObj) {
    currentTotal = 0
    if(Object.keys(fairObj).length > 2) {
        baseBoothCost = fairObj.booth_option
        costOfAdditionalBooths = fairObj.additional_booths.cost_of_booths
        currentTotal = baseBoothCost + costOfAdditionalBooths
        if(fairObj.city != 'toronto'){
            costOfAdditionalLunches = fairObj.additional_lunch.cost_of_lunch
            currentTotal += costOfAdditionalLunches
            if(fairObj.city == 'calgary' || 'edmonton'){
                console.log('here')
                if(fairObj.electricity){
                    currentTotal += 129
                }
                if(fairObj.wifi_devices){
                console.log('Here')
                    currentTotal += fairObj.wifi_devices.cost_of_wifi;
                }
            }
        }
    }
    if(currentTotal > 0) {
        targetDiv = document.getElementById('inputsForIndividualFairCost')
        if(document.getElementById(`total_cost_for_${fairObj.city}_${fairObj.fair_date}`)){
            document.getElementById(`total_cost_for_${fairObj.city}_${fairObj.fair_date}`).value = currentTotal
        }
        else{
            targetDiv.innerHTML += `<input type='hidden' name='total_cost_for_${fairObj.city}_${fairObj.fair_date}' id='total_cost_for_${fairObj.city}_${fairObj.fair_date}'  value="$${currentTotal}">`
        }

    }
    return currentTotal

}

function calculateTotal(cartName){
    return parseInt(cartName[1] + (cartName[0] * cartName[2]) + cartName[3])
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
        discountType = document.getElementById('discountHiddenInput').value = `${discountAmount}`
        currentCartTotal = parseInt(document.getElementById('priceValue').innerText)
        percentageOff = (currentCartTotal - discountAmount) / currentCartTotal
        percentageOff - 1
        theTakeAwayPercent = (percentageOff / 1) - 1
        theTakeAwayPercent.toString()
        theTakeAwayPercentRep = parseFloat(Math.abs((theTakeAwayPercent))).toFixed(2)
        console.log(theTakeAwayPercentRep)
        document.getElementById('discountPercentHiddenInput').value = "%" +  String(theTakeAwayPercentRep.slice(2, 4))
        takeAway = discountType
    }
    return takeAway
}

function calculateGrandTotal(){
       torontoCart[1] = 0
       calgaryCart[1] = 0
       edmontonCart[1] = 0
       winnipegCart[1] = 0
       torontoCart[3] = 0
       winnipegCart[3] = 0
       edmontonCart[3] = 0
       calgaryCart[3] = 0
       additionalCartItems('toronto', 'April 24th, 2019', torontoCart)
       additionalCartItems('toronto', 'September 17th, 2019', torontoCart)
       additionalCartItems('winnipeg', 'April 2nd, 2019', winnipegCart)
       additionalCartItems('winnipeg', 'July 23rd, 2019', winnipegCart)
       additionalCartItems('calgary', 'March 12th, 2019', calgaryCart)
       additionalCartItems('calgary', 'June 25th, 2019', calgaryCart)
       additionalCartItems('calgary', 'October 23rd, 2019', calgaryCart)
       additionalCartItems('edmonton', 'January 29th, 2019', edmontonCart)
       additionalCartItems('edmonton', 'May 28th, 2019', edmontonCart)
       additionalCartItems('edmonton', 'August 13th, 2019', edmontonCart)
       additionalCartItems('edmonton', 'November 19th, 2019', edmontonCart)
       value1 = calculateTotal(torontoCart)
       value2 = calculateTotal(winnipegCart)
       value3 = calculateTotal(calgaryCart)
       value4 = calculateTotal(edmontonCart)
       subtotal = value1 + value2 + value3 + value4
       typeOfDiscount = document.getElementById('discountCheckbox')
       amountToDiscount = applyDiscount(subtotal, typeOfDiscount)
       totalAfterDiscount = subtotal - amountToDiscount
       let typeOfTax = document.getElementById('id_province').value
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
       parseInt(typeOfTax, totalAfterDiscount)
       let taxToCharge = typeOfTax * totalAfterDiscount
       document.getElementById('priceValue').innerText = subtotal
       document.getElementById('discountValue').innerText = parseFloat(amountToDiscount).toFixed(2)
       document.getElementById('discountHiddenInput').value = `$${amountToDiscount}`
       document.getElementById('taxValue').innerText = parseFloat(taxToCharge).toFixed(2)
       let overallTotalWithTax = totalAfterDiscount + taxToCharge
       document.getElementById('totalValue').innerText = parseFloat(overallTotalWithTax).toFixed(2)
    // document.getElementById('cart-total').innerText = overallTotalWithTax
       document.getElementById('priceInput').value = '$'+overallTotalWithTax
       document.getElementById('subtotalHiddenInput').value = subtotal
       return overallTotalWithTax
}

document.getElementById('applyNewBoothCost').addEventListener('click', function ApplyCustomBoothCost(ev){
    applyBtn = document.getElementById('applyNewBoothCost')
    ev.preventDefault()
    customBoothCost = document.getElementById('manuelBoothCost').value
    parseInt(customBoothCost)
    discountedCost = boothOption - parseInt(customBoothCost)
    somePercentOff = discountedCost / boothOption
    percentToApply = somePercentOff.toString().slice(2, somePercentOff.length)
    document.getElementById('id_discount_amount').value = percentToApply.slice(0, -13)
    console.log(customBoothCost, discountedCost, somePercentOff, percentToApply)
    console.log('clicked', applyBtn)
})


city_inputs = document.querySelectorAll('input[name="select_cities"]')

city_inputs.forEach((input)=>{
    input.addEventListener('click', (ev)=>{
        console.log()
        if(!input.checked){
            if(input.value == 'Toronto'){
                dateCheck(input)
                console.log('happening')
                console.log(document.querySelector('label[for="id_toronto_dates_0"]').childNodes)
                document.querySelector('label[for="id_toronto_dates_0"]').childNodes.forEach((node, i)=>{
                    console.log(node, i)
                    if(node.className == 'deleteMe')
                        node.remove()
                })
                //document.querySelector('label[for="id_toronto_dates_1"]').remove()

                //fixBugWithFairsThatWontDelete(document.querySelector('label[for="id_toronto_dates_0"]'), document.getElementById('April 24th, 2019'))
                //fixBugWithFairsThatWontDelete(document.getElementById('id_toronto_dates_1'), document.getElementById('September 17th, 2019'))
            }
        }
    })
})


cartTotal = document.getElementById('cart-total')
setInterval(calculateGrandTotal, 100)