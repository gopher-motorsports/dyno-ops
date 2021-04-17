function clicked(event)
{
    if(!confirm('This will update the entry. Are you sure you want to continue?')){
        event.preventDefault()
    }
}


function changeColor(value) {
    if (value) {
        document.getElementById("throttle").style.color = "grey";
        document.getElementById("rpm").style.color= "white";
    }

    else {
        document.getElementById("rpm").style.color= "grey";
        document.getElementById("throttle").style.color= "white";
    }
    
}