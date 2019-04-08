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
    company_qs_param = document.querySelector('select[name="company"]').value
    //CSRF TOKEN GENERATED and attached to a body of data for making http requests (ONLY FOR POSTS/PUTS) GET requests do not require a csrftoken.
    csrftoken = getCookie('csrftoken')
    let data = new FormData();
    data.append('csrfmiddlewaretoken', csrftoken)

    fetch(`/company-profiles/${company_qs_param}`, {
        method: 'GET'
    }).then(function (response) {
            return response.json();
            //now that we got our company sale object then pre-populate some of the form data.

        }).then(function (myJson) {
            console.log(myJson)
            document.getElementById('id_company_name').value = myJson.company_name
            document.getElementById('id_contact_email').value = myJson.contact_email
            document.getElementById('id_contact_name').value = myJson.contact_name
            document.getElementById('id_office_phone_number').value = myJson.office_phone
            document.getElementById('id_direct_phone_number').value = myJson.direct_phone
            document.getElementById('id_address').value = myJson.address
            document.getElementById('id_secondary_address').value = myJson.secondary_address
            document.getElementById('id_province').value = myJson.province
            document.getElementById('id_city').value = myJson.city
            document.getElementById('id_postal_code').value = myJson.postal_code
            document.getElementById('id_industry').value = myJson.industry
            document.getElementById('id_facebook_link').value = myJson.facebook_link
            document.getElementById('id_website_link').value = myJson.website_link
            document.getElementById('id_twitter_link').value = myJson.twitter_link
            document.getElementById('id_instagram_link').value = myJson.instagram_link

    }).catch((err)=> {
        console.log('Error Fetching Data: ', err)
    });
}


