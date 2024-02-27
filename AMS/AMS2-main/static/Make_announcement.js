function submitAnnouncement() {
    const announcementText = document.getElementById('announcementText').value.trim();
    if (announcementText !== "") {
        // Create a new FormData object
        const formData = new FormData();
        // Append the announcement text to the form data
        formData.append('text', announcementText);
        
        // Send a POST request to the Flask server
        fetch('/submit_announcement', {
            method: 'POST',
            body: formData // Pass the form data as the body of the request
        })
        .then(response => {
            if (response.ok) {
                // If the response is successful, clear the text area
                document.getElementById('announcementText').value = '';
                return response.text();
            } else {
                throw new Error('Failed to submit announcement');
            }
        })
        .then(data => {
            console.log(data); // Log the response data
            // Optionally, do something with the response data
        })
        .catch(error => {
            console.error(error); // Log any errors
            alert('Failed to submit announcement. Please try again later.');
        });
    } else {
        alert('Please write an announcement before submitting.');
    }
}
