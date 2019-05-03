$( document ).ready(function() {
    var rule = $("span[id^=rule-]").attr('id').split('-')[1];

    // Submit post on submit
    $('#rule-can-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_laws/"+rule+"/update-can/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            can: $("#can").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#can-content").html(json.can);
        });
    });

    $('#rule-cannot-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_laws/"+rule+"/update-cannot/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            cannot: $("#cannot").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#cannot-content").html(json.cannot);
        });
    });

    $('#rule-explanation-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        var url = "/api/natural_laws/"+rule+"/update-explanation/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            explanation: $("#explanation").val()
        };
        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#explanation-content").html(json.explanation);
        });
    });

});
