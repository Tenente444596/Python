import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("dark")  # "light" ou "dark"
ctk.set_default_color_theme("green")

# Função chamada ao clicar no botão
def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()
    usuario = entry_usuario.get()
    idade = entry_idade.get()
    nacionalidade = combo_nacionalidade.get()

    print("=== DADOS ===")
    print("Email:", email)
    print("Senha:", senha)
    print("Usuário:", usuario)
    print("Idade:", idade)
    print("Nacionalidade:", nacionalidade)


    # Exemplo simples de validação
    if not email or not senha:
        label_status.configure(text="Preencha email e senha!", text_color="green")
    else:
        label_status.configure(text="Login realizado!", text_color="green")

# Criando janela principal
app = ctk.CTk()
app.title("Tela de Login")
app.geometry("700x700")

# Título
titulo = ctk.CTkLabel(app, text="Sistema de Login", font=("Arial", 50))
titulo.pack(pady=50)

# Campo usuário
entry_usuario = ctk.CTkEntry(app, placeholder_text="Nome de usuário")
entry_usuario.pack(pady=10)

# Campo email
entry_email = ctk.CTkEntry(app, placeholder_text="Email")
entry_email.pack(pady=10)

# Campo senha
entry_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*")
entry_senha.pack(pady=10)

# Campo idade
entry_idade = ctk.CTkEntry(app, placeholder_text="Idade")
entry_idade.pack(pady=10)


# Nacionalidade (define idioma futuramente)
combo_nacionalidade = ctk.CTkComboBox(
    app,
    values=["Brasil", "Estados Unidos", "Espanha", "França", "Alemanha", "Portugal", "Italia", "Russia", "Japão", "China", "Checa",
            "Dinamarca", "Polonia", "Coreia", "Hungria","Noruega","Romenia","Servia"]
)
combo_nacionalidade.set("Selecione a nacionalidade")
combo_nacionalidade.pack(pady=20)

def definir_idioma(nacionalidade):
    idiomas = {
        "Brasil": "pt",
        "Estados Unidos": "en",
        "Espanha": "es",
        "França": "fr",
        "Alemanha": "de",
        "Portugal": "pt",
        "Italia": "it",
        "Russia": "ru",
        "Japão": "ja",
        "China": "zh",
        "Checa": "cs",
        "Dinamarca": "da",
        "Polonia": "pl",
        "Coreia": "ko",
        "Hungria": "hu",
        "Noruega": "no"
        "Romenia" "ro",
        "Servia": "sr",
        }
    return idiomas.get(nacionalidade, "pt")

combo_nacionalidade = ctk.CTkComboBox(
    app,
    values = ["Estudante",
            "Engeneiro Militar", 
            "Engeneiro Aeronautico", 
            "Engeneiro Civil", 
            "Engeneiro eletrônico",
            "Engenheiro elétrico",
            "Engenheiro mecânico",
            "Engenheiro quimico",
            "Engenheiro de computação",
            "Engenheiro de telecomunicações",
            "Engenheiro ambiental",
            "Engenheiro eletrotécnico",
            "Engenheiro mecatrônico",
            "Técnico em Informatica",
            "Técnico em eletrônica",
            "Técnico em elétrica",
            "Técnico em secretariado",
            "Técnico em contabilidade",
            "Técnico em administração",
            "Técnico em enfermagem",
            "Técnico em redes de computadores",
            "Técnico em edificações",
            "Auditor",
            "Advogado",
            "Médico",
            "Dentista",
            "Policial civl",
            "Bombeiro civl",
            "Policial Militar",
            "Bombeiro Militar",
            "Magistrado",
            "Contador",
            "Policial Federal",
            "Policial Rodoviario Federal",
            "Neurologista",
            "Cientista de dados",
            "Especialista em hardware",
            "Especialista em sistemas da informação",
            "Psicologo",
            "Nutricionista",
            ]
)
combo_nacionalidade.set("Selecione a profissão")
combo_nacionalidade.pack(pady=20)

# Botão login
botao_login = ctk.CTkButton(app, text="Entrar", command=fazer_login)
botao_login.pack(pady=20)

# Label de status
label_status = ctk.CTkLabel(app, text="")
label_status.pack(pady=20)

# Rodar aplicação
app.mainloop()