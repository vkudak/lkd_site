function sp_f1(){
    document.getElementById('spoiler_id').style.display='';
    document.getElementById('show_id').style.display='none';
    }

function sp_f2(){
    document.getElementById('spoiler_id').style.display='none';
    document.getElementById('show_id').style.display='';
    }

function now_time(){
    var currentTime = new Date()
    var hours = currentTime.getHours()
    var minutes = currentTime.getMinutes()
    if (minutes < 10){
        minutes = "0" + minutes
    }
    if (hours < 10){
        hours = "0" + hours
    }
    document.getElementById("ntime").value = hours+":"+minutes;
    }

function get_name(p)
{
    var res=p.split('/').pop();
    document.write( res );
}