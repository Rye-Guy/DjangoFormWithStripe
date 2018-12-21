console.log('Animation Hello')

billingInfoBtn = document.getElementById('sideTrigger')
billingInfoContainer = document.getElementById('billingInfoContainer')

billingInfoContainer.className = 'hide-me'

billingInfoBtn.addEventListener('click', (ev)=>{
    ev.preventDefault()
    console.log('Yo yo ma')
    billingInfoContainer.className = 'animated fadeInLeft'
})