# SQL - Fundamentos

## Tópicos objetivos:
   - SQL (Structured Query Language, traduzindo, Linguagem de Consulta Estruturada) é uma linguagem de programação padronizada que é usada para gerenciar bancos de dados relacionais e realizar várias operações sobre os dados neles contidos.
   - Conhecer os comandos mais comuns do SQL
   - Usar SELECT para consultar uma tabela
   - Usar INSERT para inserir dados em uma tabela
   - Usar UPDATE para atualizar uma tabela
   - Usar DELETE para remover dados de uma tabela
   - Usar JOIN para conectar os dados de múltiplas tabelas
   - Conhecer as cláusulas (FROM, ORDER BY, etc)

## Estado da arte

### Conceitos Iniciais
A área de banco de dados é de grande importância no mundo da informática, uma vez que a informação é um bem precioso e deve ser 
armazenada de forma coerente e adequada, pois é de fundamental importância na tomada de decisão de uma empresa.
Antigamente as empresas armazenavam informações em arquivos físicos, como fichas de cadastro, mas o surgimento e evolução dos 
computadores possibilitaram o armazenamento de dados de modo digital. Assim os bancos de dados evoluíram e se tornaram o coração de muitos sistemas de informação.
Atualmente, por mais simples que seja um sistema de informação ele precisará armazenar dados, de forma que possa recuperá-los e/ou alterá-los quando necessário. Por exemplo, se você desenvolver um sistema de informação para a biblioteca da escola, este sistema deverá armazenar dados dos alunos, dos livros, dos empréstimos realizados e devoluções. É para armazenar essas informações e recuperá-las quando necessário de forma rápida e segura que utilizamos um sistema de banco de dados.

#### Dado, informação, fato e metadados
- **Dado:** é qualquer elemento identificado em sua forma bruta que, por si 
só, não conduz a uma compreensão de determinado fato ou situação. 
(Oliveira, 2005).
- **Fato:** é um conjunto de dados relacionados. Registram o mundo real.
- **Informação:** é um agrupamento de dados de forma organizada para 
fazer sentido, gerar conhecimento, e auxiliar na tomada de decisões de 
uma empresa.
- **Metadado:** São dados sobre dados. Fornecem uma descrição das 
características dos dados e do conjunto de relacionamentos que ligam 
os dados encontrados no banco de dados.

### Sistema Gerenciador de Banco de dados - SGBD
Tudo que fazemos em um banco de dados passa pelo SGBD! Ele é responsável por salvar os dados no HD, manter em memória os dados mais 
acessados, ligar dados e metadados, disponibilizar uma interface para programas e usuários externos acessem o banco de dados (para banco de dados relacionais, é utilizada a linguagem SQL), encriptar dados, controlar o acesso a informações, manter cópias dos dados para recuperação de uma possível falha, garantir transações no banco de dados, enfim, sem o SGBD o banco de dados não funciona!

#### Características de um SGBD
O SGBD faz todo o gerenciamento de transações dos bancos de dados contidos nele. Uma transação em um banco de dados consiste em um conjunto de operações que são tratadas como uma unidade lógica indivisível. Por exemplo, quando vamos fazer uma transferência bancária, são feitas no mínimo duas operações, a retirada do dinheiro da conta de quem está transferindo e o depósito na conta da pessoa que vai receber o valor transferido, ou seja, a transferência é o conjunto dessas operações. 
As transações realizadas pelo SGBD nos bancos de dados devem seguir algumas propriedades fundamentais conhecidas como ACID 
(Atomicidade, Consistência, Isolamento e Durabilidade).
- **Atomicidade:** Capacidade de uma transação ter todas as suas 
operações executada ou nenhuma delas. É tudo ou nada. Caso a 
transação não aconteça totalmente o banco de dados executa um 
rollback e retorna ao seu estado consistente anterior, caso todas a 
transação aconteça é executado o commit;
- **Consistência:** A execução de uma transição deve levar o banco de 
dados de um estado consistente a outro estado consistente. 
- **Isolamento:** A propriedade de isolamento garante que a transação não 
será interferida por nenhuma outra transação concorrente. 
- **Durabilidade:** A propriedade de durabilidade garante que o que foi 
salvo, não será mais perdido. 
Além da gerencia de transações o SGBD possui algumas características 
que permitem controlar e acompanhar melhor os dados armazenados. As 
características básicas de um SGBD são: 
- **Controle de Redundâncias:** A redundância consiste no 
armazenamento de uma mesma informação em locais diferentes, 
provocando inconsistências. Se uma mesma informação estiver 
armazenada em mais de um lugar pode acontecer de você atualizar em
um lugar e esquecer-se de atualizar no outro, ficando o banco de dados 
inconsistente. 
- **Controle de concorrência:** O SGBD permite que duas ou mais 
pessoas acessem a mesma base de dados ao mesmo tempo e o 
sistema deve controlar para que um acesso não interfira no outro. Um 
sistema de compras Web por exemplo várias pessoas podem realizar 
uma compra ao mesmo tempo, e o próprio SGBD controla pra que os 
dados de todas as compras sejam gravados corretamente. 
- **Controle de Acesso:** O SGDB tem mecanismos para criação de regras 
de segurança, que vão desde a definição de login e senha para os 
usuários, até a permissão de acesso ao SGBD e acesso aos dados 
armazenados. É possível definir por exemplo que um usuário tem 
permissão somente para leitura de dados, e um outro usuário tenha 
permissão para criar base de dados e manipulá-la, mas não pode criar 
novos usuários ou fazer backup. 
- **Controle de Integridade:** Um SGBD pode definir regras que garantem 
a integridade dos dados. Essas regras são definidas para garantir que 
os dados contidos no banco de dados estejam corretos. Por exemplo, 
podemos definir uma regra em um banco que o campo sexo pode 
receber somente “M” para masculino e “F” para feminino, não aceitando 
outro tipo de letra, o que deixaria dados errados no banco. 
- **Backups:** O SGBD apresenta facilidade para recuperar falhas de 
hardware e software, através da existência de arquivos de "pré-imagem" 
ou de outros recursos automáticos, exigindo minimamente a intervenção 
de pessoal técnico.

### CONCEITOS BÁSICOS
Banco de Dados pode ser entendido como um depósito de um conjunto de registros que são controlados por meio de um computador e que oferece aos usuários vários recursos como: inserção, eliminação e atualização dos dados. Um sistema gerenciador de banco de dados (SGBD) é basicamente o responsável por facilitar o processo de definição e manipulação do banco de dados.
Portanto, o SGBD não é o banco de dados, ele é o sistema que gerencia, ou seja, que controla o banco de dados (BD), ele é projetado para fazer o controle de grandes volumes de informações. Em um SGBD podemos ter vários bancos de dados. Nas nossas atividades usaremos o MySQL como SGBD. Porém existem outros no mercado como: Oracle, PostgreSQL, DB2, Informix, SQL Server e outros.

#### BANCOS DE DADOS RELACIONAIS
Os Bancos de Dados Relacionais foram desenvolvidos para facilitar o acesso aos dados. Pois enquanto em um banco de dados hierárquico os 
usuários precisam definir as questões de maneira mais específica, iniciando pela raiz, nos Bancos de Dados Relacionais os usuários podem fazer perguntas relacionadas através de vários pontos.

#### LINGUAGEM SQL
O nome “SQL” significa “Structured Query Language” que em português quer dizer “Linguagem de Consulta Estrutura”. Essa linguagem teve seus fundamentos no modelo relacional de Codd (1970). Sua primeira versão recebeu o nome de SEQUEL - “Structured English Query Language”, sendo definida principalmente por D.D.CHAMBERLIN, em 1974, nos laboratórios de pesquisa da IBM. 
Em 1975, foi testado um protótipo de aplicação dessa nova linguagem. Entre 1976 e 1977, o SEQUEL foi revisado e ampliado, e teve seu nome alterado para “SQL”. Devido ao sucesso dessa nova forma de consulta a manipulação de dados, dentro de um ambiente de banco de dados, a utilização da SQL foi se tornando cada vez maior. Com isso uma grande quantidade de SGBD‟s foi tendo como linguagem básica a SQL.
A SQL se tornou um padrão de fato, no mundo dos ambientes de banco de dados relacionais. Em 1982, o American National Standard Institute (ANSI) tornou a SQL padrão oficial de linguagem em ambiente relacional.
Por ser uma linguagem de numerosas aplicações, a SQL pode manipular dados de diferentes bancos entre as funções de um SGBD.

#### COMPOSIÇÃO DOS BANCOS DE DADOS – DDL e DML
A linguagem SQL é dividida em subconjuntos de acordo com as operações que se deseja efetuar sobre um banco de dados. Os principais 
subconjuntos são: 
**DDL** - Data Definition Language (Linguagem de Definição de Dados) 
O conjunto de comandos da linguagem DDL é usado para a definição das estruturas de dados, fornecendo as instruções que permitem a criação, alteração e remoção de banco de dados, tabelas e etc. 
- Principais comandos: CREATE, ALTER e DROP 
**DML** - Data Manipulation Language (Linguagem de Manipulação de Dados)
É o grupo de comandos dentro da linguagem SQL utilizado para a recuperação, inclusão, remoção e modificação de informações em bancos de 
dados.
- Principais comandos: SELECT, INSERT, UPDATE, DELETE, e outros.

### INTRODUÇÃO AO MySQL

#### Comandos
- Para conhecer quais os bancos de dados existentes dentro do MySQL basta usar o comando SHOW DATABASES. SHOW significa mostrar, 
apresentar, exibir e DATABASES significa bases de dados ou bancos de dados, ou seja, manda mostrar os bancos de dados existentes.
   
      SHOW DATABASES;
   
- Criação de um novo banco de dados

      CREATE DATABASE 'nome do banco';
   
- Para que você possa ter acesso a qualquer informação do banco de dados, ou mesmo criar tabelas, inserir registro ou fazer uma consulta você precisa entrar dentro dele. O comando para isso é USE <nome do banco>;
   
      USE 'nome do banco';
   
- Agora como você já tem o banco de dados e entrou nele, você já pode começar a criar as tabelas do seu banco. Para criar tabelas é preciso seguir um padrão básico:
   
      CREATE TABLE 'nome da tabela'(
         <nome da coluna> <tipo de dados> (<quantidade de caracteres>),
         <nome da coluna> <tipo de dados> (<quantidade de caracteres>)
      );
         
- Para ver como ficou a estrutura das tabelas criadas usamos o codigo DESCRIBE TABLE <nome da tabela>; ou somente DESC TABLE <nome da 
tabela>;
         
      DESCRIBE TABLE 'nome da tabela';
         
- Mais se você quer ver como foi criada a tabela pode usar o comando SHOW CREATE TABLE <nome da tabela>
         
      SHOW CREATE TABLE 'nome da tabela';
         
- Usando o comando ALTER, é possível realizar as seguintes alterações na estrutura de uma tabela: Adicionar, excluir e alterar colunas
Exemplo ADD:
         
      ALTER TABLE <nome da tabela> ADD <nome da coluna> <tipo de dado>;
         
Exemplo FIRST:
Usando o mesmo banco de dados, porém na tabela aluno vamos adicionar a coluna código como sendo a primeira coluna e chave primaria da tabela.
         
      ALTER TABLE <nome da tabela> ADD <nome da coluna> <tipo de dado> AUTO_INCREMENT PRIMARY KEY FIRST;
         
Exemplo AFTER:
O FIRT insere na primeira coluna, já com o AFTER você escolhe a posição que deseja que a coluna fique, ou melhor, depois de quem a coluna vai ficar. Usando a mesma tabela aluno vamos inserir a coluna nascimento depois da coluna nome.
         
      ALTER TABLE <nome da tabela> ADD <nome da coluna> <tipo de dado> AFTER 'nome da coluna';
         
Exemplo DROP:
Para excluir uma coluna usamos o comando ALTER TABLE <nome da tabela> DROP <nome da coluna>;
         
      ALTER TABLE <nome da tabela> DROP <nome da coluna>
         
Também podemos alterar o tipo e o nome de uma coluna. Usamos o comando:
         
      ALTER TABLE <nome da tabela> CHANGE <nome da coluna> <nome da nova coluna> <tipo de dado da nova coluna>;
         
Exemplo CHANGE:
Como exemplo suponha que a coluna código da tabela aluno não está no padrão das outras tabelas do banco, porque nas outras tabelas a PK é definida com o nome “id” e no máximo de 10 caracteres. Então em vez de excluir toda a tabela ou excluir toda a coluna podemos usar a cláusula CHANGE e renomear o campo.
         
      ALTER TABLE aluno CHANGE codigo id INT(10) auto_increment;
         
- Excluir Tabelas
Para que você possa excluir uma tabela é preciso que ela exista dentro do banco de dados. Normalmente primeiro usamos o comando SHOW TABLES, para saber as tabelas que existem dentro do BD. Após usamos o comando:
         
      DROP TABLE <nome da tabela>;
         
Muitos se confundem entre o DELETE e o DROP. O comando DELETE é usado para manipulação e não para definição dos dados, ou seja, o DELETE remove os registros enquanto que o DROP remove a estrutura.
- Excluir Banco de Dados
Assim como para excluir tabelas é preciso ver quais existem no BD, para excluir banco de dados é bom ver quais os bancos de dados existentes dentro do SGBD, o comando usado é SHOW DATABASES. Mas se você não quer perder tempo olhando os bancos de dados existentes é só acrescentar IF EXISTS após o comando DROP DATABASE. Assim:
         
      DROP DATABASE IF EXISTS <nome do banco de dados>;
         
- CHAVE PRIMÁRIA E CHAVE ESTRANGEIRA
Os Bancos de Dados Relacionais são formados de várias tabelas e utilizam chaves como forma de referenciar outras tabelas. Esse relacionamento entre as tabelas é feito através das chaves estrangeiras. Quando falamos de chave estrangeira usamos a sigla FK referente à palavra FOREIGN KEY.
A definição da chave estrangeira segue o seguinte padrão:
         
      FOREIGN KEY<nome da FK> REFERENCES < tabela da PK>(<nome da PK>)
         
OBS: o nome e o tipo de dado da PK devem ser o mesmo da FK. A palavra REFERENCES é usada para dizer qual tabela a FK está referenciando.

- INSERT
Já demonstramos como criar uma tabela no banco de dados, agora mostraremos as maneiras básicas de se inserir dados nessa tabela. O comando usado para inserir dados é o INSERT.  A síntese básica do comando INSERT é a seguinte:
            
   INSERT INTO <nome da tabela> (campo1, campo2) VALUES (valor1, valor2);

Cada valor é inserido no campo que corresponde à posição do valor na lista: valor1 é inserido no campo1, valor2 no campo2 e assim por diante.
OBS: Os valores devem ser separados com uma vírgula e se o tipo do campo for texto deve está entre aspas duplas ou simples

emos também a opção de omitir as declarações dos campos. Essa sintaxe funciona somente se forem repassados valores para todas as colunas.
            
   INSERT INTO <nome da tabela> VALUES (valor1, valor2, valor3,…);
            
Cada valor é inserido no campo que corresponde a sequência das colunas na tabela, se a primeira coluna, por exemplo, for o nome então o valo1 deve ser o nome, se a segunda coluna, por exemplo, for idade então o valor2 deve ser a idade e assim por diante. 
OBS: Se a coluna for declarada como AUTO_INCREMENT basta você colocar o valor que corresponde a essa coluna como sendo zero(0). O valor zero(0) não influencia em nada porem se ele for esquecido vai ser gerado um erro.
            
- CLÁUSULAS
   1. SELECT
   A forma mais simples de se fazer um SELECT é recuperando todos os dados de uma tabela. A síntese básica é: 
         
      SELECT * FROM <nome da tabela>;  
            
OBS: O * (asterisco) substitui os nomes de todas as colunas, e todas serão selecionadas para o resultado da consulta. A instrução FROM indica de qual tabela estamos buscando os dados. 
       Caso não fosse de nosso desejo mostrar todas as colunas no resultado da consulta,  bastaria  nomear  as  colunas  que  deveriam  aparecer  no  lugar  do * (asterisco) e separadas por vírgula.
            
      SELECT <coluna1>, <coluna2> FROM <nome da tabela>;

i. **FROM**: Utilizada para especificar a tabela que se vai selecionar os registros.
ii. **WHERE**: Utilizada para especificar as condições que devem reunir os registros que serão selecionados.
iii. **GROUP BY**: Utilizada para separar os registros selecionados em grupos específicos.
iv. **HAVING**: Utilizada para expressar a condição que deve satisfazer cada grupo.
v. **ORDER BY**: Utilizada para ordenar os registros selecionados com uma ordem especifica
vi. **DISTINCT**: Utilizada para selecionar dados sem repetição.
            
- Exemplo WHERE
Se quisermos ver somente o nome e o endereço do cliente, como já foi dito basta colocar os nomes das colunas depois do SELECT, porém quando temos muitos registros e precisamos de uma informação especifica usamos a condição WHERE que em português significado ONDE.  Sempre a cláusula WHERE vem acompanhada de alguma condição, por exemplo: 

      SELECT nome, endereco FROM cliente WHERE cliente_id = 2 ; 
 
Podemos ler o comando SQL da seguinte forma:  
Selecione o nome e o endereço da tabela cliente onde cliente_id for igual a 2.

- Exemplo ORDER BY
         Até  o  momento  vimos  como  obter  dados  de  uma  tabela  utilizando  os comandos SELECT e WHERE. Porém, frequentemente precisamos listar os dados por uma ordem em particular. Pode ser por ordem ascendente ou descendente. Para isso podemos utilizar a cláusula ORDER BY para ordenar os dados. A sintaxe básica da cláusula ORDER BY é a seguinte: 

      SELECT < coluna > FROM < tabela > ORDER BY < coluna >;

OBS: Por padrão o ORDER BY vem como ASC significa que os resultados serão apresentados por ordem ascendente, ou seja, do menor para o maior. Mais também pode ser DESC significa que os resultados serão apresentados por ordem descendente, para isso acontecer você precisa declara-lo.

- UPDATE 
O comando para atualizar os dados é UPDATE, ele possui a seguinte sintaxe:

      UPDATE < tabela > SET < campo > = “novo valor” WHERE < condição > ;

tabela: nome da tabela que será modificada 
set: define qual campo será alterado  
campo: campo que terá seu valor alterado 
novo valor: valor que substituirá o antigo dado cadastrado em campo 
where: se não for informado, a tabela inteira será atualizada 
condição: regra que impõe condição para execução do comando 

Também podemos alterar mais de um campo de uma vez. Suponhamos que o cliente Pedro se mudou para outra cidade, precisamos alterar o endereço e a cidade atual, não precisamos criar dois UPDATES basta separa-los por vírgula.

      UPDATE < tabela > SET < campo1 > = “valor1”, < campo2 > = “valor2” WHERE < condição > ;

OBS: Devemos passar sempre o WHERE, que é uma espécie de filtro em nossa tabela, porque senão o passarmos atualizaremos TODOS os dados da tabela e isso pode acarretar diversos problemas, dependendo do tamanho e da complexidade da sua tabela. Imagina se esquecermos de colocar uma condição em uma tabela de 1.000 registros e alterarmos todos os endereços dos clientes para um só.

- DELETE
A forma mais simples de se fazer um DELETE é excluindo todos os dados de uma tabela. A síntese básica é: 

      DELETE FROM < nome da tabela >;  

Se não for especificada nenhuma condição então serão excluídos todos os dados da tabela, porém se você quer excluir somente um registro é preciso usar a cláusula WHERE informando qual será a condição para deletar.

      DELETE FROM < nome da tabela > WHERE < condição >;

OBS:  Lembre-se  que  este  comando,  assim  como  o  UPDATE,  pode  ser perigoso  em  algumas  situações,  já  que,  uma  vez  executado  esses comandos, não será possível desfazer a ação realizada. Portanto, devemos ficar atentos ao usar esses comandos em tabelas complexas.

- FUNÇÕES DE AGREGAÇÃO
i. **COUNT**: Utilizada para devolver o número de registros da seleção.
ii. **SUM**: Utilizada para devolver a soma de todos os valores de um campo determinado.
iii. **MAX**: Utilizada para devolver o valor mais alto de um campo especificado.
iv. **MIN**: Utilizada para devolver o valor mais baixo de um campo especificado.
v. **AVG**: Utilizada para calcular a media dos valores de um campo determinado.

- Exemplo Contagem (COUNT)

      SELECT COUNT(campo) FROM  < nome da tabela > ;

- Exemplo SOMA (SUM) 

      SELECT SUM(campo) FROM  < nome da tabela > ;

- Exemplo Máximo (MAX)

      SELECT MAX(campo) FROM  < nome da tabela > ;

- Exemplo Mínimo (MIN) 

      SELECT MIN(campo) FROM  < nome da tabela > ;

- Exemplo Média (AVG)

         SELECT AVG(campo) FROM  < nome da tabela > ;

- Utilizando GROUP BY e HAVING
É possível dividir o conjunto em grupos e aplicar a função de agregação a cada grupo. Para  executar essa  ação,  utilize uma  cláusula  GROUP  BY  na  consulta. Aprendemos  que  a  cláusula  WHERE  define  uma  condição  de  retorno  de  um comando SELECT. Os grupos também podem ser filtrados utilizando uma cláusula HAVING, que testa as propriedades de grupo envolvendo funções agregadas.  
OBS: O HAVING é diferente do WHERE. O WHERE restringe os resultados obtidos  sempre  após  o  uso  da  cláusula  FROM,  ao  passo  que  a  cláusula HAVING filtra o retorno do agrupamento.
Suponhamos que precisamos saber o total de quanto cada cliente precisa pagar, para isso utilizamos o GROUP BY, veja como fica o código: 

      SELECT ClienteID, SUM(ValorTotal) FROM vendas GROUP BY ClienteID ;

Agora se queremos saber somente os totais dos clientes que vão pagar um valor que seja maior que 200,00 R$ precisamos passar uma condição para o select utilizando a cláusula HAVING.

      SELECT ClienteID, SUM(ValorTotal) FROM vendas GROUP BY ClienteID HAVING SUM(ValorTotal) > 200;

OBS: Aqui eu coloquei somente alguns exemplos, se eu fosse colocar todas as ações que podem ser feitas usando os comandos SQL. Acredito que não acabaríamos essa apostila tão cedo, espero que você não faça somente os exemplos  mostrados  na  apostila,  procure  se  aprofundar  e  com  base  nos exemplos,  construa  seus  próprios  comandos,  não  espere  pelo  professor. Estude e faça exemplos antes mesmo de o professor pedir.

- OPERADORES RELACIONAIS
i. **<**: Menor que
ii. **>**: Maior que
iii. **<>**: Diferente
iv. **<=**: Menor ou igual que
v. **>=**: Maior ou igual que
vi. **=**: Igual a
vii. **BETWEEN**: Utilizado para especificar um intervalo de valores.
viii. **LIKE**: Utilizado  na  comparação  de  um  modelo  e  para  especificar registros  de  um  banco  de  dados."Like"  +  extensão  %  vai significar  buscar  todos  resultados  com  o  mesmo  início  da extensão.

- OPERADORES LÓGICOS
i. **AND**: Avalia as condições e devolve um valor verdadeiro caso ambos sejam corretos.
ii. **OR**: Avalia as condições e devolve um valor verdadeiro se algum for correto.
iii. **NOT**: Devolve o valor contrário da expressão.

- Exemplo LIKE
Com este operador, podemos comparar Strings. O percentual (%) substitui nenhum, um ou mais caracteres, já a sublinha (_) substitui somente um caractere. Utilizando a combinação desses caracteres especiais com o que se quer localizar, pode-se conseguir uma variedade muito grande de expressões. Veja na tabela a seguir algumas possíveis combinações:
1. LIKE 'A%: Todas as palavras que iniciem com a letra A;
2. LIKE '%A: Todas que terminem com a letra A;
3. LIKE '%A%: Todas que tenham a letra A em qualquer posição;
4. LIKE 'A_': String de dois caracteres que tenham a primeira letra A e o segundo caractere seja qualquer outro;
5. LIKE '_A': String de dois caracteres cujo primeiro caractere seja qualquer     um e a última letra seja A;
6. LIKE '_A_: String de três caracteres cuja segunda letra seja A, independentemente do primeiro ou do último caractere;
7. LIKE '%A_: Todos que tenham a letra A na panúltima posição e a última seja qualquer outro caractere;
8. LIKE '_A%: Todos que tenham a letra A na segunda posição e o primeiro caractere seja qualquer um;

      SELECT * FROM contatos WHERE nome LIKE ' < condição > ' ;

- Utilizando AND / OR 
O operador AND exibe os registros se tanto a primeira condição como a segunda condição for verdadeira. O operador OR exibe os registros se a primeira condição ou a segunda for verdadeira. Esses operadores são usados para filtrar registros com base em mais de uma condição.

- Exemplo BETWEEN
O comando BETWEEN permite fazer a seleção de um intervalo, entre um e outro. A sintaxe da cláusula BETWEEN é a seguinte: 

      SELECT * FROM alunos WHERE idade BETWEEN 10 AND 20;

Este comando irá selecionar todas as linhas cuja coluna tiver um valor entre 10 e 20. Os valores podem ser números, texto ou datas. Poderíamos de outra forma obter o mesmo resultado que seria:

      SELECT * FROM alunos WHERE idade > = 10 AND idade  < = 20;

## Referências
