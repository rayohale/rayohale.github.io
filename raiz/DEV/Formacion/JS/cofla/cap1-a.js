dineroRoberto = prompt("Ingresá tu monto Roberto");
dineroPedro = prompt("Ingresá tu dinero Pedro");
dineroCofla = prompt("Ingresá tu monto Cofla");

dineroCofla = parseInt(dineroCofla); // Funcion que nos permite convertirlo a número

if (dineroRoberto >= 0.6 && dineroRoberto < 1) {
	alert("Roberto te alcanza para un helado de agua");
}

else if (dineroRoberto >= 1 && dineroRoberto <1.6) {
	alert("Roberto te alcanza para un helado de crema");
}

else if (dineroRoberto >= 1.6 && dineroRoberto <1.7) {
	alert("Roberto te alcanza bombón heladix");
}

else if (dineroRoberto >= 1.7 && dineroRoberto <1.8) {
	alert("Roberto te alcanza para un bombón heladovich");
}

else if (dineroRoberto >= 1.8 && dineroRoberto <2.9) {
	alert("Roberto te alcanza para un bombón helardo");
}

else if (dineroRoberto >= 2.9) {
	alert("Roberto te alcanza para un potecito con confites o un pote de 1/4 kg");
}

else {
	alert("Roberto no te alcanza para ningún helado");
}

if (dineroPedro >= 0.6 && dineroPedro < 1) {
	alert("Pedro te alcanza para un helado de agua");
}

else if (dineroPedro >= 1 && dineroPedro <1.6) {
	alert("Pedro te alcanza para un helado de crema");
}

else if (dineroPedro >= 1.6 && dineroPedro <1.7) {
	alert("Pedro te alcanza bombón heladix");
}

else if (dineroPedro >= 1.7 && dineroPedro <1.8) {
	alert("Pedro te alcanza para un bombón heladovich");
}

else if (dineroPedro >= 1.8 && dineroPedro <2.9) {
	alert("Pedro te alcanza para un bombón helardo");
}

else if (dineroPedro >= 2.9) {
	alert("Pedro te alcanza para un potecito con confites o un pote de 1/4 kg");
}

else {
	alert("Roberto no te alcanza para ningún helado");
}

if (dineroCofla >= 0.6 && dineroCofla < 1) {
	alert(`Cofla te alcanza para un helado de agua y te sobran ${dineroCofla - 0.6}`);
}

else if (dineroCofla >= 1 && dineroCofla <1.6) {
	alert(`Cofla te alcanza para un helado de crema y te sobran ${dineroCofla - 1}`);
}

else if (dineroCofla >= 1.6 && dineroCofla <1.7) {
	alert(`Cofla te alcanza bombón heladix y te sobran ${dineroCofla - 1.6}`);
}

else if (dineroCofla >= 1.7 && dineroCofla <1.8) {
	alert(`Cofla te alcanza para un bombón heladovich y te sobran ${dineroCofla - 1.7}`);
}

else if (dineroCofla >= 1.8 && dineroCofla <2.9) {
	alert(`Cofla te alcanza para un bombón helardo y te sobran ${dineroCofla - 1.8}`);
}

else if (dineroCofla >= 2.9) {
	alert(`Cofla te alcanza para un potecito con confites o un pote de 1/4 kg y te sobran ${dineroCofla - 2.9}`);
}

else {
	alert(`Cofla no te alcanza para ningún helado`);
}