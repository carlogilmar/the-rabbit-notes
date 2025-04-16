menu :- repeat,nl,nl,
    write('Bienvenido al primer programa en prolog para listas'),nl,
    write('1. Mostrar lista A en horizontal'),nl,
    write('2. Mostrar la lista A en vertical'),nl,
    write('3. Agregar un elemento al final'),nl,
    write('4. Agregar un elemento al inicio'), nl,
    write('5. Borrar un elemento de la lista A'), nl,
    write('6. Unir dos listas A y B'), nl,
    write('               7.- para salir'),nl,
    write('Coloca el numero de opcion seguido de un punto final-->'),nl,nl,
    read(Choice), Choice>0, Choice<8,
    doit(Choice).

doit(1):-
    write('Bienvenido a la opcion 1'),nl,
    write('Mostrando lista A en vertical:'), nl,
    escribe([1,2,3,4]).

		escribe([]).
		escribe([X|Y]):-
				write(X),nl,
				escribe(Y).

doit(2):-
	write('Bienvenido al complemento de la opc 2'),nl,
	write('Mostrando lista A en horizontal: '), nl,
	hori([1,2,3,4]).

		hori([]).
		hori([X|Y]):-
				write(X),
				hori(Y).


doit(3):-
	write('Bienvenido a la opcion 3'),nl,
	write('Agregar elemento al final de la lista A [1,2,3,4]'),nl,
	write('Dame un elemento -->'),
	read(X),
	añadir_por_detras([1,2,3,4],X,Lista_nueva), 
	hori(Lista_nueva).

			concatenar([],L,L).
		    concatenar([A|B], X, [A|C]):- concatenar(B,X,C).

		    añadir_por_detras([],[E],[E]).
		    añadir_por_detras([X|Xs],E,[X|Xz]):-concatenar(Xs,[E],Xz).

doit(4):-
	write('Bienvenido a la opcion 4'),nl,
	write('Agregar elemento al inicio de la lista A [1,2,3,4]'),nl,
	write('Dame un elemento -->'),
	read(X),
	añadir_por_delante([1,2,3,4],X,Lista_nueva), 
	hori(Lista_nueva).

			añadir_por_delante([X|Xs],E,R):-concatenar([E],[X|Xs],R).

doit(5):-
	write('Bienvenido a la opcion 5'),nl,
	write('Borrar un elemento de la lista A [1,2,3,4]'),nl,
	write('Dame el elemento a borrar-->'),
	read(X),
	eliminar_elemento([1,2,3,4],X,Nueva),
	hori(Nueva).

			    eliminar_elemento([X|C],X,C).
			    eliminar_elemento([Y|C1],E,[Y|C2]):-eliminar_elemento(C1,E,C2).

doit(6):-
	write('Bienvenido a la opcion 6'),nl,
	write('Uniendo la lista A [1,2,3,4] con la B [a,b,c,d]'),nl,
	concatenar([1,2,3,4], [a,b,c,d], Union),
	hori(Union).


doit(7):-
	nl,
	write("---------------------------------"),nl,
	write("Arnold Alois Schwarzenegger as Terminator says: See U Babe "),nl,
	write(">>>----------------------------->"),
	!.



