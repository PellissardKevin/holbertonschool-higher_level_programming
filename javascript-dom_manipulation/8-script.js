fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(response => response.json())
  .then(hello => sayHello(hello));

function sayHello(hello) {
    const helloDiv = document.querySelector("#hello");
    helloDiv.innerText = `${hello.hello}`;
    helloDiv.append(listElement);
  };
