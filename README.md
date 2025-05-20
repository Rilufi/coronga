# Botoronga - Bot de Informações sobre COVID-19

## Descrição
Este repositório unifica os projetos `coronga_bot` e `coronga2.0`, proporcionando uma solução abrangente para postagem de informações sobre COVID-19 no Twitter.

## Instalação e Utilização
Certifique-se de ter Python 3 e pip instalados em seu sistema. Você pode instalá-los utilizando os seguintes comandos:

```bash
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```
Instale os requisitos do projeto executando:

```bash
$ pip install -r requirements.txt
```
### Configuração
Credenciais do Twitter: Para conectar o bot à sua conta do Twitter, edite o arquivo credentials.py e insira suas credenciais. Se ainda não as possui, solicite uma conta de desenvolvedor no site do Twitter e crie um aplicativo.

### Personalização dos Dados
Se desejar personalizar as informações sobre o COVID-19 ou modificar as mensagens postadas, consulte a documentação da biblioteca covid19_data aqui. O bot está pronto para publicar dados sobre casos confirmados, mortes e recuperados no Brasil.

## Execução
Após configurar as credenciais e personalizar os dados conforme necessário, execute o bot utilizando o seguinte comando:

```bash
$ python corona_bot.py
```
### Informações sobre o Clima de São Paulo
O bot agora inclui funcionalidades para postar informações sobre o clima de São Paulo. As informações são obtidas da https://openweathermap.org que traz dados de temperatura atual de hora em hora e a https://wunderground.com com o histórico diário de temperatura.

### Suporte a Sistemas Operacionais
Embora este guia seja voltado para distribuições Linux, o bot pode ser executado em outros sistemas operacionais com ajustes mínimos. O único requisito é ter Python e pip instalados.

### Hospedagem na Nuvem
Consideramos hospedar o bot em um servidor na nuvem para garantir automação contínua. Serviços como Heroku, Amazon Web Services, DigitalOcean e Google Cloud oferecem opções adequadas. Recomendamos o PythonAnywhere, que oferece um plano gratuito adequado para executar scripts diariamente.

### Agradecimentos
Agradecemos à Universidade Johns Hopkins por disponibilizar os dados em https://systems.jhu.edu/ e ao usuário binarynightowl por facilitar o acesso aos dados.

#### Nota
As funcionalidades relacionadas ao jogo Tetris foram removidas do bot. No entanto, o repositório ainda está disponível no repositório [Tetris](https://github.com/Rilufi/twitris). O bot agora está postando informações sobre o clima de São Paulo em suas atualizações regulares e pode ser encontrado em [Botoronga](https://twitter.com/botoronga).
