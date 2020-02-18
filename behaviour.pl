hasValue('FrontColorSensor', S1) :- perception([S1, _, _]).
hasValue('RightColorSensor', S2) :- perception([_, S2, _]).
hasValue('LeftColorSensor', S3) :- perception([_, _, S3]).


takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Green').
takeDecision('Eat') :-
    hasValue('FrontColorSensor', 'Green'), !.

takeDecision('RotateRight') :-
    hasValue('RightColorSensor', 'Green').
takeDecision('Eat') :-
    hasValue('RightColorSensor', 'Green'), !.

takeDecision('RotateLeft') :-
    hasValue('LeftColorSensor', 'Green').
takeDecision('Eat') :-
    hasValue('LeftColorSensor', 'Green'), !.

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Yellow'), !.

takeDecision('RotateRight') :-
    hasValue('RightColorSensor', 'Yellow'), !.

takeDecision('RotateLeft') :-
    hasValue('LeftColorSensor', 'Yellow'), !.


%MoveBackward for vrep
takeDecision('TurnBackward') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'Red'),!.
