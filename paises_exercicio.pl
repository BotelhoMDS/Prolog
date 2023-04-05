% Base de Fatos

%Definição de continentes
continente(asia). 
continente(america). 
continente(africa).
continente(oceania). 
continente(europeu). 

%Definição do pais, seu continente e sua população
pais(portugal,europa,10). 
pais(franca,europa,65). 
pais(espanha,europa,46). 
pais(belgica,europa,11). 
pais(alemanha,europa,83). 
pais(holanda,europa,17). 
pais(china,asia,1400).
pais(mongolia,asia,3). 
pais(vietnam,asia,97). 
pais(laos,asia,7).
pais(india,aisa,1408). 
pais(russia,asia,143).
pais(russia,europa,143).
pais(eua,america,330).
pais(franca,america,0.2). %Guiana Francesa
pais(brasil,america,250). 
pais(colombia,america,50). 
pais(argentina,america,45). 
pais(peru,america,34). 
pais(venezuela,america,32). 
pais(chile,america,19).
pais(equador,america,17). 
pais(bolivia,america,11). 
pais(paraguai,america,7). 
pais(uruguai,america,3). 
pais(guiana,america,0.7). 
pais(suriname,america,0.5).


%definição das fronteiras de um pais

fronteira(portugal,espanha). 
fronteira(franca,espanha). 
fronteira(franca,belgica). 
fronteira(franca,brasil).
fronteira(franca,guiana).
fronteira(franca,suriname). 
fronteira(belgica,alemanha). 
fronteira(belgica,holanda). 
fronteira(alemanha,holanda). 
fronteira(alemanha,franca). 
fronteira(china,mongolia). 

juntos(Xpais,Ypais) :- fronteira(Xpais,Ypais);fronteira(Ypais,Xpais). 
paises_continente(Paises,Continente) :- findall(Pais,pais(Pais,Continente,_),Paises).
paises_grandes(Paises,Continente) :- findall(Pais,(pais(Pais,Continente,Populacao),Populacao>=100),Paises).
