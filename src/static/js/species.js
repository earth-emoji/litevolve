$( document ).ready(function() {
    var species = $("span[id^=species-]").attr('id').split('-')[1];

    // Submit post on submit
    $('#ap-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/species/"+species+"/update-appearance/";
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

        var url = "/api/species/"+species+"/update-abilities/";
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

        var url = "/api/species/"+species+"/update-intelligence/";
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

        var url = "/api/species/"+species+"/update-origins/";
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

        var url = "/api/species/"+species+"/update-ecosystem/";
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
});