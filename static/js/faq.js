const questions = document.querySelectorAll(".question")
const user = document.querySelector('.user')
const img = document.querySelector('.img')
const profile = document.querySelector('.profile')

questions.forEach(function(question) {
    const btn = question.querySelector("#btn")
    btn.addEventListener("click", function() {
        questions.forEach(function(item) {
            if(item !== question) {
                item.classList.remove("show-text")
            }
        })
        question.classList.toggle("show-text")
    })
})

window.addEventListener('scroll', ()=> {
    nav_links.classList.remove('nav-active')
    user.classList.remove('nav-active')
    profile.classList.remove('show-profile')
  })
  
  img.addEventListener('click', ()=> {
    profile.classList.toggle('show-profile')
  })
