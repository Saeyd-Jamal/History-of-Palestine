// btn navbar
const hamburgerMenu = document.querySelector('.btn_nav'),
      homebox = document.querySelector('.home');
const menuIsActive = () => {
  hamburgerMenu.classList.toggle('active');
}
hamburgerMenu.addEventListener('click', menuIsActive);
 