const toTop = document.querySelector(".toTop");

window.addEventListener("scroll", () => {

    if (window.pageYOffset > 100){
            toTop.classList.add("active");
        }
    else{
        toTop.classList.remove("active");
    }
    } 
)

// hamburger
const btn = document.getElementById('menu-btn')
const nav = document.getElementById('menu')

btn.addEventListener('click', () => {

    btn.classList.toggle('open')
    nav.classList.toggle('flex')
    nav.classList.toggle('hidden')
})

