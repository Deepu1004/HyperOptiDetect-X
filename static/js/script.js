// Preview file before upload
document.getElementById('fileInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const previewImage = document.getElementById('previewImage');
            const previewVideo = document.getElementById('previewVideo');
            const isVideoFile = file.type.startsWith('video');

            if (isVideoFile) {
                previewImage.style.display = 'none';
                previewVideo.style.display = 'block';
                previewVideo.src = e.target.result;
            } else {
                previewImage.style.display = 'block';
                previewVideo.style.display = 'none';
                previewImage.src = e.target.result;
            }
        }
        reader.readAsDataURL(file);
    }
});

// Detect objects
document.getElementById('detectButton').addEventListener('click', function() {
    const form = document.getElementById('uploadForm');
    const formData = new FormData(form);

    // Show loading screen
    const loadingScreen = document.getElementById('loadingScreen');
    const loadingText = document.getElementById('loadingText');
    const timerElement = document.getElementById('timer');
    let timer = 0;
    let interval;

    loadingScreen.style.display = 'flex';
    interval = setInterval(() => {
        timer++;
        timerElement.textContent = `${timer}s`;
    }, 1000);

    fetch('/detect', { 
        method: 'POST', 
        body: formData 
    })
    .then(response => response.json())
    .then(data => {
        clearInterval(interval); // Stop the timer
        loadingScreen.style.display = 'none'; // Hide loading screen

        if (data.error) {
            alert(data.error);
        } else {
            // Display processing time
            const processingTime = document.getElementById('processingTime');
            const timeTaken = document.getElementById('timeTaken');
            processingTime.style.display = 'block';
            timeTaken.textContent = `${data.time}s`;

            // Display results
            const resultImage = document.getElementById('resultImage');
            const downloadLink = document.getElementById('downloadLink');

            if (data.type === "image") {
                resultImage.src = data.output_file;
                resultImage.style.display = 'block';
                downloadLink.style.display = 'none';
            } else if (data.type === "video") {
                resultImage.style.display = 'none';
                downloadLink.href = data.output_file;
                downloadLink.style.display = 'inline-block';
            }

            alert(`Processing completed in ${data.time} seconds.`);
        }
    })
    .catch(error => {
        clearInterval(interval); // Stop the timer
        loadingScreen.style.display = 'none'; // Hide loading screen
        alert('Error processing request');
    });
});