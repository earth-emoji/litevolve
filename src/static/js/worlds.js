$( document ).ready(function() {
    var world = $("span[id^=world-]").attr('id').split('-')[1];

    //load rules
    load_data("/api/worlds/"+world+"/natural_laws/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#rule").prepend("<li id='rule-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/natural_laws/view/"+json[i].slug+"'>View</a> | <a id='delete-rule-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load celestial bodies
    load_data( "/api/worlds/"+world+"/celestial_bodies/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#cbodies").prepend("<li id='cbody-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/celestial_bodies/view/"+json[i].slug+"'>View</a> | <a id='delete-cbody-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load natural phenomenas
    load_data( "/api/worlds/"+world+"/natural_phenomenas/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#nphenoms").prepend("<li id='cbody-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/natural_phenomenas/view/"+json[i].slug+"'>View</a> | <a id='delete-nphenom-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load seasons
    load_data( "/api/worlds/"+world+"/seasons/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#seasons").prepend("<li id='season-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/seasons/view/"+json[i].slug+"'>View</a> | <a id='delete-season-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load natural objects
    load_data( "/api/worlds/"+world+"/natural_objects/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#nobjects").prepend("<li id='nobject-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/natural_objects/view/"+json[i].slug+"'>View</a> | <a id='delete-nobject-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load species
    load_data( "/api/worlds/"+world+"/species/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#species").prepend("<li id='nobject-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/species/view/"+json[i].slug+"'>View</a> | <a id='delete-species-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load places
    load_data( "/api/worlds/"+world+"/places/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#places").prepend("<li id='place-"+json[i].slug+"'><strong>"+json[i].name+
                "</strong> - <a href='/places/view/"+json[i].slug+"'>View</a> | <a id='delete-places-"+json[i].slug+"'>delete me</a></li>");
        }
    });

    // load histories
    load_data("/api/worlds/"+world+"/histories/", function(json) {
        for (var i = 0; i < json.length; i++) {
            var history = "<li class='event' data-date='" + json[i].year +"'>\
                <h3>"+ json[i].name +"</h3>\
                <p>" + json[i].description +"</p>\
            </li>";

            $("#history").prepend(history);
        }
    });

    // Submit post on submit
    $('#rule-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        var url = "/api/worlds/"+world+"/natural_laws/";
        var data = { name : $('#rname').val()};
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#rule-form")[0].reset();
            $("#rule").prepend("<li id='rule-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/rules/view/"+json.slug+"'>View</a> | <a id='delete-rule-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    $('#history-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_history();
        var url = "/api/worlds/"+world+"/histories/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            name: $('#history_name').val(),
            year: $('#year').val(),
            description: $('#description').val(),
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#history-form")[0].reset();
            var history = "<li class='event' data-date='" + json.year +"'>\
                    <h3>"+ json.name +"</h3>\
                    <p>" + json.description +"</p>\
                </li>";

            $("#history").append(history);
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    $('#cbody-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_celestial_body();
        var url = "/api/worlds/"+world+"/celestial_bodies/";
        var data = { name : $('#cbname').val()};
        var success = function(json) {
            $('#cbname').val(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#cbody-form")[0].reset();
            $("#cbodies").prepend("<li id='cbody-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/celestial_bodies/view/"+json.slug+"'>View</a> | <a id='delete-cbody-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    $('#nphenom-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_celestial_body();
        var url = "/api/worlds/"+world+"/natural_phenomenas/";
        var data = { name : $('#npname').val()};
        var success = function(json) {
            $('#npname').val(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#nphenom-form")[0].reset();
            $("#nphenoms").prepend("<li id='nphenom-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/natural_phenomenas/view/"+json.slug+"'>View</a> | <a id='delete-nphenom-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    $('#season-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_celestial_body();
        var url = "/api/worlds/"+world+"/seasons/";
        var data = { name : $('#seaname').val(), span: $("#span").val()};
        var success = function(json) {
            $('#seaname').val(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#season-form")[0].reset();
            $("#seasons").prepend("<li id='season-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/seasons/view/"+json.slug+"'>View</a> | <a id='delete-season-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    $('#nobject-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_celestial_body();
        var url = "/api/worlds/"+world+"/natural_objects/";
        var data = { name : $('#noname').val()};
        var success = function(json) {
            $('#noname').val(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#nobject-form")[0].reset();
            $("#nobjects").prepend("<li id='nobject-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/natural_objects/view/"+json.slug+"'>View</a> | <a id='delete-season-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    $('#species-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_celestial_body();
        var url = "/api/worlds/"+world+"/species/";
        var data = { name : $('#spcname').val()};
        var success = function(json) {
            $('#spcname').val(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#species-form")[0].reset();
            $("#species").prepend("<li id='species-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/species/view/"+json.slug+"'>View</a> | <a id='delete-species-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    $('#place-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_celestial_body();
        var url = "/api/worlds/"+world+"/places/";
        var data = { name : $('#plcname').val()};
        var success = function(json) {
            $("#place-form")[0].reset(); // remove the value from the input
            console.log(json); // log the returned json to the console
            $("#places").prepend("<li id='place-"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/places/view/"+json.slug+"'>View</a> | <a id='delete-place-"+json.slug+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };

        create(url, data, success);
    });

    // Delete post on click
    $("#rule").on('click', 'a[id^=delete-rule-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check

        var url = "/api/natural_laws/"+primary_key+"/";
        var data = { pk : primary_key };
        var success =  function(json) {
            // hide the rule
          $('#rule-'+primary_key).hide(); // hide the post on success
          console.log("natural law deletion successful");
        };

        remove(url, data, success);
    });

    $("#cbodies").on('click', 'a[id^=delete-cbody-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check

        var url = "/api/celestial_bodies/"+primary_key+"/";
        var data = { pk : primary_key };
        var success =  function(json) {
            // hide the rule
          $('#cbody-'+primary_key).hide(); // hide the post on success
          console.log(" deletion successful");
        };

        remove(url, data, success);
    });

    $("#nphenoms").on('click', 'a[id^=delete-nphenom-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check

        var url = "/api/natural_phenomenas/"+primary_key+"/";
        var data = { pk : primary_key };
        var success =  function(json) {
            // hide the rule
          $('#nphenom-'+primary_key).hide(); // hide the post on success
          console.log(" deletion successful");
        };

        remove(url, data, success);
    });
});
