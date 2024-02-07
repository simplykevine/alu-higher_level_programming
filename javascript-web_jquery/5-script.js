#!/usr/bin/node
$('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
