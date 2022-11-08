console.log("Hello")
let text_max = 500;
let initial_length = $('#countTextArea').val().length;
$('#charCount').html(' Character count - ' + initial_length + ' / ' + text_max );
$('#countTextArea').attr('maxLength', '500');

$('#countTextArea').keyup(function() {
let text_length = $('#countTextArea').val().length;
let text_remaining = text_max - text_length;

$('#charCount').html(' Character count - ' + text_length + ' / ' + text_max);

});