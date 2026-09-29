import sys
import subprocess

# ==========================================================
# INSTALAÇÃO AUTOMÁTICA DA BIBLIOTECA
# ==========================================================

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

except ImportError:
    print("Biblioteca 'cryptography' não encontrada.")
    print("Instalando automaticamente...")

    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "cryptography"
    ])

    from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# ==========================================================
# IMPORTAÇÕES
# ==========================================================

import tkinter as tk
from tkinter import messagebox, filedialog
import secrets
import os
from datetime import datetime

from arvore import No, ArvoreBinaria

# ==========================================================
# CONFIGURAÇÕES VISUAIS
# ==========================================================

LARGURA = 1280
ALTURA = 720
FUNDO = "#F4F7FB"
BRANCO = "#FFFFFF"
AZUL = "#2563EB"
AZUL_ESCURO = "#1D4ED8"
AZUL_CLARO = "#EFF6FF"
TEXTO = "#172033"
TEXTO_SECUNDARIO = "#64748B"
BORDA = "#E2E8F0"
VERDE = "#16A34A"
VERMELHO = "#DC2626"


# ==========================================================
# CONFIGURAÇÃO DA SENHA
# ==========================================================

SENHA_CORRETA = "jesussalva"


# ==========================================================
# ÁRVORE
# ==========================================================

arvore = ArvoreBinaria()
contador_mensagens = 0


# ==========================================================
# JANELA PRINCIPAL
# ==========================================================

janela = tk.Tk()

janela.title(
    "Sistema de Criptografia"
)

janela.geometry(
    f"{LARGURA}x{ALTURA}"
)

janela.resizable(
    False,
    False
)

janela.configure(
    bg=FUNDO
)


# ==========================================================
# LIMPAR TELA
# ==========================================================

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()


# ==========================================================
# TÍTULO
# ==========================================================

def criar_titulo(
    titulo,
    subtitulo=None
):
    tk.Label(
        janela,
        text=titulo,
        font=("Arial", 25, "bold"),
        fg=TEXTO,
        bg=FUNDO
    ).pack(
        pady=(55, 8)
    )

    if subtitulo:
        tk.Label(
            janela,
            text=subtitulo,
            font=("Arial", 11),
            fg=TEXTO_SECUNDARIO,
            bg=FUNDO
        ).pack(
            pady=(0, 30)
        )


# ==========================================================
# BOTÃO ARREDONDADO
# ==========================================================

def criar_botao(
    texto,
    comando,
    largura=360,
    altura=58,
    cor=AZUL
):
    canvas = tk.Canvas(
        janela,
        width=largura,
        height=altura,
        bg=FUNDO,
        highlightthickness=0
    )

    raio = 18

    # ------------------------------------------
    # DESENHAR BOTÃO
    # ------------------------------------------

    canvas.create_arc(
        0,
        0,
        raio * 2,
        raio * 2,
        start=90,
        extent=90,
        fill=cor,
        outline=cor
    )

    canvas.create_arc(
        largura - raio * 2,
        0,
        largura,
        raio * 2,
        start=0,
        extent=90,
        fill=cor,
        outline=cor
    )

    canvas.create_arc(
        0,
        altura - raio * 2,
        raio * 2,
        altura,
        start=180,
        extent=90,
        fill=cor,
        outline=cor
    )

    canvas.create_arc(
        largura - raio * 2,
        altura - raio * 2,
        largura,
        altura,
        start=270,
        extent=90,
        fill=cor,
        outline=cor
    )

    canvas.create_rectangle(
        raio,
        0,
        largura - raio,
        altura,
        fill=cor,
        outline=cor
    )

    canvas.create_rectangle(
        0,
        raio,
        largura,
        altura - raio,
        fill=cor,
        outline=cor
    )

    # ------------------------------------------
    # TEXTO
    # ------------------------------------------

    canvas.create_text(
        largura / 2,
        altura / 2,
        text=texto,
        fill=BRANCO,
        font=("Arial", 11, "bold")
    )

    # ------------------------------------------
    # CLIQUE
    # ------------------------------------------

    canvas.bind(
        "<Button-1>",
        lambda evento: comando()
    )

    # ------------------------------------------
    # EFEITO AO PASSAR O MOUSE
    # ------------------------------------------

    def mouse_entrou(evento):
        canvas.configure(
            bg=FUNDO
        )

        canvas.delete("all")

        canvas.create_arc(
            0,
            0,
            raio * 2,
            raio * 2,
            start=90,
            extent=90,
            fill=AZUL_ESCURO,
            outline=AZUL_ESCURO
        )

        canvas.create_arc(
            largura - raio * 2,
            0,
            largura,
            raio * 2,
            start=0,
            extent=90,
            fill=AZUL_ESCURO,
            outline=AZUL_ESCURO
        )

        canvas.create_arc(
            0,
            altura - raio * 2,
            raio * 2,
            altura,
            start=180,
            extent=90,
            fill=AZUL_ESCURO,
            outline=AZUL_ESCURO
        )

        canvas.create_arc(
            largura - raio * 2,
            altura - raio * 2,
            largura,
            altura,
            start=270,
            extent=90,
            fill=AZUL_ESCURO,
            outline=AZUL_ESCURO
        )

        canvas.create_rectangle(
            raio,
            0,
            largura - raio,
            altura,
            fill=AZUL_ESCURO,
            outline=AZUL_ESCURO
        )

        canvas.create_rectangle(
            0,
            raio,
            largura,
            altura - raio,
            fill=AZUL_ESCURO,
            outline=AZUL_ESCURO
        )

        canvas.create_text(
            largura / 2,
            altura / 2,
            text=texto,
            fill=BRANCO,
            font=("Arial", 11, "bold")
        )

    def mouse_saiu(evento):
        canvas.delete("all")

        canvas.create_arc(
            0,
            0,
            raio * 2,
            raio * 2,
            start=90,
            extent=90,
            fill=cor,
            outline=cor
        )

        canvas.create_arc(
            largura - raio * 2,
            0,
            largura,
            raio * 2,
            start=0,
            extent=90,
            fill=cor,
            outline=cor
        )

        canvas.create_arc(
            0,
            altura - raio * 2,
            raio * 2,
            altura,
            start=180,
            extent=90,
            fill=cor,
            outline=cor
        )

        canvas.create_arc(
            largura - raio * 2,
            altura - raio * 2,
            largura,
            altura,
            start=270,
            extent=90,
            fill=cor,
            outline=cor
        )

        canvas.create_rectangle(
            raio,
            0,
            largura - raio,
            altura,
            fill=cor,
            outline=cor
        )

        canvas.create_rectangle(
            0,
            raio,
            largura,
            altura - raio,
            fill=cor,
            outline=cor
        )

        canvas.create_text(
            largura / 2,
            altura / 2,
            text=texto,
            fill=BRANCO,
            font=("Arial", 11, "bold")
        )

    canvas.bind(
        "<Enter>",
        mouse_entrou
    )

    canvas.bind(
        "<Leave>",
        mouse_saiu
    )

    return canvas


# ==========================================================
# BOTÃO VOLTAR
# ==========================================================

def criar_botao_voltar(
    comando
):
    tk.Button(
        janela,
        text="←  Voltar",
        command=comando,
        font=("Arial", 10),
        fg=TEXTO_SECUNDARIO,
        bg=FUNDO,
        activebackground=FUNDO,
        activeforeground=AZUL,
        relief="flat",
        bd=0,
        cursor="hand2"
    ).place(
        x=25,
        y=20
    )


# ==========================================================
# GERAR CHAVE
# ==========================================================

def gerar_chave(senha):
    chave = senha.encode(
        "utf-8"
    )

    if len(chave) < 32:
        chave = chave.ljust(
            32,
            b"0"
        )

    return chave[:32]


# ==========================================================
# REGISTRAR HISTÓRICO
# ==========================================================

def registrar_historico(
    arquivo,
    status,
    mensagem
):
    global contador_mensagens

    contador_mensagens += 1

    data_hora = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    novo_no = No(
        contador_mensagens,
        arquivo,
        data_hora,
        status,
        mensagem
    )

    arvore.inserir(
        novo_no
    )


# ==========================================================
# TELA PRINCIPAL
# ==========================================================

def tela_principal():
    limpar_tela()

    # ------------------------------------------
    # ÍCONE
    # ------------------------------------------

    tk.Label(
        janela,
        text="🔐",
        font=("Arial", 42),
        bg=FUNDO,
        fg=AZUL
    ).pack(
        pady=(95, 10)
    )

    # ------------------------------------------
    # TÍTULO
    # ------------------------------------------

    tk.Label(
        janela,
        text="Criptografia",
        font=("Arial", 28, "bold"),
        fg=TEXTO,
        bg=FUNDO
    ).pack()

    tk.Label(
        janela,
        text="Comunicação segura de mensagens",
        font=("Arial", 11),
        fg=TEXTO_SECUNDARIO,
        bg=FUNDO
    ).pack(
        pady=(8, 55)
    )

    # ------------------------------------------
    # BOTÕES
    # ------------------------------------------

    criar_botao(
        "CRIPTOGRAFAR",
        tela_criptografar
    ).pack(
        pady=10
    )

    criar_botao(
        "DESCRIPTOGRAFAR",
        tela_descriptografar
    ).pack(
        pady=10
    )

    criar_botao(
        "HISTÓRICO",
        tela_historico
    ).pack(
        pady=10
    )

    # ------------------------------------------
    # RODAPÉ
    # ------------------------------------------

    tk.Label(
        janela,
        text="Sistema de mensagens seguras",
        font=("Arial", 9),
        fg=TEXTO_SECUNDARIO,
        bg=FUNDO
    ).pack(
        side="bottom",
        pady=35
    )


# ==========================================================
# TELA CRIPTOGRAFAR
# ==========================================================

def tela_criptografar():

    limpar_tela()

    criar_botao_voltar(
        tela_principal
    )

    criar_titulo(
        "Criptografar",
        "Proteja sua mensagem com a chave do sistema"
    )

    # ------------------------------------------
    # MENSAGEM
    # ------------------------------------------

    tk.Label(
        janela,
        text="Mensagem",
        font=("Arial", 11, "bold"),
        fg=TEXTO,
        bg=FUNDO
    ).pack(
        anchor="w",
        padx=45
    )

    campo_mensagem = tk.Text(
        janela,
        width=48,
        height=12,
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground=BORDA,
        highlightcolor=AZUL,
        wrap="word"
    )

    campo_mensagem.pack(
        padx=45,
        pady=(8, 25)
    )

    # ------------------------------------------
    # CHAVE
    # ------------------------------------------

    tk.Label(
        janela,
        text="Chave",
        font=("Arial", 11, "bold"),
        fg=TEXTO,
        bg=FUNDO
    ).pack(
        anchor="w",
        padx=45
    )

    campo_chave = tk.Entry(
        janela,
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO,
        relief="solid",
        bd=1,
        show="*"
    )

    campo_chave.pack(
        fill="x",
        padx=45,
        pady=(8, 40),
        ipady=10
    )

    # ------------------------------------------
    # CRIPTOGRAFAR
    # ------------------------------------------

    def criptografar():

        mensagem = campo_mensagem.get(
            "1.0",
            tk.END
        ).strip()

        senha = campo_chave.get()

        if not mensagem:
            messagebox.showwarning(
                "Atenção",
                "Digite uma mensagem."
            )
            return

        if not senha:
            messagebox.showwarning(
                "Atenção",
                "Digite a chave."
            )
            return

        # A única senha aceita pelo sistema
        if senha != SENHA_CORRETA:
            messagebox.showerror(
                "Chave inválida",
                "A chave informada está incorreta."
            )
            return

        try:

            chave = gerar_chave(
                SENHA_CORRETA
            )

            aes = AESGCM(
                chave
            )

            nonce = secrets.token_bytes(
                12
            )

            dados = aes.encrypt(
                nonce,
                mensagem.encode(
                    "utf-8"
                ),
                None
            )

            caminho = filedialog.asksaveasfilename(
                title="Salvar mensagem criptografada",
                defaultextension=".enc",
                filetypes=[
                    (
                        "Arquivo criptografado",
                        "*.enc"
                    )
                ]
            )

            if not caminho:
                return

            with open(
                caminho,
                "wb"
            ) as arquivo:

                arquivo.write(
                    nonce
                )

                arquivo.write(
                    dados
                )

            registrar_historico(
                caminho,
                "Enviada",
                mensagem
            )

            messagebox.showinfo(
                "Concluído",
                "Mensagem criptografada com sucesso."
            )

            tela_principal()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                f"Não foi possível criptografar:\n{erro}"
            )

    criar_botao(
        "Criptografar mensagem",
        criptografar
    ).pack(
        pady=10
    )


# ==========================================================
# TELA DESCRIPTOGRAFAR
# ==========================================================

def tela_descriptografar():

    limpar_tela()

    criar_botao_voltar(
        tela_principal
    )

    criar_titulo(
        "Descriptografar",
        "Recupere uma mensagem usando a chave do sistema"
    )

    # ------------------------------------------
    # ARQUIVO
    # ------------------------------------------

    tk.Label(
        janela,
        text="Arquivo criptografado",
        font=("Arial", 11, "bold"),
        fg=TEXTO,
        bg=FUNDO
    ).pack(
        anchor="w",
        padx=45
    )

    arquivo_selecionado = tk.StringVar()

    campo_arquivo = tk.Entry(
        janela,
        textvariable=arquivo_selecionado,
        font=("Arial", 10),
        bg=BRANCO,
        fg=TEXTO_SECUNDARIO,
        relief="solid",
        bd=1,
        state="readonly"
    )

    campo_arquivo.pack(
        fill="x",
        padx=45,
        pady=(8, 10),
        ipady=10
    )

    def selecionar_arquivo():

        caminho = filedialog.askopenfilename(
            title="Selecionar arquivo",
            filetypes=[
                (
                    "Arquivo criptografado",
                    "*.enc"
                )
            ]
        )

        if caminho:
            arquivo_selecionado.set(
                caminho
            )

    criar_botao(
        "Selecionar arquivo",
        selecionar_arquivo,
        largura=250,
        altura=50,
        cor=AZUL
    ).pack(
        pady=(0, 35)
    )

    # ------------------------------------------
    # CHAVE
    # ------------------------------------------

    tk.Label(
        janela,
        text="Chave",
        font=("Arial", 11, "bold"),
        fg=TEXTO,
        bg=FUNDO
    ).pack(
        anchor="w",
        padx=45
    )

    campo_chave = tk.Entry(
        janela,
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO,
        relief="solid",
        bd=1,
        show="*"
    )

    campo_chave.pack(
        fill="x",
        padx=45,
        pady=(8, 40),
        ipady=10
    )

    # ------------------------------------------
    # DESCRIPTOGRAFAR
    # ------------------------------------------

    def descriptografar():

        caminho = arquivo_selecionado.get()
        senha = campo_chave.get()

        if not caminho:
            messagebox.showwarning(
                "Atenção",
                "Selecione um arquivo."
            )
            return

        if not senha:
            messagebox.showwarning(
                "Atenção",
                "Digite a chave."
            )
            return

        # A única senha aceita pelo sistema
        if senha != SENHA_CORRETA:
            messagebox.showerror(
                "Chave inválida",
                "A chave informada está incorreta."
            )
            return

        try:

            with open(
                caminho,
                "rb"
            ) as arquivo:

                dados = arquivo.read()

            nonce = dados[:12]

            dados_criptografados = dados[12:]

            # Usa sempre a senha oficial do sistema
            chave = gerar_chave(
                SENHA_CORRETA
            )

            aes = AESGCM(
                chave
            )

            mensagem = aes.decrypt(
                nonce,
                dados_criptografados,
                None
            ).decode(
                "utf-8"
            )

            registrar_historico(
                caminho,
                "Recuperada",
                mensagem
            )

            tela_mensagem_recuperada(
                mensagem,
                caminho
            )

        except Exception:

            messagebox.showerror(
                "Erro",
                "Não foi possível descriptografar.\n\n"
                "Verifique a chave e o arquivo."
            )

    criar_botao(
        "Descriptografar mensagem",
        descriptografar
    ).pack(
        pady=10
    )


# ==========================================================
# TELA DA MENSAGEM
# ==========================================================

def tela_mensagem_recuperada(
    mensagem,
    caminho
):

    limpar_tela()

    criar_botao_voltar(
        tela_principal
    )

    criar_titulo(
        "Mensagem recuperada",
        "A mensagem foi descriptografada"
    )

    campo_mensagem = tk.Text(
        janela,
        width=48,
        height=15,
        font=("Arial", 11),
        bg=BRANCO,
        fg=TEXTO,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground=BORDA,
        wrap="word"
    )

    campo_mensagem.pack(
        padx=45,
        pady=10
    )

    campo_mensagem.insert(
        tk.END,
        mensagem
    )

    campo_mensagem.config(
        state="disabled"
    )

    def marcar_lida():

        registrar_historico(
            caminho,
            "Lida",
            mensagem
        )

        messagebox.showinfo(
            "Histórico",
            "Mensagem registrada como lida."
        )

        tela_principal()

    criar_botao(
        "Marcar como lida",
        marcar_lida
    ).pack(
        pady=25
    )


# ==========================================================
# TELA HISTÓRICO
# ==========================================================

def tela_historico():

    limpar_tela()

    criar_botao_voltar(
        tela_principal
    )

    criar_titulo(
        "Histórico",
        "Mensagens registradas no sistema"
    )

    # ------------------------------------------
    # ÁREA DO HISTÓRICO
    # ------------------------------------------

    mensagens = arvore.pos_ordem()

    if not mensagens:

        tk.Label(
            janela,
            text="Nenhuma mensagem registrada.",
            font=("Arial", 11),
            fg=TEXTO_SECUNDARIO,
            bg=FUNDO
        ).pack(
            pady=100
        )

    else:

        # --------------------------------------
        # FRAME COM SCROLL
        # --------------------------------------

        container = tk.Frame(
            janela,
            bg=FUNDO
        )

        container.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        canvas = tk.Canvas(
            container,
            bg=FUNDO,
            highlightthickness=0
        )

        barra = tk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        frame_historico = tk.Frame(
            canvas,
            bg=FUNDO
        )

        frame_historico.bind(
            "<Configure>",
            lambda evento:
            canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=frame_historico,
            anchor="nw",
            width=450
        )

        canvas.configure(
            yscrollcommand=barra.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        barra.pack(
            side="right",
            fill="y"
        )

        # --------------------------------------
        # MENSAGENS
        # --------------------------------------

        for mensagem in mensagens:

            nome_arquivo = os.path.basename(
                mensagem.arquivo
            )

            card = tk.Frame(
                frame_historico,
                bg=BRANCO,
                highlightbackground=BORDA,
                highlightthickness=1
            )

            card.pack(
                fill="x",
                pady=8
            )

            # ----------------------------------
            # STATUS
            # ----------------------------------

            tk.Label(
                card,
                text=mensagem.status.upper(),
                font=("Arial", 9, "bold"),
                fg=AZUL,
                bg=BRANCO
            ).pack(
                anchor="w",
                padx=18,
                pady=(15, 3)
            )

            # ----------------------------------
            # DATA
            # ----------------------------------

            tk.Label(
                card,
                text=mensagem.data_hora,
                font=("Arial", 9),
                fg=TEXTO_SECUNDARIO,
                bg=BRANCO
            ).pack(
                anchor="w",
                padx=18
            )

            # ----------------------------------
            # MENSAGEM
            # ----------------------------------

            tk.Label(
                card,
                text=mensagem.mensagem,
                font=("Arial", 11),
                fg=TEXTO,
                bg=BRANCO,
                justify="left",
                anchor="w",
                wraplength=410
            ).pack(
                fill="x",
                padx=18,
                pady=(12, 8)
            )

            # ----------------------------------
            # ARQUIVO
            # ----------------------------------

            tk.Label(
                card,
                text=f"Arquivo: {nome_arquivo}",
                font=("Arial", 8),
                fg=TEXTO_SECUNDARIO,
                bg=BRANCO
            ).pack(
                anchor="w",
                padx=18,
                pady=(0, 15)
            )

    # ------------------------------------------
    # INFORMAÇÃO DA ÁRVORE
    # ------------------------------------------

    tk.Label(
        janela,
        text="Árvore binária • percurso em pós-ordem",
        font=("Arial", 9),
        fg=TEXTO_SECUNDARIO,
        bg=FUNDO
    ).pack(
        pady=15
    )


# ==========================================================
# INICIAR PROGRAMA
# ==========================================================

tela_principal()

janela.mainloop()
