import tkinter as tk #interage com componentes gráficos
from tkinter import ttk #para usar "TreeView"
import crud as crud

class PrincipalBD:
    def __init__(self, win): #construtor desta classe
        
        self.lbCodigo=tk.Label(win, text='Número do Brinco')
        self.lblNome=tk.Label(win, text='Sexo do animal')
        self.lblPreco=tk.Label(win, text='Peso do animal')
        self.txtCodigo=tk.Entry(bd=3)
        self.txtNome=tk.Entry()
        self.txtPreco=tk.Entry()
        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)

        self.dadosColunas = ("BRINCO", "SEXO", "PESO")

        self.treeProdutos = ttk.Treeview(win, columns=self.dadosColunas, selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(win, orient="vertical", command=self.treeProdutos.yview)
        self.verscrlbar.pack(side='right', fill='x')

        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        self.treeProdutos.heading("BRINCO", text="BRINCO")
        self.treeProdutos.heading("SEXO", text="SEXO")
        self.treeProdutos.heading("PESO", text="PESO")

        self.treeProdutos.column("BRINCO", minwidth=0, width=100)
        self.treeProdutos.column("SEXO", minwidth=0, width=100)
        self.treeProdutos.column("PESO", minwidth=0, width=100)

        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)
        
        #Posições em janela

        self.lbCodigo.place(x=100, y=50)
        self.txtCodigo.place(x=250, y=50)

        self.lblNome.place(x=100, y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100, y=150)
        self.txtPreco.place(x=250, y=150)

        self.btnCadastrar.place(x=100, y=200)
        self.btnAtualizar.place(x=200, y=200)
        self.btnExcluir.place(x=300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300, height=225)
        self.carregarDadosIniciais()

    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():#Obtemos os registros que foram selecionados na grade de registros.
            item = self.treeProdutos.item(selection)
            BRINCO,SEXO,PESO = item["values"][0:3]#Os dados selecionados são associados às variáveis e os valores das variáveis são associados às caixas de texto.
            self.txtCodigo.insert(0, BRINCO)
            self.txtNome.insert(0, SEXO)
            self.txtPreco.insert(0, PESO)

    def carregarDadosIniciais(self):
        try:
            self.id = 0 #Necessário para gerenciar o componente "TreeView".
            self.iid = 0
            registros=self.objBD.selecionarDados()#Recupera todos os registros armazenados na tabela.
            print("********dados disponíveis no BD ********")
            for item in registros:
                BRINCO=item[0]#Obtemos os valores dos registros e associamos às respectivas variáveis.
                SEXO=item[1]
                PESO=item[2]
                print("BRINCO = ", BRINCO)
                print("SEXO = ", SEXO)
                print("PESO = ", PESO, "\n")

                self.treeProdutos.insert('', 'end', iid=self.iid, values=(BRINCO, SEXO, PESO))

                self.iid = self.iid + 1
                self.id = self.id + 1
            print('Dados da Base')
        except:
            print('Ainda não existem dados para carregar')

    #Leitura dos dados
            
    def fLerCampos(self):
        try:
            print("****** Dados disponíveis *******")
            BRINCO = int(self.txtCodigo.get())
            print('BRINCO', BRINCO)
            SEXO = self.txtNome.get()
            print('BRINCO', BRINCO)
            PESO = float(self.txtPreco.get())
            print('PESO', PESO)
            print('Leitura dos Dados realizada com Sucesso!')
        except:
            print('Não foi possível ler os dados.')
        return BRINCO, SEXO, PESO
    
    # CADASTRO DOS ANIMAIS

    def fCadastrarProduto(self):
        try:
            print("******Dados disponíveis ******")
            BRINCO, SEXO, PESO=self.fLerCampos()
            self.objBD.inserirDados(BRINCO, SEXO, PESO)
            self.treeProdutos.insert('', 'end', iid=self.iid, values=(BRINCO, SEXO, PESO))

            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Animal Cadastrado com Sucesso!')
        except:
            print('Não foi possível fazer o cadastro.')

    #ATUALIZAR 
    
    def fAtualizarProduto(self):
        try:
            print("****** Dados disponíveis *******")
            BRINCO, SEXO, PESO=self.fLerCampos()
            self.objBD.atualizarDados(BRINCO, SEXO, PESO)
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')

    #EXCLUIR
            
    def fExcluirProduto(self):
        try:
            print("******** Dados disponíveis ******")
            BRINCO, SEXO, PESO=self.fLerCampos()
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print('Produto Excluído com Sucesso!')
        except:
            print('Não foi possível fazer a exclusão do ítem.')

    #LIMPAR TELA
            
    def fLimparTela(self):
        try:
            print("***** Dados disponíveis *****")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')

    #PROGRAMA PRINCIPAL
            
janela=tk.Tk()
principal=PrincipalBD(janela)
janela.title('Bem Vindo a Aplicação de Banco de Dados')
janela.geometry("720x600+10+10")
janela.mainloop()

    


    








