$(document).on("submit", "#post-form", function (event) {
    event.preventDefault();

    $.ajax({
        type: "POST",
        url: "/create",
        data: {
            link: $("#link").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function (uuid) {
            $("h3").html("https://alshortener.herokuapp.com/" + uuid);
        },
    });
});