# coronga_bot
## Instalações necessárias
### Instale o Python

Esse programa roda em qualquer versão de Python 3

Para instalar o Python 3, digite em um terminal:

$ sudo apt-get install python3

### Instale o pip

Para instalar o gerenciador de pacotes pip, digite em um terminal:

$ sudo apt-get install python3-pip

### Requisitos

Os requisitos necessários para rodar são o tweepy para acesso ao twitter e a biblioteca covid19_data para os dados sobre o coronavirus, ambos estão inclusos no requirements.txt, então podem ser instalados com pip install requirements.txt

### Edições

Para que o programa se conecte ao seu API do twitter, é necessário editar o arquivo credentials.py com as suas credenciais, se ainda não tem será necessário pedir uma developer account no site do Twitter e criar o app: https://developer.twitter.com/en/apply-for-access

Para mudar informações sobre o coronavirus, siga as instruções em https://pypi.org/project/covid19-data/ o bot está pronto para postar informaçes sobre casos confirmados, mortes e recuperados no Brasil.

Caso queira mudar as frases postadas ou o propósito do bot é só editar o resto (não se esqueça de liberar seu app para ter permissão de ler e postar, podendo até enviar DMs) 

### Executando

Após isso, é só salvar a edição e executar o corona_bot.py na sua linha de comando com 

$ python corona_bot.py 

;)

### Sistemas Operacionais

Esse guia foi feito pensando em distribuições do Linux, mas existem paralelos para outros sistemas, onde as únicas mudanças serão instalar o python e o pip, de resto funciona normal

### Dica extra

Rodar um bot do próprio terminal do seu PC pode não ser a melhor maneira e não garante total automação (que normalmente é a meta quando se cria um bot), pense em colocá-lo em algum cloud server que tenha a função Task Schedule, como por exemplo: Heroku, Amazon, Digital-Ocean, Google, etc.

Um bom que possui um plano free que funciona para rodar scripts uma vez por dia é o https://www.pythonanywhere.com/

### Agradecimentos

Universidade John Hopkins por liberar os dados https://systems.jhu.edu/ e https://github.com/binarynightowl por disponibilizar o acesso facilitado.
