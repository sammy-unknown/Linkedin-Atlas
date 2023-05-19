console.log("SearchJs is started")
function Search() {
  console.log("Search button is clicked")
  $('#crunchbase').submit(function (event) {
    event.preventDefault();  // Prevent form from submitting normally
    var formData = $(this).serialize();
    $.post($(this).attr('action'), formData, function (response) {
      console.log(response);
    });
  });
};