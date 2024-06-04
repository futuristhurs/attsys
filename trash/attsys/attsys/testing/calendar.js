$(document).ready(function () {
    // Get the current date in YYYY-MM-DD format
    const currentDate = new Date().toISOString().split('T')[0];
  
    $("#calendar").fullCalendar({
      header: {
        left: "prev,next today",    // Navigation buttons
        center: "title",            // Calendar title
        right: "month,basicWeek,basicDay", // View options
      },
      defaultDate: currentDate,     // Use the current date as the default date
      navLinks: true,               // Enable navigation links for days/weeks
      editable: true,               // Allow event editing
      eventLimit: true,             // Limit the number of events shown per day
      events: [                     // Event data
        {
          title: "All Day Event",
          start: "2024-05-01",
        },
        {
          title: "Long Event",
          start: "2024-05-07",
          end: "2024-05-10",
        },
        {
          id: 999,
          title: "Repeating Event",
          start: "2024-05-09T16:00:00",
        },
        {
          id: 999,
          title: "Repeating Event",
          start: "2024-05-16T16:00:00",
        },
        {
          title: "Conference",
          start: "2024-05-11",
          end: "2024-05-13",
        },
        {
          title: "Meeting",
          start: "2024-05-12T10:30:00",
          end: "2024-05-12T12:30:00",
        },
        {
          title: "Lunch",
          start: "2024-05-12T12:00:00",
        },
        {
          title: "Meeting",
          start: "2024-05-12T14:30:00",
        },
        {
          title: "Happy Hour",
          start: "2024-05-12T17:30:00",
        },
        {
          title: "Dinner",
          start: "2024-05-12T20:00:00",
        },
        {
          title: "Birthday Party",
          start: "2024-05-13T07:00:00",
        },
        {
          title: "Click for Google",
          url: "https://google.com/",
          start: "2024-05-28",
        },
      ],
    });
  });
  