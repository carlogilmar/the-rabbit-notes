list_length([], 0).
list_length([_|Ls], N):-
        N #> 0,
        N #= N0 + 1,
        list_length(Ls, N0).
