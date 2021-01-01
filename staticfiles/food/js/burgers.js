var bcart = document.querySelector('#bcart'); //variable for pcart
var btotal = document.querySelector('#btotal');

// add Pizza

function addBurger(bid){ // will take argument id of pizza
    // get pizza name
    burgerId = '#bur' + bid;
    var name = document.querySelector(burgerId).innerHTML;
    //get pizza price
    var radio = 'burger' +  bid;
    var pri = document.getElementsByName(radio);
    var size, price;
    // var size, price;
    // price = pri[0].value;
    // size ='M';
    

    if (pri[0].checked) {
        price = pri[0].Value;
        size = 'M';
    }
    else {
        price = pri[1].value; 
        size = 'L';
    }
    
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    var cartSize = orders.length;
    // saving items and total in localstorage
    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders',JSON.stringify(orders));
    

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    //Updating number of items in shopping Cart
    var cart = document.querySelector('#cart');
    cart.innerHTML =orders.length;
    butto = '<div class="del" onclick="removeBurger('+ cartsize +')"> X </div>'
    
    btotal.innerHTML = "Total: " + total + ' $';


    bcart.innerHTML += '<li>'+ name +  ' ' + size +  ': ' + price +  ' $' +butto+ '</li>'; 
    // pcart.innerHTML += '<li>'+ name +  ' ' + size +  ': ' + price +  ' $</li>'; 
    //must add a new pizza when we call it
}

function bshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    var cartSize = orders.length;
    bcart.innerHTML ='';
    for (let i = 0; i < cartSize; i++) {
        butto = '<div class="del" onclick="removeBurger('+i+')"> X </div>'
        bcart.innerHTML += '<li>'+ orders[i][0] +  ' ' + orders[i][1] +  ': ' + orders[i][2] +  ' $' +butto+ '</li>'; 
    }
    btotal.innerHTML = "Total: " + total + ' $';

}

bshoppingCart();


function removeBurger(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    //Updating number of items in shopping Cart
    var cart = document.querySelector('#cart');
    cart.innerHTML =orders.length;


    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    
    bshoppingCart();
}