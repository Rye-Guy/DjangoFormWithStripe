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
        currentHeight = 0
        changedHeight = 0
        topPositioning = 0
        numOfCheckedBoxes = 0
        checkboxes.forEach((checkbox)=>{
            if(checkbox.checked){
               numOfCheckedBoxes++
            }
         })
        if(elem.checked == false){
                console.log(numOfCheckedBoxes)
                if(numOfCheckedBoxes == 1){
                    console.log('hello')
                    fairContainers.forEach((elem)=>{
                        if(parsePositioning(elem) > 300){
                            elem.style.top = 300 + 'px'
                    }
                })
                }else if(numOfCheckedBoxes >= 2){
                   console.log('hello again')
                   fairContainers.forEach((elem)=>{
                        theNum = parsePositioning(elem)
                        console.log(theNum)
                        if(theNum == 300){
                            return
                        }else if(theNum == 600){
                            elem.style.top = 300 + 'px'
                        }else if(theNum == 900){
                            elem.style.top = 600 + 'px'
                        }else if(theNum == 1200){
                            elem.style.top = 900 + 'px'
                        }
                })
                }

            value = targetElem.style.top
            theTakeAway = parseInt(value.substring(0, value.indexOf('p'))) - 300
            console.log(theTakeAway)
        }else{
            fairContainers.forEach((elem) =>{
                topHeight = elem.style.top
                if(topHeight.length > 0){
                    value = parseInt(topHeight.substring(0, topHeight.indexOf('p')))
                }else{
                    value = 0
                }
                topPositioning += value
                currentHeight +=  elem.offsetHeight
            })
        }
        targetElem.style.top = currentHeight + 300 + 'px'

        checked_box_id = elem.getAttribute('id')
        clicked_box_id = document.getElementById(checked_box_id)
        checked_box_name = elem.getAttribute('value')
            if(checked_box_name === 'Toronto' && clicked_box_id.checked){
                torontoContainer = document.getElementById('TorontoFairOptionsContainer')
                torontoContainer.style.display = 'flex'
            }else if(checked_box_name === 'Toronto' && clicked_box_id.checked == false){
                torontoContainer.style.display = 'none'
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
                calgaryContainer.style.display = 'flex'
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked == false){
                calgaryContainer.style.display = 'none'
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
                edmontonContainer.style.display = 'flex'
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked  == false){
                edmontonContainer.style.display = 'none'
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
                winnipegContainer.style.display = 'flex'
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked  == false){
                winnipegContainer.style.display = 'none'
                winnipegOptions = document.querySelectorAll("input[name='winnipeg_booth_options']")
                winnipegDates = document.querySelectorAll("input[name='winnipeg_dates']")
                winnipegDates.forEach((input)=>{
                    input.checked = false
                })
                winnipegOptions.forEach((input)=>{
                    input.checked = false
                })
        }
      targetElem.style.top = currentHeight + 300 + 'px'
    })
})
