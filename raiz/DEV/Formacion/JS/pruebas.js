/* 

##################################
ESCRITO ANTES DEL DOM-6 (26/12/22)
##################################



function resta(num1,num2) {
    res = num1 - num2;
    return res;
}

resta(10,5);

function suma(num1,num2) {
    res = num1 + num2;
    return res
}

suma(5,4);
function saludando(nombre) {
    let frase = `Hola ${nombre} como estas`;
    document.write(frase)
}

saludando("jalea"); 


// Esto funciona, pero no logro sacarle la ficha...
let jsonTexto = `{"color":"blanco","km":100000,"esNuevo":false,"rueda":{"marca":"desconocida","estado":"malo"}}`;
let coche = JSON.parse(jsonTexto);
document.write(coche);

let cadena1 = "hola gato espía"

function metodoArray(nombre){
    let comando = '{"cadena1"}'
    let comando2 = JSON.parse(comando)
    document.write(`<b>${nombre}():</b> ` + comando2)
}

metodoArray(".trim()")

*/

/*
const contenedor = document.querySelector(".contenedor");
const item = document.createElement("LI");
const textoDelItem = document.createTextNode("Este es un ítem de la lista");

console.log(textoDelItem);
*/

// document.getElementById("demo").innerHTML = "Hello World!";


