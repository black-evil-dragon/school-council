/*
var bg_mWindow = document.querySelector('.bg-mlWindow');
var modalWindow = document.querySelector('.modalWindow');
var windowContent = document.querySelector('.windowContent')

bg_mWindow.classList.toggle('active');
modalWindow.classList.toggle('active');
windowContent.classList.toggle('active');
*/
function showModalWindow() {
    document.querySelectorAll('div').forEach(
        element => element.classList.toggle('inBlur')
    );
    document.querySelector('.bg-mWindow').classList.toggle('active')
    document.querySelector('.modalWindow').classList.toggle('active')
}
