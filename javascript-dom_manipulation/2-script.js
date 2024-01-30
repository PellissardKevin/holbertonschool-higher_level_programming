const red_header = document.querySelector("#red_header");

red_header.addEventListener("click", function (e) {
  const Header = document.querySelector("header")
  Header.classList.add("red");
})
