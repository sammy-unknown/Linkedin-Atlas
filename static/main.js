console.log("main.js is working")
$(function () {

  $('.js-check-all').on('click', function () {

    if ($(this).prop('checked')) {
      $('th input[type="checkbox"]').each(function () {
        $(this).prop('checked', true);
        $(this).closest('tr').addClass('active');
      })
    } else {
      $('th input[type="checkbox"]').each(function () {
        $(this).prop('checked', false);
        $(this).closest('tr').removeClass('active');
      })
    }

  });

  $('th[scope="row"] input[type="checkbox"]').on('click', function () {
    if ($(this).closest('tr').hasClass('active')) {
      $(this).closest('tr').removeClass('active');
    } else {
      $(this).closest('tr').addClass('active');
    }
  });



});

function updateButtonName(event, element) {
  var isChecked = false;

  var emailparnetCell = element.closest('tr')
  var first = emailparnetCell.querySelector('.first').textContent;
  var last = emailparnetCell.querySelector('.last').textContent;
  var emailCell = emailparnetCell.querySelector('.Email');
  document.querySelectorAll('.check-one').forEach((checkbox, num) => {
    if (checkbox.checked) {
      var isChecked = true;
      var newElement = checkbox.closest('tr');
      var newfirst = newElement.querySelector('.first').textContent;
      var newlast = newElement.querySelector('.last').textContent;
      var newEmail = newElement.querySelector('.Email');
      var updateEmail = newElement.querySelector('.updateEmail');
      var item_id = newElement.querySelector('.item_id');
      newEmail.textContent = `${(element.textContent).replace("lastname", newlast).replace("firstname", newfirst).replace("firstinitial", newfirst[0]).replace("lastinitial", newlast[0]).toLowerCase()}@gmail.com`;
      updateEmail.value = `${(element.textContent).replace("lastname", newlast).replace("firstname", newfirst).replace("firstinitial", newfirst[0]).replace("lastinitial", newlast[0]).toLowerCase()}@gmail.com`;
      item_id.value = `${(element.textContent).replace("lastname", newlast).replace("firstname", newfirst).replace("firstinitial", newfirst[0]).replace("lastinitial", newlast[0]).toLowerCase()}@gmail.com`;
    }
  })
  if (isChecked === false) {
    emailCell.textContent = `${(element.textContent).replace("lastname", last).replace("firstname", first).replace("firstname", first).replace("firstinitial", first[0]).replace("lastinitial", last[0]).toLowerCase()}@gmail.com`;

  }
  var newLatestemail = emailparnetCell.querySelector('.Email').textContent;
  console.log("New email address:", newLatestemail);
  console.log(`${emailparnetCell.dataset.itemId}`)
  document.querySelector(`input[name="updatedEmail${emailparnetCell.dataset.itemId}"]`).value = newLatestemail;

  event.preventDefault(); // Prevent default form submission behavior
  var form = document.getElementById("my-form");
  var formData = new FormData(form); // Create form data object
  var xhr = new XMLHttpRequest(); // Create new XMLHttpRequest object
  xhr.open("POST", window.location.href); // Set request method and URL
  xhr.onreadystatechange = function () {
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      // Handle success response
      console.log("Form Submit")

    } else if (this.status >= 400) {
      // Handle error response
      console.log("Form Eror")
    }
  };
  xhr.send(formData); // Send form data object in the request

}