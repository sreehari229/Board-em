console.log("Hello")
let text_max = 500;
$('#charCount').html('0 / ' + text_max );
$('#countTextArea').attr('maxLength', '500');

$('#countTextArea').keyup(function() {
let text_length = $('#countTextArea').val().length;
let text_remaining = text_max - text_length;

$('#charCount').html(text_length + ' / ' + text_max);

});