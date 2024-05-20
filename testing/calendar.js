document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: [
            {
                title: 'Present',
                start: '2023-05-01',
                color: 'green'
            },
            {
                title: 'Absent',
                start: '2023-05-02',
                color: 'red'
            },
            {
                title: 'Present',
                start: '2023-05-03',
                color: 'green'
            },
            {
                title: 'Absent',
                start: '2023-05-04',
                color: 'red'
            },
            // Add more events here
        ]
    });
    calendar.render();
});
