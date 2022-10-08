/* Menu panel */

const menuButton = document.querySelector('.menu-button')
const menuPanel = document.querySelector('.app__menu')
const menu = document.querySelector('.menu')

menuButton.addEventListener("click", function () {
    if (menuPanel.style.maxHeight) {
        menuPanel.style.maxHeight = null;
    } else {
        menuPanel.style.height = `${100}%`
        menuPanel.style.maxHeight =  `${menu.scrollHeight}px`
    }
})

/* Menu buttons */

const openBurger = (event, targetPosition) => {
    const currentMenu = event.target.parentElement.parentElement

    currentMenu.classList.remove('_active')
    document.getElementById(`${targetPosition}`).classList.add('_active')
}
