// icons taken from https://icons.getbootstrap.com/

var SMALL_DOWN_CARET = `
  <svg class="bi bi-caret-down-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
    <path d="M7.247 11.14L2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/>
  </svg>
`;

var SMALL_UP_CARET = `
  <svg class="bi bi-caret-up-fill" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
    <path d="M7.247 4.86l-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z"/>
  </svg>
`;

function setShownIcon(){
  $( this ).parent()
    .find(".btn-collapse")
    .html(SMALL_UP_CARET);
}

function setHiddenIcon(){
  $( this ).parent()
    .find(".btn-collapse")
    .html(SMALL_DOWN_CARET);
}

$( ".collapse" ).on('shown.bs.collapse', setShownIcon);
$( ".collapse" ).on('hidden.bs.collapse', setHiddenIcon);
