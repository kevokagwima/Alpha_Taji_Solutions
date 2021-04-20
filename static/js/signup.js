const btn = document.querySelector('.btn')
const close = document.querySelector('.close-button')
const box = document.querySelector('.message')

btn.addEventListener('click', ()=> {
  btn.classList.toggle('btn--loading')
})

close.addEventListener('click', ()=> {
  box.classList.add('messages')
})
