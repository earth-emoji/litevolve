var world = $("span[id^=world-]").attr('id').split('-')[1];

// Load all rules on page load
function load_histories() {
    //
    $.ajax({
        url : "/api/worlds/"+world+"/histories/", // the endpoint
        type : "GET", // http method
        // handle a successful response
        success : function(json) {
            for (var i = 0; i < json.length; i++) {
                var history = "<li class='event' data-date='" + json[i].year +"'>\
                    <h3>"+ json[i].name +"</h3>\
                    <p>" + json[i].description +"</p>\
                </li>";

                $("#history").prepend(history);
            }
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// AJAX for posting
function create_history() {
    console.log("create history is working!") // sanity check
    //var world = $("span[id^=world-]").attr('id').split('-')[1];
    $.ajax({
        url : "/api/worlds/"+world+"/histories/", // the endpoint
        type : "POST", // http method
        data : { 
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            name: $('#history_name').val(), 
            year: $('#year').val(),
            description: $('#description').val(),

        }, // data sent with the post request
        // handle a successful response
        success : function(json) {
            //$('#name').val();  remove the value from the input
            console.log(json); // log the returned json to the console
            $("#history-form")[0].reset();
            var history = "<li class='event' data-date='" + json.year +"'>\
                    <h3>"+ json.name +"</h3>\
                    <p>" + json.description +"</p>\
                </li>";

            $("#history").append(history);
            console.log("success"); // another sanity check
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$( document ).ready(function() {
    load_histories();

    // Submit post on submit
    $('#rule-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_rule();
    });

    $('#history-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_history();
    });

    // Delete post on click
    $("#rule").on('click', 'a[id^=delete-rule-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check
        delete_rule(primary_key);
    });

});