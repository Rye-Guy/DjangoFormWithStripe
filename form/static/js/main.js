checkboxes = document.querySelectorAll('input[name="select_cities"]')
optionsContainer = document.getElementById('fair_dates_and_options_container')

checkboxes.forEach((elem) =>{
    fairOptionsDivs = elem.parentElement.parentElement.childNodes[13]

    elem.addEventListener('click', ()=>{
        checked_box_id = elem.getAttribute('id')
        clicked_box_id = document.getElementById(checked_box_id)
        checked_box_name = elem.getAttribute('value')
            if(checked_box_name === 'Toronto' && clicked_box_id.checked){
                torontoContainer = document.getElementById('TorontoFairOptionsContainer')
                torontoContainer.style = 'display: flex'
            }else if(checked_box_name === 'Toronto' && clicked_box_id.checked == false){
                torontoContainer.style = 'display: none'
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
                calgaryContainer.style = 'display: flex'
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked == false){
                calgaryContainer.style = 'display: none'
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
                edmontonContainer.style = 'display: flex'
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked  == false){
                edmontonContainer.style = 'display: none'
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
                winnipegContainer.style = 'display: flex'
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked  == false){
                winnipegContainer.style = 'display: none'
                winnipegOptions = document.querySelectorAll("input[name='winnipeg_booth_options']")
                winnipegDates = document.querySelectorAll("input[name='winnipeg_dates']")
                winnipegDates.forEach((input)=>{
                    input.checked = false
                })
                winnipegOptions.forEach((input)=>{

                    input.checked = false
                })
        }
    })
})
