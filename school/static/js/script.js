$(document).ready(function() {
  $('.scrollTop').click(function(){
    $('html, body').animate({
      scrollTop: 0
    }, 600);
    return false;
  });
});

/* Все, что написано ниже, всего лишь желание развлечься

всего лишь...

я добавил пасхалки, и некоторые перед вами */

const egg = document.querySelector('.eggs');
const target = document.querySelector('#error-ghost');
const text = egg.getAttribute('ghost');


if (target != null) {
  target.setAttribute('title', text);
  egg.setAttribute('ghost', '.. он тебя искал ..');
}
else {
  egg.removeAttribute('ghost')
}

/* «Каждый Призрак рождается, зная,
что мы должны найти нашего Стража.
Мы не знаем, как они выглядят.
Во всяком случае, не снаружи.
Внутри я всегда знаю, кем ты был.
И вместе мы могли бы быть чем-то большим.
Когда я думаю обо всем, что мы видели,
обо всем, что мы сделали, я чувствую, что...
я сделал правильный выбор.
Спасибо - знаешь - за то, что ты мой Страж» */


