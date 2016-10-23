
<?php
date_default_timezone_set("Asia/Bangkok");
$uploaddir = "cover";
$allowed_ext = "pdf";
$max_size = "5000000";
$date = date("Y-m-d");
$time = date("H:i:s");
$check=0;
error_reporting( error_reporting() & ~E_NOTICE );


for($i=1;$ok<=1;$i++){
$number=rand(1,5);

$x_string =  substr("00000".$number,-4,4);


$objScan = scandir("myfiles/".$x_string."/");
foreach ($objScan as $value) {
}

if($value=='..')
$ok=2;
}


$extension = pathinfo($_FILES['file'] ['name']);
$extension = $extension[extension];
$allowed_paths = explode(", ", $allowed_ext);
for($i = 0; $i < count($allowed_paths); $i++) {
if ($allowed_paths [$i] == "$extension") {
    $ok = "1";
}
}


if ($ok == "1")  {
    if($_FILES['file']['size'] > $max_size)
    {
        print "File is too big!";
        exit;
    }

if(is_uploaded_file($_FILES['file']['tmp_name']))
{
move_uploaded_file($_FILES['file']['tmp_name'],'myfiles/'.$x_string."/".$_FILES['file']['name']);
}

$pdfname = 'myfiles/'.$x_string."/".$_FILES['file']['name'];
$pdftext = file_get_contents($pdfname);
$numpage = preg_match_all("/\/Page\W/", $pdftext, $dummy);


$handle = fopen('myfiles/'.$x_string."/".$x_string.".txt", "w");
$count = $numpage;
fwrite($handle, $numpage);
fclose($handle);


echo "<center><img src='2.png'></center>";
echo '<center><font size ="10px"><font color=\"red\"><br>Your has been successfully uploaded!<br></font></font></center>';

echo '<font color=\"green\">File Name : </font>'.$_FILES['file']['name'];
echo '<font color=\"red\"><br>Your Code is : </font>'.$x_string;
echo "<br><font color=\"green\">Date : </font>".$date;
echo "<br><font color=\"green\">Time : </font>".$time;
echo "<br><font color=\"green\">Number of page is :</font>".$count;
} 
else {
echo "<center><img src='3.png'></center>";
echo '<center><font size ="10px"><font color="red"><br>Incorrect file extension!<br></font></font></center>';
}
?>