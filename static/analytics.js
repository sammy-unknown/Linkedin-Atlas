
$(function () {

    $('.js-check-all').on('click', function () {

        if ($(this).prop('checked')) {
            document.querySelector('.selectAllkeys').style = 'display: flex;justify-content: center;margin-right: 60px;color:white'

            $('th input[type="checkbox"]').each(function () {
                $(this).prop('checked', true);
                $(this).closest('tr').addClass('active');
            })
        } else {
            document.querySelector('.selectAllkeys').style = 'display: none;'

            $('th input[type="checkbox"]').each(function () {
                $(this).prop('checked', false);
                $(this).closest('tr').removeClass('active');
            })
        }

    });

    $('th[scope="row"] input[type="checkbox"]').on('click', function () {
        if ($(this).closest('tr').hasClass('active')) {
            $(this).closest('tr').removeClass('active');
        } else {
            $(this).closest('tr').addClass('active');
        }
    });



});