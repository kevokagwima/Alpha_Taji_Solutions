const burger = document.querySelector('.burger')
const links = document.querySelector('.links')

burger.addEventListener('click', ()=> {
  links.classList.toggle('nav-active')
})

window.addEventListener('scroll', ()=> {
  links.classList.remove('nav-active')
})
