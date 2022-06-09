/* Menu btns */
function showOptions(current_level, target_level) {
    document.querySelector(current_level).classList.remove('active');
    document.querySelector(target_level).classList.add('active');
}

/* Menu panel */

var acc = document.getElementsByClassName("btn-menu-head");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");

    var panel = document.querySelector('.panel-menu-head')

    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
        panel.style.height = 100 + '%';
        panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}
var acc = document.getElementsByClassName("btn-menu-footer");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");

    var panel = document.querySelector('.panel-menu-head')

    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
        panel.style.height = 100 + '%';
        panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}