const commentForm = document.getElementById("form-comment");
commentForm.onsubmit = function (e) {
    const commentBody = commentForm.elements.body.value;
    e.preventDefault();
    fetch(`${window.location.pathname}/create_comment`, {
        method: 'POST', body: JSON.stringify({
            'comment-body': commentBody
        }), headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json()).then(function (jsonResponse) {
        console.log("jsonResponse", jsonResponse);
        const newComment = document.createElement('li');
        const liBody = document.createElement('span');
        const liDate = document.createElement('span');
        const liAuthor = document.createElement('span');

        liBody.className = 'comment comment-body';
        liBody.appendChild(document.createTextNode(jsonResponse["body"]));
        liDate.className = 'comment comment-date';
        liDate.appendChild(document.createTextNode(jsonResponse["last_updated"]));
        liAuthor.className = 'comment comment-author';
        liAuthor.appendChild(document.createTextNode(jsonResponse["author"]));

        [liBody, liDate, liAuthor].forEach(liElement => {
            newComment.appendChild(liElement);
        });

        document.getElementById("comments").prepend(newComment)

    }).catch(function (err) {
        console.log(err)
    });
};
