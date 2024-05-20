document.querySelector('#bookingForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    let date = document.querySelector('#date').value;
    let startTime = document.querySelector('#startTime').value;
    let endTime = document.querySelector('#endTime').value;
    let customerName = document.querySelector('#customerName').value;
    let serviceType = document.querySelector('#serviceType').value;

    // Basic validation
    if (!date || !startTime || !endTime || !customerName || !serviceType) {
        alert('Please fill out all fields.');
        return;
    }

    // Create booking object
    let booking = {
        date: date,
        startTime: startTime,
        endTime: endTime,
        customerName: customerName,
        serviceType: serviceType
    };

    // Send booking data to the server
    fetch('https://www.salonsavvyke.buzz/book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(booking)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Appointment booked successfully!');
        } else {
            alert('Failed to book appointment: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while booking the appointment.');
    });
});

// Function to check if the user is logged in
function isUserLoggedIn() {
    return localStorage.getItem('authToken') !== null;
}