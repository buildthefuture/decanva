<?php
	setlocale(LC_CTYPE, "UTF8", "en_US.UTF-8");
	$search=$_GET['search'];
	echo "raw search received in php:".$search."\n";
	$search = str_replace(' ', '_', $search);
	if (isset($_GET['addition'])) {
		$search = $search.' '.$_GET['addition'];
	}
	echo "modified search in php:".$search."\n";
	//$command = escapeshellcmd("/Users/jianan/Documents/sites/decanva/pythonScripts/search.py ".$search);
	$command = escapeshellcmd(dirname(__FILE__)."/pythonScripts/search.py ".$search);
	echo "execute command:".$command."\n";
	//echo shell_exec("which python");
	//echo shell_exec($command." 2>&1");
	$imgsrc = shell_exec($command." 2>&1");
	echo $imgsrc;
?>