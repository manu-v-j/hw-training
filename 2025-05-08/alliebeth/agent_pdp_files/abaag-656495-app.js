stickyHeader = function() {

  if (window.matchMedia('(min-width: 1024px)').matches) {

    var scrollTop = $(window).scrollTop();

    if (scrollTop > 20) {
      $('#hlajc-615666').addClass('site-scroll');
    } else {
      $('#hlajc-615666').removeClass('site-scroll');
    }

  }

};

homePageHero = function() {

  var totalHeroImages = $('.site-home-page-hero-image article').length;

  var randomHeroImage = Math.floor(Math.random() * totalHeroImages + 1);
  $(".site-home-page-hero-image article:nth-child(" + randomHeroImage +  ")").css("display","block");

}

siteHomeLargeCallouts = function(){

  //if (window.matchMedia('(min-width: 768px)').matches) {
    $('.site-large-callouts-slider').slick({
      autoplay: false,
      arrows: false,
      dots: true,
      fade: false,
      speed: 900
    });
  //}
}

var siteVideoLoadDelay = 1000;

function homePageLoad() {

  // Load home page on both cms site editor and live site
  if ($('.cms-site-home-page').length > 0 || $('.site-home-page').length > 0) {

    homePageHero();

    siteHomeLargeCallouts();

    var siteVideoTimer = setInterval((function() {
      
      $(".site-home-page-hero-video-background").addClass("site-show");

      clearInterval(siteVideoTimer);

    }), siteVideoLoadDelay);

  }

  // stickyHeader();

  // $(window).scroll(function() {

  //   stickyHeader();
  // });
}





















