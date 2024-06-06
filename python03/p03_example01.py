<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shopping Cart</title>
    <script src="script.js"></script>
</head>
<body>
    <h1>Shopping Cart</h1>
    <table>
        <tr>
            <th>Product name</th>
            <th>Product price</th>
            <th>Quantity</th>
        </tr>
        <tr>
            <td><input type="text" id="name1" value="Product1"></td>
            <td><input type="text" id="price1" value="10.0"></td>
            <td><input type="text" id="quantity1" value="3"></td>
        </tr>
        <tr>
            <td><input type="text" id="name2" value="Product2"></td>
            <td><input type="text" id="price2" value="15.0"></td>
            <td><input type="text" id="quantity2" value="2"></td>
        </tr>
        <tr>
            <td><input type="text" id="name3" value="Product3"></td>
            <td><input type="text" id="price3" value="30.0"></td>
            <td><input type="text" id="quantity3" value="1"></td>
        </tr>
    </table>
    <button onclick="calculate()">Calculate</button>
    <p>Total: <input type="text" id="total" readonly></p>
    <p>Delivery (10% of total): <input type="text" id="delivery" readonly></p>
    <p>Total and delivery: <input type="text" id="total_delivery" readonly></p>
</body>
</html>




-------


function calculate() {
    let product1Price = parseFloat(document.getElementById('price1').value);
    let product1Quantity = parseInt(document.getElementById('quantity1').value);
    let product2Price = parseFloat(document.getElementById('price2').value);
    let product2Quantity = parseInt(document.getElementById('quantity2').value);
    let product3Price = parseFloat(document.getElementById('price3').value);
    let product3Quantity = parseInt(document.getElementById('quantity3').value);

    let total1 = product1Price * product1Quantity;
    let total2 = product2Price * product2Quantity;
    let total3 = product3Price * product3Quantity;

    let subtotal = total1 + total2 + total3;
    let delivery = subtotal * 0.10;
    let finalTotal = subtotal + delivery;

    document.getElementById('total').value = subtotal.toFixed(2);
    document.getElementById('delivery').value = delivery.toFixed(2);
    document.getElementById('total_delivery').value = finalTotal.toFixed(2);
}


