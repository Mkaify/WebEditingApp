document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById("theme-toggle");
  const themeLink = document.getElementById("theme-style");

  toggleBtn.addEventListener("click", () => {
    if (themeLink.getAttribute("href").includes("light")) {
      themeLink.setAttribute("href", "/static/css/style_dark.css");
    } else {
      themeLink.setAttribute("href", "/static/css/style_light.css");
    }
  });
});
