<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile Import Tool</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Profile Import Tool</h1>
        <p>Use this tool to upload your user profile for quick setup.</p>
        <form action="upload.php" method="post" enctype="multipart/form-data">
            <label for="file">Upload your profile:</label>
            <input type="file" name="file" id="file" accept=".xml" required>
            <button type="submit">Upload</button>
        </form>
    </div>
</body>
</html>
