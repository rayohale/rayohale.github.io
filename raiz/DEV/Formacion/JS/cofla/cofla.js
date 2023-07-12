	
// Capitulo 2 

// :: Problema A

function fiesta(){
	let free = false;
	const validarCliente = (time) => {
		let edad = prompt("Dime tu edad para entrar a la fiesta");
		if (edad>=18) {
			if (time >= 2 && time < 7 && !free) {
				alert(`Podes pasar gratis porque son las ${time}:00hs`)
				free = true
			} else {
				alert("Son 200 pesos la entrada")
			}
			} else {
				alert("Lo siento, usted es menor de edad")
		
		}
	}

	validarCliente(1)
	validarCliente(2)
	validarCliente(20)
}

// :: Problema B


function lista(){
	let cantidad = prompt("¿cuantos estudiantes son?");
	let alumnosTotales = [];

	for (i = 0; i < cantidad; i++) {
		alumnosTotales[i] = [prompt("Nombre del estudiante " + (i+1)),0]
	}

	const tomarLista = (nombre,p)=>{
		let presencia = prompt(nombre);
		if (presencia == "p" || presencia == "P") {
			alumnosTotales[p][1]++;
		}
	}


	for (i = 0; i < 5; i++) { // aquí va 30
		for (alumno in alumnosTotales) {
			tomarLista(alumnosTotales[alumno][0],alumno); 
		}
	}

	for (alumno in alumnosTotales) {
		let res = `${alumnosTotales[alumno][0]}:<br>
			    Presente: <b>${alumnosTotales[alumno][1]}</b><br>
	   		    Ausente: <b>${5 - alumnosTotales[alumno][1]}</b>`; 
	   		    //aquí va 30
		if (5 - alumnosTotales[alumno][1] > 2) { 
		// aquí va 30
			res += "<b style='color:red'> REPROBADO X INASISTENCIAS</b><br><br>";
		} else {
			res+= "<br><br>"
		}
		document.write(res + '<a href="capitulo-2.html">Volver</a>');
	}
}

// :: Problema C
// LA CALCULADORA

function calculadora1(){
	let resultado = prompt("LA CALCULADORA (problema C):<br>1. sumar, 2. restar, 3. dividir, 4. multiplicar");
	let numero1 = prompt("Primer número");
	let numero2 = prompt("Segundo número");
	if (resultado == 1) {
		let suma = parseInt(numero1) + parseInt(numero2);
		alert( `Su número es: ${suma}`)
	} else if (resultado == 2) {
		let resta = parseInt(numero1) - parseInt(numero2);
		alert(`Su número es: ${resta}`)
	} else if (resultado == 3) {
		let div = parseInt(numero1) / parseInt(numero2);
		alert(`Su número es: ${div}`)
	} else if (resultado == 4){
		let mult = parseInt(numero1) * parseInt(numero2);
		alert(`Su número es: ${mult}`)
	}
}

	// Dalto resolvió de otra manera >
	// const multiplicar = (num1,num2)=> return parseInt(num1) * parseInt(num2);

// Capitulo 4 :: Problema A
// LA CALCULADORA II: Mejorarla

class Calculadora {
	constructor(){
	}
	sumar(num1,num2){
		return parseInt(num1) + parseInt(num2);
	}
	restar(num1,num2){
		return parseInt(num1) - parseInt(num2);
	}
	dividir(num1,num2){
		return parseInt(num1) / parseInt(num2);
	}
	multiplicar(num1,num2){
		return parseInt(num1) * parseInt(num2);
	}
	potenciar(num,exp){
		return num**exp;
	}
	raizCuadrada(num){
		return Math.sqrt(num);
	}
	raizCubica(num){
		return Math.cbrt(num);
	}
}

const calculadora = new Calculadora();


/*
################################################
CAPITULO 5 - 
################################################

problema A: (CALCULADORA 2)
implementar nuevas funciones
*/

// CALCULADORA 2

function calculadora2() {

	let resultado = prompt("1. sumar, 2. restar, 3. dividir, 4. multiplicar, 5. potenciar, 6. Raíz cuadrada, 7. Raíz cúbica");

	if (resultado == 1) {
		let numero1 = prompt("Primer número");
		let numero2 = prompt("Segundo número");
		alert(calculadora.sumar(numero1,numero2));
	} else if (resultado == 2) {
		let numero1 = prompt("Primer número");
		let numero2 = prompt("Segundo número");
		alert(calculadora.restar(numero1,numero2));
	} else if (resultado == 3) {
		let numero1 = prompt("Primer número");
		let numero2 = prompt("Segundo número");
		alert(calculadora.dividir(numero1,numero2));
	} else if (resultado == 4) {
		let numero1 = prompt("Primer número");
		let numero2 = prompt("Segundo número");
		alert(calculadora.multiplicar(numero1,numero2))	
	} else if (resultado == 5) {
		let numero1 = prompt("Base")
		let numero2 = prompt("Exponente")
		alert(calculadora.potenciar(numero1,numero2))
	} else if (resultado == 6) {
		let numero1 = prompt("Escriba un número para saber su raíz cuadrada")
		alert(calculadora.raizCuadrada(numero1))
	} else if (resultado == 7) {
		let numero1 = prompt("Escriba un número para saber su raíz cúbica")
		alert(calculadora.raizCubica(numero1))
	} else {
		alert("Número inválido, intente nuevamente")
	}
}

/*
######################
 PROBLEMA B: materias 
######################

- crear funcion que nos devuelva:
	* profesor
	* nombre de los alumnos
- funcion que nos indique en cuántas clases está cofla
- nombre de esas clases y sus profesorxs
*/


		// Acá usando ARRAY ASOCIATIVO; ni me acordaba.
	function materiasFacultad(){
	}
	const obtenerInformacion = (materia)=>{
		materias = {
			fisica: ["Guido","ricardo","pablo","filippo","jose","magda","rena"],
			programacion: ["Ruiz","ricardo","pablo","filippo","jose","magda","rena","cofla"],
			logica: ["Perez","ricardo","pablo","magda","rena","cofla"],
			algebra: ["Ruiz","filippo","jose","magda","rena","cofla"],
			quimica: ["Solá","ricardo","pablo","filippo","jose","magda","rena","cofla"],
			filosofia: ["Montero","ricardo","pablo","filippo","jose","rena","cofla"],
			matematicas: ["Pino","ricardo",,"filippo","jose","magda","rena","cofla"],
			calculo: ["De Prada","ricardo","pablo"]
		}
		if (materias[materia] !== undefined){
			return [materias[materia],materia,materias];
		} else {
			return materias;
		}
	}

const mostrarInformacion = (materia)=>{

	let informacion = obtenerInformacion(materia);

	if (informacion !== false) {
		let profesor = informacion[0][0];
		alumnos = informacion[0];
		alumnos.shift();
		document.write(`El profesor de <b>${informacion[1]}</b> es: <i style="color:blue">${profesor}</i>.<br> Los estudiantes de <i>${informacion[1]}</i> son: <b style="color:red">${alumnos}</b><br><br><a href="capitulo-4.html">Volver</a>`)
	}
}

const cantidadDeClases = (alumno)=>{
	let informacion = obtenerInformacion();
	let clasesPresentes = [];
	let cantidadTotal = 0;
	for (info in informacion){
		if (informacion[info].includes(alumno)) {
			cantidadTotal++;
			clasesPresentes.push(" " + info);
		}
	}
	document.write(`<b>${alumno}</b> está presente en <b>${cantidadTotal}</b> clases: <i>${clasesPresentes}</i>.`)
}


/*
#############################
 PROBLEMA C: en qué materia?
#############################

- preguntarle a Cofla en qué materia se quiere inscribir
- si ya hay 20 inscriptos, negarle la inscripción
- si hay menos de 20, inscribirlo y añadirlo a la lista de estudiantes
*/


const queMateria = (materia)=>{
	let nom = prompt("Escribe tu nombre")
	let resp = prompt(`${nom} en qué materia te quieres inscribir?: 1. Matemáticas; 2. Física; 3. Química .. Escribe el número:`)
	if (resp == 1){
		
	}
}


	
	let materias = {
			fisica: ["Guido","ricardo","pablo","filippo","jose","magda","rena"],
			programacion: ["Ruiz","ricardo","pablo","filippo","jose","magda","rena","cofla"],
			logica: ["Perez","ricardo","pablo","magda","rena","cofla"],
			algebra: ["Ruiz","filippo","jose","magda","rena","cofla"],
			quimica: ["Solá","ricardo","pablo","filippo","jose","magda","rena","cofla"],
			filosofia: ["Montero","ricardo","pablo","filippo","jose","rena","cofla"],
			matematicas: ["Pino","ricardo",,"filippo","jose","magda","rena","cofla"],
			calculo: ["De Prada","ricardo","pablo"]
	}

	const inscribir = (alumno,materia)=>{
		personas = materias[materia];
		if (personas.length >= 21) {
			document.write(`Lo siento <b>${alumno}</b>, las clases de <b>${materia}</b> ya están llenas.<br>`);
		} else {
			personas.push(alumno);
			if (materia == "fisica") {
				materias = {
					fisica: personas,
					programacion: materias['programacion'],
					logica: materias['logica'],
					algebra: materias['algebra'],
					quimica: materias['quimica'],
					filosofia: materias['filosofia'],
					matematicas: materias['matematicas'],
					calculo: materias['calculo']
				}
			} else if (materia == "programacion") {
				materias = {
					fisica: materias['fisica'],
					programacion: personas,
					logica: materias['logica'],
					algebra: materias['algebra'],
					quimica: materias['quimica'],
					filosofia: materias['filosofia'],
					matematicas: materias['matematicas'],
					calculo: materias['calculo']
				}
			} else if (materia == "logica") {
				materias = {
					fisica: materias['fisica'],
					programacion: materias['programacion'],
					logica: personas,
					algebra: materias['algebra'],
					quimica: materias['quimica'],
					filosofia: materias['filosofia'],
					matematicas: materias['matematicas'],
					calculo: materias['calculo']
				}
			} else if (materia == "algebra") {
				materias = {
					fisica: materias['fisica'],
					programacion: materias['programacion'],
					logica: materias['logica'],
					algebra: personas,
					quimica: materias['quimica'],
					filosofia: materias['filosofia'],
					matematicas: materias['matematicas'],
					calculo: materias['calculo']
				}
			} else if (materia == "quimica") {
				materias = {
					fisica: materias['fisica'],
					programacion: materias['programacion'],
					logica: materias['logica'],
					algebra: materias['algebra'],
					quimica: personas,
					filosofia: materias['filosofia'],
					matematicas: materias['matematicas'],
					calculo: materias['calculo']
				}
			} else if (materia == "filosofia") {
				materias = {
					fisica: materias['fisica'],
					programacion: materias['programacion'],
					logica: materias['logica'],
					algebra: materias['algebra'],
					quimica: materias['quimica'],
					filosofia: personas,
					matematicas: materias['matematicas'],
					calculo: materias['calculo']
				}
			} else if (materia == "matematicas") {
				materias = {
					fisica: materias['fisica'],
					programacion: materias['programacion'],
					logica: materias['logica'],
					algebra: materias['algebra'],
					quimica: materias['quimica'],
					filosofia: materias['filosofia'],
					matematicas: personas,
					calculo: materias['calculo']
				}
			} else if (materia == "calculo") {
				materias = {
					fisica: materias['fisica'],
					programacion: materias['programacion'],
					logica: materias['logica'],
					algebra: materias['algebra'],
					quimica: materias['quimica'],
					filosofia: materias['filosofia'],
					matematicas: materias['matematicas'],
					calculo: personas
				}
			}
			inscriptxs = personas.length -1
			document.write(`¡Felicitaciones <b>${alumno}</b>! Te has inscripto correctamente a <b>${materia}</b>. Ahora hay <b>${inscriptxs}</b> inscriptxs.<br>`)
		}
	}

	inscribir("pedrito","fisica");
	inscribir("juan","fisica");
	inscribir("rosa","fisica");
	inscribir("pedrito","fisica");
	inscribir("juan","fisica");
	inscribir("rosa","fisica");
	inscribir("pedrito","fisica");
	inscribir("juan","fisica");
	inscribir("rosa","fisica");
	inscribir("pedrito","fisica");
	inscribir("juan","fisica");
	inscribir("rosa","fisica");
	inscribir("pedrito","fisica");
	inscribir("juan","fisica");
	inscribir("rosa","fisica");
	inscribir("rosa","fisica");
	inscribir("pedrito","fisica");
	inscribir("juan","fisica");
	inscribir("rosa","fisica");


/*
#########################################################
 			6.	DOM
#########################################################

######################
PROBLEMA A: Las llaves
######################

- indicarle las 20 llave posibles con sus 4 imágenes y cofla debe seleccionar cuál llave usar.
- una vez seleccionada enviar los datos al servidor y que otro programador se encargue

*/






/*

*/
