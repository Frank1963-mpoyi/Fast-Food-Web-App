var nam = document.querySelector("#name");
var size= document.querySelector("#size");
var price = document.querySelector("#price");
var bill = document.querySelector("#total");
var rm = document.querySelector("#rm");


function shoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    var cartSize = orders.length;

    nam.innerHTML = '<h3>Name</h3>';
    size.innerHTML = '<h3>Size</h3>';
    price.innerHTML = '<h3>Price</h3>';
    rm.innerHTML = '<h3><br></h3>';




    //pcart.innerHTML ='';
    for (let i = 0; i < cartSize; i++) {
        rm.innerHTML += '<h4><button class="btn-danger" onclick="removeItem('+i+')"> X </button></h4>';
        
        //cart.innerHTML += '<li>'+ orders[i][0] +  ' ' + orders[i][1] +  ': ' + orders[i][2] +  ' $' +butto+ '</li>'; 
        nam.innerHTML  += '<h4>' + orders[i][0] + '</h4>'
        size.innerHTML  += '<h4>' + orders[i][1] + '</h4>'
        price.innerHTML += '<h4>' + orders[i][2] + '</h4>'
    }
    bill.innerHTML = "Total: " + total + ' $';

}

shoppingCart();



function removeItem(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total =localStorage.getItem('total');
    
    total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);

    //Updating number of items in shopping Cart
    var cart = document.querySelector('#cart');
    cart.innerHTML =orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    
    shoppingCart();
}