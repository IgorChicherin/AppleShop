/**
 * Created by i.chicherin on 23.05.2017.
 */

function fill_form(id) {
    $.ajax({
            url: 'get_user/' + id,
            type: 'GET',
            datatype: 'json',
            success: function (response) {
                if (response.errors) {
                    console.log("errors = ", errors);
                } else {
                    $('#usr_form').html(response.html);
                }
            },
            error: function (xhr, status, error) {
                console.log('error =', error)
            }
        }
    )
}

function del_user(id) {
    $.ajax({
        url: 'del_user/' + id,
        type: 'GET',
        datatype: 'json',
        success: function (response) {
            if (response.errors) {
                console.log("errors = ", errors);
            }
            else {
                $('#user_list').html(response.html);
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    })

}


function del_item_content(id) {
    $.ajax({
        url: 'delete/' + id,
        type: 'GET',
        datatype: 'json',
        success: function (response) {
            if (response.errors) {
                console.log('error = ', errors);
            }
            else {
                $('#del_item_form').html(response.html);
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    })
}
