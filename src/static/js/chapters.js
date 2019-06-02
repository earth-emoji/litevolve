$( document ).ready(function() {
    var cslug = $("span[id^=cslug_]").attr('id').split('_')[1];

    load_data("/api/chapters/"+ cslug +"/scenes/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#chapters").prepend("<div id='scene_"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].title +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/scenes/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_scene_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#scene-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/chapters/"+ cslug +"/scenes/";
        var data = { 
            title : $('#title').val(),
            position: $('#position').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#scene-form")[0].reset();
            var content = "<div id='chapter_"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+json.title+"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/scenes/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_scene_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#scenes").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });
});
