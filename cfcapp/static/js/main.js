checkboxes = document.querySelectorAll('input[name="select_cities"]')
optionsContainer = document.getElementById('fair_dates_and_options_container')

fairContainers = document.querySelectorAll('.fair-options-container')
console.log(fairContainers)

function parsePositioning(elem){
    if(elem.style.top == '' || null){
        return 0
    }
    numtoParse = elem.style.top
    num = parseInt(numtoParse.substring(0, numtoParse.indexOf('p')))
    return num
}



checkboxes.forEach((elem) =>{
    console.log(elem.checked)
    elem.addEventListener('click', ()=>{
        targetElem = elem.parentNode.parentNode.childNodes[3]
        checked_box_id = elem.getAttribute('id')
        clicked_box_id = document.getElementById(checked_box_id)
        checked_box_name = elem.getAttribute('value')
            if(checked_box_name === 'Toronto' && clicked_box_id.checked){
                torontoContainer = document.getElementById('TorontoFairOptionsContainer')
                torontoContainer.style.display = 'flex'
                torontoContainer.style.top = 0 + 'px'
            }else if(checked_box_name === 'Toronto' && clicked_box_id.checked == false){
                torontoContainer.style.display = 'none'
                torontoContainer.style.top = 0 + 'px'
                torontoOptions = document.querySelectorAll("input[name='toronto_booth_options']")
                torontoDates = document.querySelectorAll("input[name='toronto_dates']")
                torontoDates.forEach((input)=>{
                    input.checked = false
                })
                torontoOptions.forEach((input)=>{

                    input.checked = false
                })
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked){
                calgaryContainer = document.getElementById('CalgaryFairOptionsContainer')
                calgaryContainer.style.display = 'block'
                calgaryContainer.style.top = 0 + 'px'
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked == false){
                calgaryContainer.style.display = 'none'
                calgaryContainer.style.top = 0 + 'px'
                calgaryOptions = document.querySelectorAll("input[name='calgary_booth_options']")
                calgaryDates = document.querySelectorAll("input[name='calgary_dates']")
                calgaryDates.forEach((input)=>{
                    input.checked = false
                })
                calgaryOptions.forEach((input)=>{

                    input.checked = false
                })
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked){
                edmontonContainer = document.getElementById('EdmontonFairOptionsContainer')
                edmontonContainer.style.display = 'block'
                edmontonContainer.style.top = 0 + 'px'
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked  == false){
                edmontonContainer.style.display = 'none'
                edmontonContainer.style.top = 0 + 'px'
                edmontonOptions = document.querySelectorAll("input[name='edmonton_booth_options']")
                edmontonDates = document.querySelectorAll("input[name='edmonton_dates']")
                edmontonDates.forEach((input)=>{
                    input.checked = false
                })
                edmontonOptions.forEach((input)=>{
                    input.checked = false
                })
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked){
                winnipegContainer = document.getElementById('WinnipegFairOptionsContainer')
                winnipegContainer.style.display = 'block'
                winnipegContainer.style.top = 0 + 'px'
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked  == false){
                winnipegContainer.style.display = 'none'
                winnipegContainer.style.top = 0 + 'px'

                winnipegOptions = document.querySelectorAll("input[name='winnipeg_booth_options']")
                winnipegDates = document.querySelectorAll("input[name='winnipeg_dates']")
                winnipegDates.forEach((input)=>{
                    input.checked = false
                })
                winnipegOptions.forEach((input)=>{
                    input.checked = false
                })
        }
        currentHeight = 0
        changedHeight = 0
        topPositioning = 0
        numOfCheckedBoxes = 0
        firstSpotTaken = false;
        secondSpotTaken = false;
        thirdSpotTaken = false;
        checkboxes.forEach((checkbox)=>{
            if(checkbox.checked){
               numOfCheckedBoxes++
            }
        })
        fairContainers.forEach((elem)=>{
          theNum = parsePositioning(elem)
          console.log(elem.style.height)
          console.log(theNum)
             if(theNum === 50){
                firstSpotTaken = true
             }else if(theNum === 475){
                secondSpotTaken = true
            }else if(theNum === 830){
                thirdSpotTaken = true
            }
         })

        if(elem.checked == false){
            if(numOfCheckedBoxes == 1){
                 fairContainers.forEach((elem)=>{
                    if(parsePositioning(elem) > 50){
                       elem.style.top = 50 + 'px'
                    }
                })
            }
            else if(numOfCheckedBoxes == 2){
                fairContainers.forEach((elem) =>{
                   theNum = parsePositioning(elem)
                   console.log(theNum)
                   if(firstSpotTaken == true && secondSpotTaken == true){
                      return
                   }else if(firstSpotTaken == false && secondSpotTaken == true && theNum != 475 && theNum != 0){
                        elem.style.top = 50 + 'px'
                   }else if(firstSpotTaken == true && secondSpotTaken == false && theNum != 50 && theNum != 0){
                        elem.style.top = 475 + 'px'
                   }
                })
            }
            else if(numOfCheckedBoxes >= 3){
                   fairContainers.forEach((elem)=>{
                        theNum = parsePositioning(elem)
                        console.log(theNum)
                        if(firstSpotTaken == true && secondSpotTaken == true && thirdSpotTaken == true){
                            return
                        }else if(firstSpotTaken == true && secondSpotTaken == true && thirdSpotTaken == false){
                            if(theNum == 1250){
                                elem.style.top = 830 + 'px'
                            }
                        }else if(firstSpotTaken == true && secondSpotTaken == false && thirdSpotTaken == true){
                            if(theNum == 1250){
                                elem.style.top = 475 + 'px'
                            }
                        }else if(firstSpotTaken == false && secondSpotTaken == true && thirdSpotTaken == true){
                            if(theNum == 1250){
                                elem.style.top = 50 + 'px'
                            }
                        }
                })
            }
            value = targetElem.style.top
            theTakeAway = parseInt(value.substring(0, value.indexOf('p'))) - 300
        }else{
            fairContainers.forEach((elem) =>{
                console.log(elem.style.height)
                topHeight = elem.style.top
                if(topHeight.length > 0){
                    value = parseInt(topHeight.substring(0, topHeight.indexOf('p')))
                }else{
                    value = 0
                }
                topPositioning += value
                currentHeight +=  elem.offsetHeight
        })
        console.log(currentHeight)
           if(currentHeight == 340){
                currentHeight = 50
           }else if(currentHeight == 680){
               currentHeight = 475
           }else if(currentHeight == 1020){
                currentHeight = 830
           }else if(currentHeight == 1360){
                currentHeight = 1250
           }
            targetElem.style.top = currentHeight + 'px'
        }
    })
})