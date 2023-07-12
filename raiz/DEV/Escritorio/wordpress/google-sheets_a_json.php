<?php

// config
$ID = "14B1V9085URE25EVFhqboiID3BrdoAJOnB_u_HSaZSMY"; // ID_DOCUMENTO
$WS = "0"; // ID_HOJA_TRABAJO
$URL_TEMPLATE = "https://docs.google.com/spreadsheets/d/{id}/gviz/tq?tqx=out:json&gid={ws}";

$url = str_replace('{id}', $ID, str_replace('{ws', $WS, $URL_TEMPLATE));
$content = file_get_contents($url);
$content = substr($content, 47,-2);
$json = json_decode($content, true); // true regresa un arreglo

print_r($json); 
?>