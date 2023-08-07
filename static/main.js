console.log("Hello there")


function limpiar_opciones_select(select_id){
    let select_item = document.getElementById(select_id);
    let options = select_item.getElementsByTagName('option');
    
    for (var i=options.length; i--;) {
        select_item.removeChild(options[i]);
    }
}


function agregar_cursos_a_ciclo(){
    const cursosSelect = document.getElementById("curso")
    const carrera = document.getElementById("carrera").value
    const ciclo = document.getElementById("ciclo").value
    limpiar_opciones_select("curso")
    agregar_default_option("curso")
    agregar_default_option("seccion")
    const url = `http://127.0.0.1:8000/cursos/get-from-ciclo/${carrera}/${ciclo}`
    fetch(url).then(response => response.json()).then(
        data => {
            data.forEach(curso => {
                const codigoCurso = curso.codigo_curso
                const nombreCurso = curso.nombre_curso
                const opcion = document.createElement("option")
                opcion.value = codigoCurso
                opcion.innerText = nombreCurso
                cursosSelect.append(opcion)
            });

        }
    )

}


function agregar_secciones_a_curso(){
    const seccionSelect = document.getElementById("seccion")
    const carrera = document.getElementById("carrera").value
    const curso = document.getElementById("curso").value
    limpiar_opciones_select("seccion")
    agregar_default_option("seccion")
    const url = `http://127.0.0.1:8000/secciones/get-secciones-from-curso/${curso}`
    fetch(url).then(response => response.json()).then(
        data => {
            data.forEach(seccion => {
                const codigoSeccion = seccion.codigo_seccion
                const numeroSeccion = seccion.numero_seccion
                const opcion = crear_opcion_de_horario(codigoSeccion, numeroSeccion, carrera)
                seccionSelect.append(opcion)
            });

        }
    )
}



function crear_opcion_de_horario(codigoSeccion, numeroSeccion, carrera){
    const url = `http://127.0.0.1:8000/horario-seccion/get-horarios-from-seccion/${carrera}/${codigoSeccion}`
    const opcion = document.createElement("option")
    fetch(url).then(response => response.json()).then(
        data => {
            const codigoSeccion = data.codigo_seccion
            let opcion_text = ""
            data.horarios.forEach(horario => {
                const dia = horario.dia
                const horaInicio = horario.hora_inicio
                const horaFin = horario.hora_fin
                opcion_text += `G.${numeroSeccion} ${dia} ${horaInicio}:00-${horaFin}:00`
            })
            opcion.value = codigoSeccion
            opcion.innerText = opcion_text
        }
    )
    return opcion
    
}


function agregar_default_option(select){
    const selectElement = document.getElementById(select)
    const defaultOption = document.createElement("option")
    let textoInicial = select == "seccion" ? "Selecciona una " : "Selecciona un " 
    defaultOption.innerText = textoInicial + select
    selectElement.append(defaultOption)

}


document.getElementById("carrera").addEventListener("change", () => {
    const selects = ["curso", "seccion"]
    selects.forEach(select => {
        limpiar_opciones_select(select)
        agregar_default_option(select)
        
    })
})
document.getElementById("ciclo").addEventListener("change", () => {
    limpiar_opciones_select("seccion")
    agregar_cursos_a_ciclo()
})
document.getElementById("curso").addEventListener("change", agregar_secciones_a_curso)