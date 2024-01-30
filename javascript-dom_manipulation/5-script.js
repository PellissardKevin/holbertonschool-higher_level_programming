const update_header = document.querySelector('#update_header')

update_header.addEventListener("click", () => {
  const Header = document.querySelector('header');
  Header.innerHTML = 'New Header!!!';
})
