const bulmaCalendar = require("bulma-calendar/dist/js/bulma-calendar.min.js")


$(window).on('load', function() {

  var options = {};

  today = new Date();  
  options['startDate'] = today;

  // Initialize all input of date type.
  var calendars = bulmaCalendar.attach('[type="date"]', options);
});
