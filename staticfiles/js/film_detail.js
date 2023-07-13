var buttonStar = document.querySelector('.button_star');
var rating = document.querySelector('.rating');

buttonStar.addEventListener('click', function() {
  rating.style.display = 'block'; // Відображати блок зі зірками при натисканні на кнопку
});