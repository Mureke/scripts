<?php
    try{
        //Do something that might go wrong
    }   
    catch(Exception $e){
         header('https://stackoverflow.com/search?q='.$e->getMessage());
         die();
    }
?>
