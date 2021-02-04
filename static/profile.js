
function submitProfile(evt) {
  evt.preventDefault();

  const formData = {
    name: $('#name-field').val(),
    age: $('#age-field').val(),
    occupation: $('#occupation-field').val()
  };

  // no api/profile route, just profile route
  $.post('/profile', formData, (response) => {
    $('#profile').append(`
      <li>${response.fullname} the ${response.occupation} is ${response.age}</li>
    `);
  });
}

$("#profile-form").on('submit', submitProfile);