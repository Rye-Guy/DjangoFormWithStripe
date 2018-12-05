console.log('Im in the shopping cart js file :D')
torontoDatesList = document.getElementById('id_toronto_dates')
console.log(torontoDatesList)

shoppingCart = document.getElementById('shoppingCart')

boothType = null
numberOfBooths = 0
selectedDates = 0
boothOptions = null


allDatesCheckboxes = document.querySelectorAll('input.dates-select')

allDatesCheckboxes.forEach((input) =>{
    input.addEventListener('click', ()=>{
        if(input.checked){
             cartText = input.parentElement.innerText
             cartItem = document.createElement('li')
             cartItem.id = cartText
             cartItem.innerText = cartText
             shoppingCart.append(cartItem)
             numberOfBooths++
             console.log(numberOfBooths)
        }else if(!input.checked){
            findInputId = input.parentElement.innerText
            document.getElementById(findInputId).remove()
            numberOfBooths--
            console.log(numberOfBooths)
        }
    })
})



function clearDiv(id){
    document.getElementById(id).innerHTML = ''

}


console.log(selectedDates)
function gatherInputData(){


    function calculateTotal(boothType, numberOfBooths, selectedDates, boothOptions){

    }
}

gatherInputData()


