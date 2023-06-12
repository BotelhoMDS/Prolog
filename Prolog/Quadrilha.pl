%Quadrilha de Carlos Drummond de Andrade. 
amava(joao, teresa).
amava(teresa, raimundo). 
amava(raimundo, maria). 
amava(maria, joaquim). 
amava(joaquim, lili). 
amava(lili, ninguem).
foi_para(X,estados_unidos) :- amava(X,teresa). 
foi_para(X,convento) :- amava(X, raimundo).
morreu(X, desastre) :- amava(X, maria). 
morreu(X, suicidio) :- amava(X, lili). 
tornou(X, tia) :- amava(X, joaquim). 
casou(X, j_pinto_fernandes) :- amava(X,ninguem). 
situacao(X, foi_para) :- foi_para(X, estados_unidos) ; foi_para(X, convento).
situacao(X, morreu) :- morreu(X, desastre) ; morreu(X, suicidio). 
situacao(X, tornou) :- tornou(X, tia). 
situacao(X, casou) :- casou(X, j_pinto_fernandes).
poema :- amava(Nome,teresa), write(Nome),
write(" amava "), amava(Nome, Amado), write(Amado) ,write(" que amava "),
amava(Amado, Amado2), write( Amado2), write(" que amava "), amava(Amado2, Amado3), 
write(Amado3), write(" que amava "),amava(Amado3 , Amado4), write(Amado4), write(" que amava "), 
amava(Amado4, Amado5), write(Amado5), write(" que não amava "), amava(Amado5, Ultimo_amado), 
write(Ultimo_amado), write(".").    
