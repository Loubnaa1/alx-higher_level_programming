$(document).ready(function() {

    function getAndShowHello() {
        var lang = $('#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/?lang=' + lang;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        });
    }


    $('#btn_translate').click(getAndShowHello);

    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            getAndShowHello();
        }
    });
});
