const modalWindow = document.querySelector('.modal')

if (!window.localStorage.getItem('modal')) {
    modalWindow.classList.remove('close')
    window.localStorage.setItem('modal', true)
}




modalWindow.addEventListener("click", () => {
    modalWindow.classList.add('close')
})