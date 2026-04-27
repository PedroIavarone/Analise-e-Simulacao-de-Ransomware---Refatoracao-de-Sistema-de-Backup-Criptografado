# Análise e Simulação de Ransomware - Refatoração de Sistema de Backup Criptografado

Este projeto foi desenvolvido para atender à atividade de Análise e Simulação de Ransomware, com foco em ambiente controlado, fins acadêmicos e compreensão do funcionamento básico de um ataque simulado.

## Aviso importante

Este código não deve ser utilizado em sistemas reais. A execução foi limitada para ocorrer apenas dentro da pasta `ambiente_teste`, criada no próprio projeto.

A simulação não possui propagação, persistência, acesso à rede, execução automática ou qualquer recurso de ocultação.

## Como executar

1. Tenha Python 3 instalado.
2. Abra o terminal dentro da pasta do projeto.
3. Execute:

```bash
python main.py
```

## Opções do sistema

1. Executar simulação
2. Recuperar arquivos
3. Ver logs
4. Sair

## Chave de recuperação

A chave de recuperação usada na simulação é:

```text
CLEVER123
```

## O que acontece na simulação

O sistema cria arquivos fictícios dentro da pasta `ambiente_teste`.

Ao executar a simulação, os arquivos são convertidos para um formato codificado em Base64 e recebem a extensão `.bloqueado_simulado`. Isso torna o conteúdo inacessível ao usuário comum dentro da proposta didática.

Depois, o sistema exibe uma tela de resgate simulada com:

* Mensagem informando que os arquivos foram bloqueados
* Valor fictício de resgate
* Instrução fictícia de pagamento
* Identificador único da vítima

## Recuperação

A recuperação é feita pela opção 2 do menu. O usuário informa a chave correta e o sistema restaura os arquivos para o estado original.

## Logs

As ações são registradas na pasta `logs`, incluindo:

* Arquivos afetados
* Data e hora da execução
* Tentativas de execução repetida
* Tentativas de recuperação
* Recuperação concluída

## Estrutura do projeto

```text
analise-simulacao-ransomware/
├── main.py
├── README.md
├── ambiente_teste/
├── logs/
└── docs/
```

## Integrantes do grupo

| Nome | RM |
|------|----|
| Alexandre Silva Alves | RM567415 |
| Julia Marcela de Faria Bonifacio | RM566673 |
| Mariana Pergentino Fonseca | RM568252 |
| Pedro Iavarone Custódio | RM567638 |

## Observação final

O objetivo deste projeto é demonstrar, de forma segura, como ataques de ransomware podem bloquear arquivos e como uma estratégia de recuperação controlada pode restaurar os dados.
