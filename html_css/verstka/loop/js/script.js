window.onload = function() {
  var sliderItems = document.querySelectorAll(".slider-item");
  var maxSliders = sliderItems.length;
  var max_height = 0;
  var sliderBlocks = document.querySelector(".slider-blocks");
  var controlBlock = document.querySelector(".slider-blocks__control");

  for (i = 0; i <= maxSliders - 1; i++) {
    var item = sliderItems[i];
    max_height = max_height < parseInt(getComputedStyle(item).height) ? parseInt(getComputedStyle(item).height) : max_height;

    item.onclick = function(e) {
      for (i = 1; i <= maxSliders; i++) {
        if (this.classList.contains('index-slider-' + i)) {
          if (i == maxSliders) {
            var nextSlider = document.querySelector('.index-slider-1');
            var nextControl = document.querySelector('.index-control-1');
          } else {
            var nextSlider = document.querySelector('.index-slider-' + (i + 1));
            var nextControl = document.querySelector('.index-control-' + (i + 1));
          }
          var currentControl = document.querySelector('.index-control-' + i);
          currentControl.classList.toggle('control__item_active');
          nextControl.classList.toggle('control__item_active');

          nextSlider.classList.toggle('slider-item_active');
          this.classList.toggle('slider-item_active');
        }
      }
    }

    var newControl = document.createElement("div");
    newControl.classList.toggle('control__item');
    newControl.classList.toggle('index-control-' + (i + 1));
    if (i == 0) {
      newControl.classList.toggle('control__item_active');
    }
    controlBlock.appendChild(newControl);
  }

  for (i = 0; i <= maxSliders - 1; i++) {
    var item = sliderItems[i];
    item.style.height = max_height + 'px';
  }


  var controlItems = document.querySelectorAll('.control__item');

  for (i = 0; i <= controlItems.length - 1; i++) {
    controlItems[i].onclick = function(i) {
      // return changeSliderByControl(i);
      // return changeSliderByControl;
        return function() {
          var currentIndex = 1;
          var currentActiveSlider = document.querySelector('.slider-item_active');
          var currentActiveControl = document.querySelector('.control__item_active');
          var nextActiveSlider = document.querySelector('.index-slider-' + (i + 1));

          currentActiveSlider.classList.toggle('slider-item_active');
          currentActiveControl.classList.toggle('control__item_active');

          this.classList.toggle('control__item_active');
          nextActiveSlider.classList.toggle('slider-item_active');
        }
    }(i)
  }
  // i = 10;
  // function changeSliderByControl(e) {
  //   // return function() {
  //     var currentIndex = 1;
  //     var currentActiveSlider = document.querySelector('.slider-item_active');
  //     var currentActiveControl = document.querySelector('.control__item_active');
  //     var nextActiveSlider = document.querySelector('.index-slider-' + (i + 1));
  //
  //     currentActiveSlider.classList.toggle('slider-item_active');
  //     currentActiveControl.classList.toggle('control__item_active');
  //
  //     this.classList.toggle('control__item_active');
  //     nextActiveSlider.classList.toggle('slider-item_active');
  //   // }
  // }

  // for (var i = 0; i < controlItems.length-1; i++) {
  //
  //   controlItems[i].onclick = function(x) {
  //
  //     return function() {
  //       alert(x)
  //     }
  //
  //   }(i)
  //
  // }

  sliderBlocks.style.height = (max_height + parseInt(getComputedStyle(sliderBlocks).height) - 100) + 'px';

}
