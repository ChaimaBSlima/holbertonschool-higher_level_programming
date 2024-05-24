#!/usr/bin/node

const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');
setItem.addEventListener('click', () => {
  const nuevo = document.createElement('li');
  nuevo.textContent = 'Item';
  listClass.appendChild(nuevo);
});
