from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
class Pergunta():
    def __init__(self):
        self.pergunta = {"pergunta":["1","2","certa"]}
        self.arquivo = ''
        self.df = pd.DataFrame()

    def setdf(self):
        self.df = pd.read_csv(self.arquivo, dtype=str)
        print("Colunas carregadas:", self.df.columns)

    def getPerguntas(self):
        for index,row in self.df.iterrows():
            self.pergunta = {row["Pergunta"]:[row["resp1"],row["resp2"],row["certo"]]}


    def leperguntas(self):
        root = Tk()
        root.withdraw()
        self.arquivo = askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
        self.setdf()
        self.getPerguntas()