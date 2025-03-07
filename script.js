const slideBtnleft = document.getElementById("slide-btn-left")
const slideBtnright = document.getElementById("slide-btn-right")
const imgIterm = document.querySelectorAll(".image-iterm")

// console.log(imageItem.length-1)
let startslider = 0
let endsliderslider = imgIterm.length-1 *100
slideBtnleft.addEventListener("click", () => {
    if(startslider < -endslider){
        startslider = startslider - 100;
    }
    startslider = startslider - 100;
    imgIterm.forEach(Element =>{
       Element.style.transformation = `translatex(${startslider}%)`;
    })
    
})
slideBtnright.addEventListener("click", () => {
    if(startslider < -endslider){
        startslider = startslider - 100;
    }
    startslider = startslider - 100;
    imgIterm.forEach(Element =>{
       Element.style.transformation = `translatex(${startslider}%)`;
    })
    
})
