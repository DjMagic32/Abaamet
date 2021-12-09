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
            { "data": "nombre" },
            { "data": "precio" },
            { "data": "detalle" },
            { "data": "activo" },
        ],
        columnDefs: [{
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="servicios/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<button type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></button>';
                    return buttons;
                }
            },
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.nombre;
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
                targets: [2],
                class: "text-right",
                orderable: true,
                render: function(data, type, row) {
                    return row.precio;
                }
            },
            {
                targets: [3],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.precio;
                }
            },
        ],
        initComplete: function(settings, json) {

        }
    });
});