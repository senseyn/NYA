const btn = document.getElementById('spin-button');

btn.addEventListener('click', () => {
    document.body.classList.add('rotating');

    setTimeout(() => {
        document.body.classList.remove('rotating');
    }, 10000);
});