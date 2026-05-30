






$$ R_{sh} = \frac{(R_g +R_c) \cdot I_{g, \, max} }{I_{Rango} - I_{g, \, max}} \quad ; \, R_c = 4.7 \, \Omega$$





hay algo q necesito cambiar del trabajo previo  
  
en el laboratorio ya habian resistencias shunt, hechas con nicrom, de valores 4.7 y 9.4 ohm,  
  
entonces para evitar hacer resistencias nuevas busque un valor para q Rsh1 fuese 4.7  
  
en papel plantee la ecuacion:  
  
$$ R_{sh} = \frac{(R_g +R_c) \cdot I_{g, \, max} }{I_{Rango} - I_{g, \, max}} \quad ; \, R_{sh3}= 4.7 \, \Omega$$  
  
entonces en mi ti nspire hice  
  
$$ Solve ( \frac{(R_g +R_c) \cdot I_{g, \, max} }{I_{Rango} - I_{g, \, max}} = 4.7, R_c)  $$
  



con I_g,max = 1 mA nominal y R_g = 380 ohm medidos en laboratorio con multitester
  
así obtuve  

  
R_3 (100 mA) =(Rc + Rg) / 9 4.7 (valor forzado)

entonces R_c = 85.3 ohm

luego iteré la formula para las demas resistencias shunt:

R_2 (50 mA) = (Rc + Rg) / 49 = 9.49 ohm

R_3 (10 mA) = (Rc + Rg) / 99

(nota para antigravity:

no hubo trabajo previo teorico-numerico, lo teorico fue el estudio y planteamiento de la ecuacion para obtener Rsh, pero se hayaron valores numericos con los valores Rc, Rg, Rsh3 = 4.7 y Rsh2 = ~9.4)



se requiere calcular valores seguros de variacion para la resistencia de caalibracion Rc sujeto a Ig, max +-10%

se plantea:
(( It - Ig) Rsh ) / (Rc + Rg) = Ig,  con Ig = {0.9, 1.1}

luego se resuelve con calculadora CAS

se obtienen los siguientes valores 

 

Tabla: valores R_c

| R_c      | 1.1 (+10%) | 1.0 +-0% | 0.9 (-10%) |
| -------- | ---------- | -------- | ---------- |
| R3 100ma | 42.58      | 85.3     | 137.52     |
| R2 50ma  | 41.87      | 85.3     | 137.73     |
| R1 10ma  | 38.3       | 85.3     | 142.74     |


dadas las restricciones de Ig +-10% se elige el supremo de la cota inferior -10% y el infimo de la cota superior +10%

entonces Rc puede variar entre 38.3 y 137.52 ohms









Necesito q cambies el orden del marco teorico

1. Calculo de resistencias shunt, con - Parámetros: Ig,max​=1 mA, Rg​=380 Ω y Forzado a Rsh3​=4.7 Ω
   
2. ###  Análisis de Tolerancia de Rcal​ / Rc​ (Inciso d)

 3. Calculo de largo de alambre de nicrom, respecto al valor de las resistencias shunt
    
4. topología del circuito y Protección
	1. Vop​=0.7 V
	2. valores extremos +-10% Ig
	3. 1.1 * 465.3 = 0.511 V
	4. 0.9 * 465.3 = 0.418 V
	5. Nunca conduce el diodo estando en el rango seguro, o sea a plena escala

 5. Circuito de contrastacion y resistencias limitadoras:
     standby, tengo q diseñar esta parte. planea para las partes anteriores por ahora









Acerca del diseño de la seccion 5 del trabajo previo, quiero q me ayudes a diseñarlo.  
  
lee de Experiencia_03.md la seccion 4.Estudios y trabajos previos a la experiencia, inciso h:  
  
Realice/diseñe el circuito de contrastación para cada instrumento y el circuito de va-

lidación con el cual estudiará el error sistemático. Para el caso del amperímetro los

circuitos deberán contar con dos resistencias limitadoras en serie: una fija ajus-

tada a la máxima corriente de ensayo y la otra variable para dar el ajuste requerido.

Calcule ambas resistencias (valores de resistencia y de corriente máxima) si usa una

fuente electrónica de tensión de 10Vcc.  
  
  
aqui pasa algo curioso. considera:  
  
estas experiencias tiene por lo menos 10 años de antiguedad, solo se les cambia la fecha al semestre actual y se hacen pequeños ajustes custom segun el ayudante de turno  
  
se menciona fuente 10Vcc. esto, asumo en el caso de fuente constante. pero en la experiencia tuvimos una fuente electronica 0-30 Vcc. para mantener rigor se usaron 10Vcc  
  
aunque si se ve el hito 2.4. Amperímetro analógico inciso g:  
  
Aplique 10Vcc a 3 resistores en paralelo, de tal manera que por cada uno de ellos

circule una corriente que sea medible en al menos un rango de su amperímetro y de

la fuente en la escala más apropiada. Considere que para la medición de la corriente

total no puede superar el rango máximo de su amperímetro (rango de 100 mA) y la

corriente de cada uno de los resistores debe ser apropiada para cada uno de los rangos

(buscando medir de manera adecuada). Indique el valor real y el valor medido en cada

caso, considere el error sistemático, la contrastación del punto anterior y si lo sabe el

error admisible. (Sea claro en cada paso)  
  
acá no ponia requisitos de resistencias especificas, asi q en la experiencia use:  

R1 = 0.981k ohm  
R2 = 146.5 0hm  
R3 = 99.1 ohm

si saco resistencia equivalente ( sum 1/R_i)^-1 me da R_eq = 55.753 ohm, entonces I = 10 / R_eq = 179.36 mA, 

aqui veo q la corriente total es mayor a 1.1 mA, el rango limite para el gaalvanometro

pero yo considere estas resistencias tal q la menor 99.1 ohm, me arrojara I_R3 = 10/99.1 = 100.3 mA, estando en plena escala

aqui, ayudame a discernir en 4.Estudios y trabajos previos a la experiencia, inciso h, se me exije medir la corriente total en algun caso? o solo debo medir la corriente de cada resistencia?




  
R1 = 0.981k ohm  
R2 = 328.5 0hm  
R3 = 1.496k ohm


si saco resistencia equivalente ( sum 1/R_i)^-1 me da R_eq = 211.12 ohm, entonces I = 10 / R_eq = 77.856 mA,  q








h.- Realice/diseñe el circuito de contrastación para cada instrumento y el circuito de va-
lidación con el cual estudiará el error sistemático. Para el caso del amperímetro los
circuitos deberán contar con dos resistencias limitadoras en serie: una fija ajus-
tada a la máxima corriente de ensayo y la otra variable para dar el ajuste requerido.
Calcule ambas resistencias (valores de resistencia y de corriente máxima) si usa una
fuente electrónica de tensión de 10Vcc.




nota:
hacer circuito trabajo orevio circuit de contrstacion

hacer cricutio conmutacion 3 resistencias paralelas

tienees circuit3tikz instalado
localizar directorio en users ->npm start

debes indicarle a antigravity cuando se de por terminado el trabajo previo, ir afinando estilo de escritura, lo ideal seria q luego de unos cuantos prompts le diga q haga un sumario de como te gusta el estilo y redaccion para q lo copie en su skill


sumado a esto, deberias evitar redundancias, exceso verbose casa fatiga en lector


driven by metrologiavault fuente, recordar skill, context rot

mejor empezar nuevo chat o buscar skill/framework anticontextrot


![[plan_inf3_2_perf]]


