from pyswip import Prolog
prolog = Prolog()
prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")
list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
for i in prolog.query("father(X,Y)"):
    print(i["X"], "is the father of", i["Y"]) # i yerine soln yazıyordu beğenmediğim için değiştirdim :)
# michael is the father of john
# michael is the father of gina