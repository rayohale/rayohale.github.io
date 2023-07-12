function UVA(monto,porcentaje) {
	let mon = monto
	let doceavo = porcentaje/12
	repeat(10) {
		let res = mon * doceavo;
		document.write(res);
	}
}