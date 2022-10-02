%%%% HECHOS %%%%

% Mis amigos
es_amigo("Martin Vazques Arispe").
es_amigo("Martin Caballero").
es_amigo("Tomas Ciganda").
es_amigo("Leonel Leguizamon").
es_amigo("Ximena Elgart").
es_amigo("Luisina Echarri").
es_amigo("Delfina Goicoechea").
es_amigo("Sol Spinelli").
es_amigo("Joaquin Benecier").
es_amigo("Agustin Zucchi").
es_amigo("Martino Ferrero").
es_amigo("Juan Francisco Herrero").
es_amigo("Juan Ignacio Sampedro").
es_amigo("Pia Bedinni Crocci").
es_amigo("David Burckhardt").
es_amigo("Mateo Billordo").

% Lenguajes que programo
programa("Python").
programa("Java").
programa("Javascript").

%Materia(Codigo,Nombre,anio,cuatrimestre)
materia(6111, "Introduccion a la Programacion", 1, 1).
materia(6112, "Analisis Matematico", 1, 1).
materia(6113, "Algebra I", 1, 1).
materia(6114, "Quimica 1", 1, 1).
materia(6121, "Ciencias de la Computacion", 1, 2).
materia(6122, "Introduccion a la Programacion II", 1, 2).
materia(6123, "Algebra Lineal", 1, 2).
materia(6124, "Fisica General", 1, 2).
materia(6125, "Matematica Discreta", 1, 2).
materia(6211, "Ciencias de la Computacion II", 2, 1).
materia(6212, "Analisis y Diseno de Algoritmos I", 2, 1).
materia(6213, "Introduccion a la Arquitectura de Sistemas", 2, 1).
materia(6214, "Analisis Matematico II", 2, 1).
materia(6215, "Electricidad y Magnetismo 2", 2, 1).
materia(6221, "Analisis y Diseno de Algoritmos II", 2, 2).
materia(6222, "Comunicacion de Datos I", 2, 2).
materia(6223, "Probabilidades y Estadistica", 2, 2).
materia(6224, "Electronica Digital", 2, 2).
materia(6225, "Ingles", 2, 2).
materia(6311, "Programacion Orientada a Objetos", 3, 1).
materia(6312, "Estructuras de Almacenamiento de Datos", 3, 1).
materia(6313, "Metodologias de Desarrollo de Software I", 3, 1).
materia(6314, "Arquitectura de Computadoras I", 3, 1).
materia(6321, "Programacion Exploratoria", 3, 2).
materia(6322, "Base de Datos I", 3, 2).
materia(6323, "Lenguajes de Programacion I", 3, 2).
materia(6324, "Sistemas Operativos I", 3, 2).
materia(6325, "Investigacion Operativa I", 3, 2).
materia(6411, "Arquitectura de Computadoras y Tecnicas Digitales", 4, 1).
materia(6412, "Teoria de la Informacion", 4, 1).
materia(6413, "Comunicacion de Datos II", 4, 1).
materia(6414, "Introduccion al Calculo Diferencial e Integral", 4, 1).
materia(6421, "Diseno de Sistemas de Software", 4, 2).
materia(6422, "Diseno de Compiladores I", 4, 2).
materia(6511, "Ingenieria de Software", 5, 1).

% correlativas(Codigo,CodigosCorrelativas)
correlativas(6122, 6111).
correlativas(6123, 6113).
correlativas(6124, 6112).
correlativas(6125, 6113).
correlativas(6211, [6121, 6122, 6125]).
correlativas(6212, [6121, 6122, 6125]).
correlativas(6213, 6122).
correlativas(6214, 6112).
correlativas(6215, 6124).
correlativas(6221, [6211, 6212]).
correlativas(6222, 6213).
correlativas(6223, [6214, 6123, 6125]).
correlativas(6224, 6215).
correlativas(6311, 6221).
correlativas(6312, [6221, 6223]).
correlativas(6313, 6221).
correlativas(6314, [6213, 6224]).
correlativas(6321, 6221).
correlativas(6322, [6312, 6313]).
correlativas(6323, 6311).
correlativas(6324, [6312, 6314]).
correlativas(6325, [6214, 6223]).
correlativas(6411, 6314).
correlativas(6412, [6212, 6222, 6223]).
correlativas(6413, [6222, 6324]).
correlativas(6414, 6214).
correlativas(6421, [6311, 6322, 6324]).
correlativas(6422, 6323).
correlativas(6511, 6421).

% Materias aprobadas
cursada_aprobada(6111).
cursada_aprobada(6112).
cursada_aprobada(6113).
cursada_aprobada(6114).
cursada_aprobada(6121).
cursada_aprobada(6122).
cursada_aprobada(6123).
cursada_aprobada(6124).
cursada_aprobada(6125).
cursada_aprobada(6211).
cursada_aprobada(6212).
cursada_aprobada(6213).
cursada_aprobada(6214).
cursada_aprobada(6215).
cursada_aprobada(6221).
cursada_aprobada(6222).
cursada_aprobada(6224).
cursada_aprobada(6311).
cursada_aprobada(6313).
cursada_aprobada(6314).

% Finales aprobados
final_aprobado(6111).
final_aprobado(6112).
final_aprobado(6113).
final_aprobado(6114).
final_aprobado(6121).
final_aprobado(6122).
final_aprobado(6123).
final_aprobado(6124).
final_aprobado(6125).
final_aprobado(6211).
final_aprobado(6213).
final_aprobado(6214).
final_aprobado(6215).
final_aprobado(6222).
final_aprobado(6223).
final_aprobado(6313).
final_aprobado(6314).

% Materias que curso, dias y horarios
cursada(6223, [lunes, viernes], 8, 11).
cursada(6321, miercoles, 13, 14).
cursada(6323, [martes, jueves], 13, 16).



%%%% REGLAS %%%%

% Consulta que devuelve los dias y horarios de cursada de una materia
cursa_horarios(Nombre, Dias, HorarioInicio, HorarioFin) :-
    materia(Codigo, Nombre, _, _),
    cursada(Codigo, Dias, HorarioInicio, HorarioFin).

% Consultas de materias
cursada_no_aprobada(Codigo) :- materia(Codigo, _, _, _), not(cursada_aprobada(Codigo)).
final_no_aprobado(Codigo) :- materia(Codigo, _, _, _), not(final_aprobado(Codigo)).

% Consultas que devuelven listas
materias_cursadas(Lista) :- findall(Nombre, (cursada_aprobada(Codigo), materia(Codigo, Nombre, _, _)), Lista).
materias_cursando(Lista) :- findall(Nombre, (cursada(Codigo,_,_,_), materia(Codigo, Nombre, _, _)), Lista).
materias_finales(Lista) :- findall(Nombre, (final_aprobado(Codigo), materia(Codigo, Nombre, _, _)), Lista).
materias_finales_pendientes(Lista) :- findall(Nombre, (cursada_aprobada(Codigo), final_no_aprobado(Codigo), materia(Codigo, Nombre, _, _)), Lista).
materias_no_cursadas(Lista) :- findall(Nombre, (materia(Codigo, Nombre, _, _), not(cursada_aprobada(Codigo))), Lista).
materias_cursa_dia(Dia, Lista) :- findall(Nombre, (cursada(Codigo, Dias, _, _), member(Dia, Dias), materia(Codigo, Nombre, _, _)), Lista).
lenguajes_que_programo(Lista) :- findall(Lenguaje, programa(Lenguaje), Lista).
grupo_de_amigos(Lista) :- findall(Amigo, es_amigo(Amigo), Lista).





