document.onreadystatechange = function () {
    if (document.readyState === "complete") {
        var cssLoaded = false;
        var stylesheets = document.styleSheets;
        for (var i = 0; i < stylesheets.length; i++) {
            if (stylesheets[i].href && stylesheets[i].href.includes('style.css')) {
                cssLoaded = true;
                break;
            }
        }
        if (cssLoaded) {
            document.body.style.visibility = 'visible';
        } else {
            setTimeout(checkCSS, 50);
        }
    }
};
