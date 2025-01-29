<?php
$host = 'db';
$db = 'messaging_db';
$user = 'root';
$pass = 'root';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$pdo = new PDO($dsn, $user, $pass);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
?>
