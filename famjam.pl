male(manan).
male(sanjay).
male(m1).
male(m2).
female(dhruvi).
female(jagruti).
female(f1).
female(f2).
parent(sanjay,manan).
parent(sanjay,dhruvi).
parent(jagruti,manan).
parent(jagruti,dhruvi).
parent(m1,sanjay).
parent(f1,sanjay).
parent(m2,jagruti).
parent(f2,jagruti).

grandparent(X,Y):- parent(X,Z),parent(Z,Y).
grandmother(X,Z):- mother(X,Y), parent(Y,Z).
grandfather(X,Z):- father(X,Y),parent(Y,Z).
father(X,Y):- parent(X,Y), male(X).
mother(X,Z):- parent(X,Z),female(X).
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).
husband(X,Y):-parent(X,Z),parent(Y,Z),female(Y),male(X).


