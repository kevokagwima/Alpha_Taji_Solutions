const burger = document.querySelector('.burger')
const links = document.querySelector('.links')

burger.addEventListener('click', ()=> {
  links.classList.toggle('nav-links')
})

window.addEventListener('scroll', ()=> {
  links.classList.remove('nav-links')
})
