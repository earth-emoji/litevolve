$( document ).ready(function() {
    load_data("/api/elements/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#elements").prepend("<div id='element_"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/elements/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_element_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#element-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/elements/";
        var data = { 
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#element-form")[0].reset();
            var content = "<div id='element_"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/elements/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_element_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#elements").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });
});
