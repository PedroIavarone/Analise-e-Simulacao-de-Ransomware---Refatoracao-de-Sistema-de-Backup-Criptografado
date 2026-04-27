"""
CP02 Cyber 1
Simulador educacional de ransomware em ambiente controlado

IMPORTANTE:
Este código foi criado apenas para fins acadêmicos.
Ele só atua dentro da pasta local "ambiente_teste".
Não possui persistência, propagação, ocultação, rede ou execução automática.
"""

import base64
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path

# Configurações de segurança da simulação
BASE_DIR = Path(__file__).resolve().parent
TEST_DIR = BASE_DIR / "ambiente_teste"
LOG_DIR = BASE_DIR / "logs"
STATE_FILE = LOG_DIR / "estado_execucao.json"
LOG_FILE = LOG_DIR / "operacoes.log"
EXTENSAO_SIMULADA = ".bloqueado_simulado"
CHAVE_RECUPERACAO = "CLEVER123"


def preparar_ambiente_teste():
    """Cria a pasta de teste e alguns arquivos fictícios, caso ainda não existam."""
    TEST_DIR.mkdir(exist_ok=True)
    LOG_DIR.mkdir(exist_ok=True)

    arquivos_exemplo = {
        "contrato_teste.txt": "Contrato ficticio para teste de seguranca.\n",
        "relatorio_financeiro_teste.txt": "Relatorio financeiro ficticio. Valor em aberto: R$ 1.200,00.\n",
        "lista_alunos_teste.csv": "nome,curso,status\nMaria,Informatica,Inadimplente\nJoao,Ingles,Regular\n",
    }

    for nome, conteudo in arquivos_exemplo.items():
        caminho = TEST_DIR / nome
        caminho_bloqueado = TEST_DIR / f"{nome}{EXTENSAO_SIMULADA}"
        if not caminho.exists() and not caminho_bloqueado.exists():
            caminho.write_text(conteudo, encoding="utf-8")


def registrar_log(acao, arquivo=None, detalhe=None):
    """Registra as ações realizadas pela simulação."""
    LOG_DIR.mkdir(exist_ok=True)
    momento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{momento}] ACAO={acao}"

    if arquivo:
        linha += f" | ARQUIVO={arquivo}"
    if detalhe:
        linha += f" | DETALHE={detalhe}"

    with LOG_FILE.open("a", encoding="utf-8") as log:
        log.write(linha + "\n")


def gerar_id_vitima():
    """Gera identificador único fictício da vítima com base no caminho do projeto e horário."""
    base = f"{BASE_DIR}-{datetime.now().isoformat()}"
    return hashlib.sha256(base.encode("utf-8")).hexdigest()[:12].upper()


def carregar_estado():
    """Carrega o estado da execução para evitar repetição indevida."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {
        "executado": False,
        "recuperado": False,
        "id_vitima": None,
        "arquivos_afetados": [],
    }


def salvar_estado(estado):
    """Salva o estado atual da simulação."""
    LOG_DIR.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(estado, indent=4, ensure_ascii=False), encoding="utf-8")


def validar_pasta_segura():
    """Impede que a simulação seja alterada para rodar fora da pasta controlada."""
    caminho_teste = TEST_DIR.resolve()
    caminho_base = BASE_DIR.resolve()

    if not str(caminho_teste).startswith(str(caminho_base)):
        raise RuntimeError("Execução bloqueada: a pasta de teste precisa estar dentro do projeto.")

    caminhos_proibidos = [Path.home(), Path("/"), Path("C:/"), Path("C:/Windows"), Path("C:/Users")]
    for proibido in caminhos_proibidos:
        try:
            if caminho_teste == proibido.resolve():
                raise RuntimeError("Execução bloqueada: diretório inseguro para teste.")
        except Exception:
            continue


def varrer_arquivos():
    """Localiza arquivos de teste que ainda não foram bloqueados."""
    validar_pasta_segura()
    arquivos = []

    for item in TEST_DIR.iterdir():
        if item.is_file() and not item.name.endswith(EXTENSAO_SIMULADA):
            arquivos.append(item)

    return arquivos


def criptografar_arquivo(caminho):
    """
    Simula criptografia usando base64.
    Esta abordagem é propositalmente didática e reversível.
    """
    conteudo_original = caminho.read_bytes()
    conteudo_simulado = base64.b64encode(conteudo_original)

    novo_nome = caminho.with_name(caminho.name + EXTENSAO_SIMULADA)
    novo_nome.write_bytes(conteudo_simulado)
    caminho.unlink()

    registrar_log("CRIPTOGRAFIA_SIMULADA", arquivo=novo_nome.name, detalhe="Arquivo convertido para formato inacessível ao usuário comum")
    return novo_nome.name


def descriptografar_arquivo(caminho):
    """Reverte a simulação, restaurando o arquivo ao estado original."""
    conteudo_bloqueado = caminho.read_bytes()
    conteudo_original = base64.b64decode(conteudo_bloqueado)

    nome_original = caminho.name.replace(EXTENSAO_SIMULADA, "")
    caminho_restaurado = caminho.with_name(nome_original)
    caminho_restaurado.write_bytes(conteudo_original)
    caminho.unlink()

    registrar_log("DESCRIPTOGRAFIA_SIMULADA", arquivo=caminho_restaurado.name, detalhe="Arquivo restaurado com chave correta")
    return caminho_restaurado.name


def exibir_tela_resgate(id_vitima):
    """Exibe a tela de resgate simulada exigida na atividade."""
    print("=" * 70)
    print("            ALERTA DE RANSOMWARE SIMULADO")
    print("=" * 70)
    print("Seus arquivos de teste foram bloqueados por uma simulação controlada.")
    print("Esta atividade tem finalidade exclusivamente educacional.")
    print()
    print(f"Identificador fictício da vítima: {id_vitima}")
    print("Valor fictício de resgate: R$ 5.000,00")
    print("Instrução simulada de pagamento: enviar comprovante fictício ao laboratório.")
    print()
    print("Para recuperar os arquivos, utilize a opção 2 do menu e informe a chave.")
    print("Chave de recuperação para o professor/teste: CLEVER123")
    print("=" * 70)


def executar_simulacao():
    """Controla a execução inicial da simulação."""
    preparar_ambiente_teste()
    estado = carregar_estado()

    if estado["executado"] and not estado["recuperado"]:
        print("A simulação já foi executada e ainda não foi recuperada.")
        exibir_tela_resgate(estado["id_vitima"])
        registrar_log("EXECUCAO_REPETIDA_BLOQUEADA", detalhe="Tentativa de nova execução sem recuperação")
        return

    arquivos = varrer_arquivos()
    if not arquivos:
        print("Nenhum arquivo disponível para a simulação.")
        registrar_log("SEM_ARQUIVOS", detalhe="Não havia arquivos para bloquear")
        return

    id_vitima = gerar_id_vitima()
    afetados = []

    for arquivo in arquivos:
        afetados.append(criptografar_arquivo(arquivo))

    estado = {
        "executado": True,
        "recuperado": False,
        "id_vitima": id_vitima,
        "data_execucao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "arquivos_afetados": afetados,
    }
    salvar_estado(estado)
    registrar_log("SIMULACAO_EXECUTADA", detalhe=f"Total de arquivos afetados: {len(afetados)}")
    exibir_tela_resgate(id_vitima)


def recuperar_arquivos():
    """Solicita chave e realiza recuperação controlada."""
    preparar_ambiente_teste()
    estado = carregar_estado()

    if not estado["executado"]:
        print("Não existe simulação executada para recuperar.")
        return

    chave = input("Informe a chave de recuperação: ").strip()
    if chave != CHAVE_RECUPERACAO:
        print("Chave incorreta. Recuperação negada.")
        registrar_log("CHAVE_INCORRETA", detalhe="Tentativa de recuperação recusada")
        return

    arquivos_bloqueados = [item for item in TEST_DIR.iterdir() if item.is_file() and item.name.endswith(EXTENSAO_SIMULADA)]

    if not arquivos_bloqueados:
        print("Nenhum arquivo bloqueado encontrado.")
        return

    restaurados = []
    for arquivo in arquivos_bloqueados:
        restaurados.append(descriptografar_arquivo(arquivo))

    estado["recuperado"] = True
    estado["data_recuperacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    estado["arquivos_restaurados"] = restaurados
    salvar_estado(estado)

    print("Arquivos restaurados com sucesso.")
    registrar_log("RECUPERACAO_CONCLUIDA", detalhe=f"Total de arquivos restaurados: {len(restaurados)}")


def exibir_logs():
    """Mostra os logs registrados."""
    if not LOG_FILE.exists():
        print("Nenhum log encontrado.")
        return

    print("\nLOGS DA SIMULAÇÃO")
    print("=" * 70)
    print(LOG_FILE.read_text(encoding="utf-8"))


def menu():
    """Menu principal da aplicação."""
    while True:
        print("\nSIMULADOR EDUCACIONAL DE RANSOMWARE")
        print("1. Executar simulação")
        print("2. Recuperar arquivos")
        print("3. Ver logs")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            executar_simulacao()
        elif opcao == "2":
            recuperar_arquivos()
        elif opcao == "3":
            exibir_logs()
        elif opcao == "4":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
