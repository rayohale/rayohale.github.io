

// Funcion para calcular el porcentaje del Plazo Fijo
function interes(monto,porcentajeAnual) {
	let mon = parseInt(monto);
	let porcentaje = parseInt(porcentajeAnual);
	let doceavo = porcentaje/1200;
	let res = mon * doceavo + mon;
	let i = 1;
	document.write(`<b>Monto inicial:</b> $${mon}` + "<br><br>");
	document.write("<b><ins>PLAZO FIJO, renovando mes a mes</ins>:</b><br>")
	while (i <= 12) {
		res;
		document.write(`Mes n° ${i} ` + "$"+res.toFixed(2) + "<br>");
		if (i <= 11) {
			res += res * doceavo;
			i++;
		} else {
			i++
			res += 0;
			let calculo = res.toFixed(2);
			let resultado = (calculo-mon)*100/mon
			document.write(`<br><b>Porcentaje anualizado:</b> <strong style="color:red">${resultado.toFixed(2)}%</strong>.`)
			document.write(`<br><b>PLAZO FIJO anual:</b> $${mon*(porcentaje/100)+mon}.<br><br>`);
			document.write(`<b>El porcentaje de interes anual es ${porcentaje}%.</b>`);
			
			document.write("<br><br><a href='porcentajes.html'>Volver</a>")
		}
	}
}


function plazoFijo() {
	let datoMonto = prompt("Ingrese el monto");
	let datoPorcentaje = prompt("Ingrese el porcentaje anual");
	interes(datoMonto,datoPorcentaje);
}

/* // UVA2() >> no la usé al final
function UVA2() {
	let monto2 = prompt(`Ingrese el monto`);
	let porcentaje2 = prompt("Ingrese el porcentaje de interes anual");
	let doceavo2 = porcentaje2/1200;
	let res2 = monto2 * doceavo2 + monto2;
	let i2 = 1;

	while (i2 < 13){
		res2;
		document.write(`Mes n° ${i2} ` + res2 + "<br>");
		res2 += res2 * doceavo;
		i++;
	}

}
*/


