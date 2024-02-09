var showFormularioMantenedor=false;

$(document).ready(function () {
    const cargarContenido = (pathArchivoHtml) => {
        console.log("Carga de mi archivo html:: ", pathArchivoHtml);
        $.get(pathArchivoHtml, function (data) {
            //Código carga html en el div contenido
            console.log("Carga html: ", data);
            $("#idDivContenido").html(data);
        })
        .catch((error) => {
            console.log("Error al obtener el archivo html", error);
        });
    };

    cargarContenido("./app/front/listaProyectos.html");

    $("#idMenuMantenedorProyecto").click(function () {
        console.log("Click en menu mantenedor de proyectos");
        showFormularioMantenedor = true;
        cargarContenido("./app/front/listaProyectos.html");
    });

});