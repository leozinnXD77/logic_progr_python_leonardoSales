import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ======================================================
# JANELA PRINCIPAL
# ======================================================

janela = tk.Tk()
janela.title("🍟 Sistema Batata Frita")
janela.geometry("820x820")
janela.configure(bg="#FFF6D5")
janela.resizable(False, False)

# ======================================================
# CORES
# ======================================================

COR_FUNDO = "#FFF6D5"
COR_TITULO = "#D35400"
COR_VERDE = "#2ECC71"
COR_AZUL = "#2C3E50"

# ======================================================
# VARIÁVEIS
# ======================================================

passo_atual = 0

passos = [

"1. Pegue a batata, uma faca e uma air fryer.",

"2. Descasque cuidadosamente a batata.",

"3. Lave bem a batata utilizando água corrente.",

"4. Corte a batata em vários pedaços retangulares.",

"5. Abra a air fryer e coloque todas as batatas.",

"6. Adicione uma pequena quantidade de sal.",

"7. Ajuste a temperatura para 200°C.",

"8. Aguarde entre 20 e 25 minutos.",

"9. Retire as batatas com cuidado.",

"10. Pronto! Agora é só aproveitar. 😋"

]

# ======================================================
# CABEÇALHO
# ======================================================

cabecalho = tk.Frame(
    janela,
    bg=COR_TITULO,
    height=80
)

cabecalho.pack(fill="x")

titulo = tk.Label(

    cabecalho,

    text="🍟 SISTEMA BATATA FRITA 🍟",

    font=("Segoe UI",22,"bold"),

    fg="white",

    bg=COR_TITULO

)

titulo.pack(pady=18)

# ======================================================
# ÁREA PRINCIPAL
# ======================================================

conteudo = tk.Frame(
    janela,
    bg=COR_FUNDO
)

conteudo.pack(fill="both", expand=True, padx=20, pady=15)

# ======================================================
# ESCOLHA DA PORÇÃO
# ======================================================

lbl = tk.Label(

    conteudo,

    text="Quantas porções deseja preparar?",

    font=("Segoe UI",12,"bold"),

    bg=COR_FUNDO

)

lbl.pack()

combo = ttk.Combobox(

    conteudo,

    values=[

        "uma porção",

        "duas porções",

        "três porções"

    ],

    width=25,

    state="readonly",

    font=("Segoe UI",11)

)

combo.current(0)

combo.pack(pady=10)

# ======================================================
# TEMPERATURA
# ======================================================

temperatura = tk.Label(

    conteudo,

    text="🌡 Temperatura da Air Fryer: 200°C",

    font=("Segoe UI",11),

    bg=COR_FUNDO,

    fg="red"

)

temperatura.pack()

# ======================================================
# PASSO ATUAL
# ======================================================

status = tk.Label(

    conteudo,

    text="Passo 0 de 10",

    font=("Segoe UI",11,"bold"),

    bg=COR_FUNDO,

    fg=COR_AZUL

)

status.pack(pady=10)

# ======================================================
# BARRA DE PROGRESSO
# ======================================================

barra = ttk.Progressbar(

    conteudo,

    orient="horizontal",

    length=600,

    mode="determinate",

    maximum=len(passos)

)

barra.pack()

# ======================================================
# CAIXA DO TUTORIAL
# ======================================================

tutorial = tk.Text(

    conteudo,

    width=85,

    height=16,

    font=("Consolas",11),

    relief="solid",

    borderwidth=1

)

tutorial.pack(pady=20)

tutorial.config(state="disabled")

# ======================================================
# RESULTADO
# ======================================================

resultado = tk.Label(

    conteudo,

    text="",

    font=("Segoe UI",14,"bold"),

    bg=COR_FUNDO,

    fg="green"

)

resultado.pack(pady=10)
# ======================================================
# FUNÇÕES
# ======================================================

def escrever(texto):
    """
    Escreve uma linha na caixa de tutorial.
    """

    tutorial.config(state="normal")

    tutorial.insert("end", texto + "\n\n")

    tutorial.see("end")

    tutorial.config(state="disabled")


def limpar_tutorial():
    """
    Limpa o conteúdo da caixa de texto.
    """

    tutorial.config(state="normal")

    tutorial.delete("1.0", "end")

    tutorial.config(state="disabled")


def finalizar():
    """
    Executado quando todos os passos terminarem.
    """

    escolha = combo.get().lower()

    if escolha == "uma porção":

        lanche = "🍟 Batata frita com PORÇÃO PEQUENA!"

    elif escolha == "duas porções":

        lanche = "🍟 Batata frita com PORÇÃO MÉDIA!"

    else:

        lanche = "🍟 Batata frita com PORÇÃO GRANDE!"

    resultado.config(

        text=f"✅ Tutorial concluído!\n\nSeu lanche será:\n{lanche}",

        fg="#1E8449"

    )

    messagebox.showinfo(

        "Tutorial Finalizado",

        f"Seu lanche será:\n\n{lanche}\n\nBom apetite! 🍟"

    )

    botao_iniciar.config(state="normal")

    combo.config(state="readonly")


def mostrar_passo():
    """
    Mostra um passo do tutorial.
    """

    global passo_atual

    if passo_atual < len(passos):

        escrever(passos[passo_atual])

        barra["value"] = passo_atual + 1

        status.config(

            text=f"Passo {passo_atual + 1} de {len(passos)}"

        )

        passo_atual += 1

        # próximo passo em 2 segundos
        janela.after(2000, mostrar_passo)

    else:

        finalizar()


def iniciar_tutorial():
    """
    Inicia o tutorial.
    """

    global passo_atual

    passo_atual = 0

    limpar_tutorial()

    barra["value"] = 0

    resultado.config(text="")

    status.config(text="Passo 0 de 10")

    combo.config(state="disabled")

    botao_iniciar.config(state="disabled")

    escrever("👤 Sessão do usuário iniciada.\n")

    janela.after(1000, mostrar_passo)
    # ======================================================
# REINICIAR O SISTEMA
# ======================================================

def preparar_novamente():
    """
    Reinicia toda a interface para um novo preparo.
    """

    global passo_atual

    passo_atual = 0

    limpar_tutorial()

    barra["value"] = 0

    status.config(text="Passo 0 de 10")

    resultado.config(text="")

    combo.config(state="readonly")

    combo.current(0)

    botao_iniciar.config(state="normal")

# ======================================================
# BOTÕES
# ======================================================

frame_botoes = tk.Frame(
    conteudo,
    bg=COR_FUNDO
)

frame_botoes.pack(pady=15)

# ------------------------------

botao_iniciar = tk.Button(

    frame_botoes,

    text="▶ Iniciar Tutorial",

    font=("Segoe UI",11,"bold"),

    bg="#27AE60",

    fg="white",

    width=18,

    cursor="hand2",

    command=iniciar_tutorial

)

botao_iniciar.grid(row=0, column=0, padx=8)

# ------------------------------

botao_reiniciar = tk.Button(

    frame_botoes,

    text="🔄 Preparar Novamente",

    font=("Segoe UI",11,"bold"),

    bg="#F39C12",

    fg="white",

    width=22,

    cursor="hand2",

    command=preparar_novamente

)

botao_reiniciar.grid(row=0, column=1, padx=8)

# ------------------------------

botao_sair = tk.Button(

    frame_botoes,

    text="❌ Sair",

    font=("Segoe UI",11,"bold"),

    bg="#C0392B",

    fg="white",

    width=12,

    cursor="hand2",

    command=janela.destroy

)

botao_sair.grid(row=0, column=2, padx=8)

# ======================================================
# RODAPÉ
# ======================================================

rodape = tk.Label(

    janela,

    text="Sistema desenvolvido em Python + Tkinter",

    bg=COR_FUNDO,

    fg="gray40",

    font=("Segoe UI",9)

)

rodape.pack(side="bottom", pady=10)

# ======================================================
# MENSAGEM INICIAL
# ======================================================

escrever("🍟 Bem-vindo ao Sistema Batata Frita!")
escrever("Escolha a quantidade de porções e clique em 'Iniciar Tutorial'.")
escrever("")

# ======================================================
# INICIAR A JANELA
# ======================================================

janela.mainloop()