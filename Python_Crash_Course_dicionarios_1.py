usuarios = {

    'albet19945':{
        'primer': 'albert',
        'ultimo': 'Einstein',
        'Localizacion':'Princeton',

    },

    'mari89': {
        'primer': 'Marie',
        'ultimo': 'Curie',
        'Localizacion': 'Paris',

    }
}

for username, user_info in usuarios.items():
    print("\n NombreUsuario: "+ username)
    nombre_completo = user_info['primer']+" " + user_info['ultimo']
    localizacion = user_info['Localizacion']

    print("\t Nombre Completo : " + nombre_completo.title())
    print("\t Localizacion :" + localizacion.title())