# Documento de Funcionamento do Sistema

## 1. Objetivo do projeto

O projeto tem como objetivo simular, em ambiente controlado, o comportamento básico de um ransomware. A finalidade é acadêmica e educacional, permitindo compreender como arquivos podem ser bloqueados por um processo de criptografia ou simulação equivalente, quais impactos isso gera ao usuário e como a recuperação pode ser feita por meio de uma chave autorizada.

## 2. Ambiente de execução

A execução deve ocorrer apenas em máquina local, máquina virtual ou diretório isolado. O sistema foi configurado para operar exclusivamente dentro da pasta `ambiente_teste`, evitando qualquer atuação em arquivos reais do computador.

## 3. Fluxo do ataque simulado

Primeiro, o sistema prepara o ambiente de teste criando arquivos fictícios. Em seguida, quando o usuário escolhe a opção de executar a simulação, o programa realiza uma varredura apenas na pasta `ambiente_teste`.

Após localizar os arquivos disponíveis, o sistema aplica uma simulação de criptografia usando codificação Base64. Os arquivos originais são substituídos por versões com a extensão `.bloqueado_simulado`, deixando o conteúdo inacessível para leitura comum.

Depois dessa etapa, o sistema grava o estado da execução e exibe uma tela de resgate simulada com informações típicas de um ataque de ransomware, incluindo valor fictício de resgate, instruções simuladas e identificador único da vítima.

## 4. Controle de execução

O sistema registra se a simulação já foi executada. Caso o usuário tente executar novamente antes da recuperação, o programa bloqueia a repetição indevida e apenas exibe novamente a tela de resgate. Esse controle evita que a operação seja repetida desnecessariamente.

## 5. Tela de resgate

A tela de resgate é exibida no terminal e contém:

* Mensagem informando que os arquivos foram bloqueados
* Valor fictício de resgate
* Instrução simulada de pagamento
* Identificador único da vítima
* Orientação para recuperação por chave

## 6. Recuperação dos arquivos

A recuperação é feita pela opção 2 do menu. O usuário precisa informar a chave correta:

`CLEVER123`

Quando a chave é validada, o sistema identifica os arquivos com a extensão `.bloqueado_simulado`, decodifica o conteúdo e restaura os nomes originais dos arquivos.

## 7. Registro de logs

O sistema registra as principais ações no arquivo `logs/operacoes.log`. Os registros incluem data, hora, ação realizada, arquivo afetado e detalhes da operação.

São registrados eventos como:

* Execução da simulação
* Arquivos afetados
* Tentativa de execução repetida
* Tentativa de recuperação com chave incorreta
* Recuperação concluída

## 8. Organização do código

O código foi estruturado em funções, incluindo:

* `varrer_arquivos()` para localizar arquivos na pasta de teste
* `criptografar_arquivo()` para simular o bloqueio dos arquivos
* `descriptografar_arquivo()` para restaurar os arquivos
* `exibir_tela_resgate()` para mostrar a mensagem simulada de ransomware
* `registrar_log()` para registrar as ações
* `executar_simulacao()` para controlar o fluxo principal
* `recuperar_arquivos()` para realizar a reversão controlada

## 9. Medidas de segurança adotadas

A simulação foi limitada à pasta `ambiente_teste`. O sistema não acessa pastas externas, não se propaga, não executa em segundo plano, não usa rede e não possui mecanismos de persistência.

## 10. Conclusão

O projeto demonstra de forma segura como um ransomware pode bloquear arquivos e pressionar a vítima por meio de uma tela de resgate. Também mostra a importância de backups, controle de acesso, logs, ambientes isolados e mecanismos de recuperação.
