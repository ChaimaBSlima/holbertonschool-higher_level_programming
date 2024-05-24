#!/usr/bin/node

const headColor = document.querySelector('header');

const setColor = document.querySelector('#toggle_header');
setColor.addEventListener('click', () => {
  if (headColor.classList.length === 0) {
    headColor.classList.add('green');
  } else if (headColor.classList.value.includes('green')) {
    headColor.classList.replace('green', 'red');
  } else if (headColor.classList.value.includes('red')) {
    headColor.classList.replace('red', 'green');
  }
});
