(deftemplate Metricas_Agua
	(multislot Temperatura_Y_Oxigeno_disuelto
		(type FLOAT)
		(default ?DERIVE)
	)
	(slot pH
		(type FLOAT)
		(default ?DERIVE)
	)
	(multislot Solidos_disueltos_Y_Conductividad
		(type NUMBER)
		(default ?DERIVE)
	)
	(slot Dias_desde_lluvia
		(type NUMBER)
		(default ?DERIVE)
	)
	(slot Caudal
		(type SYMBOL)
		(default normal)
		(allowed-symbols bajo normal alto)
	)
	(slot Sedimentos_suspendidos
		(type FLOAT)
		(default ?DERIVE)
	)
	(slot Trasnparencia
		(type NUMBER)
		(default 1)
	)
	(slot Eutrofizacion
		(type SYMBOL)
		(default nula)
		(allowed-symbols nula baja alta)
	)
	(slot Fuente_metales
		(type STRING)
		(default ?DERIVE)
	)
	(slot Metales_peces
		(type FLOAT)
		(default ?DERIVE)
	)
	(slot Ecoli
		(type NUMBER)
		(default ?DERIVE)
	)
	(slot Nitratos
		(type FLOAT)
		(default ?DERIVE)
	)
)

(deffunction testAgua(?tm ?od ?ph ?sd ?cd ?dl ?cl ?ss ?tp ?et ?fm ?mp ?ec ?nt)
	(assert
		(Metricas_Agua 
			(Temperatura_Y_Oxigeno_disuelto ?tm ?od)
			(pH ?ph)
			(Solidos_disueltos_Y_Conductividad ?sd ?cd)
			(Dias_desde_lluvia ?dl)
			(Caudal ?cl)
			(Sedimentos_suspendidos ?ss)
			(Trasnparencia ?tp)
			(Eutrofizacion ?et)
			(Fuente_metales ?fm)
			(Metales_peces ?mp)
			(Ecoli ?ec)
			(Nitratos ?nt)
		)
	)
)

(deftemplate Datos
	(slot dato
		(type NUMBER)
		(default ?DERIVE)
	)
)

(deftemplate Resultado
	(slot respuesta
		(type STRING)
		(default ?DERIVE)
	)
)

(defrule Test_Agua
	(Metricas_Agua 
		(Temperatura_Y_Oxigeno_disuelto ?tm ?od)
		(pH ?ph)
		(Solidos_disueltos_Y_Conductividad ?sd ?cd)
		(Dias_desde_lluvia ?dl)
		(Caudal ?cl)
		(Sedimentos_suspendidos ?ss)
		(Trasnparencia ?tp)
		(Eutrofizacion ?et)
		(Fuente_metales ?fm)
		(Metales_peces ?mp)
		(Ecoli ?ec)
		(Nitratos ?nt)
	)
=>
	(bind ?total 0)
	(if
		(or
			(< ?tm 4.0)(> ?od 12.0)
		)then
		(bind ?total (- ?total 5))
		else
		(if
			(or
				(>= ?tm 40.0)(< ?od 7.0)
			)then
			(bind ?total (- ?total 5))
		)
	)
	(if
		(or
			(<= ?ph 6.5)(>= ?ph 9.0)
		)then
		(bind ?total (- ?total 10))
	)
	(if
		(and
			(> ?ph 6.5)(< ?ph 9.0)
		)then
		(bind ?total (+ ?total 10))
	)
	(if
		(or
			(>= ?sd 1000)(>= ?cd 600)
		)then
		(bind ?total (- ?total 15))
	)
	(if
		(<= ?dl 3)then
		(bind ?total (- ?total 1))
	)
	(if
		(eq ?cl bajo)then
		(bind ?total (+ ?total 1))
	)
	(if
		(eq ?cl normal)then
		(bind ?total (+ ?total 3))
	)
	(if
		(eq ?cl alto)then
		(bind ?total (- ?total 3))
	)
	(if
		(> ?ss 25)then
		(bind ?total (- ?total 3))
	)
	(if
		(> ?tp 5)then
		(bind ?total (- ?total 5))
	)
	(if
		(< ?tp 5)then
		(bind ?total (+ ?total 5))
	)
	(if
		(eq ?et nula)then
		(bind ?total (+ ?total 5))
	)
	(if
		(eq ?et baja)then
		(bind ?total (- ?total 10))
	)
	(if
		(eq ?et alta)then
		(bind ?total (- ?total 20))
	)
	(if
		(eq ?fm "Erosion")then
		(bind ?total (- ?total 3))
	)
	(if
		(eq ?fm "Industria")then
		(bind ?total (- ?total 10))
	)
	(if
		(> ?mp 1.0)then
		(bind ?total (- ?total 5))
	)
	(if
		(> ?ec 394)then
		(bind ?total (- ?total 10))
	)
	(if
		(> ?nt 1.0)then
		(bind ?total (- ?total 5))
	)
	(assert (Datos (dato ?total)))
)

(defrule Resultado_Test
	(Datos (dato ?d))
=>
	(if
		(> ?d 0)then
		(assert (Resultado (respuesta "Aceptable")))
	else
		(assert (Resultado (respuesta "Inaceptable")))
	)
)
