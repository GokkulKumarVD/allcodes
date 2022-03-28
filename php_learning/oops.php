<?php

class phase1{
    public $name;
    public $email;

    public function __construct($name, $email)
    {
        $this -> name = $name;
        $this -> email = $email;
    }
    

    function trigger(){
        echo $this-> name. " logged in";
    }

    function out(){
        return $this->name;
    }
}

$obj = new phase1('gokul','g@g.com');

$obj -> trigger();

// --------------------------------------------------------

// class phase2{
//     private $name;
//     private $email;

    
//     public function setName($name){
//         $this->name=$name;
//         return $name;
//     }

//     public function getName(){
//         return $this->name;
//     }


// }

// $obj = new phase2();

// $obj -> setName('yosh');
// echo $obj -> getName();


?>





<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>