// from w3school

function copyLink() {
  var copyText = document.getElementById('links');
  copyText.select();
  copyText.setSelectionRange(0, 1000)
  document.execCommand("copy");
  alert("Copied link: " + copyText.value);
}