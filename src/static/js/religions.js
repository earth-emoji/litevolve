$( document ).ready(function() {
    //load rules
    load_data("/api/religions/", function(json) {
        for (var i = 0; i < json.length; i++) {
    var slug = $("span[id^=slug_]").attr('id').split('_')[1];
            $("#religions").prepend("<li id='religion-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/religions/view/"+json[i].slug+"'>View</a> | <a id='delete-religion-"+json[i].slug+"'>delete me</a></li>");
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
            $("#religions").prepend("<li id='religion-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/religions/view/"+json.slug+"'>View</a> | <a id='delete-religion-"+json.id+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    $('#deities-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/religions/"+slug+"/update-deities/";
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

        var url = "/api/religions/"+slug+"/update-beliefs/";
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

        var url = "/api/religions/"+slug+"/update-practices/";
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

        var url = "/api/religions/"+slug+"/update-origins/";
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

        var url = "/api/religions/"+slug+"/update-organization/";
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

        var url = "/api/religions/"+slug+"/update-holy-objects/";
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

        var url = "/api/religions/"+slug+"/update-holidays/";
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

        var url = "/api/religions/"+slug+"/update-figures/";
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

        var url = "/api/religions/"+slug+"/update-extra/";
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
