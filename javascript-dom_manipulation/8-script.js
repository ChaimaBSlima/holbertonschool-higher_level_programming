#!/usr/bin/node

document.addEventListener('DOMContentLoaded', () => {
    fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      const helloContent = document.getElementById('hello');
      helloContent.textContent = data.hello;
    });
  })
