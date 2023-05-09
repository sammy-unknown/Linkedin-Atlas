console.log('mind.js is loaded')
var fileInput = document.querySelector("input[type='file']");
var dropZone = document.getElementById('drop');
var orginalText = document.querySelector('.upload .upload-files .body p').innerHTML;

dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    dropZone.classList.add('hover');
    document.querySelector('.upload .upload-files .body').style="background:white;transition:all 0.3s ease-in;border-color:white" 
    document.querySelector('.upload .upload-files .body p').style="color:black"
    document.querySelector('#file-container').style="color:black"
    document.querySelector('.body p b').textContent = "Upload your";
});

dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    dropZone.classList.remove('hover');
    document.querySelector('.upload .upload-files .body').style="background:#161212;transition:all 0.3s ease-out;border-color:#161212"
    document.querySelector('#file-container').style="color:white"
    document.querySelector('.body p').innerHTML = orginalText;
    document.querySelector('#drop p').style="color:white" 

})

dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    dropZone.classList.remove('hover');
    document.querySelector('.upload .upload-files .body').style="background:#161212;transition:all 0.3s ease-out;border-color:#161212"
    document.querySelector('#file-container').style="color:white"
    document.querySelector('.body p').innerHTML = orginalText;
    document.querySelector('#drop p').style="color:white" 
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
