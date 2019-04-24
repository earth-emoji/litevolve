$( document ).ready(function() {
    var nphenom = $("span[id^=nphenom-]").attr('id').split('-')[1];

    // Submit post on submit
    $('#nphenom-desc-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check

        var url = "/api/natural_phenomenas/"+nphenom+"/update-description/";
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
