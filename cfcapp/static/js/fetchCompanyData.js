function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function GetCompanyInfo(e) {
    e.preventDefault()
    csrftoken = getCookie('csrftoken')
    let data = new FormData();
    data.append('csrfmiddlewaretoken', csrftoken)
// add form input from hidden input elsewhere on the page

    fetch("/company-profiles/", {
       method: 'POST',
        body: data,
        credentials: 'same-origin',
    }).then(function (response) {
            console.log(response)
            return response;
        }).then(function (myJson) {
        console.log(JSON.stringify(myJson));
    });
}

