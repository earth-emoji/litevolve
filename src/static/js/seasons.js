$( document ).ready(function() {
    load_data("/api/seasons/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#seasons").prepend("<div id='season_"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/seasons/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_season_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });
  
    $('#season-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
  
        var url = "/api/seasons/";
        var data = {
            name : $('#name').val(),
            span : $('#span').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#season-form")[0].reset();
            var content = "<div id='season_"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/seasons/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_season_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";
  
            $("#seasons").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });
  
    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    // Submit post on submit
    $('#desc-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/seasons/"+slug+"/update-description/";
        //"/api/rules/"+cbody+"/update-can/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            description: $("#desc").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#desc-content").html(json.description);
        });
    });
});

