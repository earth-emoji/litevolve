$( document ).ready(function() {
    load_rules();

// Submit post on submit
$('#rule-can-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    can_data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        can: $("#can").val()
    };
    patch_rule(can_data, "update-can", "#can-content", "can");
});

$('#rule-cannot-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    cannot_data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        cannot: $("#cannot").val()
    };
    patch_rule(cannot_data, "update-cannot", "#cannot-content", "cannot");
});

$('#rule-explanation-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    explanation_data = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        explanation: $("#explanation").val()
    };
    patch_rule(explanation_data, "update-explanation", "#explanation-content", "explanation");
});
    
});



// Load all rules on page load
function load_rules() {
    var world = $("span[id^=world-]").attr('id').split('-')[1];
    $.ajax({
        url : "/api/worlds/"+world+"/rules/", // the endpoint
        type : "GET", // http method
        // handle a successful response
        success : function(json) {
            for (var i = 0; i < json.length; i++) {
                $("#rule").prepend("<li id='rule-"+json[i].id+"'><strong>"+json[i].name+
                    "</strong> - <a href='/rules/view/"+json[i].id+"'>View</a> | <a id='delete-rule-"+json[i].id+"'>delete me</a></li>");
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
function create_rule() {
    console.log("create rule is working!") // sanity check
    var world = $("span[id^=world-]").attr('id').split('-')[1];
    $.ajax({
        url : "/api/worlds/"+world+"/rules/", // the endpoint
        type : "POST", // http method
        data : { name : $('#name').val()}, // data sent with the post request
        // handle a successful response
        success : function(json) {
            $('#name').val(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#rule-form")[0].reset();
            $("#rule").prepend("<li id='rule-"+json.id+"'><strong>"+json.name+"</strong> - <a href='/rules/view/"+json.id+"'>View</a> | <a id='delete-rule-"+json.id+"'>Delete</a></li>");
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

function patch_rule (data, url, selector, content) {
    var rule = $("span[id^=rule-]").attr('id').split('-')[1];
    $.ajax({
        url: "/api/rules/"+rule+"/"+url+"/",
        type: "PATCH",
        data: data,
        success: function(json) {
            var success = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(success);
            $(selector).html(json[content]);
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            var danger = "<div class='alert alert-danger alert-dismissible fade show' role='alert'>Oops! We have encountered an error: "+errmsg+" <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(danger); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

// AJAX for deleting
function delete_rule(primary_key){
    if (confirm('are you sure you want to remove this rule?')==true){
        $.ajax({
            url : "/api/rules/"+primary_key+"/", // the endpoint
            type : "DELETE", // http method
            data : { pk : primary_key }, // data sent with the delete request
            success : function(json) {
                // hide the rule
              $('#rule-'+primary_key).hide(); // hide the post on success
              console.log("rule deletion successful");
            },

            error : function(xhr,errmsg,err) {
                // Show an error
                $('#results').html("<div class='alert-box alert radius' data-alert>"+
                "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    } else {
        return false;
    }
};


// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

