console.log("main.js is working")
$(function () {

  $('.js-check-all').on('click', function () {

    if ($(this).prop('checked')) {
      document.querySelector('.selectAllkeys').style = 'display: flex;text-align: center;justify-content: center;margin: 30px;' 

      $('th input[type="checkbox"]').each(function () {
        $(this).prop('checked', true);
        $(this).closest('tr').addClass('active');
      })
    } else {
      document.querySelector('.selectAllkeys').style = 'display: none;' 

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
  let isChecked = false;

  let emailparnetCell = element.closest('tr')
  let first = emailparnetCell.querySelector('.first').textContent;
  let last = emailparnetCell.querySelector('.last').textContent;
  let emailCell = emailparnetCell.querySelector('.Email');
  let olditem_id = emailparnetCell.querySelector('.item_id');


  let url = emailparnetCell.querySelector('.website').textContent;
  console.log("url:", url);

  let domain = url;
  domain = domain.replace('www.', '');
  domain = domain.replace('https://', '');
  domain = domain.replace('http://', '');
  domain = domain.replace('/', '');
  console.log("domain:", domain);

  document.querySelectorAll('.check-one').forEach((checkbox, num) => {
    if (checkbox.checked) {
      isChecked = true;
      let newElement = checkbox.closest('tr');
      let newfirst = newElement.querySelector('.first').textContent;
      let newlast = newElement.querySelector('.last').textContent;
      let newEmail = newElement.querySelector('.Email');
      let updateEmail = newElement.querySelector('.updateEmail');
      let updatedurl = newElement.querySelector('.website').textContent;
      let domain = updatedurl;
      domain = domain.replace('www.', '');
      domain = domain.replace('https://', '');
      domain = domain.replace('http://', '');
      domain = domain.replace('/', '');
      newEmail.textContent = `${(element.textContent).replace("lastname", newlast).replace("firstname", newfirst).replace("firstinitial", newfirst[0]).replace("lastinitial", newlast[0]).toLowerCase()}@${domain}`;
      updateEmail.value = `${(element.textContent).replace("lastname", newlast).replace("firstname", newfirst).replace("firstinitial", newfirst[0]).replace("lastinitial", newlast[0]).toLowerCase()}@${domain}`;
    }
  })
  if (isChecked === false) {
    emailCell.textContent = `${(element.textContent).replace("lastname", last).replace("firstname", first).replace("firstname", first).replace("firstinitial", first[0]).replace("lastinitial", last[0]).toLowerCase()}@${domain}`;

  }
  document.getElementById("clicked_button").value = element.textContent;
  let newLatestemail = emailparnetCell.querySelector('.Email').textContent;
  console.log("New email address:", newLatestemail, emailparnetCell.dataset.itemId);
  document.querySelector(`input[name="updatedEmail${emailparnetCell.dataset.itemId}"]`).value = newLatestemail;

  event.preventDefault(); // Prevent default form submission behavior
  let form = document.getElementById("my-form");
  let formData = new FormData(form); // Create form data object
  let xhr = new XMLHttpRequest(); // Create new XMLHttpRequest object
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
var checkboxess = document.querySelector('#selectAllcheckbox')
var checkboxInstruct = document.querySelector('.Instruct')
var checkcheckboxes = document.querySelector('.checkcheckboxes')

function ClearSection(element){
  checkcheckboxes.value = "none"
  element.closest('div').outerHTML=`<div type="hidden" class="Instruct hidden my-2" id="selectAllcheckbox" style="display: flex;text-align: center;justify-content: center;">All 10 items are selected <a href="#" id="clearSelection" value=""></a><a href="#" id="selectAllcheckbox" onclick="allselect(this)" class="mx-2" > Select All ${profiles} profiles</a></div>`
  
}
function allselect(elem){
  elem.closest('div').outerHTML= `<div type="hidden" class="Instruct hidden my-2" id="selectAllcheckbox" style="display: flex;text-align: center;justify-content: center;">All <b class="mx-1">${profiles}</b> Profiles are selected. <a href="#" class="mx-1" id="clearSelection" onclick="ClearSection(this)">Clear Selection</div`
  checkcheckboxes.value = "selectAll"
}

