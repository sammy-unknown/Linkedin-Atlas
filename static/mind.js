console.log('mind.js is loaded')
var fileInput = document.querySelector("input[type='file']");
var dropZone = document.querySelector('body');
var orginalText = dropZone.innerHTML;

dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    dropZone.classList.add('hover');
    document.querySelector('body').style = 'border:5px dashed #fffdfd75;pading:10px;background:#2c3fc8:;opacity: 0.6;'
    document.querySelector('body').innerHTML='<div class="dropzonebxo" style="display: flex;justify-content: center;text-align: center;align-content: center;margin-top: 40vh;flex-direction: column;"><h3 class="text-light">Drop it like it’s hot</h3><p class="text-light">Upload files or folders by dropping them in this window</p></div>'
});

dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    dropZone.classList.remove('hover');
    document.querySelector('body ').innerHTML = orginalText;
    document.querySelector('body').style = 'opacity: 1;'


})

dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    dropZone.classList.remove('hover');
    document.querySelector('body ').innerHTML = orginalText;
    document.querySelector('body').style = 'opacity: 1;'
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
            try {
                var response = JSON.parse(xhr.responseText);
                console.log('File uploaded successfully. Name: ' + response.file_name);
                var fileContainer = document.getElementById('file-container');
                fileContainer.innerHTML = 'File Uploaded: ' + response.file_name;

                // Retrieve the updated data from the server and update the UI
                var xhr2 = new XMLHttpRequest();
                xhr2.open('GET', '/get_data'); // Replace with your Django view URL to retrieve the updated data
                xhr2.onreadystatechange = function() {
                    if (xhr2.readyState === 4 && xhr2.status === 200) {
                        var data = JSON.parse(xhr2.responseText);
                        console.log('Data retrieved successfully.');
                        // Update the UI with the updated data
                        // ...
                    }
                };
                xhr2.send();

            } catch (e) {
                var fileContainer = document.getElementById('file-container');
                fileContainer.innerHTML = 'File uploaded successfully.' ;
            }

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
