var fileInput = document.querySelector("input[type='file']");
var dropZone = document.getElementById('drop');

dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    dropZone.classList.add('hover');
});

dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    dropZone.classList.remove('hover');
});

dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    dropZone.classList.remove('hover');

    var files = e.dataTransfer.files;
    handleFiles(files);
});

function handleFiles(files) {
    // Create a new form data object
    var formData = new FormData();
    formData.append('csv_file', files[0]);

    // Send the form data to the server using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload'); // Replace with your Django view URL
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log('File uploaded successfully. Name: ' + response.file_name);

            // Show the file name in the HTML
            var fileContainer = document.getElementById('file-container');
            fileContainer.innerHTML = 'File Uploaded: ' + response.file_name;
        }
    };
    xhr.send(formData);
}

// Show the file input dialog when the 'browse' link is clicked
var triggerFile = document.getElementById("triggerFile");
triggerFile.addEventListener("click", function (e) {
    e.preventDefault();
    fileInput.click();
});

var container = document.getElementById("file-container");

fileInput.addEventListener("change", function () {
    var files = fileInput.files;

    // Create a new form data object
    var formData = new FormData();
    formData.append('csv_file', files[0]);

    // Send the form data to the server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            console.log('File uploaded successfully. Name: ' + response.file_name);

            // Show the file name in the HTML
            var fileContainer = document.querySelector('#file-container');
            fileContainer.innerHTML = 'File Uploaded: ' + response.file_name;
        }
    };
    xhr.send(formData);
});
