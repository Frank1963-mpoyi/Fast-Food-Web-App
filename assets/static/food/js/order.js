var pcart = document.querySelector('#pcart'); //variable for pcart
var ptotal = document.querySelector('#ptotal');

// add Pizza
// will take argument id of pizza
function addPizza(pid){ 
    // get pizza name
    pizzaId = '#piz' + pid;
    var name = document.querySelector(pizzaId).innerHTML;
    //get pizza price
    var radio = 'pizza' +  pid;
    var pri = document.getElementsByName(radio);
    var size, price;
    // var size, price;
    // price = pri[0].value;
    // size ='M';
    

    if (pri[1].checked) {
        price = pri[1].Value;
        size = 'L';
    }
    else {
        price = pri[0].value; 
        size = 'M';
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

    butto = '<div class="del" onclick="removePizza('+ cartSize +')"> X </div>'
    ptotal.innerHTML = "Total: " + total + ' $';


    pcart.innerHTML += '<li>'+ name +  ' ' + size +  ': ' + price +  ' $' + butto+  '</li>'; 
    // pcart.innerHTML += '<li>'+ name +  ' ' + size +  ': ' + price +  ' $</li>'; 
    //must add a new pizza when we call it
}

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    var cartSize = orders.length;
    pcart.innerHTML ='';
    for (let i = 0; i < cartSize; i++) {
        butto = '<div class="del" onclick="removePizza('+i+')"> X </div>'
        pcart.innerHTML += '<li>'+ orders[i][0] +  ' ' + orders[i][1] +  ': ' + orders[i][2] +  ' $' +butto+ '</li>'; 
    }
    ptotal.innerHTML = "Total: " + total + ' $';

}

pshoppingCart();

function removePizza(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);

    //Updating number of items in shopping Cart
    var cart = document.querySelector('#cart');
    cart.innerHTML =orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    
    pshoppingCart();
}