<html>

<?php
    // Connect to MySQL
    // include("dbconnect.php");

    // Prepare the SQL statement
    //"http://puzh.xyz/add_data.php?tokenID=0408&val=1";
    //http://drone-ads.com/app/drone.php?control=1&lat=37.7761859&long=-122.3887722

    // Execute SQL statement
    // $SQL = "INSERT INTO dron_db (control, lat, long) VALUES ('".$_GET["control"]."', '".$_GET["lat"]."', '".$_GET["long"]."')";
     // mysql_query($SQL);

    // Go to the review_data.php (optional)
     echo "Command Received: ";
     echo ($_GET["control"]);
     echo (" latitude: ");
     	echo ($_GET["lat"]);
     echo (" longitude: ");
     	echo ($_GET["long"]);
    // header("Location: dashboard.php");
?>	


</html>
