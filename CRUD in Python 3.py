from time import sleep
import os
def semfun():
	print("__"*20)
	print(" "*15 ,"Sem função")
	print("__"*20)
	sleep(0.5)
def volt():
	print("__"*20)
	print(" !!Voltando!!")
	print("__"*20)
	sleep(0.5)
def tralist():
	vrfc = 0
	arq = open("CRUD in Python 3.txt")
	list = arq.readlines()
	quatL = (len(list))
	qd = qtd*6
	if qd<=quatL:
		vrfc = 1
		return vrfc,qd,quatL,list
	else:
		print("_"*53)
		print(" !! Você não têm esse cadastro salvo !!")
		print("_"*53)
		sleep(0.5)
		vrfc = 0
		return vrfc,qd,quatL,list
def amostrar():
	if os.path.exists("CRUD in Python 3.txt"):
		arqr=open('CRUD in Python 3.txt','r')
		h = arqr.readlines()
		qtL = (len(h))
		if qtL>=6:
			print("=="*12,"Cadastros Registrados","="*17)
			cont=1
			for linha in h:
				if "Nome:" in linha:
					print(" ",linha, end='')
				elif "E-mail:" in linha:
					print(" ",linha, end='')
				elif "CPF:" in linha:
					print(" ",linha, end='')
				elif "Telefone:" in linha:
					print(" ",linha, end='')
				elif "Senha:" in linha:
					print(" ",linha, end='')
					sleep(0.5)
				elif 'Cadastro' in linha:
					print("-="*5,"Cadastro",cont,"-="*5)
					cont+=1
			print("----"*16)
			arqr.close()
		else:
			arqr.close()
			os.remove('CRUD in Python 3.txt')
			print("_"*53)
			print(" !! Você não têm cadastros salvos !!")
			print("_"*53)
			sleep(0.5)
	else:
		print("_"*53)
		print(" !! Você não têm cadastros salvos !!")
		print("_"*53)
		sleep(0.5)
print("----------------------------------------------------------------------------------------------\n")
print("                              Bem Vindo ao Programa CRUD in file")
print("                                        Feito por:")
sleep(1)
print("                    💻     Anderson Melo da Silva  N.º05 1°B 2022     💻")
sleep(0.25)
print("                                           and")
sleep(0.25)
print("                    💻    Kauã Silva Barreto Caldas  N.º32 1°B 2022   💻")
print("\n----------------------------------------------------------------------------------------------")
sleep(0.5)
me=0
while me==0:
	print("-="*32)
	print("="*25,"Menu Inicial","="*25)
	print(" 1 - Cadastro\n 2 - Ler\n 3 - Deletar\n 4 - Atualiza\n 5 - Sair")
	opc=input(" Digite qual você deseja entrar: ")
	if opc=="1":
		qtc=int(input(" Digite quantos cadastros você quer fazer: "))
		registro=0
		while  registro<qtc:
			print("-="*5,"Cadastro ",registro+1,"-="*5)
			no=input(" Digite seu nome completo: ")
			e=input(" Digite seu e-mail: ")
			cpf1=input(" Digite seu CPF: ")
			t=input(" Digite seu telefone: ")
			s=input(" Digite sua senha: ")
			print("__" *32)
			sn=0
			while sn==0:
				print("-"*40)
				esc=input(" 1 - Salvar\n 2 - Refazer\n Digite sua escolha: ")
				if esc=="1":
					if no=="" or e=="" or cpf1=="" or t=="" or s=="":
						print("__"*25)
						print(" "*5,"!!Há campos vazios!!")
						print(" "*2,"Por favor preencha os campos corretamente")
						print("__"*25)
						break
					else:
						arqw=open('CRUD in Python 3.txt','a')
						arqw.write("-="*5+"Cadastro"+"-="*5+'\n')
						arqw.write("Nome: "+no+'\n')
						arqw.write("E-mail: "+e+'\n')
						arqw.write("CPF: "+cpf1+'\n')
						arqw.write("Telefone: "+t+'\n')
						arqw.write("Senha: "+s+'\n')
						registro+=1
						arqw.close()
						print("__"*20)
						print("  "*6 ,"Dados salvos")
						print("__"*20)
						sleep(0.5)
						break
				elif esc=="2":
					break
				else:
					semfun()
	elif opc=="2":
		amostrar()
		conf=input(" Precione enter para voltar ao menu inicial: ")
	elif opc=="3":
		amostrar()
		if os.path.exists("CRUD in Python 3.txt"):
			qtd=int(input(" Digite 0 para voltar\n -1 Para deleter todos\n ou\n Digite qual você deseja deletar: "))
			if qtd==0:
				volt()
			elif qtd==-1:
				os.remove("CRUD in Python 3.txt")
				print("__"*20)
				print(" Deletado")
				print("__"*20)
				sleep(0.5)
			elif qtd > 0:
				c = tralist()
				vrfc2 = c[0]
				if vrfc2 == 1:
					qd2 = c[1]
					lista = c[3]
					del lista[qd2-6:qd2]
					os.remove('CRUD in Python 3.txt')
					arqw = open('CRUD in Python 3.txt','a')
					for linha in lista:
						arqw.write(linha)
					arqw.close()
					print("__"*20)
					print("    !! Cadastro ",qtd," Deletado !!")
					print("__"*20)
					sleep(0.5)
	elif opc=="4":
		amostrar()
		if os.path.exists("CRUD in Python 3.txt"):
			qtd=int(input(" Digite 0 para voltar\n -1 Para atualizar todos\n ou\n Digite qual você deseja atualizar: "))
			if qtd==0:
				volt()
			elif qtd==-1:
				c = tralist()
				vrfc2 = c[0]
				if vrfc2 == 1:
					qd2 = c[1]
					lista = c[3]
					quatL = c[2]
					qtd = 1
					while qtd<= quatL/6:
						print("-="*3,"Atualizando Cadastro ",qtd,"-="*3)
						sleep(0.5)
						no=input(" Digite seu novo nome completo: ")
						e=input(" Digite seu novo e-mail: ")
						cpf1=input(" Digite seu novo CPF: ")
						t=input(" Digite seu novo telefone: ")
						s=input(" Digite sua nova senha: ")
						print("__" *32)
						print("-"*40)
						sns = input(" 1 - Alterar\n 2 - Voltar ao menu\n Digite sua escolha: ")
						if sns == "1":
							if no=="" or e=="" or cpf1=="" or t=="" or s=="":
								print("__"*25)
								print(" "*5,"!!Há campos vazios!!")
								print(" "*2,"Por favor preencha os campos corretamente")
								print("__"*25)
							else:
								qd2=qtd*6
								os.remove('CRUD in Python 3.txt')
								lista[qd2-6]=("-="*5+"Cadastro"+"-="*5+'\n')
								lista[qd2-5]=("Nome: "+no+'\n')
								lista[qd2-4]=("E-mail: "+e+'\n')
								lista[qd2-3]=("CPF: "+cpf1+'\n')
								lista[qd2-2]=("Telefone: "+t+'\n')
								lista[qd2-1]=("Senha: "+s+'\n')
								arqw = open("CRUD in Python 3.txt","a")
								for linha in lista:
									arqw.write(linha)
								arqw.close()
								print("__"*20)
								print("    !! Cadastro ",qtd," Atualizado !!")
								print("__"*20)
								qtd+=1
								sleep(0.5)
						elif sns == "2":
							break
						else:
							semfun()
			elif qtd > 0:
				c = tralist()
				vrfc2 = c[0]
				if vrfc2 == 1:
					qd2 = c[1]
					lista = c[3]
					n=0
					while n == 0:
						print("-="*3,"Atualizando Cadastro ",qtd,"-="*3)
						sleep(0.5)
						no=input(" Digite seu novo nome completo: ")
						e=input(" Digite seu novo e-mail: ")
						cpf1=input(" Digite seu novo CPF: ")
						t=input(" Digite seu novo telefone: ")
						s=input(" Digite sua nova senha: ")
						print("__" *32)
						print("-"*40)
						sns = input(" 1 - Alterar\n 2 - Voltar ao menu\n Digite sua escolha: ")
						if sns == "1":
							if no=="" or e=="" or cpf1=="" or t=="" or s=="":
								print("__"*25)
								print(" "*5,"!!Há campos vazios!!")
								print(" "*2,"Por favor preencha os campos corretamente")
								print("__"*25)
							else:
								os.remove('CRUD in Python 3.txt')
								lista[qd2-6]=("-="*5+"Cadastro"+"-="*5+'\n')
								lista[qd2-5]=("Nome: "+no+'\n')
								lista[qd2-4]=("E-mail: "+e+'\n')
								lista[qd2-3]=("CPF: "+cpf1+'\n')
								lista[qd2-2]=("Telefone: "+t+'\n')
								lista[qd2-1]=("Senha: "+s+'\n')
								arqw = open("CRUD in Python 3.txt","a")
								for linha in lista:
									arqw.write(linha)
								arqw.close()
								print("__"*20)
								print("    !! Cadastro ",qtd," Atualizado !!")
								print("__"*20)
								sleep(0.5)
								break
						elif sns == "2":
							break
						else:
							semfun()
	elif opc=="5":
		p=0
		while p==0:
			print("-"*40)
			esc=input(" 1 - Sair\n 2 - Voltar ao menu\n Digite sua escolha: ")
			if esc=="1":
				me=1
				break
			if esc=="2":
				volt()
				break
			else:
				semfun()
	else:
		semfun()
