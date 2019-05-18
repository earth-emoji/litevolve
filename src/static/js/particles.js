$( document ).ready(function() {
    load_data("/api/particles/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#particles").prepend("<div id='particle-"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/particles/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete-particle-"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#particle-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        
        var url = "/api/particles/";
        var data = { 
            name : $('#name').val(),
            size: $('#size').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#particle-form")[0].reset();
            var content = "<div id='particle-"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/particles/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete-particle-"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#particles").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    $('#desc-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/particles/"+slug+"/update-description/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            description: $("#desc").val()
        };
        console.log(data)
        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#desc-content").html(json.description);
        });
    });
});
