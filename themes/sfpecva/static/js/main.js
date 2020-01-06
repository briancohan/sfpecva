$('#next_event article').each(function() {
    var date = Date.parse($(this).data('date'));
    if (date > Date.now()) {
        $(this).removeClass('d-none');
        $(this).addClass('border-info');
        return false;
    }
});

$('#paypal-meeting').each(function() {
    var date = Date.parse($(this).data('date'));
    if (date > Date.now()) {
        $(this).removeClass('d-none');
        return false;
    }
});

$('#Meetings article').each(function() {
    var date = Date.parse($(this).data('date'));
    if (date > Date.now()) {
        $(this).addClass('border-info');
    }
});