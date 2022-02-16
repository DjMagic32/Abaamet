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
            { "data": "n_entrada" },
            { "data": "nombre" },
            { "data": "marca" },
            { "data": "modelo" },
            { "data": "serie" },
            { "data": "identificacion" },
            { "data": "descripcion_particular" },
            { "data": "fecha_de_recepcion" },
            { "data": "modo" },
            { "data": "cliente" },
            { "data": "estatus" },
            { "data": "orden_compra" },
            { "data": "n_cotizacion" },
            { "data": "n_cotizacion" },

        ],
        columnDefs: [{
                targets: [0],
                class: 'text-center',
                orderable: true,
                render: function(data, type, row) {
                    return row.n_entrada;
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
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.marca;
                }
            },
            {
                targets: [3],
                class: "text-right",
                orderable: false,
                render: function(data, type, row) {
                    return row.modelo;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.serie;
                }
            }, {
                targets: [5],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.identificacion;
                }
            }, {
                targets: [6],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.descripcion_particular;
                }
            }, {
                targets: [7],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.fecha_de_recepcion;
                }
            }, {
                targets: [8],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.modo;
                }
            }, {
                targets: [9],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.cliente;
                }
            }, {
                targets: [10],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.estatus;
                }
            }, {
                targets: [11],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.orden_compra;
                }
            }, {
                targets: [12],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.n_cotizacion;
                }
            }, {
                targets: [13],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="recepcion/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function(settings, json) {

        }
    });
});

