import tkinter as tk

jogador_atual = "X"

def jogar():
    frame_inicial.pack_forget()
    frame_tabuleiro.pack()

def verificar_vitoria():
    for i in range(3):
        if botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"] != "":
            return True
        
    for j in range(3):
        if botoes[0][j]["text"] == botoes[1][j]["text"] == botoes[2][j]["text"] != "":
            return True
        
    if botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "":
        return True
    
    if botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != "":
        return True
    
    return False

def verificar_empate():
    for i in range(3):
        for j in range(3):
            if botoes[i][j]["text"] == "":
                return False
    return True

def mostrar_tela_final(mensagem):
        for widget in frame_final.winfo_children():
            widget.destroy()

        lbl_resultado = tk.Label(frame_final, text=mensagem, font=("Arial", 30))
        lbl_resultado.grid(row = 0, column = 0, pady = 10)

        lbl_pergunta_final = tk.Label(frame_final, text="Deseje jogar novamente?", font=("Arial", 20))
        lbl_pergunta_final.grid(row=1, column=0, pady=40)

        frame_botoes_resposta = tk.Frame(frame_final)
        frame_botoes_resposta.grid(row=2, column=0, pady=10) 

        btn_jogar_de_novo = tk.Button(frame_botoes_resposta, text="Sim", font=("Arial", 18), command=reiniciar)
        btn_jogar_de_novo.pack(side="left", padx=20)

        btn_sair = tk.Button(frame_botoes_resposta, text="Não", font=("Arial", 18), command=sair)
        btn_sair.pack(side="left", padx=20)
        
        frame_tabuleiro.pack_forget()
        frame_final.pack()
    
def clicar(i, j):
    global jogador_atual
    botoes[i][j].config(text=jogador_atual, state="disabled")

    if verificar_vitoria():
        mostrar_tela_final(f"Jogador {jogador_atual} venceu!")
        return

    if not verificar_vitoria() and verificar_empate():
        mostrar_tela_final("Empate")
        return
    
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"

def reiniciar():
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal")
    frame_final.pack_forget()
    frame_tabuleiro.pack()

def sair():
    frame_final.pack_forget()
    frame_inicial.pack()
    global jogador_atual
    jogador_atual = "X"
    for i in range(3):
        for j in range(3):
            botoes[i][j].config(text="", state="normal")

root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("400x400")

frame_inicial = tk.Frame(root)
frame_inicial.pack()

lbl_titulo = tk.Label(frame_inicial, text="Jogo da Velha", font=("Arial", 30))
lbl_titulo.pack(pady = 30)

btn_iniciar = tk.Button(frame_inicial, text="Jogar", font=("Arial", 16), command=jogar)
btn_iniciar.pack(pady=10)

frame_tabuleiro = tk.Frame(root)
botoes = []

for i in range(3):
    linha = []
    for j in range(3):
        btn_tabuleiro = tk.Button(frame_tabuleiro, text="", font=("Arial", 30), width=5, height=2, command=lambda i=i, j=j: clicar(i, j))
        btn_tabuleiro.grid(row=i, column=j)
        linha.append(btn_tabuleiro)
    botoes.append(linha)

frame_final = tk.Frame(root)



root.mainloop()