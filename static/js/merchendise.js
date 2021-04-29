const burger = document.querySelector('.burger')
const user = document.querySelector('.user')
const links = document.querySelector('.links')
const img = document.querySelector('.img')
const profile = document.querySelector('.profile')

burger.addEventListener('click', ()=> {
  links.classList.toggle('nav-active')
  user.classList.toggle('nav-active')
})

window.addEventListener('scroll', ()=> {
  links.classList.remove('nav-active')
  user.classList.remove('nav-active')
  profile.classList.remove('show-profile')
})

img.addEventListener('click', ()=> {
  profile.classList.toggle('show-profile')
})
