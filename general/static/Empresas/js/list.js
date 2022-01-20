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
            { "data": "nombre" },
            { "data": "nombre" },
        ],
        columnDefs: [{
                targets: [-1],
                class: 'text-right',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="empresas/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="empresas/detail/' + row.id + '/" type="button" class="btn btn-flat"><i class="fas fa-info-circle"></i></a> ';
                    if(row.empresa_activa == true || row.empresa_activa == 'true'){
                        buttons += '<button type="button" id="'+ row.id + '" class="btn btn-xs btn-flat delete"  alt="Desactivar registro"><i class="fas fa-toggle-on"></i></button>';
                    }
                    else{
                        buttons += '<button type="button" id="' + row.id + '" class="btn btn-xs btn-flat active" alt="Activar registro"><i class="fas fa-toggle-off"></i></button>';
                        
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
                url:"empresas/borrar/"+val+"/",
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin',
                method: 'POST',
                data : {
                    "active": false
                },
                success: function(request){
                    Swal.fire({
                        title: 'Registro desactivado exitosamente',
                        icon: 'success',
                        showCancelButton: false,
                    }).then( (response) => {
                        if(response.isConfirmed){
                            location.reload()
                        }
                    });
                }
            });
        }
    });
});

//funcion para activar de manera logica
$(document).on('click', ".active", function(e){
    e.preventDefault();
    let val = $(this)[0].id;
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
                url:"empresas/borrar/"+val+"/",
                headers: {'X-CSRFToken': csrftoken},
                mode: 'same-origin',
                method: 'POST',
                data : {
                    "active": true
                },
                success: function(request){
                    Swal.fire({
                        title: 'Registro activado exitosamente',
                        icon: 'success',
                        showCancelButton: false,
                    }).then( (response) => {
                        if(response.isConfirmed){
                            location.reload()
                        }
                    });
                }
            });
        }
    });
});