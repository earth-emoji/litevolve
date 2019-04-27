$( document ).ready(function() {
    //load rules
    load_data("/api/societies/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#societies").prepend("<li id='society-"+json[i].id+"'><strong>"+json[i].name+
                "</strong> - <a href='/societies/view/"+json[i].id+"'>View</a> | <a id='delete-society-"+json[i].id+"'>delete me</a></li>");
        }
    });
    

    // Submit post on submit
    $('#society-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        var url = "/api/societies/";
        var data = { name : $('#name').val()};
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#society-form")[0].reset();
            $("#societies").prepend("<li id='society-"+json.id+"'><strong>"+json.name+"</strong> - <a href='/societies/view/"+json.id+"'>View</a> | <a id='delete-society-"+json.id+"'>Delete</a></li>");
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    // Delete post on click
    $("#rule").on('click', 'a[id^=delete-rule-]', function(){
        var primary_key = $(this).attr('id').split('-')[2];
        console.log(primary_key) // sanity check

        var url = "/api/rules/"+primary_key+"/";
        var data = { pk : primary_key };
        var success =  function(json) {
            // hide the rule
          $('#rule-'+primary_key).hide(); // hide the post on success
          console.log("rule deletion successful");
        };

        remove(url, data, success);
    });
});