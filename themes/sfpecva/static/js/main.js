$('#next_event article').each(function() {
    var date = Date.parse($(this).data('date'));
    if (date > Date.now()) {
        $(this).removeClass('d-none');
        return false;
    }
});

$('#paypal-meeting').each(function() {
    var date = Date.parse($(this).data('date'));
    if (date > Date.now()) {
        $(this).removeClass('d-none');
        return false;
    }
})