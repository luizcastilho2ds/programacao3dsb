"""
Sistema de Biblioteca Digital Expandido
Gerencia informações sobre livros cadastrados com funcionalidades avançadas
"""

from datetime import datetime
from typing import List, Optional


class Livro:
    """
    Classe que representa um livro na biblioteca digital.
    
    Atributos:
        titulo (str): Título do livro
        autor (str): Autor do livro
        paginas (int): Número de páginas do livro
        isbn (str): ISBN do livro (número único)
        ano_publicacao (int): Ano de publicação
        genero (str): Gênero do livro
        disponivel (bool): Status de disponibilidade
    """
    
    def __init__(self, titulo, autor, paginas, isbn, ano_publicacao, genero, disponivel=True):
        """
        Inicializa um novo livro com os dados fornecidos.
        
        Args:
            titulo (str): Título do livro
            autor (str): Autor do livro
            paginas (int): Número de páginas do livro
            isbn (str): ISBN do livro
            ano_publicacao (int): Ano de publicação
            genero (str): Gênero do livro
            disponivel (bool): Status de disponibilidade (padrão: True)
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.genero = genero
        self.disponivel = disponivel
    
    def __str__(self):
        """
        Retorna uma representação textual formatada do livro.
        
        Returns:
            str: String contendo informações completas do livro formatadas
        """
        status = "✓ Disponível" if self.disponivel else "✗ Indisponível"
        return (
            f"Livro: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Páginas: {self.paginas}\n"
            f"ISBN: {self.isbn}\n"
            f"Ano de Publicação: {self.ano_publicacao}\n"
            f"Gênero: {self.genero}\n"
            f"Status: {status}"
        )
    
    def __repr__(self):
        """Representação técnica do objeto."""
        return f"Livro('{self.titulo}', '{self.autor}', {self.paginas}, '{self.isbn}')"
    
    def __eq__(self, outro):
        """Compara dois livros pelo ISBN."""
        if isinstance(outro, Livro):
            return self.isbn == outro.isbn
        return False
    
    def __lt__(self, outro):
        """Compara livros por número de páginas (menor que)."""
        if isinstance(outro, Livro):
            return self.paginas < outro.paginas
        return NotImplemented
    
    def __le__(self, outro):
        """Compara livros por número de páginas (menor ou igual)."""
        if isinstance(outro, Livro):
            return self.paginas <= outro.paginas
        return NotImplemented
    
    def __gt__(self, outro):
        """Compara livros por número de páginas (maior que)."""
        if isinstance(outro, Livro):
            return self.paginas > outro.paginas
        return NotImplemented
    
    def __ge__(self, outro):
        """Compara livros por número de páginas (maior ou igual)."""
        if isinstance(outro, Livro):
            return self.paginas >= outro.paginas
        return NotImplemented
    
    def obter_info_resumida(self):
        """Retorna um resumo rápido das informações do livro."""
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"
    
    def emprestar(self):
        """Marca o livro como indisponível."""
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    
    def devolver(self):
        """Marca o livro como disponível."""
        if not self.disponivel:
            self.disponivel = True
            return True
        return False


class Biblioteca:
    """
    Classe que gerencia uma biblioteca digital com múltiplos livros.
    
    Atributos:
        nome (str): Nome da biblioteca
        livros (List[Livro]): Lista de livros cadastrados
        data_criacao (datetime): Data de criação da biblioteca
    """
    
    def __init__(self, nome):
        """
        Inicializa uma nova biblioteca.
        
        Args:
            nome (str): Nome da biblioteca
        """
        self.nome = nome
        self.livros = []
        self.data_criacao = datetime.now()
    
    def adicionar_livro(self, livro: Livro) -> bool:
        """
        Adiciona um livro à biblioteca.
        
        Args:
            livro (Livro): Objeto da classe Livro a ser adicionado
            
        Returns:
            bool: True se adicionado com sucesso, False se ISBN já existe
        """
        # Verifica se ISBN já existe
        if any(l.isbn == livro.isbn for l in self.livros):
            return False
        self.livros.append(livro)
        return True
    
    def remover_livro(self, isbn: str) -> bool:
        """
        Remove um livro da biblioteca pelo ISBN.
        
        Args:
            isbn (str): ISBN do livro a remover
            
        Returns:
            bool: True se removido com sucesso, False se não encontrado
        """
        livro = self.buscar_por_isbn(isbn)
        if livro:
            self.livros.remove(livro)
            return True
        return False
    
    def buscar_por_titulo(self, titulo: str) -> List[Livro]:
        """
        Busca livros pelo título (busca parcial, case-insensitive).
        
        Args:
            titulo (str): Título ou parte do título a buscar
            
        Returns:
            List[Livro]: Lista de livros encontrados
        """
        titulo_lower = titulo.lower()
        return [livro for livro in self.livros 
                if titulo_lower in livro.titulo.lower()]
    
    def buscar_por_autor(self, autor: str) -> List[Livro]:
        """
        Busca livros pelo autor (busca parcial, case-insensitive).
        
        Args:
            autor (str): Nome ou parte do nome do autor a buscar
            
        Returns:
            List[Livro]: Lista de livros encontrados
        """
        autor_lower = autor.lower()
        return [livro for livro in self.livros 
                if autor_lower in livro.autor.lower()]
    
    def buscar_por_genero(self, genero: str) -> List[Livro]:
        """
        Busca livros pelo gênero.
        
        Args:
            genero (str): Gênero a buscar
            
        Returns:
            List[Livro]: Lista de livros encontrados
        """
        genero_lower = genero.lower()
        return [livro for livro in self.livros 
                if genero_lower in livro.genero.lower()]
    
    def buscar_por_isbn(self, isbn: str) -> Optional[Livro]:
        """
        Busca um livro específico pelo ISBN.
        
        Args:
            isbn (str): ISBN do livro a buscar
            
        Returns:
            Optional[Livro]: O livro encontrado ou None
        """
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None
    
    def listar_por_genero(self, genero: str) -> List[Livro]:
        """
        Lista todos os livros de um determinado gênero.
        
        Args:
            genero (str): Gênero desejado
            
        Returns:
            List[Livro]: Lista de livros do gênero
        """
        return self.buscar_por_genero(genero)
    
    def listar_disponiveis(self) -> List[Livro]:
        """
        Lista todos os livros disponíveis para empréstimo.
        
        Returns:
            List[Livro]: Lista de livros disponíveis
        """
        return [livro for livro in self.livros if livro.disponivel]
    
    def listar_indisponiveis(self) -> List[Livro]:
        """
        Lista todos os livros indisponíveis para empréstimo.
        
        Returns:
            List[Livro]: Lista de livros indisponíveis
        """
        return [livro for livro in self.livros if not livro.disponivel]
    
    def ordenar_por_paginas(self, decrescente=False) -> List[Livro]:
        """
        Ordena livros pelo número de páginas.
        
        Args:
            decrescente (bool): Se True, ordena em ordem decrescente
            
        Returns:
            List[Livro]: Lista ordenada de livros
        """
        return sorted(self.livros, key=lambda l: l.paginas, reverse=decrescente)
    
    def ordenar_por_ano(self, decrescente=False) -> List[Livro]:
        """
        Ordena livros pelo ano de publicação.
        
        Args:
            decrescente (bool): Se True, ordena em ordem decrescente
            
        Returns:
            List[Livro]: Lista ordenada de livros
        """
        return sorted(self.livros, key=lambda l: l.ano_publicacao, reverse=decrescente)
    
    def ordenar_por_titulo(self) -> List[Livro]:
        """
        Ordena livros alfabeticamente pelo título.
        
        Returns:
            List[Livro]: Lista ordenada de livros
        """
        return sorted(self.livros, key=lambda l: l.titulo.lower())
    
    def comparar_livros(self, isbn1: str, isbn2: str) -> dict:
        """
        Compara dois livros pelo ISBN.
        
        Args:
            isbn1 (str): ISBN do primeiro livro
            isbn2 (str): ISBN do segundo livro
            
        Returns:
            dict: Dicionário com comparação dos livros
        """
        livro1 = self.buscar_por_isbn(isbn1)
        livro2 = self.buscar_por_isbn(isbn2)
        
        if not livro1 or not livro2:
            return {"erro": "Um ou ambos os livros não foram encontrados"}
        
        return {
            "livro1": livro1.obter_info_resumida(),
            "livro2": livro2.obter_info_resumida(),
            "mesmo_autor": livro1.autor.lower() == livro2.autor.lower(),
            "mesmo_genero": livro1.genero.lower() == livro2.genero.lower(),
            "livro1_maior_paginas": livro1 > livro2,
            "livro2_maior_paginas": livro2 > livro1,
            "diferenca_paginas": abs(livro1.paginas - livro2.paginas),
            "diferenca_anos": abs(livro1.ano_publicacao - livro2.ano_publicacao)
        }
    
    def obter_estatisticas(self) -> dict:
        """
        Obtém estatísticas gerais da biblioteca.
        
        Returns:
            dict: Dicionário com estatísticas
        """
        if not self.livros:
            return {
                "total_livros": 0,
                "total_disponivel": 0,
                "total_indisponivel": 0,
                "media_paginas": 0,
                "ano_mais_antigo": 0,
                "ano_mais_recente": 0,
                "generos": []
            }
        
        disponibilidade = sum(1 for l in self.livros if l.disponivel)
        generos_unicos = set(l.genero for l in self.livros)
        
        return {
            "total_livros": len(self.livros),
            "total_disponivel": disponibilidade,
            "total_indisponivel": len(self.livros) - disponibilidade,
            "media_paginas": round(sum(l.paginas for l in self.livros) / len(self.livros), 2),
            "ano_mais_antigo": min(l.ano_publicacao for l in self.livros),
            "ano_mais_recente": max(l.ano_publicacao for l in self.livros),
            "generos": sorted(list(generos_unicos))
        }
    
    def __str__(self):
        """Representação textual da biblioteca."""
        return (
            f"Biblioteca: {self.nome}\n"
            f"Total de livros: {len(self.livros)}\n"
            f"Data de criação: {self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')}"
        )
    
    def __len__(self):
        """Retorna o número total de livros."""
        return len(self.livros)


def exibir_menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n" + "="*60)
    print("       SISTEMA DE BIBLIOTECA DIGITAL - MENU PRINCIPAL")
    print("="*60)
    print("1  - Cadastrar novo livro")
    print("2  - Buscar livro")
    print("3  - Listar todos os livros")
    print("4  - Listar por gênero")
    print("5  - Listar livros disponíveis")
    print("6  - Emprestar livro")
    print("7  - Devolver livro")
    print("8  - Ordenar livros")
    print("9  - Comparar dois livros")
    print("10 - Ver estatísticas")
    print("11 - Remover livro")
    print("12 - Sair")
    print("="*60)


def exibir_menu_busca():
    """Exibe o menu de busca."""
    print("\nOPÇÕES DE BUSCA:")
    print("1 - Buscar por título")
    print("2 - Buscar por autor")
    print("3 - Buscar por ISBN")
    print("0 - Voltar ao menu principal")


def exibir_menu_ordenacao():
    """Exibe o menu de ordenação."""
    print("\nOPÇÕES DE ORDENAÇÃO:")
    print("1 - Ordenar por páginas (crescente)")
    print("2 - Ordenar por páginas (decrescente)")
    print("3 - Ordenar por ano de publicação (crescente)")
    print("4 - Ordenar por ano de publicação (decrescente)")
    print("5 - Ordenar por título (A-Z)")
    print("0 - Voltar ao menu principal")


def cadastrar_livro(biblioteca: Biblioteca):
    """Solicita dados de um novo livro e o cadastra na biblioteca."""
    print("\n" + "="*60)
    print("CADASTRO DE NOVO LIVRO")
    print("="*60)
    
    try:
        titulo = input("Título do livro: ").strip()
        if not titulo:
            print("✗ Erro: Título não pode estar vazio!")
            return
        
        autor = input("Nome do autor: ").strip()
        if not autor:
            print("✗ Erro: Nome do autor não pode estar vazio!")
            return
        
        while True:
            try:
                paginas = int(input("Número de páginas: "))
                if paginas <= 0:
                    print("✗ Erro: Número de páginas deve ser maior que zero!")
                    continue
                break
            except ValueError:
                print("✗ Erro: Digite um número inteiro válido!")
        
        isbn = input("ISBN (número único): ").strip()
        if not isbn:
            print("✗ Erro: ISBN não pode estar vazio!")
            return
        
        if biblioteca.buscar_por_isbn(isbn):
            print("✗ Erro: Já existe um livro com este ISBN!")
            return
        
        while True:
            try:
                ano_publicacao = int(input("Ano de publicação: "))
                if ano_publicacao < 0 or ano_publicacao > datetime.now().year:
                    print(f"✗ Erro: Ano deve estar entre 0 e {datetime.now().year}!")
                    continue
                break
            except ValueError:
                print("✗ Erro: Digite um ano válido!")
        
        genero = input("Gênero do livro: ").strip()
        if not genero:
            print("✗ Erro: Gênero não pode estar vazio!")
            return
        
        novo_livro = Livro(titulo, autor, paginas, isbn, ano_publicacao, genero)
        
        if biblioteca.adicionar_livro(novo_livro):
            print("\n" + "="*60)
            print("✓ LIVRO CADASTRADO COM SUCESSO!")
            print("="*60)
            print(novo_livro)
            print("="*60)
        else:
            print("✗ Erro ao adicionar livro!")
    
    except Exception as e:
        print(f"✗ Erro inesperado: {e}")


def buscar_livro(biblioteca: Biblioteca):
    """Menu para buscar livros."""
    while True:
        exibir_menu_busca()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            titulo = input("Digite o título ou parte dele: ").strip()
            resultado = biblioteca.buscar_por_titulo(titulo)
            exibir_resultados_busca(resultado, f"Título: {titulo}")
        
        elif opcao == "2":
            autor = input("Digite o nome do autor ou parte dele: ").strip()
            resultado = biblioteca.buscar_por_autor(autor)
            exibir_resultados_busca(resultado, f"Autor: {autor}")
        
        elif opcao == "3":
            isbn = input("Digite o ISBN: ").strip()
            resultado = biblioteca.buscar_por_isbn(isbn)
            if resultado:
                print("\n" + "="*60)
                print("RESULTADO DA BUSCA")
                print("="*60)
                print(resultado)
                print("="*60)
            else:
                print("\n✗ Nenhum livro encontrado com este ISBN!")
        
        elif opcao == "0":
            break
        
        else:
            print("\n✗ Opção inválida!")


def exibir_resultados_busca(livros: List[Livro], criterio: str):
    """Exibe os resultados de uma busca."""
    if livros:
        print("\n" + "="*60)
        print(f"RESULTADOS DA BUSCA - {criterio}")
        print(f"Total encontrado: {len(livros)}")
        print("="*60)
        for i, livro in enumerate(livros, 1):
            print(f"\n--- Livro {i} ---")
            print(livro)
    else:
        print(f"\n✗ Nenhum livro encontrado com {criterio}!")


def listar_todos_livros(biblioteca: Biblioteca):
    """Lista todos os livros cadastrados."""
    if not biblioteca.livros:
        print("\n✗ Nenhum livro cadastrado na biblioteca!")
        return
    
    print("\n" + "="*60)
    print("TODOS OS LIVROS CADASTRADOS")
    print(f"Total: {len(biblioteca.livros)} livro(s)")
    print("="*60)
    for i, livro in enumerate(biblioteca.livros, 1):
        print(f"\n--- Livro {i} ---")
        print(livro)
    print("\n" + "="*60)


def listar_por_genero(biblioteca: Biblioteca):
    """Lista livros por gênero selecionado."""
    if not biblioteca.livros:
        print("\n✗ Nenhum livro cadastrado!")
        return
    
    generos = sorted(set(l.genero for l in biblioteca.livros))
    
    print("\n" + "="*60)
    print("GÊNEROS DISPONÍVEIS")
    print("="*60)
    for i, genero in enumerate(generos, 1):
        print(f"{i} - {genero}")
    print("="*60)
    
    try:
        escolha = int(input("\nEscolha um gênero (número): "))
        if 1 <= escolha <= len(generos):
            genero_selecionado = generos[escolha - 1]
            livros = biblioteca.listar_por_genero(genero_selecionado)
            exibir_resultados_busca(livros, f"Gênero: {genero_selecionado}")
        else:
            print("✗ Opção inválida!")
    except ValueError:
        print("✗ Digite um número válido!")


def listar_disponiveis(biblioteca: Biblioteca):
    """Lista livros disponíveis para empréstimo."""
    livros = biblioteca.listar_disponiveis()
    exibir_resultados_busca(livros, "Livros Disponíveis")


def emprestar_livro(biblioteca: Biblioteca):
    """Realiza o empréstimo de um livro."""
    isbn = input("\nDigite o ISBN do livro a emprestar: ").strip()
    livro = biblioteca.buscar_por_isbn(isbn)
    
    if not livro:
        print("✗ Livro não encontrado!")
        return
    
    if livro.emprestar():
        print(f"\n✓ Livro '{livro.titulo}' emprestado com sucesso!")
    else:
        print(f"✗ Livro '{livro.titulo}' não está disponível!")


def devolver_livro(biblioteca: Biblioteca):
    """Realiza a devolução de um livro."""
    isbn = input("\nDigite o ISBN do livro a devolver: ").strip()
    livro = biblioteca.buscar_por_isbn(isbn)
    
    if not livro:
        print("✗ Livro não encontrado!")
        return
    
    if livro.devolver():
        print(f"\n✓ Livro '{livro.titulo}' devolvido com sucesso!")
    else:
        print(f"✗ Livro '{livro.titulo}' já está disponível!")


def ordenar_livros(biblioteca: Biblioteca):
    """Menu para ordenar livros."""
    if not biblioteca.livros:
        print("\n✗ Nenhum livro cadastrado!")
        return
    
    while True:
        exibir_menu_ordenacao()
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            resultado = biblioteca.ordenar_por_paginas()
            exibir_lista_ordenada(resultado, "Ordenados por páginas (crescente)")
        
        elif opcao == "2":
            resultado = biblioteca.ordenar_por_paginas(decrescente=True)
            exibir_lista_ordenada(resultado, "Ordenados por páginas (decrescente)")
        
        elif opcao == "3":
            resultado = biblioteca.ordenar_por_ano()
            exibir_lista_ordenada(resultado, "Ordenados por ano (crescente)")
        
        elif opcao == "4":
            resultado = biblioteca.ordenar_por_ano(decrescente=True)
            exibir_lista_ordenada(resultado, "Ordenados por ano (decrescente)")
        
        elif opcao == "5":
            resultado = biblioteca.ordenar_por_titulo()
            exibir_lista_ordenada(resultado, "Ordenados por título (A-Z)")
        
        elif opcao == "0":
            break
        
        else:
            print("✗ Opção inválida!")


def exibir_lista_ordenada(livros: List[Livro], titulo: str):
    """Exibe uma lista de livros ordenados."""
    print("\n" + "="*60)
    print(titulo)
    print("="*60)
    for i, livro in enumerate(livros, 1):
        print(f"{i:2d}. {livro.obter_info_resumida()}")
    print("="*60)


def comparar_livros(biblioteca: Biblioteca):
    """Compara dois livros da biblioteca."""
    if len(biblioteca.livros) < 2:
        print("\n✗ É necessário ter pelo menos 2 livros para comparar!")
        return
    
    print("\n" + "="*60)
    print("COMPARAÇÃO DE LIVROS")
    print("="*60)
    
    isbn1 = input("Digite o ISBN do primeiro livro: ").strip()
    isbn2 = input("Digite o ISBN do segundo livro: ").strip()
    
    resultado = biblioteca.comparar_livros(isbn1, isbn2)
    
    if "erro" in resultado:
        print(f"\n✗ {resultado['erro']}")
        return
    
    print("\n" + "="*60)
    print("RESULTADO DA COMPARAÇÃO")
    print("="*60)
    print(f"Livro 1: {resultado['livro1']}")
    print(f"Livro 2: {resultado['livro2']}")
    print("-"*60)
    print(f"Mesmo autor: {'Sim' if resultado['mesmo_autor'] else 'Não'}")
    print(f"Mesmo gênero: {'Sim' if resultado['mesmo_genero'] else 'Não'}")
    print(f"Livro 1 tem mais páginas: {'Sim' if resultado['livro1_maior_paginas'] else 'Não'}")
    print(f"Livro 2 tem mais páginas: {'Sim' if resultado['livro2_maior_paginas'] else 'Não'}")
    print(f"Diferença de páginas: {resultado['diferenca_paginas']}")
    print(f"Diferença de anos: {resultado['diferenca_anos']}")
    print("="*60)


def ver_estatisticas(biblioteca: Biblioteca):
    """Exibe estatísticas gerais da biblioteca."""
    stats = biblioteca.obter_estatisticas()
    
    print("\n" + "="*60)
    print("ESTATÍSTICAS DA BIBLIOTECA")
    print("="*60)
    print(f"Total de livros: {stats['total_livros']}")
    print(f"Livros disponíveis: {stats['total_disponivel']}")
    print(f"Livros indisponíveis: {stats['total_indisponivel']}")
    print(f"Média de páginas: {stats['media_paginas']}")
    print(f"Ano mais antigo: {stats['ano_mais_antigo']}")
    print(f"Ano mais recente: {stats['ano_mais_recente']}")
    print(f"Gêneros cadastrados: {len(stats['generos'])}")
    if stats['generos']:
        print(f"  - {', '.join(stats['generos'])}")
    print("="*60)


def remover_livro(biblioteca: Biblioteca):
    """Remove um livro da biblioteca."""
    isbn = input("\nDigite o ISBN do livro a remover: ").strip()
    
    livro = biblioteca.buscar_por_isbn(isbn)
    if livro:
        print(f"\n✓ Livro '{livro.titulo}' removido com sucesso!")
        biblioteca.remover_livro(isbn)
    else:
        print("✗ Livro não encontrado!")


def criar_dados_exemplo(biblioteca: Biblioteca):
    """Cria alguns livros de exemplo para demonstração."""
    livros_exemplo = [
        Livro("Dom Casmurro", "Machado de Assis", 256, "978-8535914529", 1899, "Romance"),
        Livro("Grande Sertão: Veredas", "Guimarães Rosa", 638, "978-8535928777", 1956, "Romance"),
        Livro("O Cortiço", "Aluísio Azevedo", 348, "978-8525406243", 1890, "Romance"),
        Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 368, "978-8535916447", 1899, "Romance"),
        Livro("O Alienista", "Machado de Assis", 160, "978-8535909265", 1882, "Novela"),
        Livro("Sagarana", "Guimarães Rosa", 224, "978-8535914536", 1946, "Contos"),
        Livro("O Programador Pragmático", "David Thomas", 352, "978-8577807223", 1999, "Tecnologia"),
        Livro("Clean Code", "Robert Martin", 440, "978-8576082676", 2008, "Tecnologia"),
        Livro("Design Patterns", "Gang of Four", 416, "978-8577880539", 1994, "Tecnologia"),
        Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96, "978-8539002122", 1943, "Infantil")
    ]
    
    for livro in livros_exemplo:
        biblioteca.adicionar_livro(livro)


def main():
    """Função principal que coordena o funcionamento do sistema."""
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║         BEM-VINDO À BIBLIOTECA DIGITAL EXPANDIDA          ║")
    print("║      Sistema Completo de Gerenciamento de Livros          ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    biblioteca = Biblioteca("Biblioteca Central")
    
    # Pergunta se deseja carregar dados de exemplo
    print("\nDeseja carregar alguns livros de exemplo? (S/N)")
    if input().upper() == 'S':
        criar_dados_exemplo(biblioteca)
        print(f"✓ {len(biblioteca.livros)} livros de exemplo carregados!")
    
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_livro(biblioteca)
        
        elif opcao == "2":
            buscar_livro(biblioteca)
        
        elif opcao == "3":
            listar_todos_livros(biblioteca)
        
        elif opcao == "4":
            listar_por_genero(biblioteca)
        
        elif opcao == "5":
            listar_disponiveis(biblioteca)
        
        elif opcao == "6":
            emprestar_livro(biblioteca)
        
        elif opcao == "7":
            devolver_livro(biblioteca)
        
        elif opcao == "8":
            ordenar_livros(biblioteca)
        
        elif opcao == "9":
            comparar_livros(biblioteca)
        
        elif opcao == "10":
            ver_estatisticas(biblioteca)
        
        elif opcao == "11":
            remover_livro(biblioteca)
        
        elif opcao == "12":
            print("\n╔════════════════════════════════════════════════════════════╗")
            print("║         Obrigado por usar a Biblioteca Digital!          ║")
            print("║                    Até logo! 👋                          ║")
            print("╚════════════════════════════════════════════════════════════╝\n")
            break
        
        else:
            print("\n✗ Opção inválida! Digite um número de 1 a 12.")


if __name__ == "__main__":
    main()
