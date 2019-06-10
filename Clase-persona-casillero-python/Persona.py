# -*- coding: utf-8 -*-
#!/usr/bin/env python
import datetime

#x = datetime.datetime.now()
#print (u"Año = %s" %x.year)
#ayo = x.year
class Persona:
    def __init__(self, nombre, cedula, correo, ano_Naci, mes_Naci ):
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.ano_Naci = ano_Naci
        self.mes_Naci = mes_Naci
		
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_cedula(self, cedula):
        self.cedula = cedula
        
    def get_cedula(self):
        return self.cedula

    def set_correo(self, email):
        self.correo = correo

    def get_correo(self):
        return self.correo

    def set_ano_Naci(self, ano_Naci):
        self.ano_Naci = ano_Naci

    def get_ano_Naci(self):
        return self.ano_Naci

    def set_mes_Naci(self):
        self.mes_Naci = mes_Naci

    def get_mes_Naci(self):
        return mes_Naci

    def calcular_Edad(self, ayo, mes):
        x = datetime.datetime.now()
        ayo_Actual = x.year
        mes_Actual = x.month
        edad = ayo_Actual - ayo
        if (mes<mes_Actual):
            return edad
        else:
            return (edad - 1)
            
    def salude(self):
        print "Hola mundo soy: " + self.get_nombre()

    def __str__(self):
        return "Nombre completo: " + self.get_nombre() + " Cedula: " + self.get_cedula() + " correo: " + self.get_correo() + " edad: " + str(self.calcular_Edad(self.get_ano_Naci(), self.get_mes_Naci))


def buscar(nombre):
    for persona in lst_personas:
        if (persona.get_nombre() == nombre):
            print persona
            break
def convert_int(numero):
    try:
        numero = int(numero)
        return numero
    except(ValueError):
        return False

def menu():
	null
def ultimaLinea():
	for per in lst_personas:
		print per
		print "\t\n::::::::::::::::::::::::::::|ultima linea|::::::::::::::::::::::::::::\n\n"
	
lst_personas = []

#isinstance(Vehicle(), Vehicle)
path = r'./Registros/registro.txt'
def ingreso():
	n = input("Cuantas personas desea agregar: ")
	archivo = open(path,"a+")
	for i in range(n):
		nombre = raw_input("Cual es su nombre? ")
		cedula = raw_input("Cual es su cedula? ")
		correo = raw_input("Cual es su email? ")
		nacimiento = raw_input("Cual es su ano de nacimiento ")
		nacimiento = convert_int(nacimiento)
		while (not nacimiento):
			print "Se esperaba un dato int"
			nacimiento = raw_input("Cual es su ano de nacimiento ")
			nacimiento = convert_int(nacimiento)                                
		mes = input("Cual es su mes de nacimiento  ")
		persona = Persona(nombre, cedula, correo, nacimiento, mes)
		lst_personas.append(persona)
		archivo.write(nombre)
		archivo.write(', ')
		archivo.write(cedula)
		archivo.write(', ')
		archivo.write(correo)
		archivo.write(', ')
		archivo.write(str(nacimiento))
		archivo.write(', ')
		archivo.write(str(mes))
		print "_________________________________________________________\n"
	archivo.close()
def header():
	archivo = open(path,'a+')
	archivo.write('NOMBRE, CEDULA, CORREO, NACIMIENTO, MES')
	archivo.write('\n')
	archivo.close()

def principal():
	ingreso()

	
#header()
principal()
ultimaLinea()
buscar("andres")
