const toggle_header = document.querySelector("#toggle_header");

toggle_header.addEventListener("click", function (e) {
  const Header = document.querySelector("header")
  if (Header.className === "green") {
    Header.classList.replace("green", "red");
  } else {
    Header.classList.replace("red", "green");
  }
})
