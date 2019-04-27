$( document ).ready(function() {
    //load rules
    load_data("/api/religions/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#religions").prepend("<li id='religion-"+json[i].id+"'><strong>"+json[i].name+
                "</strong> - <a href='/religions/view/"+json[i].id+"'>View</a> | <a id='delete-religion-"+json[i].id+"'>delete me</a></li>");
        }
    });
    

    // Submit post on submit
    $('#religion-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        var url = "/api/religions/";
        var data = { name : $('#name').val()};
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#religion-form")[0].reset();
            $("#religions").prepend("<li id='religion-"+json.id+"'><strong>"+json.name+"</strong> - <a href='/religions/view/"+json.id+"'>View</a> | <a id='delete-religion-"+json.id+"'>Delete</a></li>");
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