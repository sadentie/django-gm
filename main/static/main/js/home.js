function edit(buttonId) {
    elem = document.querySelector('#'+buttonId).innerHTML;
    elem2 = document.getElementById('hide'+buttonId);
    if (elem == '<i class="fa-solid fa-xmark"></i>') {
      elem2.style.display = 'none'
      document.querySelector('#'+buttonId).innerHTML = '<i class="fa-solid fa-pen"></i>';
      document.getElementById("goal"+buttonId).setAttribute("style", "display: block");
      document.getElementById('suc'+buttonId).removeAttribute("style");
    }
    else {
      elem2.style.display = 'flex'
      document.querySelector('#'+buttonId).innerHTML = '<i class="fa-solid fa-xmark"></i>';
      document.getElementById("goal"+buttonId).setAttribute("style", "display: none");
      document.getElementById('suc'+buttonId).setAttribute("style", "display: none");

    }

};
try {
  document.getElementById('id_logusername').placeholder = 'Имя пользователя'
  document.getElementById('id_logpassword').placeholder = 'Пароль'
} catch {}

// изменение цвета шкалы прогресса в зависимости от того на сколько она заполнена
progressbars = document.getElementsByClassName('progbar')
progressindex = 0
while (progressindex<progressbars.length) {
  percent = parseInt(progressbars[progressindex].style.width)
  if (percent == 200) {
    progressbars[progressindex].classList.add('infprog')
    progressbars[progressindex].parentElement.classList.add('infbar')
  }
  else if (percent > 33 && percent < 66) {
    progressbars[progressindex].classList.add('midprog')
    progressbars[progressindex].parentElement.classList.add('midprog')
  }
  else if (percent > 66) {
    progressbars[progressindex].classList.add('endprog')
    progressbars[progressindex].parentElement.classList.add('endbar')
  }
  progressindex++
}

// заполнение инпута редактируемой цели текущей целью
try {
goals = document.querySelectorAll('.goaltext')
inp = document.getElementsByName('goal')
inp[0].placeholder = 'Твоя цель'
i = 1
while (i<inp.length) {
  goal = goals[i-1].innerHTML
  inp[i].value = goal
  i++
};
} catch{}


// закрытие/открытие окна регистрации
document.getElementById('btnreg').onclick = function(){
  document.getElementById('reg').classList.contains('hideblock') ? document.getElementById('reg').classList.remove('hideblock') : document.getElementById('reg').classList.add('hideblock')
}
document.getElementById('regclose').onclick = function() {document.getElementById('reg').classList.add('hideblock')}
document.addEventListener('keyup', function(e) { if(e.code == 'Escape'){document.getElementById('reg').classList.add('hideblock')}} )

// здесь планировался вывод ошибок в реальном времени, но справился и без этого
// document.getElementById('id_username').oninput = function(){
//   $.ajax({
//     url: 'validate',
//     // data: {'username': document.getElementById('id_username').value},
//     data: {'username': $('#id_username').val()},
//     dataType: 'json',
//     success: function(data){
//       if (data.is_taken){ document.getElementById('message').innerHTML = 'taken'}
//       else { document.getElementById('message').innerHTML = ''}

//     }
//   })
// }

// окно регистрации
document.getElementById('regconf').onclick = function(){
  $.ajax({
    url:'reg',
    data: {
      'username': $('#id_username').val(),
      'password1': $('#id_password1').val(),
      'password2': $('#id_password2').val()
    },
    dataType: 'json',
    success: function(data){
      if (data.reg['password2'] || data.reg['password1']){document.getElementById('err2').innerHTML = data.reg['password2'].join(' ')
      document.getElementById('err1').innerHTML = data.parse()
      } else {
        document.getElementById('err2').innerHTML = ''
        location.reload()
      }
    }
  })
}
