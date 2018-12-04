checkboxes = document.querySelectorAll('input[name="select_cities"]')
optionsContainer = document.getElementById('fair_dates_and_options_container')
checkboxes.forEach(function (elem){
    elem.addEventListener('click', ()=>{
        checked_box_id = elem.getAttribute('id')
        console.log(elem, checked_box_id)
        clicked_box_id = document.getElementById(checked_box_id)
        console.log(clicked_box_id)
        checked_box_name = elem.getAttribute('value')
            if(checked_box_name === 'Toronto' && clicked_box_id.checked){
                heading = document.createElement('h2')
                console.log('Toronto Box is Clicked!')
                heading.id = 'TorontoFairDatesHeading'
                heading.innerHTML = 'Toronto Fair Dates'
                optionsContainer.append(heading)

            }else if(checked_box_name === 'Toronto' && clicked_box_id.checked == false){
                document.getElementById('TorontoFairDatesHeading').remove()
            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked){
                console.log('Calgary Box')
                heading = document.createElement('h2')
                heading.id = 'CalgaryFairDatesHeading'
                heading.innerHTML = 'Calgary Fair Dates'
                optionsContainer.append(heading)

            }else if(checked_box_name === 'Calgary' && clicked_box_id.checked == false){
                document.getElementById('CalgaryFairDatesHeading').remove()
            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked){
                console.log('Edmonton Box')
                heading = document.createElement('h2')
                heading.id = 'EdmontonFairDatesHeading'
                heading.innerHTML = 'Edmonton Fair Dates'
                optionsContainer.append(heading)

            }else if(checked_box_name === 'Edmonton' && clicked_box_id.checked  == false){
                 document.getElementById('EdmontonFairDatesHeading').remove()
            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked){
                console.log('Winnipeg Box')
                heading = document.createElement('h2')
                heading.id = 'WinnipegFairDatesHeading'
                heading.innerHTML = 'Winnipeg Fair Dates'
                optionsContainer.append(heading)

            }else if(checked_box_name === 'Winnipeg' && clicked_box_id.checked  == false){
                document.getElementById('WinnipegFairDatesHeading').remove()

            }






    })
})
