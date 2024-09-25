var count = 0;
var output = document.getElementById('output');

function Click(){
    count = count + 1;
    output.innerHTML = count;
}

const box = document.getElementById('box');

function handleRadioClick() {
  if (document.getElementById('show').checked) {
    box.style.visibility = 'visible';
  } else {
    box.style.visibility = 'hidden';
  }
}

const radioButtons = document.querySelectorAll('input[name="select"]');
radioButtons.forEach(radio => {
  radio.addEventListener('click', handleRadioClick);
});

//collapsible

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}
