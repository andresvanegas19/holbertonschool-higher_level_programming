$(document).ready(() => {
  $('DIV#clear_list').click(() => {
    $('UL.my_list>li').remove();
  });

  $('DIV#remove_item').click(() => {
    $('UL.my_list>li:last-child').remove();
  });

  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });

});
