const nav_links = document.querySelector('.links')
const user = document.querySelector('.user')
const burger = document.querySelector('.burger')

burger.addEventListener('click', ()=> {
  nav_links.classList.toggle('nav-active')
  user.classList.toggle('nav-active')
})

window.addEventListener('scroll', ()=> {
  nav_links.classList.remove('nav-active')
  user.classList.remove('nav-active')
})
