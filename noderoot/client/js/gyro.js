

var delay = 250;
var alpha = 0;
var beta = 0;
var gamma = 0;

var alphaSend = 0;
var betaSend = 0;
var gammaSend = 0;



var minRect = 10;
var maxRect = 45;


var canvas = document.getElementById('myCanvas');
var context = canvas.getContext('2d');
var centerX = canvas.width / 2;
var centerY = canvas.height / 2;
var radius = 7;

var scale = 2;



if (window.DeviceMotionEvent == undefined) {
    document.getElementById("no").style.display = "block";
    document.getElementById("yes").style.display = "none";
}
else {


    window.ondeviceorientation = function (event) {
        alpha = Math.round(event.alpha);
        beta = Math.round(event.beta);
        gamma = Math.round(event.gamma);
    }

    function d2h(d) { return d.toString(16); }
    function h2d(h) { return parseInt(h, 16); }

    function makecolor(a, b, c) {
        red = Math.abs(a) % 255;
        green = Math.abs(b) % 255;
        blue = Math.abs(c) % 255;
        return "#" + d2h(red) + d2h(green) + d2h(blue);
    }


    setInterval(function () {

        document.getElementById("alphalabel").innerHTML = "Alpha: " + alpha;
        document.getElementById("betalabel").innerHTML = "Beta: " + beta;
        document.getElementById("gammalabel").innerHTML = "Gamma: " + gamma;


        document.getElementById("gyrocolor").innerHTML = "Color: " + makecolor(alpha, beta, gamma);
        document.getElementById("gyrocolor").style.background = makecolor(alpha, beta, gamma);
        document.getElementById("gyrocolor").style.color = "#FFFFFF";
        document.getElementById("gyrocolor").style.fontWeight = "bold";

        //clear canvase
        context.clearRect(0, 0, canvas.width, canvas.height);

        //facenkreuz
        context.beginPath();
        context.moveTo(0, centerY);
        context.lineTo(canvas.width, centerY);
        context.strokeStyle = '#CACACA'; //'green';
        context.stroke();

        context.beginPath();
        context.moveTo(centerX, 0);
        context.lineTo(centerX, canvas.height);
        context.strokeStyle = '#CACACA'; //'green';
        context.stroke();

        //rect min

        context.beginPath();
        context.rect(centerX - minRect * scale, centerY - minRect * scale, minRect * 2 * scale, minRect * 2 * scale);
        context.lineWidth = 1;
        context.strokeStyle = '#CACACA'; //'green';
        context.stroke();

        //rect max

        context.beginPath();
        context.rect(centerX - maxRect * scale, centerY - maxRect * scale, maxRect * 2 * scale, maxRect * 2 * scale);
        context.lineWidth = 1;
        context.strokeStyle = '#CACACA'; //'green';
        context.stroke();

        //ball
        var gammaCap = limit(gamma, maxRect);
        var betaCap = limit(beta, maxRect);

        gammaCap = mindestens(gammaCap, minRect);
        betaCap = mindestens(betaCap, minRect);

        context.beginPath();
        context.arc(centerX + gammaCap * scale, centerY + betaCap * scale, radius * scale, 0, 2 * Math.PI);
        context.fillStyle = makecolor(alpha, beta, gamma); //'green';
        context.fill();

        //document.bgColor = makecolor(alpha, beta, gamma);
        //gammaCap = 24;




        if (alpha != alphaSend || beta != betaSend || gamma != gammaSend) {

            var dir;
            if (gammaCap > 0) {
                dir = 'left';
            } else {
                dir = 'right';
            }
            var speed = Math.abs((1.0 * gammaCap / maxRect));
            start(2, dir, speed);

            alphaSend = alpha;
            betaSend = beta;
            gammaSend = gamma;
        }


    }, delay);
}
function limit(val, cap) {
    if (val > cap) {
        return cap;
    }
    if (val < (-cap)) {
        return -cap;
    }
    return val;

}

function mindestens(val, cap) {
    if (val >= cap) {
        return val;
    }
    if (val <= (-cap)) {
        return val;
    }
    return 0;

}
