$( document ).ready(function() {
    load_data("/api/stories/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#stories").prepend("<div id='story"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].title +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/stories/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_story_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#story-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/stories/";
        var data = { 
            title : $('#title').val(),
            genre: $('#genre').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#story-form")[0].reset();
            var content = "<div id='story"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.title +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/stories/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_story_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#stories").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var prslug = $("span[id^=prslug_]").attr('id').split('_')[1];

    // Submit post on submit
    $('#synop-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/premises/"+prslug+"/update-synopsis/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            synopsis: $("#synop").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>Premise has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#synop-content").html(json.synopsis);
        });
    });

    var plslug = $("span[id^=plslug_]").attr('id').split('_')[1];

    // Submit post on submit
    $('#expo-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/plots/"+plslug+"/update-exposition/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            exposition: $("#expo").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>Plot has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#expo-content").html(json.exposition);
        });
    });


    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    load_data("/api/story/"+ slug +"/acts/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#acts").prepend("<div id='story"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>Act: "+ json[i].act_number + " " + json[i].title +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/acts/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_act_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#act-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/story/"+ slug +"/acts/";
        var data = { 
            title : $('#title').val(),
            act_number: $('#act_number').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#act-form")[0].reset();
            var content = "<div id='story"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>Act: "+ json[i].act_number + " " + json[i].title +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/acts/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_act_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#acts").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });
});
