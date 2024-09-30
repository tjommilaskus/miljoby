document.addEventListener("DOMContentLoaded", () => {
  const navBar = document.getElementById("navBar");
  if (navBar) {
    navBar.innerHTML = `
      <nav>
        <ul>
          <li class="logo-item"><a href="index.html"><img src="bilder/hvl-topia-logo.svg" alt="HVLTopia Logo" class="logo"></a></li>
          <li class="link-item"><a href="lesMer.html">Les Mer</a></li>
          <li class="link-item"><a href="berekraft.html">Bærekraft</a></li>
          <li class="link-item"><a href="omOss.html">Om Oss</a></li>
          <li class="link-item"><a href="kontaktOss.html">Kontakt oss</a></li>
          
        </ul>
      </nav>
    `;
  }

  // Legg til aktiv klasse på gjeldende side
  const currentPage = window.location.pathname.split("/").pop();
  const navLinks = document.querySelectorAll("nav ul li a");
  navLinks.forEach((link) => {
    if (link.getAttribute("href") === currentPage) {
      link.classList.add("active");
    }
  });
});
