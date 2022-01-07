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
                    if(row.empresa_activa){
                        buttons += '<button type="button" id="'+ row.id + '" class="btn btn-xs btn-flat delete"  alt="Activar registro"><i class="fas fa-toggle-on"></i></button>';
                    }
                    else{
                        buttons += '<button type="button" id="' + row.id + '" class="btn btn-xs btn-flat active" alt="Desactivar registro"><i class="fas fa-toggle-off"></i></button>';
                        
                    }
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

//Funcion para borrar de manera logica
$(document).on('click', ".delete", function(e){
    e.preventDefault();
    let val = $(this)[0].id;
    console.log(val);
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    Swal.fire({
        title: '¿Está seguro de desactivar este registro?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Aceptar',
        cancelButtonText:'Cancelar',
    }).then((result) => {
        if(result.isConfirmed){
            $.ajax({
                url:"empresas/borrar",
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin',
                method: 'POST',
                data : {
                    "id": val,
                    "empresa_activa": false
                },
            }).then(function (request){
                console.log(request);
            }).catch(function(error){
                console.log(error);
            });
        }
    });
});

//funcion para activar de manera logica
$(document).on('click', ".active", function(e){
    e.preventDefault();
    let val = $(this)[0].id;
    console.log(val);
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    Swal.fire({
        title: '¿Está seguro de activar este registro?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Aceptar',
        cancelButtonText:'Cancelar',
    }).then((result) => {
        if(result.isConfirmed){
            $.ajax({
                url:"empresas/borrar",
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin',
                method: 'POST',
                data : {
                    "id": val,
                    "empresa_activa": true
                },
            }).then(function (request){
                console.log(request);
            }).catch(function(error){
                console.log(error);
            });
        }
    });
});