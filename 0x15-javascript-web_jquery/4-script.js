$('DIV#toggle_header').click(function() {
  if ($("HEADER").hasClass("red")) {
    $("HEADER").toggleClass( "green");
  } else {
    $("HEADER").toggleClass( "red" );
  }
});
