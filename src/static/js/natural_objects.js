$( document ).ready(function() {
    var nobject = $("span[id^=nobject-]").attr('id').split('-')[1];

    // Submit post on submit
    $('#ap-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_objects/"+nobject+"/update-appearance/";
        //"/api/rules/"+cbody+"/update-can/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            appearance: $("#appearance").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#ap-content").html(json.appearance);
        });
    });

    $('#history-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_objects/"+nobject+"/update-history/";
        //"/api/rules/"+cbody+"/update-can/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            history: $("#history").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#history-content").html(json.history);
        });
    });

    $('#value-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_objects/"+nobject+"/update-value/";
        //"/api/rules/"+cbody+"/update-can/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            value: $("#value").val(),
            value_description: $("#value-desc").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#rank").html(json.value);
            $("#value-content").html(json.value_description);
        });
    });
});

