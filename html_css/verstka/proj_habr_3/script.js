
//Обнуление нажатия кнопки по-умолчанию <a>
var all_a = document.querySelectorAll('a');
for (i = 0; i <= all_a.length - 1; i++) {
  var elem = all_a[i];
  elem.onclick = function(e) {
    e.preventDefault();
  }
}

var sliders = document.querySelectorAll('.slide');

for (i = 0; i <= sliders.length-1; i++) {
  css_left = parseInt(getComputedStyle(sliders[i]).width);
  css_margin = parseInt(getComputedStyle(sliders[i]).marginLeft)
  sliders[i].style.left = css_left * i + css_margin*2*i + 'px';
}

var menu_burger = document.body.getElementsByClassName("burger-button");
var header = document.body.getElementsByClassName("page-1")[0].getElementsByClassName("header")[0];

if (menu_burger.length != 0) {
  var btn = menu_burger[0];
  btn.onclick = function(e) {
    if (e.target.checked) {
      header.style.visibility = "visible";
    } else {
      header.style.visibility = "hidden";
    }
  }
}
