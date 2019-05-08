$( document ).ready(function() {

    load_data("/api/natural_laws/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#rules").prepend("<div id='rule-"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/natural_laws/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete-rule_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    // Submit post on submit
    $('#rule-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/natural_laws/";
        var data = { 
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#rule-form")[0].reset();
            var content = "<div id='universe-"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/natural_laws/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete-rule-"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#rules").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    // Submit post on submit
    $('#can-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_laws/"+slug+"/update-can/";
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

    $('#cannot-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_laws/"+slug+"/update-cannot/";
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

    $('#explanation-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        var url = "/api/natural_laws/"+slug+"/update-explanation/";
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
