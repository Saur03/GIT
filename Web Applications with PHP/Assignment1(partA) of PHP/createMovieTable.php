<!DOCTYPE html
<html>
<head>
<title>Create MOVIES Table</title>
</head>
<body>
<?php
// Bootstrap the application by loading required library file
require_once('includes/bootstrap.php');
// Create a database connection object using PDO
$dbc = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME,DB_USER,DB_PASSWORD);
$query="CREATE TABLE `movies`(
`id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
`title` VARCHAR(255), 
`production_company` VARCHAR(255), 
`year_released` TEXT, 
`director` VARCHAR(255)
)";
//run the query using PDO syntax
$result = $dbc->query($query);
if($result) {
	echo "The query was successfully executed!";
} else {
	echo "The query could not be executed! ". $dbc->errorInfo()[2];
}


?>
</body>
</html>
