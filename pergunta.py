from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import random as rand

class Pergunta:
    def __init__(self):
        self.arquivo = ''
        self.df = pd.DataFrame()
        self.perguntas = []  
        self.perguntas_disponiveis = []

    def setdf(self):
        self.df = pd.read_csv(self.arquivo, dtype=str)
        self.perguntas = [
            {"pergunta": row["Pergunta"], "respostas": [row["resp1"], row["resp2"]]}
            for _, row in self.df.iterrows()
        ]
        self.perguntas_disponiveis = list(range(len(self.perguntas)))
        print("Colunas carregadas:", self.df.columns)

    def leperguntas(self):
        root = Tk()
        root.withdraw()
        self.arquivo = askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
        self.setdf()

    def get_pergunta_atual(self):
        if self.perguntas_disponiveis:
            random_index = rand.choice(self.perguntas_disponiveis)
            self.perguntas_disponiveis.remove(random_index)
            
            pergunta_data = self.perguntas[random_index]
            return {
                "pergunta": pergunta_data["pergunta"],
                "respostas": pergunta_data["respostas"],
                "certo": self.df.iloc[random_index]["certo"]
            }
        return None

    def proxima_pergunta(self):
        
        pass
