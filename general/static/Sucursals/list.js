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
            { "data": "rfc" },
            { "data": "id_direccion" },
            { "data": "id_empresa" },

        ],
        columnDefs: [
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
                    return row.rfc;
                }
            },
            {
                targets: [2],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.id_direccion;
                }
            },{
                targets: [3],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.id_empresa;
                }
            },

        ],
        initComplete: function(settings, json) {

        }
    });
});