console.log("Inicialización de la table");
var $tblListaProyectos = $('#idTblListaProyectos');

var listaProyectos = [];

$(document).ready(function () {
    const initTblListaProyectos = () => {
        $tblListaProyectos.bootstrapTable({
            columns: [{
                field: 'state',
                checkbox: true
            }, {
                field: 'id',
                title: 'ID'
            }, {
                field: 'nombre',
                title: 'Nombre'
            }, {
                field: 'descripcion',
                title: 'Descripción'
            }],
            data: listaProyectos,
            search: true,
            pagination: true,
            showSearchButton: true,
            paginationPreText: "Anterior",
            paginationNextText: "Siguiente",
            pageList: [5, 10],
            pageSize: 5,
            locale: "es",
            clickToSelect: true,
            singleSelect: true
        })
    }

    const showFormulario = () => {
        console.log("Parametros lista proyecctos: ", showFormularioMantenedor);
        if (showFormularioMantenedor) {
            //Mostrar el formulario
            $("#idDivMantenedorProyecto").show();
        } else {
            //Ocultar el formulario
            $("#idDivMantenedorProyecto").hide();
        }
    }

    initTblListaProyectos();
    showFormulario();

    $("#idAgregarProyecto").click(function () {
        console.log("Click Agregar Proyecto....");
        let siguienteId = 0;
        // for ( let element of listaProyectos ) {

        //     // Evalúa si «max» es menor que «numero» para almacenar
        //     // en él el número más grande hasta el momento:
        //     if (siguienteId < element.id)
        //         siguienteId = element.id;
        // }

        listaProyectos.forEach((element) => {
            if (siguienteId < element.id)
                siguienteId = element.id;
        });

        siguienteId += 1;



        //console.log(listaOrdenada);
        let nuevoProyecto = {
            id: siguienteId,
            nombre: $("#idTxtNombreProyecto").val(),
            descripcion: $("#idTxtDescripciónProyecto").val()
        }

        listaProyectos.push(nuevoProyecto);
        $tblListaProyectos.bootstrapTable('refreshOptions', {
            data: listaProyectos
        });
    });

    $("#idEliminarProyecto").click(function () {
        //$tblListaProyectos.bootstrapTable('getSelections');
        //Se remueve según documentación de bootstrap table: https://live.bootstrap-table.com/example/methods/remove.html
        var ids = $.map($tblListaProyectos.bootstrapTable('getSelections'), function (row) {
            return row.id
        });
        $tblListaProyectos.bootstrapTable('remove', {
            field: 'id',
            values: ids
        });
        listaProyectos = $tblListaProyectos.bootstrapTable('getData');
    });
});






// $tblListaProyectos.bootstrapTable('refreshOptions', {
//     locale: "es-CL"
// })