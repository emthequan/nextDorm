function newPost(){
	
	comment = document.getElementById("input").value;
	console.log(comment);
	var p = document.getElementById("addStuff");
    var newElement = document.createElement("div");
    newElement.setAttribute('class', "post-subtitle");
    newElement.innerHTML = comment;
    p.appendChild(newElement);

    var newButton = document.createElement("button");
    newButton.setAttribute('class', "post-subtitle");
    newButton.setAttribute('class', "btn-secondary");

    newButton.innerHTML = "Respond";
    p.appendChild(newButton);
}