from PyQt5.QtWidgets import QDialog, QApplication, QDesktopWidget, QStackedWidget, QWidget, QMessageBox
from PyQt5 import QtWidgets, uic, QtCore
#import konekDB
import mysql.connector
import sys
class login(QDialog):
	def __init__(self):
		super(login, self).__init__()
		uic.loadUi("Login.ui", self)
		self.masuk.clicked.connect(self.loginfungsion)
	
	def loginfungsion(self):
		username = self.emailfield.text()
		password = self.passwordfield.text()
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
		curr = conn.cursor()
		sql = "SELECT * FROM auth where username = '" + username + "' and pass = '" + password + "'"
		curr.execute(sql)
		user = curr.fetchone()
		if user is not None:
			self.masukkasir()
			QMessageBox.information(self, 'Alert', 'login berhasil')
		else:
			self.error.setText("masukkan akun yang benar")

	def masukkasir(self):
		self.openkasir = Main_UI()
		self.openkasir.show()
		self.close()  

class Main_UI(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		uic.loadUi("main.ui", self)
		self.isEdit = False
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.tot()
		self.mainEvent()
		self.tabelWidtg()
		self.loaddata2()
		self.loaddata()
		
	def mainEvent(self):
		self.pushButton.clicked.connect(lambda: MainApp.exit())
		self.pushButton_2.clicked.connect(lambda: self.showFullScreen())
		self.pushButton_3.clicked.connect(lambda: self.showMinimized())
		self.frame_2.mouseMoveEvent = self.MoveWindow
		self.toolButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Daftarmenu))
		self.toolButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Datapendapatan))
		self.simpan.clicked.connect(self.simpandata)
		#elf.edit.clicked.connect(self.editData)
		self.hapus.clicked.connect(self.hapusData)
		self.tableWidget.clicked.connect(self.getitem)
		self.edit.clicked.connect(self.edittext)
		self.batal.clicked.connect(self.batals)
		self.activeText(False)

		self.toolButton.clicked.connect(lambda: self.Side_Menu_Def_0())
		
		QtWidgets.QSizeGrip(self.frame_6)

		self.frame_5.mousePressEvent = self.Side_Menu_Def_1
	
	def tabelWidtg(self):
		#Tabel Daftar Menu
		self.tableWidget.setColumnWidth(0,100)
		self.tableWidget.setColumnWidth(1,150)
		self.tableWidget.setColumnWidth(2,180)
		self.tableWidget.setColumnWidth(3,165)

		#Tabel Data Pendapatan
		self.tableWidget_2.setColumnWidth(0,330)
		self.tableWidget_2.setColumnWidth(1,250)
		self.tableWidget_2.setColumnWidth(2,280)
	
	#def editData(self):
		#if self.edit.text() == 'Edit':
			#self.edit.setText('Batal')
			#self.simpan.setText('Simpan')
			#self.activeText(True)
			#self.isEdit = True
		#elif self.edit.text() == 'Batal':
			#self.edit.setText('Edit')
			#self.simpan.setText('Baru')
			#self.activeText(False)
			#self.clearform()
			#self.isEdit = False
		
	def getitem(self):
		row = self.tableWidget.currentRow()
		idMenu = self.tableWidget.item(row,0).text()
		tipeMenu = self.tableWidget.item(row,1).text()
		namaMenu = self.tableWidget.item(row,2).text()
		hargaa = self.tableWidget.item(row,3).text()
		self.textIdMenu.setText(idMenu)
		self.cbKategori.setCurrentText(tipeMenu)
		self.textMenu.setText(namaMenu)
		self.textHarga.setText(hargaa)
	
	def clearform(self):
		self.textIdMenu.setFocus()
		self.textIdMenu.setText('')
		self.cbKategori.setCurrentText('')
		self.textMenu.setText('')
		self.textHarga.setText('')
	
	def activeText(self,bool):
		self.textIdMenu.setEnabled(bool)
		self.cbKategori.setEnabled(bool)
		self.textMenu.setEnabled(bool)
		self.textHarga.setEnabled(bool)
	
	def hapusData(self):
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
		curr = conn.cursor()
		idMenu = self.textIdMenu.text()
		query = f"DELETE FROM tbbarang Where idMenu = '{idMenu}'"
		curr.execute(query)
		print("Hapus berhasil")
		conn.commit()
		curr.close()
		conn.close()
		self.loaddata()
	
	def tot(self):
		tota = 0
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
		curr = conn.cursor()
		query = "SELECT total FROM laporan"
		curr.execute(query)
		rows = curr.fetchall()  # Mengambil semua baris hasil query
		conn.commit()
		for row in rows:
			total = float(row[0])
			tota += total
		conn.close()
		self.Total.setStyleSheet("font-size: 18px")
		self.Total.setText("RP.{:.0f}".format(tota))
	
	def edittext(self):
		cb = self.edit.text()
		print(cb)
		if cb == 'edit tabel':
			self.activeText(True)
			self.clearform()
			self.edit.setText('simpan')
		elif cb == 'simpan':
			conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
			curr = conn.cursor()
			self.activeText(True)
			idMenu = self.textIdMenu.text()
			tipeMenu = self.cbKategori.currentText()
			namaMenu = self.textMenu.text()
			hargaa = self.textHarga.text()
			query = f"UPDATE tbbarang SET kategori = '{tipeMenu}', namaMenu = '{namaMenu}', harga = '{hargaa}' WHERE idMenu = '{idMenu}'"
			curr.execute(query)
			print("Edit berhasil")
			conn.commit()
			curr.close()
			conn.close()
			self.loaddata()
			self.activeText(False)
			self.clearform()
			self.edit.setText('edit tabel')
	
	def simpandata(self):
		cb = self.simpan.text()
		print(cb)
		if cb == 'baru':
			self.activeText(True)
			self.clearform()
			self.simpan.setText('simpan')

		elif cb == 'simpan':
			conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
			curr = conn.cursor()
			self.simpan.setText('baru')
			idMenu = self.textIdMenu.text()
			tipeMenu = self.cbKategori.currentText()
			namaMenu = self.textMenu.text()
			hargaa = self.textHarga.text()
			query = f"INSERT INTO tbbarang (idMenu, kategori, namaMenu, harga) VALUES ('{idMenu}', '{tipeMenu}', '{namaMenu}', '{hargaa}')"
			curr.execute(query)
			print("Simpan berhasil")
			conn.commit()
			curr.close()
			conn.close()
			self.loaddata()
			self.activeText(False)
			self.clearform()

		
	#def simpandata(self):
		#cb = self.simpan.text()
		#print(cb)
		#if cb == 'baru':
			#self.activeText(True)
			#self.clearform()
			#self.simpan.setText('simpan')
			#self.edit.setText('Batal')
		#elif cb == 'simpan':
			#conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
			#curr = conn.cursor()
			#if self.isEdit == False:
				#self.simpan.setText('baru')
				#idMenu = self.textIdMenu.text()
				#tipeMenu = self.cbKategori.currentText()
				#namaMenu = self.textMenu.text()
				#hargaa = self.textHarga.text()
				#query = f"INSERT INTO tbbarang (idMenu, kategori, namaMenu, harga) VALUES ('{idMenu}', '{tipeMenu}', '{namaMenu}', '{hargaa}')"
				#curr.execute(query)
				#print("Simpan berhasil")
			#elif self.isEdit == True:
				#idMenu = self.textIdMenu.text()
				#tipeMenu = self.cbKategori.currentText()
				#namaMenu = self.textMenu.text()
				#hargaa = self.textHarga.text()
				#query = f"UPDATE tbbarang SET kategori = '{tipeMenu}', namaMenu = '{namaMenu}', harga = '{hargaa}' WHERE idMenu = '{idMenu}'"
				#curr.execute(query)
				#print("Edit berhasil")
		
			#conn.commit()
			#curr.close()
			#conn.close()
			#self.loaddata()
			#self.activeText(False)
			#self.clearform()
			#self.simpan.setText('baru')
			#self.edit.setText('edit')
	

	def loaddata(self):
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')	
		curr = conn.cursor()
		querry = "SELECT * FROM tbbarang ORDER BY total DESC"
		curr.execute(querry)
		result = curr.fetchall()
		print(result)
		row = 0
		self.tableWidget.setRowCount(len(result))
		for item in result:
			self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(item[0]))
			self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(item[1]))
			self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(item[2]))
			self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(item[3])))
			row += 1
	
	def batals(self):
		cb = self.simpan.text()
		ed = self.edit.text()
		if cb == 'simpan':
			self.simpan.setText('baru')
			self.clearform()
			self.activeText(False)
		elif ed == 'simpan':
			self.edit.setText('edit table')
			self.clearform()
			self.activeText(False)		
			
	def loaddata2(self):
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')	
		curr = conn.cursor()
		querry = "SELECT * FROM laporan"
		curr.execute(querry)
		result = curr.fetchall()
		print(result)
		row = 0
		self.tableWidget_2.setRowCount(len(result))
		for item in result:
			self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(item[1]))
			self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(str(item[2])))
			self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(str(item[3])))
			row += 1

	def Side_Menu_Def_0(self):
		if self.frame_4.width() <= 50:
			self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
			self.animation1.setDuration(500)
			self.animation1.setStartValue(35)
			self.animation1.setEndValue(110)
			self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation1.start()

			self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
			self.animation2.setDuration(500)
			self.animation2.setStartValue(35)
			self.animation2.setEndValue(110)
			self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation2.start()

		else:
			self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
			self.animation1.setDuration(500)
			self.animation1.setStartValue(110)
			self.animation1.setEndValue(35)
			self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation1.start()

			self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
			self.animation2.setDuration(500)
			self.animation2.setStartValue(110)
			self.animation2.setEndValue(35)
			self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
			self.animation2.start()

	def Side_Menu_Def_1(self, Event):
		if Event.button() == QtCore.Qt.LeftButton:
			if self.frame_4.width() >= 50:
				self.animation1 = QtCore.QPropertyAnimation(self.frame_4, b"maximumWidth")
				self.animation1.setDuration(500)
				self.animation1.setStartValue(110)
				self.animation1.setEndValue(35)
				self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
				self.animation1.start()

				self.animation2 = QtCore.QPropertyAnimation(self.frame_4, b"minimumWidth")
				self.animation2.setDuration(500)
				self.animation2.setStartValue(110)
				self.animation2.setEndValue(35)
				self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
				self.animation2.start()
			else:
				pass


	def MoveWindow(self, event):
		if self.isMaximized() == False:
			self.move(self.pos() + event.globalPos() - self.clickPosition)
			self.clickPosition = event.globalPos()
			event.accept()
			pass
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()
		pass
if __name__ == "__main__":
	MainApp = QtWidgets.QApplication(sys.argv)
	widget = QWidget()
	App = login()
	App.show()
	sys.exit(MainApp.exec_())

