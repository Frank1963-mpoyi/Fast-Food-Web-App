//we use location storage to store data of the browser of the user 
var hours = 24; // local storage dont have an expiration date expiration date
var now = new Date().getTime();// get time when the user visite the application
var stepTime = localStorage.getItem('stepTime');// to check if the user visite the website in last 24 hours


if (stepTime == null) {// stepTime  is equal null which mean there is no stepTime store in our storage and it is the first time the user visite our website
    localStorage.setItem('stepTime', now);// and we wil store the variable now in the browser of the user Note: variable now is on top 
}
else {
    if (now - stepTime > hours*60*60*1000) {// if the user has visited the webapplication before, (if the different the last time he visited - and the time now) > is more than 24Hrs or hours*60*60*1000 the same as 24Hrs
        localStorage.clear(); // we will clear all data store in the browser of the user
        localStorage.setItem('stepTime', now); // and we will set stepTime now , like the time retart again the process
    }
}


//orders.js
var orders = JSON.parse(localStorage.getItem('orders'));
var total =localStorage.getItem('total');

if (orders === null || orders === undefined) {
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}


if (orders === null || orders === undefined) {
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total');
}

var cart = document.querySelector("#cart");
cart.innerHTML = orders.length;

