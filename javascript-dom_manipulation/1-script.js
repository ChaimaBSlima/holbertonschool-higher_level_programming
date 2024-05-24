#!/usr/bin/node
const headColor = document.querySelector('header');
const setColor = document.querySelector('#red_header');
setColor.addEventListener('click', () => {
  headColor.style.color = '#FF0000';
});
