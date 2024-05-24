#!/usr/bin/node

const UpdateHeader = document.querySelector('header');

const setHeader = document.querySelector('#update_header');
setHeader.addEventListener('click', () => {
  UpdateHeader.textContent = 'New Header!!!';
});
