$(document).on("submit", "#post-form", function (event) {
    event.preventDefault();

    $.ajax({
        type: "POST",
        url: "/create",
        data: {
            link: $("#link").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function (alias) {
            shortener_url = "https://alshortener.herokuapp.com/" + alias

            $("#shortener_url").attr("href", shortener_url)
            $("#shortener_url").html("https://alshortener.herokuapp.com/" + alias);
        },
    });
});