# Python - MVC e MTV

## Tópicos objetivos:
   - MVC e MTV são dois padrões de projeto (design patterns) utilizados para implementar interfaces e aplicações web.
   - Entender o padrão MVC
   - Entender o padrão MTV
   - Compreender a diferença entre os padrões MVC e MTV

## Padrão MVC

### o que é MVC?
O MVC é um padrão de arquitetura de software. O MVC sugere uma maneira para você pensar na divisão de responsabilidades, principalmente dentro de um software web.

O princípio básico do MVC é a divisão da aplicação em três camadas: a camada de interação do usuário (view), a camada de manipulação dos dados (model) e a camada de controle (controller).

Com o MVC, é possível separar o código relativo à interface do usuário das regras de negócio, o que sem dúvida traz muitas vantagens que veremos mais à frente.

### Camadas
Quando falamos sobre o MVC, cada uma das camadas apresenta geralmente as seguintes responsabilidades:

● Model A responsabilidade dos models é representar o negócio. Também é responsável pelo acesso e manipulação dos dados na sua aplicação.

● View A view é responsável pela interface que será apresentada, mostrando as informações do model para o usuário.

● Controller É a camada de controle, responsável por ligar o model e a view, fazendo com que os models possam ser repassados para as views e vice-versa.

### Exemplo
Vamos utilizar o exemplo de uma página web, onde o usuário pode realizar o cadastro de clientes. Neste caso, provavelmente você teria uma classe chamada cliente.php que contém as informações do cliente que você deseja guardar (como nome, endereço, cidade, etc.). Essa classe seria o seu model.

Aqui, ainda poderíamos acoplar aspectos de manipulação de bancos de dados, concentrando nesta estrutura os métodos para inserir, alterar, excluir e listar os clientes a partir de uma tabela em um banco de dados.

A página HTML seria nossa view, que mostraria, por exemplo, a lista de usuários cadastrados ou mesmo o próprio formulário para cadastro de novos usuários.

O controller faz o meio de campo entre o model e a view. Ele é necessário porque as estruturas presentes com view não deveriam acessar diretamente os models, já que isso poderia criar um acoplamento entre as estruturas de apresentação e definição de negócio: é necessária uma estrutura intermediária para fazer essa ligação.

E aqui entra o controller, que age como uma ponte entre os dois. Você pode ter uma classe dentro do seu projeto PHP para fazer o papel de um controller, realizando a ligação entre models e views.

### O MVC e sua importância
Não dá para falar do MVC sem citar a importância que ele traz em meio ao desenvolvimento de software.

Uma dessas vantagens é que ele nos ajuda a deixar o código mais manutenível, ou seja, mais fácil de fazer manutenção, já que temos as responsabilidades devidamente separadas. Isso também traz uma facilidade na compreensão do código, além da sua reutilização.

Além disso, você tem um código mais testável, pois ele é mais granular: se você tem uma aplicação onde, por exemplo, na página de listagem de usuários, o nome do usuário está sendo cortado ou não está sendo exibido da maneira correta, é muito mais fácil você fazer um teste que atinja somente as estruturas de views.

Aqui, podemos ver claramente que você tem um problema de apresentação: os models não são responsáveis por aspectos de apresentação, assim como os controllers também não são… Veja que é até mais fácil de identificar que o problema está na view. Por isso, você consegue corrigir somente a view e testá-la de maneira isolada.

Um segundo exemplo seria se você tivesse um problema de validação ou uma informação de um campo que o usuário está preenchendo na view e não está chegando no banco de dados: não é a view que envia coisas para o banco de dados, assim como também não é o model que é responsável por esse papel (aliás, o model pode até enviar coisas para o banco de dados, mas essas informações são repassadas por outras estruturas anteriores).

Então, podemos chegar à conclusão de que o problema é no controller. Sendo assim, você consegue trabalhar somente no controller, sabendo que as alterações provavelmente não irão impactar nas views e nos models. Além disso, você conseguirá realizar testes de uma maneira muito mais rápida e eficiente.

## Padrão MTV

### Como funciona a arquitetura MTV
Um padrão de projeto bem conhecido é o MVC (Model, View, Controller) que é um padrão de design (padrões de projetos) baseado em separação em três planos os quais estão conectados entre si e desempenham papéis para que sua aplicação funcione. Essa lógica é utilizada em linguagens bem famosas no mercado como Java, C#, Ruby e PHP.

A arquitetura MTV é uma derivação do padrão de projeto. O que se altera é a nomenclatura de arquivos e quais são as firmas interconectadas. Este modelo é utilizado dentro do framework Django, e a ideia deste artigo é mostrar como funciona dentro de um aplicativo web embutido no framework de Python.

A definição de Model é a mesma para a arquitetura MVC e MTV, que é o arquivo que contém a estrutura lógica do projeto e funciona como um intermediário para manipular dados entre o banco de dados e a View. Dentro do arquivo Model é determinado quais tipos de dados, e como serão armazenados dentro do seu banco e, como serão exibidos quando solicitados pela View.

O arquivo View é muito confundido com o Controller da arquitetura MVC, porém não tem relação. O papel desta camada é formatar os dados que são vindos do banco através do Model para visualização.

E por último o Template, que cuida da parte desta visualização para o usuário final. Ele é como o front-end de sua aplicação. Nesta arquitetura, esta camada fica armazenada os arquivos html, css, javascript extendidos e por conta disso auxilia numa velocidade maior de desenvolvimento e conforme o retorno da aplicação, ele renderiza seus arquivos HTML de sua aplicação no navegador. Como referência, esta camada seria como a camada View em uma estrutura MVC, e no caso do Django framework , tem um plus que é possível trabalhar com extensão de arquivos, ou seja, para o dev front-end isso auxilia muito em seu trabalho.

Para entender um pouco melhor, a ideia é mostrar como funciona a arquitetura do Django e como a arquitetura MTV influencia nessa estrutura.

O Django é baseado em requisições e respostas. Sempre que há uma atualização ou mudança dentro do Template, esta solicitação é enviada para o servidor através da View que pode, por exemplo, ser um clique para uma URL de acesso. Esta parte de mapeamento de URLs também é um componente existente dentro do Django, que o faz através de expressões regulares, um ponto bem bacana para uma aplicação web pois ajuda na parte de SEO.

Voltando a parte da solicitação da URL, após essa requisição, a lógica da aplicação começa a funcionar pois fará a verificação se é uma URL válida, e bate dentro da Model para conseguir acessar o banco de dados. Se a requisição for válida e estiver tudo certo, é retornado um status http como 200, ou o formato desejado através da View, e que por fim é renderizado pelo Template e que responde com o arquivo HTML solicitado. Um exemplo do dia a dia é um caso de um site, que é criado em Django, e seu usuário quer acessar uma página de login. Vem essa solicitação do Template, ea View retorna com uma url correspondente como algumacoisa/login e é renderizada no navegador.

Após isso, aparece o formulário (página HTML) para preencher com suas credenciais (login e senha), e estes dados são novamente enviados para validação através da View, são recebidos pela Model e batem no banco de dados e é verificado se é o mesmo que está salvo na base. Se sim, é retornado com os dados pela Model, como por exemplo, imagem de perfil, dados pessoais, dados de compra e etc e enviados para a View que formatará o mesmo para ser renderizado dentro do Template. Caso sejam dados inválidos, a Model retorna que não encontrou, e este resultado negativo é processado pela View e pode ser renderizado uma página de erro no navegador, ou a própria página de login com uma mensagem de erro.

De forma básica, este é o funcionamento da arquitetura do Django que é baseado em uma arquitetura MTV. É um framework em Python então para quem está iniciando o ideal é ter um conhecimento prévio de Python e sua lógica, e estudar a documentação que é bem completa.

## Referências
- https://www.treinaweb.com.br/blog/o-que-e-mvc#:~:text=O%20MVC%20sugere%20uma%20maneira,camada%20de%20controle%20(controller).
- https://diandrasilva.medium.com/como-funciona-a-arquitetura-mtv-django-86af916f1f63