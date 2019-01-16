myStorage = window.sessionStorage

console.log(myStorage)
price = document.getElementById('cart-total')

eventTrigger = document.getElementById('nextSlide')

if(null == undefined){
    console.log(true)
}

eventTrigger.addEventListener('click', ()=>{
    console.log('hello')
    if(price.innerText === ''){
        console.log('no price srovided')
    }else{
        if(myStorage.getItem('totalPrice') == null){
        }else{
            myStorage.getItem('totalPrice')
            myStorage.setItem('totalPrice', parseInt(price.innerText))
        }
    }
})

//Run window on window load run this
window.addEventListener('load', ()=>{

console.log('load 1')
            if(document.getElementById('id_select_cities_0').checked){
                document.getElementById('TorontoFairOptionsContainer').style = 'display: block'
            }
            if(document.getElementById('id_select_cities_1').checked){
                document.getElementById('WinnipegFairOptionsContainer').style = 'display: block'
            }
            if(document.getElementById('id_select_cities_2').checked){
                document.getElementById('CalgaryFairOptionsContainer').style = 'display: block'
            }
            if(document.getElementById('id_select_cities_3').checked){
                 document.getElementById('EdmontonFairOptionsContainer').style = 'display: block'

            }
})