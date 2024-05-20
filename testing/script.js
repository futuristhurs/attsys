document.addEventListener('DOMContentLoaded', function() {
    const studentForm = document.getElementById('student-login');
    const staffForm = document.getElementById('staff-login');
    const switchToStaff = document.querySelector('.switch');
    const switchToStudent = staffForm.querySelector('.switch');
    const adminButton = staffForm.querySelector('.admin-button');

    switchToStaff.addEventListener('click', function() {
        studentForm.classList.remove('active');
        staffForm.classList.add('active');
    });

    switchToStudent.addEventListener('click', function() {
        staffForm.classList.remove('active');
        studentForm.classList.add('active');
    });

    adminButton.addEventListener('click', function() {
        // Redirect to the Django admin page
        window.location.href = '/admin/';
    });

    studentForm.addEventListener('submit', function(event) {
        event.preventDefault();
        // Perform student login validation and redirection
    });

    staffForm.addEventListener('submit', function(event) {
        event.preventDefault();
        // Perform staff login validation and redirection
    });
});

// script.js

document.addEventListener("DOMContentLoaded", () => {
    const profileMenu = document.getElementById("profile-menu");
    const subMenu = profileMenu.querySelector(".sub-menu");
    const logoutModal = document.getElementById("logout-modal");
    const closeModalButton = document.querySelector(".close-button");
    const confirmLogoutButton = document.getElementById("confirm-logout");
    const cancelLogoutButton = document.getElementById("cancel-logout");

    profileMenu.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent default link behavior
        subMenu.style.display = subMenu.style.display === "block" ? "none" : "block";
    });

    // Close the submenu if clicked outside
    document.addEventListener("click", (event) => {
        if (!profileMenu.contains(event.target)) {
            subMenu.style.display = "none";
        }
    });

    // Show logout modal
    document.getElementById("log-out").addEventListener("click", (event) => {
        event.preventDefault();
        logoutModal.style.display = "flex";
    });

    // Close modal
    closeModalButton.addEventListener("click", () => {
        logoutModal.style.display = "none";
    });

    // Cancel logout
    cancelLogoutButton.addEventListener("click", () => {
        logoutModal.style.display = "none";
    });

    // Confirm logout
    confirmLogoutButton.addEventListener("click", () => {
        // Perform logout action, e.g., redirect or AJAX request
        window.location.href = "login.html"; // Example redirect to a login page
        // Alternatively, you could make an AJAX call to invalidate the session
        // Example:
        // fetch('/logout', { method: 'POST' })
        //     .then(response => {
        //         if (response.ok) {
        //             window.location.href = 'login.html'; // Redirect to login page
        //         }
        //     });
    });

    // Close modal if clicked outside of it
    window.addEventListener("click", (event) => {
        if (event.target === logoutModal) {
            logoutModal.style.display = "none";
        }
    });
});
