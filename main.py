import tkinter as tk


# =========================
# CONFIGURAÇÃO DA JANELA
# =========================

LARGURA = 540
ALTURA = 960

FUNDO = "#F4F7FB"
BRANCO = "#FFFFFF"
AZUL = "#2563EB"
AZUL_ESCURO = "#1D4ED8"
TEXTO = "#172033"
TEXTO_SECUNDARIO = "#64748B"
BORDA = "#E2E8F0"


# =========================
# FUNÇÕES
# =========================

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()


def criar_titulo(titulo, subtitulo):
    tk.Label(
        janela,
        text=titulo,
        font=("Arial", 25, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(pady=(50, 8))

    tk.Label(
        janela,
        text=subtitulo,
        font=("Arial", 11),
        bg=FUNDO,
        fg=TEXTO_SECUNDARIO
    ).pack(pady=(0, 40))


def criar_botao(texto, comando):
    botao = tk.Button(
        janela,
        text=texto,
        command=comando,
        font=("Arial", 12, "bold"),
        bg=AZUL,
        fg=BRANCO,
        activebackground=AZUL_ESCURO,
        activeforeground=BRANCO,
        relief="flat",
        bd=0,
        width=30,
        height=3,
        cursor="hand2"
    )

    botao.pack(pady=12)

    return botao


# =========================
# TELAS
# =========================

def tela_criptografar():
    limpar_tela()

    criar_titulo(
        "Criptografar",
        "Proteja sua mensagem com uma chave"
    )

    tk.Label(
        janela,
        text="Mensagem",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(anchor="w", padx=55)

    mensagem = tk.Text(
        janela,
        width=45,
        height=10,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    mensagem.pack(pady=(8, 25))

    tk.Label(
        janela,
        text="Chave",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(anchor="w", padx=55)

    chave = tk.Entry(
        janela,
        width=40,
        font=("Arial", 11),
        show="*",
        relief="solid",
        bd=1
    )

    chave.pack(pady=8)

    criar_botao(
        "CRIPTOGRAFAR",
        lambda: print("Criptografar")
    )

    tk.Button(
        janela,
        text="← Voltar",
        command=tela_principal,
        font=("Arial", 11),
        bg=FUNDO,
        fg=AZUL,
        relief="flat",
        cursor="hand2"
    ).pack(pady=30)


def tela_descriptografar():
    limpar_tela()

    criar_titulo(
        "Descriptografar",
        "Recupere uma mensagem protegida"
    )

    tk.Label(
        janela,
        text="Arquivo criptografado",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(anchor="w", padx=55)

    arquivo = tk.Entry(
        janela,
        width=40,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    arquivo.pack(pady=(8, 25))

    tk.Label(
        janela,
        text="Chave",
        font=("Arial", 11, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack(anchor="w", padx=55)

    chave = tk.Entry(
        janela,
        width=40,
        font=("Arial", 11),
        show="*",
        relief="solid",
        bd=1
    )

    chave.pack(pady=8)

    criar_botao(
        "DESCRIPTOGRAFAR",
        lambda: print("Descriptografar")
    )

    tk.Button(
        janela,
        text="← Voltar",
        command=tela_principal,
        font=("Arial", 11),
        bg=FUNDO,
        fg=AZUL,
        relief="flat",
        cursor="hand2"
    ).pack(pady=30)


def tela_historico():
    limpar_tela()

    criar_titulo(
        "Histórico",
        "Mensagens enviadas e recuperadas"
    )

    tk.Label(
        janela,
        text="O histórico das mensagens aparecerá aqui.",
        font=("Arial", 11),
        bg=FUNDO,
        fg=TEXTO_SECUNDARIO
    ).pack(pady=100)

    tk.Button(
        janela,
        text="← Voltar",
        command=tela_principal,
        font=("Arial", 11),
        bg=FUNDO,
        fg=AZUL,
        relief="flat",
        cursor="hand2"
    ).pack(pady=30)


def tela_principal():
    limpar_tela()

    tk.Label(
        janela,
        text="🔐",
        font=("Arial", 45),
        bg=FUNDO
    ).pack(pady=(80, 15))

    tk.Label(
        janela,
        text="Criptografia",
        font=("Arial", 28, "bold"),
        bg=FUNDO,
        fg=TEXTO
    ).pack()

    tk.Label(
        janela,
        text="Sistema de troca segura de mensagens",
        font=("Arial", 11),
        bg=FUNDO,
        fg=TEXTO_SECUNDARIO
    ).pack(pady=(8, 70))

    criar_botao(
        "CRIPTOGRAFAR",
        tela_criptografar
    )

    criar_botao(
        "DESCRIPTOGRAFAR",
        tela_descriptografar
    )

    criar_botao(
        "HISTÓRICO",
        tela_historico
    )

    tk.Label(
        janela,
        text="Mensagens protegidas por criptografia simétrica",
        font=("Arial", 9),
        bg=FUNDO,
        fg=TEXTO_SECUNDARIO
    ).pack(side="bottom", pady=35)


# =========================
# JANELA PRINCIPAL
# =========================

janela = tk.Tk()

janela.title("Criptografia")

janela.geometry(f"{LARGURA}x{ALTURA}")

janela.resizable(False, False)

janela.configure(bg=FUNDO)

tela_principal()

janela.mainloop()
