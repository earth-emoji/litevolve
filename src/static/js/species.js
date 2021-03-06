$( document ).ready(function() {
    load_data("/api/species/", function(json) {
        for (var i = 0; i < json.length; i++) {
            $("#species").prepend("<div id='species"+json[i].slug+"' class='media'>\
                <img class='align-self-center mr-3' src='' alt=''>\
                <div class='media-body'>\
                <h5 class='mt-0'>"+ json[i].name +"</h5>\
                <ul class='list-inline'>\
                    <li class='list-inline-item'><a href='/species/view/"+json[i].slug+"'><i class='far fa-eye'></i> View</a></li>\
                    <li class='list-inline-item'><a id='delete_species_"+json[i].slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                </ul>\
            </div></div>");
        }
    });
  
    $('#species-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        //create_rule();
  
        var url = "/api/species/";
        var data = {
            name : $('#name').val()
        };
        var success = function(json) {
            console.log(json); // log the returned json to the console
            $("#species-form")[0].reset();
            var content = "<div id='nobject_"+json.slug+"' class='media'>\
                                <img class='align-self-center mr-3' src='' alt=''>\
                                <div class='media-body'>\
                                <h5 class='mt-0'>"+ json.name +"</h5>\
                                <ul class='list-inline'>\
                                    <li class='list-inline-item'><a href='/species/view/"+json.slug+"'><i class='far fa-eye'></i> View</a></li>\
                                    <li class='list-inline-item'><a id='delete_species_"+json.slug+"'><i class='far fa-trash-alt'></i> Delete</a></li>\
                                </ul>\
                            </div></div>";
  
            $("#species").prepend(content);
            console.log("success"); // another sanity check
        };
        create(url, data, success);
    });

    var slug = $("span[id^=slug_]").attr('id').split('_')[1];

    // Submit post on submit
    $('#ap-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-appearance/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            appearance: $("#appearance").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#ap-content").html(json.appearance);
        });
    });

    // Submit post on submit
    $('#ua-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-abilities/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            unique_abilities: $("#ua").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#ua-content").html(json.unique_abilities);
        });
    });
    
    // Submit post on submit
    $('#intell-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-intelligence/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            intelligence: $("#intell").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#intell-content").html(json.intelligence);
        });
    });

    // Submit post on submit
    $('#origins-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-origins/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            origins: $("#origins").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#origins-content").html(json.origins);
        });
    });

    // Submit post on submit
    $('#habitat-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+species+"/update-habitat/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            habitat: $("#habitat").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#habitat-content").html(json.habitat);
        });
    });

    // Submit post on submit
    $('#ecosystem-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-ecosystem/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            ecosystem: $("#ecosystem").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#ecosystem-content").html(json.ecosystem);
        });
    });

    // Submit post on submit
    $('#diet-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-diet/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            diet: $("#diet").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#diet-content").html(json.diet);
        });
    });

    // Submit post on submit
    $('#predators-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-predators/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            predators: $("#predators").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#predators-content").html(json.predators);
        });
    });

    // Submit post on submit
    $('#defense-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-defense/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            defense: $("#defense").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#defense-content").html(json.defense);
        });
    });
    // Submit post on submit
    $('#extra-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+slug+"/update-extra/";
        var data = {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            extra: $("#extra").val()
        };

        patch(url, data, function(json) {
            var successful = "<div class='alert alert-success alert-dismissible fade show' role='alert'>"+ json.name + " has successfully been update <button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div>";
            $('#results').html(successful);
            $("#extra-content").html(json.extra);
        });
    });
});
