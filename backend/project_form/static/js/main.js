// script.js
document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".counter .number");
  const speed = 1000; // Adjust the speed as necessary

  counters.forEach((counter) => {
    const updateCount = () => {
      const target = +counter.parentElement.getAttribute("data-target");
      const count = +counter.innerText;
      const increment = target / speed;

      if (count < target) {
        counter.innerText = Math.ceil(count + increment);
        setTimeout(updateCount, 1);
      } else {
        counter.innerText = target;
      }
    };

    updateCount();
  });
});

document.getElementById("nav-button").addEventListener("click", () => {
  window.location.href = "./registration";
});

// on click mobile-menu add/remove class .active from .nav-links
document.getElementById("mobile-menu").addEventListener("click", () => {
  document.getElementById("nav-links").classList.toggle("active");
});
