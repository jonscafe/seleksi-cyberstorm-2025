<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    // Check database for credentials
    include('db.php');
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user'] = $user['username'];
        header("Location: index.php");
        exit();
    } else {
        echo "Invalid login credentials.";
    }
}
?>
<head>
    <title>Web CTF Messaging App</title>
    <link rel="stylesheet" href="styles.css">
</head>
<h1>Login</h1>
<form method="post">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <button type="submit">Login</button>
</form>
<a href="register.php">Register</a>
