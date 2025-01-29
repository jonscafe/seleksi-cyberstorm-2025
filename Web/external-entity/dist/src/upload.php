<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $fileTmpPath = $_FILES['file']['tmp_name'];
    $fileType = mime_content_type($fileTmpPath);

    if ($fileType !== 'text/xml' && $fileType !== 'application/xml') {
        die("Invalid file type. Please upload an XML file.");
    }

    require_once 'xml-handler.php';
    processProfileXML($fileTmpPath);
} else {
    die("Invalid request.");
}
