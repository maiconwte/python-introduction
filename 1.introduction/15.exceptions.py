# Exceptions (Exceções) em Python

# Exceções são erros que ocorrem durante a execução do programa. Em Python, as exceções são objetos que representam condições de erro e podem ser capturadas e tratadas.

# Hierarquia de Exceções Comuns

# BaseException
# ├── KeyboardInterrupt
# ├── SystemExit
# └── Exception
#       ├── ArithmeticError
#       │    ├── ZeroDivisionError
#       │    └── FloatingPointError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── OSError
#       │    ├── FileNotFoundError
#       │    ├── PermissionError
#       │    └── ConnectionError
#       ├── TypeError
#       ├── ValueError
#       ├── NameError
#       ├── AttributeError
#       └── RuntimeError

# 5 Exemplos Práticos de Tratamento de Exceções
# 1. Validação de Entrada do Usuário

# Basic Example

print("Digite sua idade: ")
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = numero / 10
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(f"Erro: {e}")
    raise ValueError("Digite um número inteiro válido")
except Exception as e:
    print(f"Erro: {e}")
else:
    print("Não houve erro")
finally:
    print("Operação finalizada")

# Exemplo 1: Validação de Entrada do Usuário

def obter_idade_valida():
    """
    Solicita idade do usuário com tratamento de erros
    """
    while True:
        try:
            idade = int(input("Digite sua idade: "))

            if idade < 0:
                raise ValueError("Idade não pode ser negativa!")
            elif idade > 120:
                raise ValueError("Idade muito alta! Verifique o valor.")

            return idade

        except ValueError as e:
            # Captura tanto conversão inválida quanto ValueError levantado
            if "invalid literal" in str(e):
                print("Erro: Digite um número válido!")
            else:
                print(f"Erro: {e}")

        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
            return None

        except Exception as e:
            print(f"Erro inesperado: {type(e).__name__} - {e}")
            # Opcional: logar o erro
            # logging.error(f"Erro ao obter idade: {e}")
            continuar = input("Tentar novamente? (s/n): ")
            if continuar.lower() != 's':
                return None

# Uso:

#idade = obter_idade_valida()
#if idade is not None:
#   print(f"Idade válida registrada: {idade} anos")

# 2. Sistema de Arquivos com Tratamento de Erros

import os
import json
from datetime import datetime

def gerenciar_arquivo_configuracao():
    """
    Lê, escreve e atualiza arquivo de configuração com tratamento de erros
    """
    CONFIG_FILE = "config.json"
    config_padrao = {
        "ultimo_acesso": None,
        "preferencias": {
            "tema": "claro",
            "idioma": "pt-br",
            "notificacoes": True
        },
        "estatisticas": {
            "acessos": 0
        }
    }

    def carregar_configuracao():
        """Carrega configuração do arquivo"""
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Arquivo de configuração não encontrado. Criando novo...")
            return config_padrao
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            print("Criando novo arquivo de configuração...")
            return config_padrao
        except PermissionError:
            print("Erro de permissão: Não é possível ler o arquivo.")
            return None
        except OSError as e:
            print(f"Erro de sistema ao ler arquivo: {e}")
            return None

    def salvar_configuracao(config):
        """Salva configuração no arquivo"""
        try:
            # Atualiza dados
            config['ultimo_acesso'] = datetime.now().isoformat()
            config['estatisticas']['acessos'] += 1

            # Cria backup se o arquivo já existir
            if os.path.exists(CONFIG_FILE):
                backup_file = f"{CONFIG_FILE}.backup"
                try:
                    os.replace(CONFIG_FILE, backup_file)
                    print(f"Backup criado: {backup_file}")
                except OSError as e:
                    print(f"Aviso: Não foi possível criar backup: {e}")

            # Salva novo arquivo
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)

            print("Configuração salva com sucesso!")
            return True

        except PermissionError:
            print("Erro: Sem permissão para escrever no arquivo.")
            return False
        except OSError as e:
            print(f"Erro ao salvar arquivo: {e}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {type(e).__name__} - {e}")
            return False

    # Execução principal
    print("=== GERENCIADOR DE CONFIGURAÇÃO ===")

    # Tenta carregar configuração
    config = carregar_configuracao()
    if config is None:
        print("Não foi possível carregar a configuração.")
        return

    # Exibe configuração atual
    print("\nConfiguração atual:")
    print(f"Tema: {config['preferencias']['tema']}")
    print(f"Idioma: {config['preferencias']['idioma']}")
    print(f"Total de acessos: {config['estatisticas']['acessos']}")

    # Tenta modificar uma configuração
    try:
        novo_tema = input("\nNovo tema (claro/escuro): ").lower()
        if novo_tema in ['claro', 'escuro']:
            config['preferencias']['tema'] = novo_tema
        else:
            raise ValueError("Tema deve ser 'claro' ou 'escuro'")

        # Tenta salvar
        if salvar_configuracao(config):
            print("Alterações aplicadas com sucesso!")
        else:
            print("Não foi possível salvar as alterações.")

    except ValueError as e:
        print(f"Erro de validação: {e}")
    except KeyboardInterrupt:
        print("\nOperação cancelada.")
    except Exception as e:
        print(f"Erro inesperado durante modificação: {e}")

# Executar
# gerenciar_arquivo_configuracao()

# import sqlite3
import time
from contextlib import contextmanager

class BancoDeDados:
    """Classe para gerenciar conexão com banco de dados com tratamento de erros"""

    def __init__(self, arquivo_db="dados.db"):
        self.arquivo_db = arquivo_db
        self.max_tentativas = 3
        self.delay_tentativas = 1  # segundos

    @contextmanager
    def conectar(self):
        """Context manager para conexão automática com tratamento de erros"""
        conexao = None
        tentativa = 0

        while tentativa < self.max_tentativas:
            try:
                conexao = sqlite3.connect(self.arquivo_db)
                conexao.row_factory = sqlite3.Row  # Para acesso por nome de coluna
                print(f"Conexão estabelecida (tentativa {tentativa + 1})")
                yield conexao
                conexao.commit()
                break

            except sqlite3.OperationalError as e:
                tentativa += 1
                print(f"Erro operacional (tentativa {tentativa}): {e}")

                if "unable to open database file" in str(e):
                    print("Verifique se o diretório existe e tem permissões de escrita")
                    break
                elif tentativa < self.max_tentativas:
                    print(f"Tentando novamente em {self.delay_tentativas} segundos...")
                    time.sleep(self.delay_tentativas)
                else:
                    print("Número máximo de tentativas excedido")
                    raise

            except sqlite3.IntegrityError as e:
                print(f"Erro de integridade: {e}")
                if conexao:
                    conexao.rollback()
                raise

            except sqlite3.Error as e:
                print(f"Erro no banco de dados: {e}")
                if conexao:
                    conexao.rollback()
                raise

            except Exception as e:
                print(f"Erro inesperado: {type(e).__name__} - {e}")
                if conexao:
                    conexao.rollback()
                raise

            finally:
                if conexao:
                    conexao.close()
                    print("Conexão fechada")

    def criar_tabela_usuarios(self):
        """Cria tabela de usuários se não existir"""
        try:
            with self.conectar() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        idade INTEGER CHECK (idade >= 0),
                        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                print("Tabela 'usuarios' verificada/criada")
        except Exception as e:
            print(f"Falha ao criar tabela: {e}")

    def inserir_usuario(self, nome, email, idade):
        """Insere um usuário com tratamento de erros"""
        try:
            with self.conectar() as conn:
                cursor = conn.execute(
                    "INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)",
                    (nome, email, idade)
                )
                print(f"Usuário inserido com ID: {cursor.lastrowid}")
                return cursor.lastrowid

        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(f"Erro: Email '{email}' já está cadastrado")
            else:
                print(f"Erro de integridade: {e}")
            return None

        except sqlite3.Error as e:
            print(f"Erro ao inserir usuário: {e}")
            return None

    def buscar_usuario(self, user_id=None, email=None):
        """Busca usuário por ID ou email"""
        try:
            with self.conectar() as conn:
                if user_id:
                    cursor = conn.execute(
                        "SELECT * FROM usuarios WHERE id = ?",
                        (user_id,)
                    )
                elif email:
                    cursor = conn.execute(
                        "SELECT * FROM usuarios WHERE email = ?",
                        (email,)
                    )
                else:
                    raise ValueError("Deve fornecer ID ou email")

                usuario = cursor.fetchone()

                if usuario:
                    return dict(usuario)
                else:
                    raise ValueError("Usuário não encontrado")

        except ValueError as e:
            print(f"Erro de validação: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Erro na busca: {e}")
            return None

    def executar_query_segura(self, query, params=()):
        """Executa uma query SQL com tratamento completo de erros"""
        try:
            with self.conectar() as conn:
                cursor = conn.execute(query, params)

                if query.strip().upper().startswith("SELECT"):
                    resultados = cursor.fetchall()
                    return [dict(row) for row in resultados]
                else:
                    conn.commit()
                    return cursor.rowcount

        except sqlite3.ProgrammingError as e:
            print(f"Erro na query SQL: {e}")
            print(f"Query: {query}")
            print(f"Parâmetros: {params}")
            return None
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            return None

# Uso:
def exemplo_banco_dados():
    print("=== SISTEMA DE BANCO DE DADOS COM TRATAMENTO DE ERROS ===\n")

    db = BancoDeDados("teste.db")

    # 1. Criar tabela
    db.criar_tabela_usuarios()

    # 2. Tentar inserir usuários (um vai falhar por email duplicado)
    print("\n1. Inserindo usuários:")
    db.inserir_usuario("Ana Silva", "ana@email.com", 25)
    db.inserir_usuario("Carlos Santos", "carlos@email.com", 30)
    db.inserir_usuario("Ana Silva", "ana@email.com", 25)  # Email duplicado!

    # 3. Buscar usuário existente
    print("\n2. Buscando usuário:")
    usuario = db.buscar_usuario(email="carlos@email.com")
    if usuario:
        print(f"Encontrado: {usuario['nome']}, {usuario['email']}")

    # 4. Buscar usuário inexistente
    print("\n3. Buscando usuário inexistente:")
    usuario = db.buscar_usuario(email="inexistente@email.com")

    # 5. Query mal formada (vai gerar erro)
    print("\n4. Executando query mal formada:")
    resultado = db.executar_query_segura(
        "SELECT * FROM tabela_inexistente"  # Tabela não existe
    )

    # 6. Query com injeção SQL tentativa (será tratada)
    print("\n5. Tentativa de injeção SQL (protegida):")
    email_maligno = "teste@email.com' OR '1'='1"
    resultado = db.executar_query_segura(
        "SELECT * FROM usuarios WHERE email = ?",
        (email_maligno,)  # Parâmetro seguro
    )

# 3. Conexão com Banco de Dados Resiliente

import sqlite3
import time
from contextlib import contextmanager

class BancoDeDados:
    """Classe para gerenciar conexão com banco de dados com tratamento de erros"""

    def __init__(self, arquivo_db="dados.db"):
        self.arquivo_db = arquivo_db
        self.max_tentativas = 3
        self.delay_tentativas = 1  # segundos

    @contextmanager
    def conectar(self):
        """Context manager para conexão automática com tratamento de erros"""
        conexao = None
        tentativa = 0

        while tentativa < self.max_tentativas:
            try:
                conexao = sqlite3.connect(self.arquivo_db)
                conexao.row_factory = sqlite3.Row  # Para acesso por nome de coluna
                print(f"Conexão estabelecida (tentativa {tentativa + 1})")
                yield conexao
                conexao.commit()
                break

            except sqlite3.OperationalError as e:
                tentativa += 1
                print(f"Erro operacional (tentativa {tentativa}): {e}")

                if "unable to open database file" in str(e):
                    print("Verifique se o diretório existe e tem permissões de escrita")
                    break
                elif tentativa < self.max_tentativas:
                    print(f"Tentando novamente em {self.delay_tentativas} segundos...")
                    time.sleep(self.delay_tentativas)
                else:
                    print("Número máximo de tentativas excedido")
                    raise

            except sqlite3.IntegrityError as e:
                print(f"Erro de integridade: {e}")
                if conexao:
                    conexao.rollback()
                raise

            except sqlite3.Error as e:
                print(f"Erro no banco de dados: {e}")
                if conexao:
                    conexao.rollback()
                raise

            except Exception as e:
                print(f"Erro inesperado: {type(e).__name__} - {e}")
                if conexao:
                    conexao.rollback()
                raise

            finally:
                if conexao:
                    conexao.close()
                    print("Conexão fechada")

    def criar_tabela_usuarios(self):
        """Cria tabela de usuários se não existir"""
        try:
            with self.conectar() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        idade INTEGER CHECK (idade >= 0),
                        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                print("Tabela 'usuarios' verificada/criada")
        except Exception as e:
            print(f"Falha ao criar tabela: {e}")

    def inserir_usuario(self, nome, email, idade):
        """Insere um usuário com tratamento de erros"""
        try:
            with self.conectar() as conn:
                cursor = conn.execute(
                    "INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)",
                    (nome, email, idade)
                )
                print(f"Usuário inserido com ID: {cursor.lastrowid}")
                return cursor.lastrowid

        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(f"Erro: Email '{email}' já está cadastrado")
            else:
                print(f"Erro de integridade: {e}")
            return None

        except sqlite3.Error as e:
            print(f"Erro ao inserir usuário: {e}")
            return None

    def buscar_usuario(self, user_id=None, email=None):
        """Busca usuário por ID ou email"""
        try:
            with self.conectar() as conn:
                if user_id:
                    cursor = conn.execute(
                        "SELECT * FROM usuarios WHERE id = ?",
                        (user_id,)
                    )
                elif email:
                    cursor = conn.execute(
                        "SELECT * FROM usuarios WHERE email = ?",
                        (email,)
                    )
                else:
                    raise ValueError("Deve fornecer ID ou email")

                usuario = cursor.fetchone()

                if usuario:
                    return dict(usuario)
                else:
                    raise ValueError("Usuário não encontrado")

        except ValueError as e:
            print(f"Erro de validação: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Erro na busca: {e}")
            return None

    def executar_query_segura(self, query, params=()):
        """Executa uma query SQL com tratamento completo de erros"""
        try:
            with self.conectar() as conn:
                cursor = conn.execute(query, params)

                if query.strip().upper().startswith("SELECT"):
                    resultados = cursor.fetchall()
                    return [dict(row) for row in resultados]
                else:
                    conn.commit()
                    return cursor.rowcount

        except sqlite3.ProgrammingError as e:
            print(f"Erro na query SQL: {e}")
            print(f"Query: {query}")
            print(f"Parâmetros: {params}")
            return None
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            return None

# Uso:
def exemplo_banco_dados():
    print("=== SISTEMA DE BANCO DE DADOS COM TRATAMENTO DE ERROS ===\n")

    db = BancoDeDados("teste.db")

    # 1. Criar tabela
    db.criar_tabela_usuarios()

    # 2. Tentar inserir usuários (um vai falhar por email duplicado)
    print("\n1. Inserindo usuários:")
    db.inserir_usuario("Ana Silva", "ana@email.com", 25)
    db.inserir_usuario("Carlos Santos", "carlos@email.com", 30)
    db.inserir_usuario("Ana Silva", "ana@email.com", 25)  # Email duplicado!

    # 3. Buscar usuário existente
    print("\n2. Buscando usuário:")
    usuario = db.buscar_usuario(email="carlos@email.com")
    if usuario:
        print(f"Encontrado: {usuario['nome']}, {usuario['email']}")

    # 4. Buscar usuário inexistente
    print("\n3. Buscando usuário inexistente:")
    usuario = db.buscar_usuario(email="inexistente@email.com")

    # 5. Query mal formada (vai gerar erro)
    print("\n4. Executando query mal formada:")
    resultado = db.executar_query_segura(
        "SELECT * FROM tabela_inexistente"  # Tabela não existe
    )

    # 6. Query com injeção SQL tentativa (será tratada)
    print("\n5. Tentativa de injeção SQL (protegida):")
    email_maligno = "teste@email.com' OR '1'='1"
    resultado = db.executar_query_segura(
        "SELECT * FROM usuarios WHERE email = ?",
        (email_maligno,)  # Parâmetro seguro
    )

# Executar
# exemplo_banco_dados()