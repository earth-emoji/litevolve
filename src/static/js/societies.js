$( document ).ready(function() {

  //load data
  load_data("/api/societies/", function(json) {
      for (var i = 0; i < json.length; i++) {
          $("#societies").prepend("<li id='society-"+json[i].slug+"'><strong>"+json[i].name+
              "</strong> - <a href='/societies/view/"+json[i].slug+"'>View</a> | <a id='delete-society-"+json[i].slug+"'>delete me</a></li>");
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
          $("#societies").prepend("<li id='society-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/societies/view/"+json.slug+"'>View</a> | <a id='delete-society-"+json.slug+"'>Delete</a></li>");
          console.log("success"); // another sanity check
      };
      create(url, data, success);
  });

  var slug = $("span[id^=slug_]").attr('id').split('_')[1];

  $('#type-form').on('submit', function(event){
      event.preventDefault();
      console.log("form submitted!")  // sanity check

      var url = "/api/societies/"+slug+"/update-type/";
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

      var url = "/api/societies/"+slug+"/update-gov/";
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

      var url = "/api/societies/"+slug+"/update-leadership/";
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

      var url = "/api/societies/"+slug+"/update-military/";
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

      var url = "/api/societies/"+slug+"/update-social-capital/";
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

      var url = "/api/societies/"+slug+"/update-hierarchy/";
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

      var url = "/api/societies/"+slug+"/update-origin/";
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

      var url = "/api/societies/"+slug+"/update-economy/";
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

      var url = "/api/societies/"+slug+"/update-legal/";
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

      var url = "/api/societies/"+slug+"/update-rivals/";
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

      var url = "/api/societies/"+slug+"/update-extra/";
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
});
