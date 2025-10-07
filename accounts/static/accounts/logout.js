// Functionality to show/hide the modal and handle redirection
const logoutButton = document.getElementById('logoutButton');
const confirmationModal = document.getElementById('confirmationModal');
const yesButton = document.getElementById('yesButton');
const noButton = document.getElementById('noButton');

function showModal() {
    confirmationModal.style.display = 'flex'; // Show the overlay
}

function hideModal() {
    confirmationModal.style.display = 'none'; // Hide the overlay
}

function handleYes() {
    // THIS is where the Django redirect URL goes
    console.log("Redirecting to Django logout endpoint...");
    window.location.href = '/logout-confirm/';
}

// 1. Show modal when LOGOUT is clicked
logoutButton.addEventListener('click', showModal);

// 2. Hide modal when NO is clicked (stay on page)
noButton.addEventListener('click', hideModal);

// 3. Redirect when YES is clicked
yesButton.addEventListener('click', handleYes);