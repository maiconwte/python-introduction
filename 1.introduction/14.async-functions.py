# 5 Exemplos de Funções Assíncronas (Async)

# 1. Função para Baixar Múltiplos URLs

import aiohttp
import asyncio

async def baixar_url(session, url, timeout=10):
    """
    Baixa o conteúdo de uma URL de forma assíncrona
    Args:
        session: sessão aiohttp
        url: URL para baixar
        timeout: timeout em segundos
    Returns:
        dict: informações sobre o download
    """
    try:
        async with session.get(url, timeout=timeout) as response:
            status = response.status
            content_type = response.headers.get('Content-Type', 'desconhecido')
            tamanho = len(await response.read())

            return {
                'url': url,
                'status': status,
                'tipo_conteudo': content_type,
                'tamanho_bytes': tamanho,
                'sucesso': 200 <= status < 300
            }
    except asyncio.TimeoutError:
        return {
            'url': url,
            'status': 'timeout',
            'erro': 'Timeout excedido',
            'sucesso': False
        }
    except Exception as e:
        return {
            'url': url,
            'status': 'erro',
            'erro': str(e),
            'sucesso': False
        }

async def baixar_multiplos_urls(urls, max_concorrente=5):
    """
    Baixa múltiplas URLs concorrentemente
    Args:
        urls: lista de URLs
        max_concorrente: número máximo de downloads concorrentes
    Returns:
        list: resultados de todos os downloads
    """
    connector = aiohttp.TCPConnector(limit=max_concorrente)

    async with aiohttp.ClientSession(connector=connector) as session:
        tarefas = [baixar_url(session, url) for url in urls]
        resultados = await asyncio.gather(*tarefas)

    return resultados

# Uso:
async def exemplo_download():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/200",
        "https://httpbin.org/status/404",
        "https://httpbin.org/delay/2",
        "https://example.com"
    ]

    print("Iniciando downloads...")
    resultados = await baixar_multiplos_urls(urls, max_concorrente=3)

    print("\nResultados:")
    for resultado in resultados:
        if resultado['sucesso']:
            print(f"✅ {resultado['url']} - {resultado['status']} ({resultado['tamanho_bytes']} bytes)")
        else:
            print(f"❌ {resultado['url']} - {resultado.get('erro', resultado['status'])}")

# Para executar: asyncio.run(exemplo_download())

# 2. Função para Monitorar Sistema em Tempo Real

import asyncio
import psutil
import datetime

async def monitorar_cpu(intervalo=1, duracao=10):
    """
    Monitora o uso da CPU em tempo real
    Args:
        intervalo: segundos entre medições
        duracao: tempo total de monitoramento
    Yields:
        dict: informações de uso da CPU
    """
    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < duracao:
        uso_cpu = psutil.cpu_percent(interval=None)
        uso_memoria = psutil.virtual_memory().percent
        temperatura = None

        # Tenta obter temperatura (nem todos os sistemas suportam)
        try:
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
                if temps:
                    temperatura = list(temps.values())[0][0].current
        except:
            pass

        yield {
            'timestamp': datetime.datetime.now().isoformat(),
            'cpu_percent': uso_cpu,
            'memoria_percent': uso_memoria,
            'temperatura': temperatura
        }

        await asyncio.sleep(intervalo)

async def monitorar_sistema_completo():
    """
    Monitora múltiplas métricas do sistema concorrentemente
    """
    print("Iniciando monitoramento do sistema...")
    print("Pressione Ctrl+C para parar\n")

    # Cabeçalho da tabela
    print(f"{'Tempo':<12} {'CPU%':<6} {'Mem%':<6} {'Temp°C':<8}")
    print("-" * 35)

    try:
        async for dados in monitorar_cpu(intervalo=2, duracao=30):
            hora = dados['timestamp'].split('T')[1][:8]
            cpu = dados['cpu_percent']
            mem = dados['memoria_percent']
            temp = dados['temperatura'] or 'N/A'

            print(f"{hora:<12} {cpu:<6.1f} {mem:<6.1f} {str(temp):<8}")

    except asyncio.CancelledError:
        print("\nMonitoramento interrompido pelo usuário")

# Para executar: asyncio.run(monitorar_sistema_completo())

# 3. Função para Processamento em Lote Assíncrono

async def processar_item(item, delay=0.1):
    """
    Processa um item individual (simula I/O)
    Args:
        item: item a ser processado
        delay: simulação de tempo de processamento
    Returns:
        dict: resultado do processamento
    """
    await asyncio.sleep(delay)  # Simula operação I/O

    # Simula algum processamento
    resultado = {
        'id': item['id'],
        'processado': True,
        'timestamp': asyncio.get_event_loop().time(),
        'dados_transformados': f"{item['nome']}_{item['valor']}".upper()
    }

    return resultado

async def processar_em_lote(items, batch_size=3, delay_between_batches=0.5):
    """
    Processa itens em lotes concorrentemente
    Args:
        items: lista de itens a processar
        batch_size: tamanho do lote
        delay_between_batches: delay entre lotes
    Returns:
        list: todos os resultados
    """
    todos_resultados = []

    # Divide os itens em lotes
    lotes = [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

    print(f"Total de itens: {len(items)}")
    print(f"Total de lotes: {len(lotes)}")
    print(f"Tamanho do lote: {batch_size}\n")

    for i, lote in enumerate(lotes, 1):
        print(f"Processando lote {i}/{len(lotes)} com {len(lote)} itens...")

        # Processa todos os itens do lote concorrentemente
        tarefas = [processar_item(item) for item in lote]
        resultados_lote = await asyncio.gather(*tarefas)

        todos_resultados.extend(resultados_lote)

        # Aguarda entre lotes (para não sobrecarregar o sistema)
        if i < len(lotes):
            await asyncio.sleep(delay_between_batches)

    return todos_resultados

# Uso:
async def exemplo_processamento_lote():
    # Cria dados de exemplo
    dados = [
        {'id': i, 'nome': f'item_{i}', 'valor': i * 10}
        for i in range(1, 11)
    ]

    resultados = await processar_em_lote(dados, batch_size=4, delay_between_batches=0.3)

    print(f"\nTotal processado: {len(resultados)} itens")
    print("\nPrimeiros 3 resultados:")
    for resultado in resultados[:3]:
        print(f"  ID {resultado['id']}: {resultado['dados_transformados']}")

# Para executar: asyncio.run(exemplo_processamento_lote())

# 4. Função para WebSocket em Tempo Real

import websockets
import json
import asyncio

async def cliente_websocket(uri, mensagens_para_enviar, callback=None):
    """
    Cliente WebSocket assíncrono
    Args:
        uri: URI do servidor WebSocket
        mensagens_para_enviar: lista de mensagens para enviar
        callback: função callback para processar mensagens recebidas
    """
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Conectado ao WebSocket: {uri}")

            # Envia mensagens
            for i, mensagem in enumerate(mensagens_para_enviar, 1):
                if isinstance(mensagem, dict):
                    mensagem = json.dumps(mensagem)

                await websocket.send(mensagem)
                print(f"Enviada mensagem {i}: {mensagem}")

                # Aguarda resposta
                try:
                    resposta = await asyncio.wait_for(websocket.recv(), timeout=5)

                    if callback:
                        await callback(resposta)
                    else:
                        print(f"Resposta recebida: {resposta}")

                except asyncio.TimeoutError:
                    print("Timeout aguardando resposta")

                await asyncio.sleep(1)  # Intervalo entre mensagens

            print("Todas as mensagens foram enviadas")

    except websockets.exceptions.ConnectionClosedError:
        print("Conexão WebSocket foi fechada")
    except Exception as e:
        print(f"Erro na conexão WebSocket: {e}")

async def processar_resposta(resposta):
    """
    Exemplo de callback para processar respostas do WebSocket
    """
    try:
        dados = json.loads(resposta)
        print(f"✅ Resposta processada: {dados.get('status', 'N/A')}")
    except json.JSONDecodeError:
        print(f"📨 Resposta texto: {resposta[:50]}...")

# Uso:
async def exemplo_websocket():
    # Nota: Você precisa de um servidor WebSocket rodando para testar
    # Pode usar: python -m websockets ws://localhost:8765

    uri = "ws://localhost:8765"
    mensagens = [
        {"comando": "ping", "id": 1},
        {"comando": "echo", "mensagem": "Olá WebSocket!"},
        {"comando": "status", "query": "sistema"}
    ]

    print("Iniciando cliente WebSocket...")
    await cliente_websocket(uri, mensagens, callback=processar_resposta)

# Para executar: asyncio.run(exemplo_websocket())

# 5. Função para Pool de Conexões de Banco de Dados

import asyncpg
import asyncio
from datetime import datetime

class AsyncDatabase:
    """Classe para gerenciar pool de conexões assíncronas"""

    def __init__(self, dsn, pool_size=5):
        self.dsn = dsn
        self.pool_size = pool_size
        self.pool = None

    async def connect(self):
        """Cria o pool de conexões"""
        self.pool = await asyncpg.create_pool(
            dsn=self.dsn,
            min_size=1,
            max_size=self.pool_size,
            command_timeout=60
        )
        print(f"Pool de conexões criado (tamanho: {self.pool_size})")

    async def executar_query(self, query, *args):
        """Executa uma query SQL"""
        if not self.pool:
            await self.connect()

        async with self.pool.acquire() as conexao:
            try:
                resultado = await conexao.fetch(query, *args)
                return resultado
            except Exception as e:
                print(f"Erro na query: {e}")
                return None

    async def inserir_usuario(self, nome, email):
        """Insere um usuário no banco"""
        query = """
        INSERT INTO usuarios (nome, email, criado_em)
        VALUES ($1, $2, $3)
        RETURNING id
        """

        resultado = await self.executar_query(
            query, nome, email, datetime.now()
        )

        if resultado:
            return resultado[0]['id']
        return None

    async def buscar_usuarios(self, limite=10):
        """Busca usuários do banco"""
        query = "SELECT * FROM usuarios ORDER BY id DESC LIMIT $1"
        return await self.executar_query(query, limite)

    async def estatisticas_usuarios(self):
        """Obtém estatísticas dos usuários"""
        queries = [
            ("total_usuarios", "SELECT COUNT(*) FROM usuarios"),
            ("usuarios_hoje", """
                SELECT COUNT(*) FROM usuarios
                WHERE DATE(criado_em) = CURRENT_DATE
            """),
            ("ultimos_usuarios", """
                SELECT nome, email FROM usuarios
                ORDER BY id DESC LIMIT 3
            """)
        ]

        resultados = {}

        for nome, query in queries:
            resultado = await self.executar_query(query)
            if resultado:
                resultados[nome] = resultado

        return resultados

    async def fechar(self):
        """Fecha o pool de conexões"""
        if self.pool:
            await self.pool.close()
            print("Pool de conexões fechado")

# Uso:
async def exemplo_database():
    # Nota: Você precisa ter um banco PostgreSQL rodando
    dsn = "postgresql://usuario:senha@localhost/meubanco"

    try:
        db = AsyncDatabase(dsn, pool_size=3)

        # Criar tabela de exemplo (em um caso real, isso seria uma migração)
        await db.executar_query("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                criado_em TIMESTAMP DEFAULT NOW()
            )
        """)

        # Inserir alguns usuários concorrentemente
        usuarios = [
            ("Alice Silva", "alice@email.com"),
            ("Bob Santos", "bob@email.com"),
            ("Carol Oliveira", "carol@email.com"),
            ("David Costa", "david@email.com")
        ]

        print("Inserindo usuários...")
        tarefas = [db.inserir_usuario(nome, email) for nome, email in usuarios]
        ids = await asyncio.gather(*tarefas)
        print(f"Usuários inseridos com IDs: {ids}")

        # Buscar estatísticas
        print("\nEstatísticas:")
        estatisticas = await db.estatisticas_usuarios()
        for chave, valor in estatisticas.items():
            print(f"{chave}: {valor}")

        # Buscar últimos usuários
        print("\nÚltimos usuários cadastrados:")
        usuarios = await db.buscar_usuarios(limite=5)
        for usuario in usuarios:
            print(f"  - {usuario['nome']} ({usuario['email']})")

    finally:
        await db.fechar()

# Para executar: asyncio.run(exemplo_database())

# Como Executar os Exemplos Async:

# Para executar qualquer função async, você precisa:
import asyncio

# Método 1: Usando asyncio.run() (Python 3.7+)
async def main():
    await exemplo_download()  # Substitua pela função desejada

if __name__ == "__main__":
    asyncio.run(main())

# Método 2: Usando loop (Python 3.6)
async def main():
    await exemplo_download()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())