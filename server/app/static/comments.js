const commentForm = document.getElementById("form-comment");
commentForm.onsubmit = function (e) {
    const commentBody = commentForm.elements.body.value;
    e.preventDefault();
    fetch(`${window.location.pathname}/create-comment`, {
        method: 'POST', body: JSON.stringify({
            'comment-body': commentBody
        }), headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => response.json()).then(function (jsonResponse) {
        console.log("jsonResponse", jsonResponse);
        const newComment = document.createElement('li');
        const liBody = document.createElement('div');
        const liDate = document.createElement('span');
        const liAuthor = document.createElement('span');
        const liImg = document.createElement('img');
        const liAuthorA = document.createElement('a');

        newComment.className = "comment";
        liImg.className = 'comment-img';
        liImg.src = jsonResponse["img"];
        liBody.className = 'comment-body';
        liBody.appendChild(document.createTextNode(jsonResponse["body"]));
        liDate.className = 'comment-date';
        console.log(jsonResponse["last_updated"]);
        liDate.appendChild(document.createTextNode(jsonResponse["last_updated"]));
        liAuthor.className = 'comment-author';
        liAuthorA.appendChild(document.createTextNode(jsonResponse["author"]));
        liAuthor.appendChild(liAuthorA);

        [liImg, liAuthor, liDate, liBody].forEach(liElement => {
            newComment.appendChild(liElement);
        });

        document.getElementById("comments").prepend(newComment)

    }).catch(function (err) {
        console.log(err)
    });
};
