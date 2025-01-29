<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Messaging App</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Welcome, <?= htmlspecialchars($_SESSION['user']); ?>!</h1>
        <a href="sendMessage.php">Send Message</a>
        <a href="messages.php">View Messages</a>
        <a href="logout.php">Logout</a>
    </div>
</body>
</html>
