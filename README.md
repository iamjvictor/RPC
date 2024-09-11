
# Sistema de Sincronização de Arquivos via RPC

## Descrição do Projeto

Este projeto consiste em um sistema distribuído composto por duas máquinas que se comunicam através de chamadas de procedimento remoto (RPC) utilizando a biblioteca xmlrpc do Python. O objetivo é garantir que, ao criar um arquivo em uma pasta específica em uma das máquinas, o mesmo arquivo com o mesmo conteúdo seja criado na outra máquina.

## Componentes do Sistema

### Máquina Cliente
- **Observador de Arquivos**: Monitora uma pasta específica em busca de novos arquivos.
- **Cliente RPC**: Envia uma solicitação ao servidor para criar o mesmo arquivo na outra máquina quando um novo arquivo é detectado.

### Máquina Servidora
- **Servidor RPC**: Recebe as solicitações do cliente RPC para criar arquivos.
- **Manipulador de Arquivos**: Lida com a criação e manipulação de arquivos na máquina servidora.

## Funcionamento

1. **Monitoramento de Arquivos**: O observador de arquivos na máquina cliente monitora continuamente uma pasta específica.
2. **Detecção de Novo Arquivo**: Quando um novo arquivo é criado na pasta monitorada, o observador detecta essa mudança.
3. **Chamada RPC**: O observador aciona o cliente RPC, que envia uma solicitação ao servidor RPC na outra máquina, incluindo o nome e o conteúdo do arquivo.
4. **Criação do Arquivo na Máquina Servidora**: O servidor RPC recebe a solicitação e utiliza o manipulador de arquivos para criar o mesmo arquivo com o mesmo conteúdo na pasta correspondente na máquina servidora.

## Arquivos do Projeto

### Servidor
- Lida com a recepção de solicitações RPC.
- Manipula a criação e atualização de arquivos na máquina servidora.

### Cliente
- Observa a pasta específica na máquina cliente.
- Realiza chamadas RPC para o servidor quando um novo arquivo é detectado.

## Como Executar

### Pré-requisitos
- Duas máquinas conectadas em rede.
- Ambiente de desenvolvimento configurado com suporte a RPC.

### Passos

1. **Configurar o Servidor**:
   - Inicie o servidor RPC na máquina servidora.
   - Certifique-se de que o servidor está pronto para receber solicitações.

2. **Configurar o Cliente**:
   - Inicie o observador de arquivos na máquina cliente.
   - Configure o cliente RPC para se comunicar com o servidor.

3. **Testar o Sistema**:
   - Crie um arquivo na pasta monitorada pela máquina cliente.
   - Verifique se o mesmo arquivo é criado na pasta correspondente na máquina servidora.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Para isso, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch: `git checkout -b minha-branch`.
3. Faça suas alterações e commit: `git commit -m 'Minha contribuição'`.
4. Envie para o repositório original: `git push origin minha-branch`.
5. Crie um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

