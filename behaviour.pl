hasValue('FrontColorSensor', S1) :- perception([S1, _, _]).
hasValue('RightColorSensor', S2) :- perception([_, S2, _]).
hasValue('LeftColorSensor', S3) :- perception([_, _, S3]).


takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Yellow').
takeDecision('Eat') :-
    hasValue('FrontColorSensor', 'Yellow'), !.

takeDecision('TurnRight') :-
    hasValue('RightColorSensor', 'Yellow').
takeDecision('MoveForward') :-
    hasValue('RightColorSensor', 'Yellow').
takeDecision('Eat') :-
    hasValue('RightColorSensor', 'Yellow'), !.

takeDecision('TurnLeft') :-
    hasValue('LeftColorSensor', 'Yellow').
takeDecision('MoveForward') :-
    hasValue('LeftColorSensor', 'Yellow').
takeDecision('Eat') :-
    hasValue('LeftColorSensor', 'Yellow'), !.

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'White'), !.

takeDecision('TurnRight') :-
    hasValue('RightColorSensor', 'White').
takeDecision('MoveForward') :-
    hasValue('RightColorSensor', 'White'), !.

takeDecision('TurnLeft') :-
    hasValue('LeftColorSensor', 'White').
takeDecision('MoveForward') :-
    hasValue('LeftColorSensor', 'White'), !.



takeDecision('TurnBackward') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'Red'),!.
