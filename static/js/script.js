window.onload = function() {
    const textboxes = document.querySelectorAll('.draggable');

    textboxes.forEach(textbox => {
        textbox.addEventListener('mousedown', startDragging);
        textbox.addEventListener('keydown', preventLineBreak);
    });

    function startDragging(event) {
        const textbox = event.target;

        let shiftX = event.clientX - textbox.getBoundingClientRect().left;
        let shiftY = event.clientY - textbox.getBoundingClientRect().top;

        textbox.style.position = 'absolute';
        textbox.style.zIndex = 1000;

        moveAt(event.pageX, event.pageY);

        function moveAt(pageX, pageY) {
            textbox.style.left = pageX - shiftX + 'px';
            textbox.style.top = pageY - shiftY + 'px';
        }

        function onMouseMove(event) {
            moveAt(event.pageX, event.pageY);
        }

        document.addEventListener('mousemove', onMouseMove);

        window.onmouseup = function() {
            document.removeEventListener('mousemove', onMouseMove);
            window.onmouseup = null;
        };
    }

    function preventLineBreak(event) {
        if (event.keyCode === 13 && !event.shiftKey) {
            event.preventDefault();
        }
    }
};