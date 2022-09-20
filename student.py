student1 = {
    "nombre": "Andrey",
    "matematicas": 5.0,
    "español": 4.5,
    "ciencias": 4.0,
    "literatura": 3.0,
    "arte": 3.5
}

student2 = {
    "nombre": "Stefany",
    "matematicas": 4.0,
    "español": 5.0,
    "ciencias": 2.0,
    "literatura": 3.0,
    "arte": 1.5
}

student3 = {
    "nombre": "Kevin",
    "matematicas": 1.0,
    "español": 2.5,
    "ciencias": 5.0,
    "literatura": 3.0,
    "arte": 1.5
}

student4 = {
    "nombre": "Pedro",
    "matematicas": 3.0,
    "español": 2.5,
    "ciencias": 1.0,
    "literatura": 3.0,
    "arte": 5.0
}

student5 = {
    "nombre": "Juan",
    "matematicas": 0.1,
    "español": 2.5,
    "ciencias": 1.0,
    "literatura": 3.0,
    "arte": 1.2
}


def mejor_de_cada_curso(estudiante1, estudiante2, estudiante3, estudiante4, estudiante5):
    students = [estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]
    sorted_students = sorted(students, key=lambda d: d['nombre'])

    return {
        "matematicas": sorted(sorted_students, key=lambda d: d['matematicas'], reverse=True)[0]["nombre"],
        "español": sorted(sorted_students, key=lambda d: d['español'], reverse=True)[0]["nombre"],
        "ciencias": sorted(sorted_students, key=lambda d: d['ciencias'], reverse=True)[0]["nombre"],
        "literatura": sorted(sorted_students, key=lambda d: d['literatura'], reverse=True)[0]["nombre"],
        "arte": sorted(sorted_students, key=lambda d: d['arte'], reverse=True)[0]["nombre"]
    }


if __name__ == '__main__':
    print(mejor_de_cada_curso(student1, student2, student3, student4, student5))
