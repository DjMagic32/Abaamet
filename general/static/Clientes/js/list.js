$(function() {
    $('#datatable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: { 'action': 'searchdata' },
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "nombre_completo" },
            { "data": "telefono" },
            { "data": "telefono_ad" },
            { "data": "email" },
            { "data": "id_sucursal" },
            { "data": "id_sucursal" },

        ],
        columnDefs: [{
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="clientes/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<button type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></button>';
                    return buttons;
                }
            },
            {
                targets: [0],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.id;
                }
            },
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.nombre_completo;
                }
            },
            {
                targets: [2],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.telefono;
                }
            },
            {
                targets: [3],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.telefono_ad;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.email;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.id_sucursal;
                }
            },

        ],
        initComplete: function(settings, json) {

        }
    });
    $('.btnAdd').on('click', function() {
        $('input[name="action"]').val('add');
        // modal_title.find('span').html('Creación de un cliente');
        // console.log(modal_title.find('i'));
        // modal_title.find('i').removeClass().addClass('fas fa-plus');
        // $('form')[0].reset();
        $('#myModalcliente').modal('show');
    });

    $('form').on('submit', function(e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function() {
            $('#myModalcliente').modal('hide');
            tblClient.ajax.reload();
            //getData();
        });
    });
});

// function submit_with_ajax(url, title, content, parameters, callback) {
//     $.confirm({
//         theme: 'material',
//         title: title,
//         icon: 'fa fa-info',
//         content: content,
//         columnClass: 'small',
//         typeAnimated: true,
//         cancelButtonClass: 'btn-primary',
//         draggable: true,
//         dragWindowBorder: false,
//         buttons: {
//             info: {
//                 text: "Si",
//                 btnClass: 'btn-primary',
//                 action: function() {
//                     $.ajax({
//                         url: url, //window.location.pathname
//                         type: 'POST',
//                         data: parameters,
//                         dataType: 'json',
//                         processData: false,
//                         contentType: false,
//                     }).done(function(data) {
//                         console.log(data);
//                         if (!data.hasOwnProperty('error')) {
//                             callback();
//                             return false;
//                         }
//                         message_error(data.error);
//                     }).fail(function(jqXHR, textStatus, errorThrown) {
//                         alert(textStatus + ': ' + errorThrown);
//                     }).always(function(data) {

//                     });
//                 }
//             },
//             danger: {
//                 text: "No",
//                 btnClass: 'btn-red',
//                 action: function() {

//                 }
//             },
//         }
//     })
// }