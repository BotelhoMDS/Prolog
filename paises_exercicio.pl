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
pais(franca,america,0.2). %Guiana Francesa,guadalupe,martinica
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
pais(mexico,america,127). 
pais(canada,america,38). 
pais(honduras,america,10). 
pais(guatemala,america,17). 
pais(belize,america,0.4). 
pais(el_salvador,america,6).
pais(cuba,america,11). 
pais(costa_rica,america,5). 
pais(panama,america,4). 
pais(nicaragua,america,6). 
pais(jamaica,america,3). 
pais(haiti,america,11). 
pais(republica_dominicana,america,11). 
pais(porto_rico,america,3). 
pais(aruba,america,0.1). 
pais(barbados,america,0.2). 
pais(curacao,america,0.1). 
pais(granada,america,0.1). 
pais(trindade_e_tobago,america,1). 
pais(santa_lucia,america,0.1). 



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
fronteira(brasil,uruguai). 
fronteira(brasil,argentina). 
fronteira(brasil,bolivia). 
fronteira(brasil,paraguai). 
fronteira(brasil,colombia). 
fronteira(brasil,suriname). 
fronteira(brasil,venezuela). 
fronteira(brasil,guiana). 
fronteira(argentina,bolivia). 
fronteira(argentina,uruguai). 
fronteira(argentina,chile). 
fronteira(argentina,paraguai). 

juntos(Xpais,Ypais) :- fronteira(Xpais,Ypais);fronteira(Ypais,Xpais). 
paises_continente(Paises,Continente) :- findall(Pais,pais(Pais,Continente,_),Paises).
paises_grandes(Paises,Continente) :- findall(Pais,(pais(Pais,Continente,Populacao),Populacao>=100),Paises).
