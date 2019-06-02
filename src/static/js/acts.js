$( document ).ready(function() {
    var slug = $("span[id^=aslug_]").attr('id').split('_')[1];

    load_data("/api/acts/"+ slug +"/chapters/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#chapters").prepend("<div id='chapter_"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>Chapter: "+ json[i].chap_number + " " + json[i].title +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/chapters/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_chap_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#chap-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/acts/"+ slug +"/chapters/";
        var data = { 
            title : $('#title').val(),
            chap_number: $('#chap_number').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#chap-form")[0].reset();
            var content = "<div id='chapter_"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>Act: "+ json.act_number + " " + json.title +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/chapters/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_chap_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#chapters").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });
});
