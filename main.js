const myTitle = document.querySelector(".myTitle");

const titles = [
    'software engineer',
    'web developer',
    'data engineer',
    'cloud engineer'
];

let index = 0;

myTitle.textContent = "I am";

function updateTitle() {
    myTitle.classList.remove("show");
    setTimeout(() => {
        myTitle.textContent = titles[index];
        myTitle.classList.add("show");
        index = (index + 1) % titles.length;
    }, 1000);
}

setInterval(updateTitle, 2000);
