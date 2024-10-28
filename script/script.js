document.addEventListener("DOMContentLoaded", () => {
  const navBar = document.getElementById("navBar");

  // Check if the navBar element exists
  if (navBar) {
    navBar.innerHTML = `
      <nav>
        <ul>
          <li class="logo-item">
            <a href="index.html">
              <img src="bilder/hvl-topia-logo.svg" alt="HVLTopia Logo" class="logo">
            </a>
          </li>
          <li class="link-item"><a href="omProsjektet.html">Om Prosjektet</a></li>
          <li class="link-item"><a href="berekraft.html">Bærekraft</a></li>
          <li class="link-item"><a href="lesMer.html">Les Mer</a></li>
          <li class="link-item"><a href="maalinger.html">Målinger</a></li>
          <li class="link-item"><a href="omOss.html">Om Oss</a></li>
        </ul>
        <div class="hamburger">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </nav>
    `;
  }

  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector("nav ul");

  hamburger.addEventListener("mouseover", () => {
    navMenu.classList.toggle("show");
  });

  const currentPage = window.location.pathname.split("/").pop();
  const navLinks = document.querySelectorAll("nav ul li a");

  navLinks.forEach((link) => {
    if (link.getAttribute("href") === currentPage) {
      link.classList.add("active");
    }
  });
});
