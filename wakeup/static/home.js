var detect = function() {
    $.get('/detect')
        .done(function(data){
            if(data == '1') {
                $('#status-info').text('On');
                $('#wake-btn').addClass('disabled');
                $('#sleep-btn').removeClass('disabled');
            } else {
                $('#status-info').text('N/A');
                $('#wake-btn').removeClass('disabled');
                $('#sleep-btn').addClass('disabled');
            }
        });
};

var sleep = function() {
    $.get('/sleep')
        .done(function(data){
            if(data=='1')
                alert('Slept!');
            else
                alert('Sleep Failed!');
        });
};

var wake = function() {
    $.get('/wake')
        .done(function(data){
            if(data=='1')
                alert('Waked!');
            else
                alert('Wake Failed!');
        });
};

$(document).ready(function(){
    detect();
    $('#wake-btn').click(wake).removeClass('disabled');
    $('#sleep-btn').click(sleep).addClass('disabled');
    setInterval(detect, 3000);
});

