$( document ).ready(function() {
    //load rules
    load_data("/api/religions/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#religions").prepend("<li id='religion-"+json[i].id+"'><strong>"+json[i].name+
                "</strong> - <a href='/religions/view/"+json[i].id+"'>View</a> | <a id='delete-religion-"+json[i].id+"'>delete me</a></li>");
        }
    });


    // Submit post on submit
    $('#religion-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        var url = "/api/religions/";
        var data = { name : $('#name').val()};
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#religion-form")[0].reset();
            $("#religions").prepend("<li id='religion-"+json.id+"'><strong>"+json.name+"</strong> - <a href='/religions/view/"+json.id+"'>View</a> | <a id='delete-religion-"+json.id+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var religion = $("span[id^=religion-]").attr('id').split('-')[1];

    $('#deities-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-deities/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            deities: $("#deities").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#deities-content").html(json.deities);
        });
    });

    $('#beliefs-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-beliefs/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            beliefs: $("#beliefs").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#beliefs-content").html(json.beliefs);
        });
    });

    $('#prac-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-practices/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            practices: $("#prac").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#prac-content").html(json.practices);
        });
    });

    $('#origins-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-origins/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            origins: $("#origins").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#origins-content").html(json.origins);
        });
    });

    $('#org-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-organization/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            organization: $("#org").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#org-content").html(json.organization);
        });
    });

    $('#hobj-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-holy-objects/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            holy_objects: $("#hobj").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#hobj-content").html(json.holy_objects);
        });
    });

    $('#hdays-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-holidays/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            holidays: $("#hdays").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#hdays-content").html(json.holidays);
        });
    });

    $('#rfigs-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-figures/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            revered_figures: $("#rfigs").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#rfigs-content").html(json.revered_figures);
        });
    });

    $('#extra-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+religion+"/update-extra/";
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
