checkboxes = document.querySelectorAll('input[name="select_cities"]')
optionsContainer = document.getElementById('fair_dates_and_options_container')
checkboxes.forEach((elem) =>{
    elem.addEventListener('click', ()=>{
        checked_box_id = elem.getAttribute('id')
        clicked_box_id = document.getElementById(checked_box_id)
        checked_box_name = elem.getAttribute('value')
            if(checked_box_name === 'Toronto' && clicked_box_id.checked){
                torontoContainer = document.getElementById('TorontoFairOptionsContainer')
                torontoContainer.style = 'display: block'
            }else if(checked_box_name === 'Toronto' && clicked_box_id.checked == false){
                torontoContainer.style = 'display: none'
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked){
                calgaryContainer = document.getElementById('CalgaryFairOcptionsContainer')
                calgaryContainer.style = 'display: block'
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked == false){
                calgaryContainer.style = 'display: none'
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked){
                edmontonContainer = document.getElementById('EdmontonFairOptionsContainer')
                edmontonContainer.style = 'display: block'
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked  == false){
                 edmontonContainer.style = 'display: none'
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked){
                winnipegContainer = document.getElementById('WinnipegFairOptionsContainer')
                winnipegContainer.style = 'display: block'
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked  == false){
                winnipegContainer.style = 'display: none'
            }

    })
})
