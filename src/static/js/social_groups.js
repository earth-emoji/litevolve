$( document ).ready(function() {
    //load rules
    load_data("/api/social_groups/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#sgroups").prepend("<li id='sgroup-"+json[i].id+"'><strong>"+json[i].name+
                "</strong> - <a href='/social_groups/view/"+json[i].id+"'>View</a> | <a id='delete-sgroup-"+json[i].id+"'>delete me</a></li>");
        }
    });
    

    // Submit post on submit
    $('#sg-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        var url = "/api/social_groups/";
        var data = { name : $('#name').val()};
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#sg-form")[0].reset();
            $("#sgroups").prepend("<li id='sg-"+json.id+"'><strong>"+json.name+"</strong> - <a href='/social_groups/view/"+json.id+"'>View</a> | <a id='delete-sg-"+json.id+"'>Delete</a></li>");
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