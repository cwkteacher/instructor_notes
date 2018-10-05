$(function(){
    
    for (var i=0; i<16; i++){
        $("#container").append("<div class='square'></div>")
    }

    setInterval(update, 1000);
    
    function update(){
        $(".square").each(function(index, element){
            $(element).css("background-color", randomColor())
        });
    } 
    
    function randomColor(){
        return "rgb("+rcv()+","+rcv()+","+rcv()+")";
    
    }
    
    function rcv(){
        return Math.floor(Math.random()*256);
    }
});