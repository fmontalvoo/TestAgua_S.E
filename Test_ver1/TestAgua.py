from Tkinter import *
import ttk
import tkMessageBox
import clips

cl = ''
et = ''
fm = ''

class Ventana(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.master.resizable(False, False)
		self.inicializar()

	def inicializar(self):
		self.master.title("Test para la calidad del agua")
		self.pack(fill = BOTH, expand = 1)
		
		self.img = PhotoImage(file = "gota.png")
		self.widget = Label(self, image=self.img)
		self.widget.grid(columnspan = 7, rowspan = 7, sticky = W + E + N + S,row = 1, column = 5)
		
		self.lblTemperatura = Label(self, text = "Temperatura:")
		self.lblTemperatura.grid(row = 1, column = 1)
		self.txtTemperatura = Text(self, height = 1, width = 22)
		self.txtTemperatura.grid(row = 1, column = 2)
		self.temperatura = self.txtTemperatura
		
		self.lblOxigeno = Label(self, text = "Oxigeno disuelto:")
		self.lblOxigeno.grid(row = 2, column = 1)
		self.txtOxigeno = Text(self, height = 1, width = 22)
		self.txtOxigeno.grid(row = 2, column = 2)
		self.oxigeno = self.txtOxigeno
		
		self.lblPH = Label(self, text = "pH:")
		self.lblPH.grid(row = 3, column = 1)
		self.txtPH = Text(self, height = 1, width = 22)
		self.txtPH.grid(row = 3, column = 2)
		self.pH = self.txtPH
		
		self.lblSolidos = Label(self, text = "Solidos disueltos:")
		self.lblSolidos.grid(row = 4, column = 1)
		self.txtSolidos = Text(self, height = 1, width = 22)
		self.txtSolidos.grid(row = 4, column = 2)
		self.solidos = self.txtSolidos	
		
		self.lblConductividad = Label(self, text = "Conductividad:")
		self.lblConductividad.grid(row = 5, column = 1)
		self.txtConductividad = Text(self, height = 1, width = 22)
		self.txtConductividad.grid(row = 5, column = 2)
		self.conductividad = self.txtConductividad		
		
		self.lblDias = Label(self, text = "Dias desde que lluvio:")
		self.lblDias.grid(row = 6, column = 1)
		self.txtDias = Text(self, height = 1, width = 22)
		self.txtDias.grid(row = 6, column = 2)
		self.dias = self.txtDias	
	
		self.lblCaudal = Label(self, text = "Caudal:")
		self.lblCaudal.grid(row = 7, column = 1)
		self.cmbCaudal = ttk.Combobox(self, state = "readonly")
		self.cmbCaudal["values"] = ["Bajo", "Normal", "Alto"]
		self.cmbCaudal.grid(row = 7, column = 2)
		self.cmbCaudal.bind("<<ComboboxSelected>>",self.caudal)
	
		self.lblSedimentos = Label(self, text = "Sedimentos suspendidos:")
		self.lblSedimentos.grid(row = 1, column = 3)
		self.txtSedimentos = Text(self, height = 1, width = 22)
		self.txtSedimentos.grid(row = 1, column = 4)
		self.sedimentos = self.txtSedimentos
	
		self.lblTransparencia = Label(self, text = "Transparencia:")
		self.lblTransparencia.grid(row = 2, column = 3)
		self.txtTransparencia = Text(self, height = 1, width = 22)
		self.txtTransparencia.grid(row = 2, column = 4)
		self.transparencia = self.txtTransparencia

		self.lblEutrofizacion = Label(self, text = "Eutrofizacion:")
		self.lblEutrofizacion.grid(row = 3, column = 3)
		self.cmbEutrofizacion = ttk.Combobox(self, state = "readonly")
		self.cmbEutrofizacion["values"] = ["Nula", "Baja", "Alta"]
		self.cmbEutrofizacion.grid(row = 3, column = 4)
		self.cmbEutrofizacion.bind("<<ComboboxSelected>>",self.eutrofizacion)	

		self.lblFuente = Label(self, text = "Fuente metales:")
		self.lblFuente.grid(row = 4, column = 3)
		self.cmbFuente = ttk.Combobox(self, state = "readonly")
		self.cmbFuente["values"] = ["Erosion", "Industria"]
		self.cmbFuente.grid(row = 4, column = 4)
		self.cmbFuente.bind("<<ComboboxSelected>>",self.fuente)

		self.lblMetales = Label(self, text = "Metales en peces:")
		self.lblMetales.grid(row = 5, column = 3)
		self.txtMetales = Text(self, height = 1, width = 22)
		self.txtMetales.grid(row = 5, column = 4)
		self.metales = self.txtMetales

		self.lblEcoli = Label(self, text = "Ecoli:")
		self.lblEcoli.grid(row = 6, column = 3)
		self.txtEcoli = Text(self, height = 1, width = 22)
		self.txtEcoli.grid(row = 6, column = 4)
		self.ecoli = self.txtEcoli

		self.lblNitratos = Label(self, text = "Nitratos:")
		self.lblNitratos.grid(row = 7, column = 3)
		self.txtNitratos = Text(self, height = 1, width = 22)
		self.txtNitratos.grid(row = 7, column = 4)
		self.nitratos = self.txtNitratos

		btnEvaluar = Button(self, text = "Evaluar", command = self.evaluar)
		btnEvaluar.grid(columnspan = 1, rowspan = 1, sticky = W + E + N + S, row = 12, column = 3)
			
	
	def caudal(self, event):
		global cl
		cl = self.cmbCaudal.get().lower()
		cdl = {0 : 1, 1 : 2, 2 : 3}
		actual = self.cmbCaudal.current()
		ss = float(self.sedimentos.get('1.0', END))
		tp = int(self.transparencia.get('1.0', END))
		cd = int(self.conductividad.get('1.0', END))
		self.sedimentos.delete('1.0', END)
		self.transparencia.delete('1.0', END)
		self.conductividad.delete('1.0', END)
		self.sedimentos.insert(END, str(ss * cdl[actual]))
		self.transparencia.insert(END, str(tp * cdl[actual]))
		self.conductividad.insert(END, str(cd * cdl[actual]))
	
	def eutrofizacion(self, event):
		global et
		niveles = { 0 : 1, 1 : 0.25, 2 : 0.75 }
		et = self.cmbEutrofizacion.get().lower()
		ox = float(self.oxigeno.get('1.0', END))
		nt = float(self.nitratos.get('1.0', END))
		actual = self.cmbEutrofizacion.current()
		if(actual != 0):
			self.oxigeno.delete('1.0', END)
			self.nitratos.delete('1.0', END)
			self.oxigeno.insert(END, ox - (ox * niveles[actual]))
			self.nitratos.insert(END, nt + (nt * niveles[actual]))
		
	
	def fuente(self, event):
		global fm
		fm = self.cmbFuente.get()
		actual =  self.cmbFuente.current()
		fm = {0 : 1, 1 : 2}
		if(actual != 0):
			mt = float(self.metales.get('1.0', END))
			self.metales.delete('1.0', END)
			self.metales.insert(END, mt * fm[actual])
		
		

	def evaluar(self):
		clips.Load("Test_Agua.clp")
		tm = float(self.temperatura.get('1.0', END))
		od = float(self.oxigeno.get('1.0', END))
		ph = float(self.pH.get('1.0', END))
		sd = float(self.solidos.get('1.0', END))
		cd = float(self.conductividad.get('1.0', END))
		dl = int(self.dias.get('1.0', END))
		ss = float(self.sedimentos.get('1.0', END))
		tp = int(self.transparencia.get('1.0', END))
		mp = float(self.metales.get('1.0', END))
		ec = int(self.ecoli.get('1.0', END))
		nt = float(self.nitratos.get('1.0', END))
		clips.Call("testAgua", ''+str(tm)+' '+str(od)+' '+str(ph)+' '+str(sd)+' '+str(cd)+' '+str(dl)+' '+str(cl)+' '+str(ss)+' '+str(tp)+' '+str(et)+' "'+str(fm)+'" '+str(mp)+' '+str(ec)+' '+str(nt)+'')
		clips.Run()
		#print(clips.PrintFacts())
		res = clips.Eval("(fact-slot-value 3 respuesta)")
		tkMessageBox.showinfo("Resultado", "La calidad del agua es: " + res.upper())
		clips.Eval("(clear)")
		
if __name__ == '__main__':
	root = Tk()
	ventana = Ventana(root)
	root.mainloop()
