<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    
    include('db.php');
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->execute([$username, $password]);
    echo "Registration successful!";
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Register</h1>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <button type="submit">Register</button>
        </form>
        <a href="login.php">Login</a>
    </div>
</body>
</html>
