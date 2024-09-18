window.onload = function() {
    fetch('navBar.html')
      .then(response => response.text())
      .then(data => {
        document.getElementById('navBar').innerHTML = data;
      });
  };