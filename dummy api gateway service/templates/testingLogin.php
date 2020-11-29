<?php

require_once 'login-5.php';
$conn = new mysqli($hn,$un,$pw,$db);
if ($conn->connect_error)die(fatal_error());

$username = $password = $email = "";

if(isset($_POST['uname']))
{
  $username = fix_string($_POST['uname']);
  	
}
if(isset($_POST['psw']))
{
  $password = fix_string($_POST['psw']);
  	
}
if(isset($_POST['email']))
{
  $email = fix_string($_POST['email']);	
}

$fail  = validate_username($username);
$fail .= validate_password($password);
$fail .= validate_email($email);


if(isset($_POST['Login']))
{
  if(isset($_SERVER['PHP_AUTH_USER'])&& isset($_SERVER['PHP_AUTH_PW']))
  {
		$un_temp = mysql_entities_fix_string($conn,$_SERVER['PHP_AUTH_USER']);
		$pw_temp = mysql_entities_fix_string($conn,$_SERVER['PHP_AUTH_PW']);
		
		$query = "SELECT * FROM users WHERE username ='".$un_temp."'"; // table - user, query column name - username
		$result = $conn->query($query);
		if(!$result) die(fatal_error());
		elseif($result->num_rows)
		{
			$row = $result->fetch_array(MYSQLI_NUM);
			$result->close();
			$salt1 = $row[2];
			$salt2 = $row[3];
			$token = hash('ripemd128',"$salt1$pw_temp$salt2");
			if($token == $row[1])
			{
				// session
				session_start();
				$_SESSION['username'] = $un_temp;
                                $_SESSION['check'] = hash('ripemd128',$_SERVER['REMOTE_ADDR'].$_SERVER['HTTP_USER_AGENT']);
				echo "You are now logged in";
				die("<p><a href=../notes_service/templates/multiple_upload_form.html>Click here to continue</a></p>");
			}
			else die("Invalid username/password combination");
		}
		else die("Invalid username/password combination");
  }
  else
  {
     header('WWW-Authenticate: Basic realm="Restricted Section"');
     header('HTTP/1.0 401 Unauthorized');
     die("Please enter your username and password");
  }
}

//echo "<!DOCTYPE html>\n<html><head><title>An Example Form</title>";
//echo "<p><a href=adduser.php>Signup complete, Click here to continue</a></p>";

if($fail == "")
{
  //echo "</head><body>Form data successfully validated: $username,$password,$email.</body></html>";

  //enter into data base
  // using hash
  $salts = saltCreator();
  $token1 = hash('ripemd128',$salts[0].$password.$salts[1]);
  $stmt = $conn->prepare('INSERT INTO users VALUES(?,?,?,?,?)');
  $stmt->bind_param('sssss',$username,$token1,$salts[0],$salts[1],$email);
  $stmt->execute();
  $stmt->close();
  echo "<p><a href=../notes_service/templates/multiple_upload_form.html>Signup complete, Click here to continue</a></p>";
  exit;
}

echo <<<_END

<!DOCTYPE html>
<html>
<head>
    <title>SummarAIze</title>
    <!-- <img src = "summarAIze.png" width = "200"/> -->
    <img class="logo-img" src="summarAIze.png" width="200" ALT="align box" ALIGN=CENTER/>
</head>
<meta name = "viewport" content = "width=device-width, initial-scale=1">
<style>

body {font-family:Calibri, sans-serif;}
/* 
html, body {
    height: 100%;
} */

/* html {
    display: table;
    margin: auto;
} */
.logo-img{
    float: left;
    position: relative;
    margin: 0px 20px 0px 20px;
}
/* body{
    display: table;
    margin: auto;
} */


/* Full-width input fields */
input[type = text], input[type = password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

/* Extra styles for the cancel button */
.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

/* Center the image and position the close button */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
  position: relative;
}

img.avatar {
  width: 40%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
  padding-top: 60px;
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 50%; /* Could be more or less, depending on screen size */
}

/* Add Zoom Animation */
.animate {
  -webkit-animation: animatezoom 0.6s;
  animation: animatezoom 0.6s
}

@-webkit-keyframes animatezoom {
  from {-webkit-transform: scale(0)} 
  to {-webkit-transform: scale(1)}
}
  
@keyframes animatezoom {
  from {transform: scale(0)} 
  to {transform: scale(1)}
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}
</style>
<body style = "background-color: #282c34;">

<h2 style="color: seagreen; font-weight:500; font-family:'Trebuchet MS';">welcome to summarAIze</h2>
    
<button onclick = "document.getElementById('id01').style.display = 'block'" style = "width:auto;">Signup</button>

<div id = "id01" class = "modal">
  
  <form class = "modal-content animate" action = "testingLogin.php" method = "POST" onsubmit="return validate(this)">

    <div class = "container">
      <label for = "unamw"><b>Username</b></label>
        <input type = "text" placeholder = "Enter your Username" name = "uname" value="$uname" required>

      <label for = "email"><b>Email ID</b></label>
      <input type = "text" placeholder = "Enter your Email ID" name = "email" value="$email" required>

      <label for = "pwd"><b>Password</b></label>
      <input type = "password" placeholder = "Enter Password" name = "psw" value="$psw" required>
        
      <label>
        <input type = "checkbox" unchecked = "true" name = "remember"> Remember me
      </label>

      <button type = "submit" value="Signup">Signup</button>
    </div>

    <div class = "container" style = "background-color:#f1f1f1">
      <button type = "button" onclick = "document.getElementById('id01').style.display = 'none'" class = "cancelbtn">Cancel</button>
      <span class = "psw">Forgot <a href = "#">password?</a></span>
    </div>
  </form>
</div>

<script>
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
</script>
</body>
</html>

_END;



function validate_username($field)
{
  if($field == "") return "No Username was entered<br>";
  else if (strlen($field)<5)
   return "Username must be at least 5 characters<br>";
  else if(preg_match("/[^a-zA-Z0-9_-]/", $field))
   return "Only letters, numbers, - and _ in username<br>";
 return "";
}

function validate_password($field)
{
  if($field == "") return "No password was entered<br>";
  else if (strlen($field) < 6)
   return"Passwords must be at least 6 characters<br>";
  else if(!preg_match("/[a-z]/", $field) ||
          !preg_match("/[A-Z]/", $field) ||
          !preg_match("/[0-9]/", $field))
   return "Passwords require 1 each of a-z, A-Z, and 0-9<br>";
 return "";
}

function validate_email($field)
{
  if($field == "") return "No email was entered<br>";
  else if (!((strpos($field, ".")>0) &&
             (strpos($field, "@")>0)) ||
              preg_match("/[^a-zA-Z0-9.@_-]/", $field)) 
return "The email address is invalid<br>";
  return "";
}

function fix_string($string)
{
 if(get_magic_quotes_gpc()) $string = stripslashes($string);
 return htmlentities ($string);
}

function mysql_entities_fix_string($conn,$string)
{
	return htmlentities(mysql_fix_string($conn,$string));
}

function mysql_fix_string($conn,$string)
{
	if(get_magic_quotes_gpc())$string = stripslashes($string);
	return $conn->real_escape_string($string);
}

function add_user($conn,$un,$pw,$s1,$s2,$e)
{
	$stmt = $conn->prepare('INSERT INTO users VALUES(?,?,?,?,?)');
	$stmt->bind_param('sssss',$un,$pw,$s1,$s2,$e);
	$stmt->execute();
	$stmt->close();
}

function saltCreator()
{
	$salt = array("qm&h*","pg!@","hell","pink");
	$rand_index1 = mt_rand(0,3);
	$rand_index2 = mt_rand(0,3);
	return array($salt[$rand_index1], $salt[$rand_index2]);
}

function fatal_error()
{	
	echo "Oops, something went wrong (x __ x)";
	echo '<br>';
}


?>
