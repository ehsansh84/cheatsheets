# PHP cheatsheet by Ehsan Shirzadi

### Test DB Connection:
```
<?php
$link = mysqli_connect('localhost', 'username', 'password');
if (!$link) {
die('Could not connect: ' . mysqli_error());
}
echo 'Connected successfully';
mysqli_close($link);
?>
```


Email: Ehsan.Shirzadi@Gmail.com
Web: www.ehsanshirzadi.com
