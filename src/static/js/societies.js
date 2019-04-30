$( document ).ready(function() {

  //load data
  load_data("/api/societies/", function(json) {
      for (var i = 0; i < json.length; i++) {
          $("#societies").prepend("<li id='society-"+json[i].id+"'><strong>"+json[i].name+
              "</strong> - <a href='/societies/view/"+json[i].id+"'>View</a> | <a id='delete-society-"+json[i].id+"'>delete me</a></li>");
      }
  });


  // Submit data
  $('#society-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check
      var url = "/api/societies/";
      var data = { name : $('#name').val()};
      var success = function(json) {
          console.log(json); // log the returned json to the console
          $("#society-form")[0].reset();
          $("#societies").prepend("<li id='society-"+json.id+"'><strong>"+json.name+"</strong> - <a href='/societies/view/"+json.id+"'>View</a> | <a id='delete-society-"+json.id+"'>Delete</a></li>");
          console.log("success"); // another sanity check
      };
      create(url, data, success);
  });

  var society = $("span[id^=society-]").attr('id').split('-')[1];

  $('#type-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-type/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          type: $("#stype").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#type-content").html(json.type);
      });
  });

  $('#gov-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-gov/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          government: $("#gov").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#gov-content").html(json.government);
      });
  });

  $('#lead-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-leadership/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          leadership: $("#lead").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#lead-content").html(json.leadership);
      });
  });

  $('#mil-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-military/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          military: $("#mil").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#mil-content").html(json.military);
      });
  });

  $('#sc-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-social-capital/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          social_capital: $("#scap").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#sc-content").html(json.social_capital);
      });
  });

  $('#hier-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-hierarchy/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          hierarchy: $("#hier").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#hier-content").html(json.hierarchy);
      });
  });

  $('#origin-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-origin/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          origin: $("#origin").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#origin-content").html(json.origin);
      });
  });

  $('#econ-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-economy/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          economy: $("#econ").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#econ-content").html(json.economy);
      });
  });

  $('#legal-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-legal/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          legal: $("#legal").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#legal-content").html(json.legal);
      });
  });

  $('#rivals-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-rivals/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          rivals: $("#rivals").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#rivals-content").html(json.rivals);
      });
  });

  $('#extra-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+society+"/update-extra/";
      var data = {
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          extra: $("#extra").val()
      };

      patch(url, data, function(json) {
          var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
          $('#results').html(successful);
          $("#extra-content").html(json.extra);
      });
  });

  // Delete post on click
  $("#rule").on('click', 'a[id^=delete-rule-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check

        var url = "/api/rules/"+primary_key+"/";
        var data = { pk : primary_key };
        var success =  function(json) {
            // hide the rule
          $('#rule-'+primary_key).hide(); // hide the post on success
          console.log("rule deletion successful");
        };

        remove(url, data, success);
    });
});
