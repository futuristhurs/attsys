// Function to fetch user activity data from the server
function fetchUserActivity() {
    // Dummy data for demonstration
    const userActivityData = [
        { day: 'Monday', active: 4, break: 2, inactive: 1 },
        { day: 'Tuesday', active: 5, break: 3, inactive: 1 },
        { day: 'Wednesday', active: 6, break: 1, inactive: 2 },
        { day: 'Thursday', active: 3, break: 2, inactive: 2 },
        { day: 'Friday', active: 7, break: 1, inactive: 1 },
        { day: 'Saturday', active: 2, break: 3, inactive: 4 },
        { day: 'Sunday', active: 1, break: 1, inactive: 6 }
    ];

    // Call function to update the bar chart with the fetched data
    updateActivityChart(userActivityData);
}

// Function to update the bar chart with user activity data
function updateActivityChart(activityData) {
    // Extract data for each activity mode
    const daysOfWeek = activityData.map(entry => entry.day);
    const activeData = activityData.map(entry => entry.active);
    const breakData = activityData.map(entry => entry.break);
    const inactiveData = activityData.map(entry => entry.inactive);

    // Use Chart.js to create/update the bar chart
    const ctx = document.getElementById('activity-chart').getContext('2d');
    const activityChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: daysOfWeek,
            datasets: [
                {
                    label: 'Active',
                    data: activeData,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Break',
                    data: breakData,
                    backgroundColor: 'rgba(255, 206, 86, 0.5)',
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Inactive',
                    data: inactiveData,
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Fetch user activity data when the page is loaded
document.addEventListener('DOMContentLoaded', function() {
    fetchUserActivity();
});
