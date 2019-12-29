$('#next_event article').each(function() {
    var date = Date.parse($(this).data('date'));
    console.log(date);
    if (date > Date.now()) {
        $(this).removeClass('d-none');
        return false;
    }
});