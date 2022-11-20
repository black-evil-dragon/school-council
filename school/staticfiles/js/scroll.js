const timeline = document.querySelector('.widget__wrapper')
const widgets = document.querySelectorAll('.widget__content')

if (timeline) {
    timeline.onmousedown = () => {
        let pageX = 0;

        document.onmousemove = e => {
            if (pageX !== 0) {
                timeline.scrollLeft = timeline.scrollLeft + (pageX - e.pageX);
            }
            pageX = e.pageX;
        };

        timeline.onmouseup = () => {
            document.onmousemove = null;
            timeline.onmouseup = null;
        };

        timeline.ondragstart = () => {
            return false;
        };
    };
}
