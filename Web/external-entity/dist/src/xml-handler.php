<?php
function processProfileXML($filePath) {
    $xmlContent = file_get_contents($filePath);

    $dom = new DOMDocument();
    $dom->loadXML($xmlContent, LIBXML_NOENT | LIBXML_DTDLOAD);

    $data = simplexml_import_dom($dom);

    echo "<h2>Profile Details</h2>";
    echo "Name: " . htmlspecialchars($data->name ?? 'Unknown') . "<br>";
    echo "Email: " . htmlspecialchars($data->email ?? 'Unknown') . "<br>";
    echo "Bio: " . htmlspecialchars($data->bio ?? 'No bio provided') . "<br>";
}
