var showMoreBtn = document.getElementById('showMoreBtn');
var showLessBtn = document.getElementById('showLessBtn');
var filmFields = document.querySelectorAll('.filmfield');
var visibleFilms = 6;

showMoreBtn.addEventListener('click', function() {
  var hiddenFilmFields = document.querySelectorAll('.filmfield.hidden');

  for (var i = 0; i < hiddenFilmFields.length; i++) {
    hiddenFilmFields[i].classList.remove('hidden');
    hiddenFilmFields[i].classList.add('animate__fadeIn');
  }

  var visibleFilmFields = document.querySelectorAll('.filmfield:not(.hidden)');
  var numVisibleFilms = visibleFilmFields.length;

  if (numVisibleFilms >= 6) {
    var filmsToHide = Array.from(visibleFilmFields).slice(0, numVisibleFilms - 6);

    for (var j = 0; j < filmsToHide.length; j++) {
      filmsToHide[j].classList.add('hidden');
    }
  }

});

showLessBtn.addEventListener('click', function() {
  var visibleFilmFields = document.querySelectorAll('.filmfield:not(.hidden)');
  var numVisibleFilms = visibleFilmFields.length;

  for (var i = numVisibleFilms - 1; i >= 0; i--) {
    visibleFilmFields[i].classList.remove('animate__fadeIn');
  }

  var filmsToShow = Array.from(filmFields).slice(0, visibleFilms);

  for (var j = 0; j < filmsToShow.length; j++) {
    filmsToShow[j].classList.remove('hidden');
    filmsToShow[j].classList.add('animate__fadeIn');
  }

  for (var i = numVisibleFilms - 1; i >= numVisibleFilms - 6; i--) {
    visibleFilmFields[i].classList.remove('animate__fadeIn');
    visibleFilmFields[i].classList.add('hidden');
  }

  visibleFilms += 6;

 
});