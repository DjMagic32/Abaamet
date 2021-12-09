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
            { "data": "pais" },
            { "data": "estado" },
            { "data": "municipio" },
            { "data": "localidad" },
            { "data": "referencia" },
            { "data": "colonia" },
            { "data": "calle" },
            { "data": "num_interior" },
            { "data": "num_exterior" },
            { "data": "codigo_postal" },
            { "data": "codigo_postal" },

        ],
        columnDefs: [{
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="direcciones/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
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
                    return row.pais;
                }
            },
            {
                targets: [2],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.estado;
                }
            },
            {
                targets: [3],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.municipio;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.localidad;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.referencia;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.colonia;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.calle;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.num_interior;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.num_exterior;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.codigo_postal;
                }
            },
        ],
        initComplete: function(settings, json) {

        }
    });
});