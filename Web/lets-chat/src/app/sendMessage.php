<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit();
}

$blacklist = ['echo', 'nc', 'lvnp', 'bash', 'sh', 'script', 'wget'];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $recipient = $_POST['recipient'];
    $message = $_POST['message'];

    include('db.php');

    foreach ($blacklist as $command) {
        if (stripos($recipient, $command) !== false || stripos($message, $command) !== false) {
            die("Invalid input: Command found in input.");
        }
    }

    $stmt = $pdo->prepare("INSERT INTO messages (sender, recipient, message) VALUES (?, ?, ?)");
    $stmt->execute([$_SESSION['user'], $recipient, $message]);

    $messageSent = "echo '$message' | mail -s 'Message from " . $_SESSION['user'] . "' $recipient";
    exec($messageSent);

    echo "Message sent and stored in the database!";
}
?>

<form method="post">
    Recipient: <input type="text" name="recipient"><br>
    Message: <input type="text" name="message"><br>
    <button type="submit">Send Message</button>
</form>
