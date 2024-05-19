#INTEGRANTES:
#Laura Natalia Diaz Chavarro
#Johan Santiago Ayala Osorio
#Diego Andres Quintero Pineda


from PyQt5 import QtCore, QtGui, QtWidgets
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 909)
        MainWindow.setStyleSheet("background-color: rgb(223, 215, 213);\n"
"background-color: rgb(229, 229, 229);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1071, 61))
        self.frame.setStyleSheet("\n"
"background-color: rgb(136, 136, 136);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 1031, 41))
        self.label.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 631, 311))
        self.frame_2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 601, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.grafica1 = QtWidgets.QWidget(self.frame_2)
        self.grafica1.setGeometry(QtCore.QRect(20, 50, 601, 251))
        self.grafica1.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.grafica1.setObjectName("grafica1")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 390, 631, 131))
        self.frame_4.setStyleSheet("background-color: rgb(224, 152, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 601, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.borrar = QtWidgets.QPushButton(self.frame_4)
        self.borrar.setGeometry(QtCore.QRect(490, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.borrar.setFont(font)
        self.borrar.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.borrar.setObjectName("borrar")
        self.borrar.clicked.connect(self.dele)
        self.disparar = QtWidgets.QPushButton(self.frame_4)
        self.disparar.setGeometry(QtCore.QRect(490, 50, 111, 31))
        self.disparar.clicked.connect(self.exe)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.disparar.setFont(font)
        self.disparar.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.disparar.setObjectName("disparar")
        self.v = QtWidgets.QLabel(self.frame_4)
        self.v.setGeometry(QtCore.QRect(250, 60, 48, 51))
        self.v.setObjectName("v")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 41, 41))
        self.label_4.setObjectName("label_4")
        self.vy = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.vy.setGeometry(QtCore.QRect(300, 70, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vy.setFont(font)
        self.vy.setMaximum(300.0)
        self.vy.setObjectName("vy")
        self.vx = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.vx.setGeometry(QtCore.QRect(80, 70, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.vx.setFont(font)
        self.vx.setMinimum(-300.0)
        self.vx.setMaximum(300.0)
        self.vx.setObjectName("vx")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(-10, 540, 1081, 331))
        self.frame_5.setStyleSheet("\n"
"background-color: rgb(83, 106, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 1031, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(720, 140, 271, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.gradosd = QtWidgets.QLabel(self.gridLayoutWidget)
        self.gradosd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gradosd.setText("")
        self.gradosd.setObjectName("gradosd")
        self.gridLayout.addWidget(self.gradosd, 2, 1, 1, 1)
        self.distanciad = QtWidgets.QLabel(self.gridLayoutWidget)
        self.distanciad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.distanciad.setText("")
        self.distanciad.setObjectName("distanciad")
        self.gridLayout.addWidget(self.distanciad, 0, 1, 1, 1)
        self.coordenadasd = QtWidgets.QLabel(self.gridLayoutWidget)
        self.coordenadasd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.coordenadasd.setText("")
        self.coordenadasd.setObjectName("coordenadasd")
        self.gridLayout.addWidget(self.coordenadasd, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(820, 80, 81, 31))
        self.label_10.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.grafica2 = QtWidgets.QWidget(self.frame_5)
        self.grafica2.setGeometry(QtCore.QRect(30, 50, 611, 271))
        self.grafica2.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.grafica2.setObjectName("grafica2")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(650, 70, 421, 451))
        self.frame_7.setStyleSheet("background-color: rgb(255, 133, 102);\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.textEdit = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit.setGeometry(QtCore.QRect(0, 20, 421, 431))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setStyleSheet("\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 133, 102);")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1071, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.V0 = 6
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Cálculos para un tiro parabólico PERFECTO</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">GRÁFICA DE POSICIÓN</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">PARÁMETROS</span></p></body></html>"))
        self.borrar.setText(_translate("MainWindow", "BORRAR"))
        self.disparar.setText(_translate("MainWindow", "DISPARAR"))
        self.v.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Y:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">X:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SIMULACIÓN DEL TIRO</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Coordenadas:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Distancia: </span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Grados:</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">DATOS</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#333333;\">INSTRUCCIONES:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br /></span><span style=\" font-size:10pt; font-weight:600; color:#333333;\">1. Ingrese las coordenadas en X y Y en el panel &quot;parámetros&quot; (para &quot;X el rango es -300 a 300 y &quot;Y&quot; el rengo es de 0 a 300).</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br /></span><span style=\" font-size:10pt; font-weight:600; color:#333333;\">2. Ejecute el programa con el botón &quot;DISPARAR&quot;.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br /></span><span style=\" font-size:10pt; font-weight:600; color:#333333;\">3. Le aparecerán 2 gráficas, una de posición, y otra de inclinación, estos son datos para un tiro parabolico perfecto (A donde va disparar y a que inclinacion), ademas en el panel 'Datos' tiene toda la información sobre su tiro.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"><br /></span><span style=\" font-size:10pt; font-weight:600; color:#333333;\">4. Para volver a calcular presione el botón &quot;BORRAR&quot; y vuelva a ingresar los datos.</span></p></body></html>"))
    
    def calculos(self):
        global angP
        x = self.vx.value()
        y = self.vy.value()
        V_0 = self.V0
        try: 
            #Teorema de pitagoras para hallar distancia:
            hip=round(((x**2)+(y**2))**(1/2),3)
            #Para hallar el ángulo de rotación:
            if x != 0:
                a = math.atan(y/x)
            else:
                a = math.pi/2 
            #Metodo para pasar de radianes a grados
            angulo=round(a*(180/math.pi),3)

            if angulo > 0:
                angR =  angulo - 90
            else:
                angulo += 180
                angR = round(angulo - 90,2)

            print(f'\nEl objetivo se encuentra a {hip} cm en un angulo de {angulo} y el debe rotar {angR}º')


            #Para hallar el ángulo del tiro:
            # Formula para hallar el angulo de rotacion en el z del cañon
            b = (math.asin((hip/100)*9.8/V_0**2))/2
            #Metodo para pasar de radianes a grados
            angP = round(b*(180/math.pi),3)
            print(f'Para hacer su tiro perfecto, el dispositivo debe tener un ángulo de {angP}º')
            
            
            coor = f"{x},{y}"
            l = [hip, coor, angulo, angP]
            ll = []
            for i in l:
                ll.append(str(i))
            print(l)

            return ll
        except:
            self.distanciad.setText("¡ERROR")
            self.coordenadasd.setText("EN")
            self.gradosd.setText("CALCULOS!")

    
    def grafica_1(self,x,y):
                l = self.calculos()

                fig = Figure(figsize=(3, 3))
                ax = fig.add_subplot(111)
                ax.set_aspect('equal')
                ax.set_xlim(-300, 300) #eje x de -300 a 300 y eje y de 0 a 300
                ax.set_ylim(0, 300)
                ax.set_title(f"Grados: {l[2]}°")
                ax.set_xlabel('CM')
                ax.set_ylabel('En centimetros')
                #cuadricula
                ax.grid(True, linestyle='-', color='gray')
                ax.axhline(y=0, color='r', linestyle='-') #linea roja

                ax.plot([0, x], [0, y], 'k-')
                ax.plot(x, y, 'ro')

                ax.annotate(" Objetivo", xy=(x,y))


                canvas = FigureCanvas(fig)
                layout = self.grafica1.layout()
                if layout is None:
                    layout = QtWidgets.QVBoxLayout(self.grafica1)
                else:
                    while layout.count():
                        item = layout.takeAt(0)
                        widget = item.widget()
                        if widget:
                            widget.deleteLater()
                layout.addWidget(canvas)

    def grafica_2(self,angulo):
            fig = Figure(figsize=(3, 3))
            ax = fig.add_subplot(111)
            ax.set_aspect('equal')
            ax.set_xlim(0, 300)
            ax.set_ylim(0, 300)
            ax.set_title(f"Inclinacion: {angulo}°")
            ax.grid(True, linestyle='-', color='gray')
            ax.set_ylabel('En centimetros')

            m = np.tan(np.radians(angulo))
            b = 0
            x1 = np.linspace(0, 300, 100)
            y1 = m * x1 + b
            ax.plot(x1, y1, "r")

            canvas = FigureCanvas(fig)
            layout = self.grafica2.layout()
            if layout is None:
                layout = QtWidgets.QVBoxLayout(self.grafica2)
            else:
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()
            layout.addWidget(canvas)

    def exe(self):
        global angP
        x = self.vx.value()
        y = self.vy.value()

        

        if y == 0 and x == 0:
            aleatoriox = randint(1,300)
            aleatorioy = randint(1,300)

            self.vx.setValue(aleatoriox)
            self.vy.setValue(aleatorioy)
            self.distanciad.setText("CAMBIAR VALOR CERO")
            self.coordenadasd.setText("EN X Y Y")
            self.gradosd.setText("EJM: X Y Y ACTUALES")

        else:
            self.disparar.setEnabled(False)
            
            l = self.calculos()

            self.distanciad.setText(l[0]+"CM")
            self.coordenadasd.setText(l[1]+"(XY)")
            self.gradosd.setText(l[2]+"°")

            self.grafica_1(x,y)
            self.grafica_2(angP)
            

    def dele(self):
        self.disparar.setEnabled(True)

        self.vx.setValue(0)
        self.vy.setValue(0)
        self.distanciad.setText("")
        self.coordenadasd.setText("")
        self.gradosd.setText("")
        

        #borrar grafica 2 
        layout = self.grafica1.layout()
        if layout is not None:
            self.clear_layout(layout)

        #borrar grafica 2 
        layout = self.grafica2.layout()
        if layout is not None:
            self.clear_layout(layout)


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
