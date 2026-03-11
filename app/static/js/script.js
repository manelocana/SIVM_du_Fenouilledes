

/* cerrar flash en 3seg */
setTimeout(function() {
    const flashes = document.querySelector('.flash-messages');
    if (flashes) {
        flashes.style.display = 'none';
    }
}, 3000);




/* ckeditor */
document.addEventListener('DOMContentLoaded', () => {

    const editors = document.querySelectorAll('textarea.ckeditor');

    if (editors.length > 0) {

        editors.forEach(textarea => {
            ClassicEditor
                .create(textarea)
                .then(editor => {
                    textarea.editorInstance = editor;
                })
                .catch(error => console.error(error));
        });

        const forms = document.querySelectorAll('form');

        forms.forEach(form => {
            form.addEventListener('submit', () => {

                editors.forEach(textarea => {
                    if (textarea.editorInstance) {
                        textarea.value = textarea.editorInstance.getData();
                    }
                });

            });
        });
    }

});