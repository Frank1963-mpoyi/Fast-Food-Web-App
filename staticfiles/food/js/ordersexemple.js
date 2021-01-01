
var orders = JSON.parse(localStorage.getItem('orders'));// to store items selected by the user in array//JSON.parse convert JSON to array

var total =localStorage.getItem('total');

if (orders === null || orders === undefined) {// if the data above is not in local storage we will save an empty array
    localStorage.setItem('orders', JSON.stringify([]));// will save an empty array in the browser of the user
    orders = JSON.parse(localStorage.getItem('orders'));// will save an empty array in the browser of the user
}


if (orders === null || orders === undefined) { // if the total doent exist we will save the total 0 in the local storage
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total');
}

var cart = document.querySelector("#cart");
cart.innerHTML = orders.length; // get shoping in my navbar and the number will be the length of my orders


