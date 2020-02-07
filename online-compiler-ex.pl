hasValue('FrontColorSensor', 'Red').
hasValue('RightColorSensor', 'Yellow').
hasValue('LeftColorSensor', 'Red').

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'White'), !.
%if true dont look for the remainings = cut operator

%prolog decisionunu liste olarak alıp her item için iterate etmek
%gerekebilir. örn decisionlar MoveForward ve Eat ise, sırasıyla
%çalıştırılırlar

%+++++++++++ front sarıysa ilerle sonra yemek ye
takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Yellow').

takeDecision('Eat') :-
    hasValue('FrontColorSensor', 'Yellow'), !.

takeDecision('TurnRight') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'White').

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'White'), !.

%+++++++++++ front kırmızı ve sağ sarıysa sağa dön sonra ilerle, sonra yemek ye
takeDecision('TurnRight') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Yellow').

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Yellow').

takeDecision('Eat') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Yellow'), !.
%+++++++++++ front kırmızı ve sağ kırmızıysa ve sol beyazsa sola dön sonra ilerle

takeDecision('TurnLeft') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'White').

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'White'), !.

%+++++++++++ front kırmızı ve sağ kırmızıysa ve sol sarıysa sola dön sonra ilerle sonra yemek ye

takeDecision('TurnLeft') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'Yellow').

takeDecision('MoveForward') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'Yellow').

takeDecision('Eat') :-
    hasValue('FrontColorSensor', 'Red'), hasValue('RightColorSensor', 'Red'), hasValue('LeftColorSensor', 'Yellow'), !.

%+++++++++++ front kırmızı ve sağ kırmızı ve sol kırmızıysa
