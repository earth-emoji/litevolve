$( document ).ready(function() {

    //load data
    load_data("/api/universes/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#universes").prepend("<div id='universe-"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/universes/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete-universe-"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    // Submit post on submit
    $('#universe-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/universes/";
        var data = { 
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#universe-form")[0].reset();
            var content = "<div id='universe-"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/universes/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete-universe-"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#universes").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    // Submit post on submit
    $('#details-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/universes/"+slug+"/update-overview/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            overview: $("#details").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#details-content").html(json.overview);
        });
    });

    $('#history-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_history();
        var url = "/api/universes/"+universe+"/histories/";
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

    $('form.natural_laws').each(function() {
        $(this).on("submit", function(event) {
            event.preventDefault();
            console.log("form submitted!")  // sanity check
            var url = "/api/universes/"+slug+"/natural_laws/";
            var data = {
                natural_law: $(this).children("input[id^=rule_]").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            };
            var success = function(json) {
                $("#laws").prepend("<li id='law_"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/natural_laws/view/"+json.slug+"'>View</a></li>");
                var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully added <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
                $("#slug_"+json.slug).fadeOut();
                $("#slug_"+json.slug).remove();
                $('#results').html(successful); 
            };
            create(url, data, success);
    
        });
    });

    $('form.particle-form').each(function() {
        $(this).on("submit", function(event) {
            event.preventDefault();
            console.log("form submitted!")  // sanity check
            var url = "/api/universes/"+slug+"/particles/";
            var data = {
                particle: $(this).children("input[id^=par_]").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            };
            var success = function(json) {
                $("#particles").prepend("<li id='particle_"+json.slug+"'><strong>"+json.name+"</strong> - <a href='/particles/view/"+json.slug+"'>View</a></li>");
                var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully added <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
                $("#slug_"+json.slug).fadeOut();
                $("#slug_"+json.slug).remove();
                $('#results').html(successful); 
            };
            create(url, data, success);
    
        });
    });

    load_data("/api/universes/"+slug+"/natural_laws/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#laws").prepend("<li id='law_"+json[i].slug+"'><strong>"+json[i].name+"</strong> - <a href='/natural_laws/view/"+json[i].slug+"'>View</a>");
        }
    });

    load_data("/api/universes/"+slug+"/particles/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#particles").prepend("<li id='particle_"+json[i].slug+"'><strong>"+json[i].name+"</strong> - <a href='/particles/view/"+json[i].slug+"'>View</a>");
        }
    });


    $("#universes").on('click', 'a[id^=delete-universe-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check

        var url = "/api/universes/"+primary_key+"/";
        var data = { pk : primary_key };
        var success =  function(json) {
            // hide the rule
          $('#nphenom-'+primary_key).hide(); // hide the post on success
          console.log(" deletion successful");
        };

        remove(url, data, success);
    });


});
