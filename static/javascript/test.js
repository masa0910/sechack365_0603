// import execSync = require('child_proccess').execSync;
console.log('[ok] test.js');

(() => {
    onload = () => {
        const pages = [...document.getElementsByTagName('div')];
        let nowPage = 0;

        const switchPage = (x, y) => {
            pages[x].style.animation = 'showToHide 400ms ease-in-out forwards';

            if (pages[y] === undefined) {
                pages[y] = null;
            } else {
            pages[y].style.animation = 'hideToShow 400ms ease-in-out forwards';
                nowPage++;
            }

            console.log(`Switched page :: ${x} -> ${y}\n`, pages[x], '->', pages[y]);
        };

        document.addEventListener('keydown', e => {
            if (e.keyCode === 32) {
                switchPage(nowPage, nowPage + 1);
            }
        });

        // usb test
    };
})();
