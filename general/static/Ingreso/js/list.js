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
            { "data": "n_recepcion" },
            { "data": "n_recepcion" },
            { "data": "n_servicio" },
            { "data": "serv_prest" },
            { "data": "fecha_ingreso" },
        ],
        columnDefs: [{
                targets: [0],
                class: 'text-center',
                orderable: true,
                render: function(data, type, row) {
                    return row.id;
                }
            },
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return '3';
                }
            },
            {
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return '32434';
                }
            },
            {
                targets: [3],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.n_servicio;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.serv_prest;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.fecha_ingreso;
                }
            },
        ],
        initComplete: function(settings, json) {

        }
    });
});