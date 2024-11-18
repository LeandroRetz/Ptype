from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd

class Pergunta:
    def __init__(self):
        self.arquivo = ''
        self.df = pd.DataFrame()
        self.perguntas = []  
        self.current_index = 0  

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
        
        if self.perguntas:
            return {
                "pergunta": self.perguntas[self.current_index]["pergunta"],
                "respostas": self.perguntas[self.current_index]["respostas"],
                "certo": self.df.iloc[self.current_index]["certo"]
            }
        return None

    def proxima_pergunta(self):
        
        self.current_index = (self.current_index + 1) % len(self.perguntas)
