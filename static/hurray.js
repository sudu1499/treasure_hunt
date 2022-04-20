let b=document.getElementsByClassName('burger')[0]
let link=document.getElementsByClassName('links')[0]
b.addEventListener('click',()=>{
link.classList.toggle('active_links')
})