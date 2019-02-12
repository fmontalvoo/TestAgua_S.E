from Tkinter import *
import ttk
import tkMessageBox
import clips
from Graficas import *

class Ventana(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.master.resizable(False, False)
		self.inicializar()

	def inicializar(self):
		self.master.title("Test para la calidad del agua")
		self.pack(fill = BOTH, expand = 1)

		self.lblColiformes = Label(self, text = "Coliformes Fecales (NMP/100ml):")
		self.lblColiformes.grid(row = 1, column = 1)
		self.txtColiformes = Text(self, height = 1, width = 22)
		self.txtColiformes.grid(row = 1, column = 2)
		self.coliformes = self.txtColiformes
		
		self.lblPH = Label(self, text = "pH:")
		self.lblPH.grid(row = 2, column = 1)
		self.txtPH = Text(self, height = 1, width = 22)
		self.txtPH.grid(row = 2, column = 2)
		self.pH = self.txtPH

		self.lblDBO = Label(self, text = "DBO5 (DBO5 mg/L):")
		self.lblDBO.grid(row = 3, column = 1)
		self.txtDBO = Text(self, height = 1, width = 22)
		self.txtDBO.grid(row = 3, column = 2)
		self.dbo = self.txtDBO	
		
		self.lblNitratos = Label(self, text = "Nitratos (NO3 mg/L):")
		self.lblNitratos.grid(row = 4, column = 1)
		self.txtNitratos = Text(self, height = 1, width = 22)
		self.txtNitratos.grid(row = 4, column = 2)
		self.nitratos = self.txtNitratos
		
		self.lblFosfatos = Label(self, text = "Fosfatos (PO4 mg/L):")
		self.lblFosfatos.grid(row = 5, column = 1)
		self.txtFosfatos = Text(self, height = 1, width = 22)
		self.txtFosfatos.grid(row = 5, column = 2)
		self.fosfatos = self.txtFosfatos	

		self.lblTemperaturaA = Label(self, text = "Temperatura Ambiente (Celsius):")
		self.lblTemperaturaA.grid(row = 1, column = 3)
		self.txtTemperaturaA = Text(self, height = 1, width = 22)
		self.txtTemperaturaA.grid(row = 1, column = 4)
		self.tempAmbiente = self.txtTemperaturaA
	
		self.lblTemperaturaM = Label(self, text = "Temperatura Muestra (Celsius):")
		self.lblTemperaturaM.grid(row = 2, column = 3)
		self.txtTemperaturaM = Text(self, height = 1, width = 22)
		self.txtTemperaturaM.grid(row = 2, column = 4)
		self.tempMuestra = self.txtTemperaturaM
	
		self.lblTurbidez = Label(self, text = "Turbidez (FAU):")
		self.lblTurbidez.grid(row = 3, column = 3)
		self.txtTurbidez = Text(self, height = 1, width = 22)
		self.txtTurbidez.grid(row = 3, column = 4)
		self.turbidez = self.txtTurbidez
	
		self.lblSolidos = Label(self, text = "Solidos Disueltos (mg/L):")
		self.lblSolidos.grid(row = 4, column = 3)
		self.txtSolidos = Text(self, height = 1, width = 22)
		self.txtSolidos.grid(row = 4, column = 4)
		self.solidos = self.txtSolidos	

		
		self.btnEvaluar = Button(self, text = "Evaluar", command = self.evaluar)
		self.btnEvaluar.grid(columnspan = 2, rowspan = 1, sticky = W + E + N + S, row = 5, column = 3)
		
	def evaluar(self):
		clips.Load("Test_ver2.clp")
		cl = float(self.coliformes.get('1.0', END))
		ph = float(self.pH.get('1.0', END))
		db = float(self.dbo.get('1.0', END))
		nt = float(self.nitratos.get('1.0', END))
		ff = float(self.fosfatos.get('1.0', END))
		tma = float(self.tempAmbiente.get('1.0', END))
		tmm = float(self.tempMuestra.get('1.0', END))
		tb = float(self.turbidez.get('1.0', END))
		sd = float(self.solidos.get('1.0', END))
		print(cl,ph,db,nt,ff,tma,tmm,tb,sd)
		clips.Call("testAgua", ''+str(cl)+' '+str(ph)+' '+str(db)+' '+str(nt)+' '+str(ff)+' '+str(tma)+' '+str(tmm)+' '+str(tb)+' '+str(sd)+'')
		clips.Run()
		resultado = clips.Eval("(fact-slot-value 1 resultado)")
		calidad = clips.Eval("(fact-slot-value 2 calidad)")
		tkMessageBox.showinfo("Resultado", "La calidad del agua es: " + calidad.upper())
		clips.Eval("(clear)")
		g = Graficas()
		g.graficar(float(resultado))
		print('Valor Obtenido:',resultado)
		
if __name__ == '__main__':
	root = Tk()
	ventana = Ventana(root)
	root.mainloop()
