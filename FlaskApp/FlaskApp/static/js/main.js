// Example JavaScript for handling checkbox actions and status updates

// Function to simulate connection status update
function keepAlive() {
    setTimeout(function() {
        document.getElementById('connection_id').innerText = 'Connected';
    }, 1000);
}

// Function to update motion status
function time() {
    setTimeout(function() {
        document.getElementById('motion_id').innerText = 'Motion Detected';
    }, 2000);
}

// Toggle Fan/AC based on checkbox
function toggleFanAC(checkbox) {
    if (checkbox.checked) {
        alert('Fan/AC is ON');
    } else {
        alert('Fan/AC is OFF');
    }
}

// Toggle Lights based on checkbox
function toggleLight(checkbox) {
    if (checkbox.checked) {
        alert('Lights are ON');
    } else {
        alert('Lights are OFF');
    }
}

// Handle Buzzer Toggle
function handleClick(checkbox) {
    if (checkbox.checked) {
        alert('Buzzer ON');
    } else {
        alert('Buzzer OFF');
    }
}
// Example JavaScript for handling checkbox actions and status updates

// Function to simulate connection status update
function keepAlive() {
    setTimeout(function() {
        document.getElementById('connection_id').innerText = 'Connected';
    }, 1000);
}

// Function to update motion status
function time() {
    setTimeout(function() {
        document.getElementById('motion_id').innerText = 'Motion Detected';
    }, 2000);
}

// Toggle Fan/AC based on checkbox
function toggleFanAC(checkbox) {
    if (checkbox.checked) {
        alert('Fan/AC is ON');
    } else {
        alert('Fan/AC is OFF');
    }
}

// Toggle Lights based on checkbox
function toggleLight(checkbox) {
    if (checkbox.checked) {
        alert('Lights are ON');
    } else {
        alert('Lights are OFF');
    }
}

// Handle Buzzer Toggle
function handleClick(checkbox) {
    if (checkbox.checked) {
        alert('Buzzer ON');
    } else {
        alert('Buzzer OFF');
    }
}
