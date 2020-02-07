hasValue('NorthSensor', S1) :- perception([S1, _, _, _]).
hasValue('WestSensor', S2) :- perception([_, S2, _, _]).
hasValue('EastSensor', S3) :- perception([_, _, S3, _]).
hasValue('SouthSensor', S4) :- perception([_, _, _, S4]).

takeDecision('North') :-
    hasValue('NorthSensor', 'False'), !.

takeDecision('West') :-
    hasValue('WestSensor', 'False'), !.

takeDecision('East') :-
    hasValue('EastSensor', 'False'), !.

takeDecision('South') :-
    hasValue('SouthSensor', 'False').