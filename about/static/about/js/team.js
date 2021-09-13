// Change button caption on click
 $(function () {
    $('.instructor-card-button').click(function () {
        if ($(this).html() != 'HIDE') {
            $(this).html('HIDE');
        } else {
            $(this).html('CLICK FOR BIO');
        }
    });
});