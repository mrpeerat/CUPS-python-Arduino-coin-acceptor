<head><title>Print Files</title> 
</head>  
<?php

echo "<center><img src='1.jpg'></center>";

echo '<FONT FACE="Ms Sans Serif"> <U><B><center><font size ="10px"><font color="red"><br>Welcome To Printer Website<br></font></font></center></B></U> ';


?>
<a href="how2.php"><FONT FACE="Ms Sans Serif"> <font color="red"><span style="background-color:yellow"><font size ="5px">คลิก! เพื่อดูวิธีใช้งาน</font></span></font></a>

<?php
echo "<img src='4.jpg'>";
echo '<FONT FACE="Ms Sans Serif"> <font size ="5px"><font color=\"red\"><br><br>เลือกไฟล์ที่จะอัพโหลด<br></font></font>';

?>

<form action ="upload2.php" name="upload" method="post" enctype="multipart/form-data" Onchange="check();">
เลือกไฟล์ที่จะอัพโหลด : 
<input type="file" name="file" size="30"> 
<br><input type="submit" value="คลิกที่นี้!" Onmouseover="check();">

</form>
<script> 

 function check()
 {	
	if(/[ก-ฮ]\B/.test(document.upload.file.value))
	{
	alert("ห้ามใช้ชื่อไฟล์ภาษาไทย!!");
	}
 }
 
 </script>
 