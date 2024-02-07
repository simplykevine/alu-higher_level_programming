$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: (json) => {
    $('div#hello').text(json);
  }
});
