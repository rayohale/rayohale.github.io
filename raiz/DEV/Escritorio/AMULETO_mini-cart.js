


  const amuleto_subtotal = document.getElementById("amuleto_subtotal");

  /* convirtiendo el dato de WOOCOMMERCE con parseFloat()*/
  const amuleto_total = parseFloat(amuleto_subtotal.textContent)*1000;

  /* el VALUE del ENVIO */
  const amuleto_billing = document.getElementById("billing_city");
  const amuleto_billing_city = parseFloat(amuleto_billing.value);
  
  /* 4. calculando la zona */

  /* 5. Sumando zona + pedido */
  const amuleto_final = amuleto_total+500

  /* Funcion para convertir el VALUE en ENVIO */
  

  /* Funcion para el botón ENVIAR */
  function recargar(){
      document.getElementById("amuleto_span_total").innerHTML = amuleto_final;
  }

  function calcularTotal(a, b) {
    var amuleto_envio;
  
    if (a <= 14) {
      amuleto_envio = 10;
    } else {
      if (a <= 25 && a > 14) {
        amuleto_envio = 20;
      } else {
        amuleto_envio = 30;
      }
    }
  
    document.write(amuleto_total + b);
  }