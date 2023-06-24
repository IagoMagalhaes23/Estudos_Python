# Linha de comando - Fundamentos

## Tópicos objetivos:
   - CLI é um programa de linha de comando que aceita entradas de texto para executar funções do sistema operacional.
   - Conhecer os principais comandos

## CLI

### O Que Significa CLI?
<p>
Uma interface de linha de comando (command-line interface, ou CLI) processa os comandos que serão enviados para um programa de computador na forma de linhas de texto. Desde os anos 60, sistemas operacionais usam interfaces chamadas Shell (mais sobre isso abaixo) para permitir o acesso interativo a suas funções ou serviços.
</p>

### As Origens do CLI
<p>
Nos anos 60, o CLI era usado a todo momento. Naquele tempo, as pessoas tinham apenas teclados como um dispositivo de entrada e a tela do computador mostrava apenas informações em texto. Sistemas operacionais como o MS-DOS usavam o CLI como a interface de usuário padrão.

Basicamente, os usuários tinham que digitar um comando no CLI para conseguir fazer alguma ação. E essa era a única forma de se comunicar com os computadores.

Depois de digitar um comeando, o resultado que o usuário recebia era ou uma informação em texto ou uma ação específica desempenhada pelo computador. Dito isso, digitar a linha de comando era crucial. Hoje em dia esse também é o caso.

Se o usuário digitar o comando errado, é possível que ele remova algo ou configure algo errado acidentalmente. Também pode ser que ele feche o programa sem querer antes de salvar seu trabalho até aquele momento. Isso é o que algumas pessoas consideram como ponto negativo do CLI.

Então, depois de anos de desenvolvimento usando apenas um teclado e o risco de uma linha de comando errada, o mouse foi inventado.
A invenção de um mouse marcou o início de um método conhecido como point-and-click (apontar e clicar), que acabou se tornando um novo jeito de interagir com um computador. 

Esse método era muito mais seguro para os usuários, por isso, eles deixaram o CLI de lado muito rapidamente. Mas, logo mais, vamos discutir por que usar o CLI ainda é uma opção melhor em determinados casos.
</p>

### Para que Serve o CLI e Quais as Suas Vantagens?
1. Menos Recursos
Não é segredo para ninguém que programas baseados em textos consomem bem poucos recursos de um computador. Isso significa que o CLI pode fazer tarefas similares a uma GUI com o mínimo de recursos possível.

2. Alta Precisão
Você pode usar um comando específico para alcançar os locais que quiser com facilidade. Considerando que você não digite os comandos incorretamente, ele vai funcionar como o desejado. Assim que você aprender o básico, escrever uma sintaxe passa a ser bem menos difícil do que você tinha imaginado.

3. Tarefas Repetitivas Amigavelmente
O GUI se desenvolveu bem ao longo dos anos. Mas, pode ser que o sistema operacional não dê todas as opções de botões e menus para realizar todas as tarefas. Uma das razões para isso acontecer é a segurança. E isso pode fazer com que você fique sobrecarregado ao ter que fazer tarefas repetitivas.

Por exemplo, quando você precisa gerenciar centenas de arquivos dentro de uma pasta, o CLI permite que você use um único comando para fazer a automação desta tarefa de maneira super fácil.

4. Poder de Sobra
A maioria dos sistemas operacionais previne que você faça uma bagunça nos processos centrais do sistema. O Windows conta com um sistema de proteção e o MacOS tem o SIP (System Integrity Protection – Proteção da Integridade do Sistema). Com isso, você não vai poder fazer certas tarefas que estão protegidas pelo próprio sistema. É por isso que, com o CLI, você ganha controle total sobre o seu sistema de escolha.

Para ilustrar um exemplo, existe um método que converte PSD para HTML quando se está desenvolvendo um site. 

Nessa conversão, o processo começa com um modelo (rascunho) em tamanho real de um objeto no Photoshop. Então, o documento do Photoshop (formato .psd) é convertido para HTML.

Converter PSD para HTML é um trabalho pesado de codificação. O desenvolvedor tem o papel fundamental de fazer com que o código usado na conversão esteja totalmente limpo. Isso é passo importantíssimo para estar de acordo com os padrões do W3. 

O acordo W3C garante que cada site publicado na internet tenha uma boa programação, que seja livre de erros e compatível com o maior número possível de navegadores.

Então, entender os códigos e como eles funcionam é vital para sacar como os processos funcionam na sua parte mais intrínseca. 

O mesmo acontece com o CLI no sistema operacional. Enquanto o GUI pode até parece mais atrativo, o CLI é leve, poderoso e bem mais direto nas suas ações.

### Shell – A Base do CLI
Se formos mergulhar fundo na parte do CLI como sistema operacional, vamos encontrar o Shell.

O Shell é uma interface de usuário responsável por processar todos os comandos digitados no CLI. Ele lê e interpreta os comandos e as instruções do sistema operacional e, então, executa as ações como foram pedidas.

Em outras palavras, um shell é uma interface de usuário que gerencia o CLI e age como um intermediário, conectando os usuários com o sistema operacional. 

Na prática, existem muitas coisas que o shell pode processar. Algumas delas são:

- Funciona com arquivos e diretórios;
- Abre e fecha um programa;
- Gerencia processos do computador
- Executa ações e atividades repetitivas.

### Tipos Mais Populares de CLI

- Windows Shell
O shell padrão no Windows é o CMD.exe ou o Prompt de Comando (Command Prompt). De fato, a Microsoft tem usado o Prompt de Comando desde quando o MS-DOS era o principal sistema operacional da empresa.

Para abrir o Prompt de Comando, você pode clicar em Iniciar → Todos os Programas → Acessórios → Prompt de Comando. Ou, simplesmente, apertar Windows+R, digitar CMD e ENTER.  

Dependendo da sua necessidade, você pode digitar um único comando ou uma combinação de comandos. Você também pode digitar comandos que são executados em sequência (um comando é executado depois de outro e assim por diante).

O Prompt de Comando é tão robusto que ele pode gerenciar muitas coisas dentro do sistema operacional Windows. Algumas das principais são:

    Modificar diretórios, listar diretórios, conteúdos, arquivos e assim por diante;
    Gerenciar ambientes de rede, assim como mostrar configurações de IPs de redes de internet;
    Gerenciar arquivos, como renomear, mover de um local para outro, apagar e mais;
    Gerenciar tipos de mídia, como formatar, renomear e outras ações.

Agora, vamos aprender a usar algumas das sintaxes no prompt de comando. Veja a listagem logo abaixo, sua descrição e o comando exato.

**Modificar um Diretório**
Para navegar para um diretório ou pasta específica pelo prompt de comando, use CD [caminho]. Garanta que tenha um espaço antes de colocar o caminho (path) que você quer alcançar. Por exemplo:

    CD C:\Program Files

**Renomear um Arquivo**
Para renomear um arquivo dentro de uma pasta específica, use REN [drive:][caminho] [fonte] [alvo]. Se você mencionar o local (path), isso significa que o arquivo renomeado será salvo na mesma pasta mencionada. Por exemplo:

    REN d:untitled.txt untitled1.txt

**Apagar um Arquivo**
Para apagar um arquivo pelo prompt de comando, use DEL [nomedoarquivo]. Se você quer forçar a exclusão de um arquivo, é só adicionar o comando certo antes do nome do arquivo. Por exemplo:

    DEL /F untitled.txt

**Renomear um Disco**
Para editar o nome de um disco específico, use LABEL [drive:][novo nome do disco]. Saiba que, aqui, você pode usar até 32 caracteres no volume NTFS e 11 caracteres no volume FAT. Por exemplo:

    D:\ > LABEL d:MyData

- Bash
Bash é o acrônimo para Bourne Again Shell. Ele foi desenvolvido pela Free Software Foundation. 

O Bash é um tipo de shell usado no MacOS e outras distribuições do Linux. Porém, você também pode usar o Bash Linux no Windows 10, se quiser.

No Linux, o Bash shell é só um dos muitos tipos de shell que o Linux pode usar. Outros tipos bem conhecidos são o Techs shell, Ksh shell e Zsh shell. 

Na maioria das distribuições Linux, o shell é localizado no menu Utilities (Utilidades). Se você usar o desktop Gnome, o nome será Terminal. Mas, se você usar o KDE, o nome será Konsole. 

Enquanto isso, no MacOS, o programa é o Terminal.app. Para rodar esse programa, vá em Application → Utilities → Terminal. Ou simplesmente digite Terminal usando a busca pelo software Spotlight. 

Assim que o terminal abrir, você já pode começar a colocar seus primeiros comandos. Basicamente, a maioria dos comandos consiste em: o comando em si, o argumento e a opção.  

Enquanto o comando contém a instrução que queremos desempenhar, é o argumento que diz onde o comando deve operar. Já a opção faz o pedido para a modificação do resultado do comando.

Agora, é hora de aprender a como usar o shell.

Para começar, você deve conhecer a sintaxe para saber lidar com a plataforma. Isso também é conhecido como script do shell, ou seja, maneiras de usar um script que se comunica com o CLI para realizar determinadas tarefas.

Basicamente, os comandos são divididos em:

    - Comandos que gerenciam os processos;
    - Comandos que gerenciam os arquivos.

Para entender a sintaxe de comando no MacOS, vamos aprender alguns exemplos. Eles estão logo abaixo.

**Listar Todos os Arquivos em uma Pasta**
Para saber quais arquivos estão em uma pasta, use ls. O comando padrão vai excluir os arquivos escondidos. Para mostrar todos os arquivos, você adicionar um -a. Por exemplo:

    ls -a

**Mudar de Diretório**
Para mover para mudar para um diretório específico, use cd destino. Por exemplo:

    cd ~/Desktop

**Renomear Arquivos**
Para renomear um arquivo dentro de uma pasta específica, use mv fonte destino. Neste caso, você precisa saber qual o nome do arquivo e a extensão dele. Por exemplo:

    mv ~/Desktop/untitled.rtf ~/Desktop/untitled1.rtf

**Apagar Arquivos**
Para apagar um arquivo em uma pasta específica, use rm nome do arquivo. Para evitar deletar arquivos que você não quer, garanta que você mova estes arquivos para a pasta certa antes. Por exemplo:

    rm untitled.rtf

Mais uma vez, digitar o comando certo é crucial quando se trabalha com qualquer CLI. Isso significa que você deve prestar atenção em cada caractere que for usar. Além disso, use o comando certo para cada caso.

E se por algum motivo você quiser parar de usar o Prompt de Comando ou o Bash, é só digitar Control+C. Você vai sair das telas deles e voltar ao sistema operacional normalmente.

### Principais Tipos de CLI
Quem trabalha como programador sabe que existem CLIs que são muito mais utilizadas no mercado e importantes de se aprender do que outras.

Elas podem ser de código aberto, como é o caso do GIT, ou de propriedade de empresas como Amazon, Google e Microsoft.

Confira abaixo os quatro principais tipos de CLI do mercado:

- AWS CLI (Amazon): a interface de linha de comando do Amazon Web Services permite ter controle total sobre os serviços da gigante do eCommerce, além de automatizar uma série de funções usando scripts.
- Azure CLI (Microsoft): do mesmo modo, a Microsoft também tem sua própria CLI para gerenciar a nuvem Azure. Ela pode ser usada no próprio navegador através da Azure Cloud Shell ou até mesmo instalada no macOS, no Linux ou no Windows.
- GCloud CLI (Google): para completar, temos a interface de linha de comando da própria Google. Ela permite operar os recursos do Google Cloud como uma máquina do Compute Engine, instâncias do SQL ou clusters do Cloud Dataproc.
- GIT (Código aberto): a linha de comandos é a única ferramenta que permite rodar todos os comandos do GIT. Pode até ser mais simples e cômodo usar um software de controle de versões com uma interface gráfica, mas às vezes é necessário usar o CLI para se ter acesso a um recurso específico.

## CLI com Python
### Estrutura de uma CLI em python
A primeira vez que pensei em criar uma ferramenta de linha de comando me parecer que seria difícil, porém é quase o extremo contrário.

Claro que depende muito do tamanho do projeto, mas para poder criar algo funcional apenas precisamos de uma estrutura simples como esta abaixo:

    pasta_principal/ 
    ├── README.md 
    ├── install.sh 
    ├── extensão 
    ├── __init__.py 
    ├── __main__.py 
    └── search_handler.py 
    └── setup.py

**pasta_principal/**
É a raiz do projeto, dentro dela que colocamos os arquivos e outros diretórios.

**README.md & install.sh**
Opcionais, servindo para documentar o seu projeto e fazer a instalação diretamente sem utilizar o pip install (mais abaixo eu explícito), respectivamente.

**extensão**
É a estrutura de um pacote python, que seria o mesmo que um diretório, porém com um arquivo __init__.py que faz o papel de indicar ao python que isso se trata de um pacote.

Outro arquivo é o __main__.py , que é o arquivo principal do sistema, centralizando tudo que será chamado pelo comando ext, ou seja, é o que será executado primeiro no sistema, e todo o resto do fluxo deve seguir a partir dele e de sua função main() , como pode ser visto no projeto no GitHub.

O terceiro arquivo, search_handler.py , é um módulo python, que é um arquivo python que serve como um agregador de funções, usado para organizar melhor o código.
Ele possui uma biblioteca chamada wikipedia que faz o contato com o site de mesmo nome, assim retornando o resultado!

**setup.py**
Responsável por fazer a mágica de deixar o seu código instalável, basicamente ele cria sua CLI, e não precisa ser mais complexo que isso:

    from setuptools import setup 
    setup( 
        name = 'extension', 
        version = '0.1.0', 
        packages = ['extension'], 
        entry_points = { 
            'console_scripts': [ 
                'ext = extension.__main__:main' 
            ] 
        })

O argumento responsável por executar o sistema é o “ext”, ele irá executar os processos que estiverem no caminho: extension.__main__.main()

Para fazer a instalação, é necessário utilizar o pip install do python, e com ele usaremos também a flag -e para sinalizar que queremos atualizar o código assim que o projeto sofrer alterações (de forma automática), e por último, diremos ao pip que iremos instalar o diretório atual, posicionando um ponto ( . ).

    pip instalar -e .

## CLI e AWS
A AWS Command Line Interface (AWS CLI) é uma ferramenta unificada para o gerenciamento de seus produtos da AWS. Com apenas uma ferramenta para baixar e configurar, você poderá controlar vários produtos da AWS pela linha de comando e automatizá-los usando scripts.

A AWS CLI v2 oferece diversos novos recursos incluindo instaladores aprimorados, novas opções de configuração, como AWS IAM Identity Center (sucessor do AWS SSO), e vários recursos interativos.

### aws-shell (Visualização do desenvolvedor)
O aws-shell é um programa shell de linha de comando que oferece conveniência e recursos de produtividade para ajudar usuários novos e avançados da Interface da Linha de Comando da AWS. Os principais recursos incluem o seguinte.

- Preenchimento automático de fuzzies para
    Comandos (ex.: ec2, describe-instances, sqs, create-queue)
    Opções (ex.: --instance-ids, --queue-url)
    Identificadores de recurso (ex.: IDs de instância do Amazon EC2, URLs de fila do Amazon SQS, nomes de tópico do Amazon SNS)
- Documentação em linha dinâmica
    A documentação para comandos e opções é exibida conforme você vai digitando
- Execução de comandos do shell do SO
    Use comandos OS comuns, como cat, ls e cp, além de entradas e saídas pipe, sem sair do shell
- Exporte comandos executados para um editor de texto

Para saber mais, verifique a postagem relacionada no blog da Interface da Linha de Comando da AWS.

### Uso
O Guia do usuário da Interface da Linha de Comando da AWS orienta você durante a instalação e configuração da ferramenta. Depois disso, você pode começar a fazer chamadas para seus serviços AWS pela linha de comando.

    $ aws ec2 describe-instances

    $ aws ec2 start-instances --instance-ids i-1348636c

    $ aws sns publish --topic-arn arn:aws:sns:us-east-1:546419318123:OperationsError --message "Script Failure"

    $ aws sqs receive-message --queue-url https://queue.amazonaws.com/546419318123/Test

Você pode obter ajuda na linha de comando para ver os serviços compatíveis,

    $ aws help

as operações para um serviço,

    $ aws autoscaling help

e os parâmetros para uma operação de serviço.

    $ aws autoscaling create-auto-scaling-group help

### Comandos de arquivos para o Amazon S3
Novos comandos de arquivos facilitam o gerenciamento dos seus objetos do Amazon S3. Usando uma sintaxe familiar, você pode visualizar o conteúdo dos seus buckets do S3 em uma listagem baseada em diretório.

    $ aws s3 ls s3://mybucket


        LastWriteTime            Length Name


        ------------             ------ ----


                                PRE myfolder/


2013-09-03 10:00:00           1234 myfile.txt



Você pode fazer uploads e downloads recorrentes de vários arquivos com um único comando em nível de pasta. A ILC da AWS executará essas transferências em paralelo para obter maior performance.

    $ aws s3 cp myfolder s3://mybucket/myfolder --recursive

upload: myfolder/file1.txt to s3://mybucket/myfolder/file1.txt
upload: myfolder/subfolder/file1.txt to s3://mybucket/myfolder/subfolder/file1.txt

O comando sync facilita a sincronização do conteúdo de uma pasta local com uma cópia em um bucket do S3.

    $ aws s3 sync myfolder s3://mybucket/myfolder --exclude *.tmp

upload: myfolder/newfile.txt to s3://mybucket/myfolder/newfile.txt

## Referências
- https://www.hostinger.com.br/tutoriais/o-que-e-cli
- https://itanuromero.medium.com/como-criar-uma-cli-em-python-fd80320f7968
- https://aws.amazon.com/pt/cli/