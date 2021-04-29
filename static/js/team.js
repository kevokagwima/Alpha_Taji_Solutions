const user = document.querySelector('.user')
const img = document.querySelector('.img')
const profile = document.querySelector('.profile')

window.addEventListener('scroll', ()=> {
  user.classList.remove('nav-active')
  profile.classList.remove('show-profile')
})

img.addEventListener('click', ()=> {
  profile.classList.toggle('show-profile')
})
