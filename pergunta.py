from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd

class Pergunta:
    def __init__(self):
        self.arquivo = ''
        self.df = pd.DataFrame()
        self.perguntas = []  # Lista para armazenar perguntas
        self.current_index = 0  # Índice para rastrear a pergunta atual

    def setdf(self):
        self.df = pd.read_csv(self.arquivo, dtype=str)
        self.perguntas = [
            {"pergunta": row["Pergunta"], "respostas": [row["resp1"], row["resp2"]]}
            for _, row in self.df.iterrows()
        ]
        print("Colunas carregadas:", self.df.columns)

    def leperguntas(self):
        root = Tk()
        root.withdraw()
        self.arquivo = askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
        self.setdf()

    def get_pergunta_atual(self):
        # Retorna a pergunta e respostas atuais
        if self.perguntas:
            return self.perguntas[self.current_index]
        return None

    def proxima_pergunta(self):
        # Avança para a próxima pergunta
        self.current_index = (self.current_index + 1) % len(self.perguntas)
