// Makes the header logo link to the external Etherion Designs website
document.addEventListener("DOMContentLoaded", function () {
  var logo = document.querySelector(".md-header__button.md-logo");
  if (logo) {
    logo.setAttribute("href", "https://www.etheriondesigns.com");
    logo.setAttribute("target", "_blank");
  }
});