# CREIAMO IL CANVAS DI GIOCO
# from tkinter import *
import tkinter
import random
import time

# velocita = []  # lista per valore velocità della ball inizialm. a 0.0099
POINTS = 0  # lista contenente il punteggio quante volte la platform ha colpito la ball


# CREIAMO LA CLASSE DELLA PALLA
class Palla:
    def __init__(self, canvas, racchetta, color):
        self.ball_speed = 0.0099
        self.canvas = canvas
        # passiamo l'oggetto platform a Palla
        self.racchetta = racchetta
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # MODIFICA DELLA DIREZIONE PALLA
        starts = [-3, -2, -1, 1, 2, 3, ]
        # random.shuffle(starts)
        # self.x = starts[0]
        self.x = random.choice(starts)
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()  # CONTROLLA CHE LA PALLA NON ESCA DALLA PARTE ALTA E BASSA
        self.canvas_width = self.canvas.winfo_width()  # CONTROLLA CHE LA PALLA NON ESCA DALLA PARTE DX E SN
        self.palla_persa = False

    # Funzione che verifica se la ball viene colpita o no dalla platform
    def colpita_racchetta(self, pos):
        racchetta_pos = self.canvas.coords(self.racchetta.id)
        if pos[2] >= racchetta_pos[0] and pos[0] <= racchetta_pos[2]:
            if pos[3] >= racchetta_pos[1] and pos[3] <= racchetta_pos[3]:
                return True
        return False

    # FAR SPOSTARE LA PALLA E FAR RIMBALZARE LA PALLA
    def draw(self):

        time.sleep(ball.ball_speed)
        # print('I',velocita[0])

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # print(self.canvas.coords(self.id))#mostra le coordinate
        # come lista di 4 numeri.

        # condizione aumento velocità ball quando colpita dalla platform e punteggio
        if self.colpita_racchetta(pos) == True:
            ball.ball_speed -= 0.0004
            # v = velocita[0] - 0.0004
            # velocita.append(v)
            # del velocita[0]
            # print('II',velocita)
            global POINTS
            POINTS += 1
            # p = POINTS[0] + 1
            # POINTS.append(p)
            # del POINTS[0]
            # print('POINTS', POINTS)
            canvas.create_rectangle(10, 10, 80, 40, fill='light green')
            canvas.create_text(46, 25, text=POINTS, font=('Helvetica', 15))

        # CONTROLLA CHE LA PALLA RIMBALZI SENZA USCIRE DALLO SCHERMO
        if pos[1] <= 0:
            self.y = 3
        if self.colpita_racchetta(pos) == True:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.palla_persa = True
            time.sleep(0.5)  # ritarda l'apparizione scritta GAME OVER
            canvas.create_text(250, 200, text='GAME OVER', font=('Helvetica', 30))  # messaggio GAME OVER
            time.sleep(2)
            game_loop()

        # verifica se la ball ha colpito il fondo dello schermo (non è stata
        # colpita dalla platform)
        if self.colpita_racchetta(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


# AGGIUNGIAMO LA RACCHETTA
class Racchetta:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        # Variabile oggetto x per la platform
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.partenza = False

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Down>', self.inizio_gioco)  # il gioco parte
        # dopo la pressione tasto dx mouse

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 3
        elif pos[2] >= self.canvas_width:
            self.x = -3

    def turn_left(self, evt):
        self.x = -3  # aumentando 3 aumenta la velocità della platform

    def turn_right(self, evt):
        self.x = 3  # aumentando 3  aumenta la velocità della platform

    def inizio_gioco(self, evt):  # funzione partenza gioco
        self.partenza = True
        # velocita.append(0.0099)  # impostazione velocità iniziale ball





def game_loop():
    while True:
        if ball.palla_persa == False and platform.partenza == True:  # il ciclo while 1 parte se anche la condizione
            # platform.partenza è vera cioè è stato premuto il tasto dx del mouse.
            ball.draw()  # Aggiunta la ball al ciclo
            platform.draw()  # Aggiunta la platform al ciclo
        tk.update_idletasks()
        tk.update()
        # time.sleep(0.01)#Impostando 0.0050 aumenta la velocità della pallae della
        # platform
    #


#
if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.title("Game")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(10, 10, 80, 40, fill='light green')
    tk.update()

    # Fa parte della classe Racchetta
    platform = Racchetta(canvas, 'blue')
    # Sempre in CREIAMO LA CLASSE DELLA PALLA
    ball = Palla(canvas, platform, 'red')

    game_loop()
