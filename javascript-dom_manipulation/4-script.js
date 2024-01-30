const add_items = document.querySelector("#add_item");

add_items.addEventListener("click", () => {
  const myList = document.querySelector(".my_list");
  myList.insertAdjacentHTML(
    "beforeend",
    "<li>Item</li>"
  );
});
