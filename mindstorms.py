import turtle #módulo para desenhos em python

#função de movimento, recebemos um objeto turtle e utilizando de suas funções num loop para criação do quadrado
def draw_square(some_turtle): # @param turtle objeto
	for i in range(4):
		some_turtle.forward(100) 
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen() # adicionando janela para o desenho
	window.bgcolor("red") #definindo cor de fundo para janela

	# turtle.Turtle() -> faz a cahmada peo módulo importado, ou seja usanmos a classes Turtle do import turtle
	brad = turtle.Turtle() # criando objeto Turtle
	# utilizando mais estilos e atributos da classe
	brad.shape("turtle")
	brad.color("white")
	brad.speed(10)
	for i in range(35):# o loop executara 36 vezes (motivo: rigth muda de 10 em 10 36 x 10 360 graus)
		draw_square(brad)#chamando função responsavel pela criação do quadrado
		brad.right(10) #girando o circulo após seu desenho em 10 graus
	window.exitonclick()

draw_art()

	#criando um circulo
	#angie = turtle.Turtle()
	#angie.color("blue")
	#angie.circle(100)
	#angie.shape("arrow")
	#angie.speed(5)
