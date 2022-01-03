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
            { "data": "nombre_empresa" },
            { "data": "phone" },
            { "data": "email" },
            { "data": "nombre" },
            { "data": "razon_social" },
        ],
        columnDefs: [{
                targets: [-1],
                class: 'text-right',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="empresas/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="empresas/detail/' + row.id + '/" type="button" class="btn btn-flat"><i class="fas fa-info-circle"></i></a> ';
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
                class: "text-center",
                orderable: true,
                render: function(data, type, row) {
                    return row.nombre_empresa;
                }
            },
            {
                targets: [2],
                class: "text-center",
                orderable: true,
                render: function(data, type, row) {
                    return row.phone;
                }
            },
            {
                targets: [3],
                class: "text-center",
                orderable: true,
                render: function(data, type, row) {
                    return row.email;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: true,
                render: function(data, type, row) {
                    return row.nombre;
                }
            },
        ],
        initComplete: function(settings, json) {

        }
    });
});