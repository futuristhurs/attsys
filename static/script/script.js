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
