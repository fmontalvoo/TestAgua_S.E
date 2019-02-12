(deftemplate Resultado
	(slot resultado
		(type FLOAT)
		(default ?DERIVE)
	)
)

(deftemplate Calidad
	(slot calidad
		(type STRING)
		(default ?DERIVE)
	)
)

(deffunction tablaOxigeno (?val)
	(if (= ?val 1) then (bind ?y 14.19))
	(if (= ?val 2) then (bind ?y 13.81))
	(if (= ?val 3) then (bind ?y 13.44))
	(if (= ?val 4) then (bind ?y 13.09))
	(if (= ?val 5) then (bind ?y 12.75))
	(if (= ?val 6) then (bind ?y 12.43))
	(if (= ?val 7) then (bind ?y 12.12))
	(if (= ?val 8) then (bind ?y 11.83))
	(if (= ?val 9) then (bind ?y 11.55))
	(if (= ?val 10) then (bind ?y 11.27))
	(if (= ?val 11) then (bind ?y 11.01))
	(if (= ?val 12) then (bind ?y 10.76))
	(if (= ?val 13) then (bind ?y 10.52))
	(if (= ?val 14) then (bind ?y 10.29))
	(if (= ?val 15) then (bind ?y 10.07))
	(if (= ?val 16) then (bind ?y 9.85))
	(if (= ?val 17) then (bind ?y 9.65))
	(if (= ?val 18) then (bind ?y 9.45))
	(if (= ?val 19) then (bind ?y 9.26))
	(if (= ?val 20) then (bind ?y 9.07))
	(if (= ?val 21) then (bind ?y 8.90))
	(if (= ?val 22) then (bind ?y 8.72))
	(if (= ?val 23) then (bind ?y 8.56))
	(if (= ?val 24) then (bind ?y 8.40))
	(if (= ?val 25) then (bind ?y 8.24))
	(if (= ?val 26) then (bind ?y 8.09))
	(if (= ?val 27) then (bind ?y 7.95))
	(if (= ?val 28) then (bind ?y 7.81))
	(if (= ?val 29) then (bind ?y 7.67))
	(if (= ?val 30) then (bind ?y 7.54))
	(if (= ?val 31) then (bind ?y 7.41))
	(if (= ?val 32) then (bind ?y 7.28))
	(if (= ?val 33) then (bind ?y 7.16))
	(if (= ?val 34) then (bind ?y 7.05))
	(if (= ?val 35) then (bind ?y 6.93))
	(if (= ?val 36) then (bind ?y 6.82))
	(if (= ?val 37) then (bind ?y 6.71))
	(if (= ?val 38) then (bind ?y 6.61))
	(if (= ?val 39) then (bind ?y 6.51))
	(if (= ?val 40) then (bind ?y 6.41))
	(if (= ?val 41) then (bind ?y 6.31))
	(if (= ?val 42) then (bind ?y 6.22))
	(if (= ?val 43) then (bind ?y 6.13))
	(if (= ?val 44) then (bind ?y 6.04))	
	(return ?y)
)

(deffunction saturacion(?tmm)
	(bind ?ox (tablaOxigeno ?tmm))
	(bind ?y (/ (* 1 100) ?ox))
	(return ?y)
)

(defrule Resultado_Test
	(Resultado (resultado ?total))
=>
	(if
		(and
			(>= ?total 91)(<= ?total 100)
		)then
			(assert (Calidad (calidad "Excelente")))	
	)
	(if
		(and
			(>= ?total 71)(<= ?total 90.99)
		)then
			(assert (Calidad (calidad "Buena")))
	)
	(if
		(and
			(>= ?total 51)(<= ?total 70.99)
		)then
			(assert (Calidad (calidad "Regular")))	
	)
	(if
		(and
			(>= ?total 26)(<= ?total 50.99)
		)then
			(assert (Calidad (calidad "Mala")))	
	)
	(if
		(and
			(>= ?total 0)(<= ?total 25.99)
		)then
			(assert (Calidad (calidad "Pesima")))	
	)
)

(deffunction coliformes(?cl)
	(if	
		(<= ?cl 3)	
	then
		(bind ?y 97.0)
	else
		(if
			(> ?cl 10e4)
		then
			(bind ?y 3.0)	
		else
			(bind ?y (* 141.1 (** ?cl -0.294)))	
		)			
	)
	(return ?y)
)

(deffunction pH(?ph)
	(if	
		(<= ?ph 2)	
	then
		(bind ?y 2.0)
	else
		(if
			(>= ?ph 12)
		then
			(bind ?y 3.0)	
		else
			(bind ?y (+ (* -0.0192(** ?ph 6)) (* 0.8353 (** ?ph 5)) (* -14.167 (** ?ph 4)) (* 117.99 (** ?ph 3)) (* -501.51 (** ?ph 2)) (* 1032.6 ?ph) -802.79 ))	
		)			
	)
	(return ?y)
)

(deffunction dbo(?db)
	(if	
		(< ?db 0)	
	then
		(bind ?y 98.0)
	else
		(if
			(>= ?db 30)
		then
			(bind ?y 2.0)	
		else
			(bind ?y (+ (* 1e-05 (** ?db 4)) (* -0.0065 (** ?db 3)) (* 0.4108 (** ?db 2)) (* -9.9735 ?db) 98.426 ))			
		)
	)
	(return ?y)
)

(deffunction nitratos(?nt)
	(if	
		(< ?nt 1)	
	then
		(bind ?y 96.0)
	else
		(if
			(>= ?nt 90)
		then
			(bind ?y 2.0)	
		else
			(bind ?y (+ (* -21.09 (log ?nt)) 96.838 ))
		)			
	)
	(return ?y)
)

(deffunction fosfatos(?ff)
	(if	
		(< ?ff 0)	
	then
		(bind ?y 99.0)
	else
		(if
			(> ?ff 10)
		then
			(bind ?y 5.0)	
		else
			(bind ?y (+ (* 0.004 (** ?ff 6)) (* -0.1411 (** ?ff 5)) (* 1.9875 (** ?ff 4)) (* -14.007 (** ?ff 3)) (* 51.73 (** ?ff 2)) (* -98.403 ?ff) 99.801 ))
		)			
	)
	(return ?y)
)

(deffunction temperatura(?tm)
	(if	
		(< ?tm -5)	
		then
		(bind ?y 56)
		else
		(if
			(> ?tm 15)
		then
			(bind ?y 9.0)	
		else
			(bind ?y (+ (* -0.0082 (** ?tm 4)) (* 0.2273 (** ?tm 3)) (* -1.475 (** ?tm 2)) (* -6.8833 ?tm) 92 ))
		)			
	)
	(return ?y)
)

(deffunction turbidez(?tb)
	(if	
		(< ?tb 0)	
	then
		(bind ?y 100)
	else
		(if
			(> ?tb 96)
		then
			(bind ?y 5.0)	
		else
			(bind ?y (+ (* 1.8356e-06 (** ?tb 4)) (* -0.0005 (** ?tb 3)) (* 0.0481 (** ?tb 2)) (* -2.5989 ?tb) 98 ))
		)			
	)
	(return ?y)
)

(deffunction solidos(?sd)
	(if	
		(< ?sd 0)	
	then
		(bind ?y 80.0)
	else
		(if
			(> ?sd 500)
		then
			(bind ?y 30.0)	
		else
			(bind ?y (+ (* 1.0256e-11 (** ?sd 5)) (* -1.7435e-08 (** ?sd 4)) (* 0.000010958 (** ?sd 3)) (* -0.003174 (** ?sd 2)) (* 0.2883 ?sd) 79.105 ))
		)			
	)
	(return ?y)
)

(deffunction oxigeno(?ox)
	(if	
		(<= ?ox 0)	
	then
		(bind ?y 0)
	else
		(if
			(> ?ox 140)
		then
			(bind ?y 47.0)	
		else
			(bind ?y (+ (* 4e-11 (** (- (/ ?ox 1.1) 22.0130338686347) 6)) (* 2e-08 (** (- (/ ?ox 1.1) 22.0130338686347) 5)) (* -1e-05 (** (- (/ ?ox 1.1) 22.0130338686347) 4)) (* 0.001 (** (- (/ ?ox 1.1) 22.0130338686347) 3)) (* -0.0305 (** (- (/ ?ox 1.1) 22.0130338686347) 2)) (* 0.8703 (- (/ ?ox 1.1) 22.0130338686347)) 46.1600 ))
		)			
	)
	(return ?y)
)

(deffunction testAgua(?cl ?ph ?db ?nt ?ff ?tma ?tmm ?tb ?sd)
	(bind ?total (+ (* (coliformes ?cl) 0.15) (* (pH ?ph) 0.12) (* (dbo ?db) 0.1) (* (nitratos ?nt) 0.1) (* (fosfatos ?ff) 0.1) (* (temperatura (- ?tma ?tmm)) 0.1) (* (turbidez ?tb) 0.08) (* (solidos ?sd) 0.08) (* (oxigeno (saturacion ?tmm)) 0.17) ))
	(assert (Resultado (resultado ?total)))
)
