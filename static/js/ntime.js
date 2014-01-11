function ft(){
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