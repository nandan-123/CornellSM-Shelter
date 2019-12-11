$(document).ready(function() {
	getTimetable();
	// console.log(data)
	// data[0].RouteDirections;
	// for (let route of data[0].RouteDirections) {
	// 	$("#serv_info").append("<p>" + route.RouteId + "</p>");
	// }
})


function runClock() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById("date").innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(runClock, 500);
}
