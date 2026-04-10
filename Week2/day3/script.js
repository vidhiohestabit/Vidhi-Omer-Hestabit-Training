const items = document.querySelectorAll(".item");

items.forEach(item => {
  const title = item.querySelector(".title");
  const icon = item.querySelector(".icon");

  title.addEventListener("click", () => {
    item.classList.toggle("active");
    icon.textContent =
      item.classList.contains("active") ? "-" : "+";
  });
});
