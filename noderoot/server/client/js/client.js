
$(document).ready(function () {
    $("input").on("touchstart mousedown", function (event) {

        if (event.target.id.length == 2) {
            //add("clickup1");
            var dir;
            if (event.target.id.substring(1, 2) == 'l') {
                dir = 'left';
            } else {
                dir = 'right';
            }
            start(event.target.id.substring(0, 1), dir);
        }

    });
    $("input").on("touchend mouseup", function (event) {
        if (event.target.id.length == 2) {
            //add("clickup1");
            var dir;
            if (event.target.id.substring(1, 2) == 'l') {
                dir = 'left';
            } else {
                dir = 'right';
            }
            stop(event.target.id.substring(0, 1), dir);
        }



    });
    $("input").on("change", function (event) {

        if (event.target.id.length == 3) {
            //add("clickup1");
            var dir;
            if (event.target.id.substring(1, 2) == 'l') {
                dir = 'left';
            } else {
                dir = 'right';
            }
            if (event.target.id.substring(2, 3) == 'g') {
                start(event.target.id.substring(0, 1), dir);
            } else if (event.target.id.substring(2, 3) == 's') {
                stop(event.target.id.substring(0, 1), dir);
            }


        }

    });
});