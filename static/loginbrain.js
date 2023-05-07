var current = null;
document.querySelector('#email').addEventListener('focus', function (e) {
    if (current) current.pause();
    current = anime({
        targets: 'path',
        strokeDashoffset: {
            value: 0,
            duration: 700,
            easing: 'easeOutQuart'
        },
        strokeDasharray: {
            value: '240 1386',
            duration: 700,
            easing: 'easeOutQuart'
        },
        transform: ['translate(0, 0)'],
        value: -730,
    });
    $("#submit")[0].style="color:#707075" 
});
document.querySelector('#password').addEventListener('focus', function (e) {
    if (current) current.pause();
    current = anime({
        targets: 'path',
        strokeDashoffset: {
            value: -336,
            duration: 700,
            easing: 'easeOutQuart'
        },
        strokeDasharray: {
            value: '240 1386',
            duration: 700,
            easing: 'easeOutQuart'
        },
        transform: ['translate(0, 0)'],
        value: -730,
    });
    if (document.activeElement !== this) {
        $("#submit")[0].style.color = '#707075';
        $("#submit")[0].style.opacity = (this.value.length > 0) ? 1 : 0.5;
    } else {
        $("#submit")[0].style.color = '#f2f2f2';
        $("#submit")[0].style.opacity = 1;
    }
});
document.querySelector('#submit').addEventListener('focus', function (e) {
    $("#submit")[0].style.color = '#f2f2f2';

});
