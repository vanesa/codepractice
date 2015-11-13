function addLinks () {
	for (var i=0, link; i<5; i++) {
		link = document.createElement("a");
		link.innerHTML = "Link " + i;
		link.onclick = function (num) {
			return function () {
				alert(num);
			};
		}(i);
		document.body.appendChild(link);
	}
}
window.onload = addLinks;