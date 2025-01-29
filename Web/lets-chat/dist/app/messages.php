<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

include('db.php');

$stmt = $pdo->prepare("SELECT sender, recipient, message, sent_at FROM messages WHERE recipient = ? ORDER BY sent_at DESC");
$stmt->execute([$_SESSION['user']]);
$messages = $stmt->fetchAll();

echo "Messages for " . $_SESSION['user'] . ":<br>";
foreach ($messages as $message) {
    echo "<strong>From:</strong> " . htmlspecialchars($message['sender']) . "<br>";
    echo "<strong>Message:</strong> " . htmlspecialchars($message['message']) . "<br>";
    echo "<strong>Sent at:</strong> " . $message['sent_at'] . "<br><br>";
}
?>
