$( document ).ready(function() {

    //load rules
    load_data("/api/projects/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#projects").prepend("<div id='project-"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/projects/view/"+json[i].slug+"'><i class='icofont-eye-alt'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete-project-"+json[i].slug+"'><i class='icofont-delete-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    // Submit post on submit
    $('#project-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/projects/";
        var data = { 
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#project-form")[0].reset();
            var content = "<div id='project-"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                <li class='list-inline-item'><a href='/projects/view/"+json.slug+"'><i class='icofont-eye-alt'></i> View</a></li>\
                                <li class='list-inline-item'><a id='delete-project-"+json.slug+"'><i class='icofont-delete-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#projects").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var slug = $("span[id^=slug_]").attr('id').split('_')[1];
    
    load_data("/api/projects/"+slug+"/tasks/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#tasks").prepend("<div id='task-"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/tasks/view/"+json[i].slug+"'><i class='icofont-eye-alt'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete-task-"+json[i].slug+"'><i class='icofont-delete-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });

    $('#task-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/projects/"+slug+"/tasks/";
        var data = { 
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#task-form")[0].reset();
            var content = "<div id='project-"+json.data.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.data.name +"</h5>\
                                <ul class='list-inline'>\
                                <li class='list-inline-item'><a href='/tasks/view/"+json.data.slug+"'><i class='icofont-eye-alt'></i> View</a></li>\
                                <li class='list-inline-item'><a id='delete-task-"+json.data.slug+"'><i class='icofont-delete-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";

            $("#tasks").prepend(content);
            $("#pbar").attr("aria-valuenow", json.progress)
            $("#pbar").css("width", json.progress)
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var tslug = $("span[id^=tslug_]").attr('id').split('_')[1];

    $('#ctype-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
        
        var url = "/api/tasks/"+tslug+"/content_type/";
        var data = { 
            ctype : $('#ctype').val(),
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#ctype-form")[0].reset();
            var content = "<div id='ctype-"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                <li class='list-inline-item'><a href="+json.url+"'><i class='icofont-eye-alt'></i> View</a></li>\
                                </ul>\
                            </div></div>";
            $("#ctype-content").html(content);
            $('#ctype-btn').addClass('d-none');
            $('#ctype-content').removeClass('d-none');
            $('#ctypeModal').modal('hide')

            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    $("#complete-form").on('submit', function(e) {
        e.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/tasks/"+tslug+"/update-complete/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            is_complete: $("#complete").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#ic-btn").attr("disabled", "disabled");
            $("#ic-btn").html("Completed");
        });
    })

    // // Submit post on submit
    // $('#details-form').on('submit', function(event){
    //     event.preventDefault();
    //     console.log("form submitted!")  // sanity check

    //     var url = "/api/universes/"+slug+"/update-overview/";
    //     var data = {
    //         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    //         overview: $("#details").val()
    //     };

    //     patch(url, data, function(json) {
    //         var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
    //         $('#results').html(successful);
    //         $("#details-content").html(json.overview);
    //     });
    // });

    // $("#universes").on('click', 'a[id^=delete-universe-]', function(){
    //     var primary_key = $(this).attr('id').split('-')[2];
    //     console.log(primary_key) // sanity check

    //     var url = "/api/universes/"+primary_key+"/";
    //     var data = { pk : primary_key };
    //     var success =  function(json) {
    //         // hide the rule
    //       $('#nphenom-'+primary_key).hide(); // hide the post on success
    //       console.log(" deletion successful");
    //     };

    //     remove(url, data, success);
    // });


});
