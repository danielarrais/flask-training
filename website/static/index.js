function deleteNote(noteId) {
    fetch(`/${noteId}`, {
        method: "DELETE",
    }).then((response) => {
        window.location.href = "/"
    })
}