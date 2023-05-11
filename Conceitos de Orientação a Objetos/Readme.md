# Conceitos de Orientação a Objetos

## Tópicos objetivos:
    - A Programação Orientada a Objetos é um paradigma de programação de software baseado na composição e interação entre diversas unidades chamadas de 'objetos' e as classes, que contêm uma identidade, propriedades e métodos). Ela é baseada em quatro componentes da programação: abstração digital, encapsulamento, herança e polimorfismo.
   - Como funcionam objetos
   - Criar e utilizar construtores
   - O que são classes
   - Criar e utilizar métodos
   - Como funciona encapsulamento
   - O que é herança
   - O que é polimorfismo
   - Como funcionam interfaces
   - O que são abstrações

## Estudo da arte

### Introdução a Programação Orientada a Objetos (POO)
    A orientação a objetos é, sem dúvida alguma, um dos mais significativos conhecimentos daquele que quer efetivamente se aprofundar no universo da Ciência da Computação. Para haver uma precisa compreensão do que vem a ser tal conteúdo, torna-se indispensável, antes de mais nada, conhecer aspectos como sua origem e conceitos relacionados.

### Objeto x Classe x Instância
Na POO (Programação Orientada a Objetos), os objetos do mundo real são analisados de uma forma abstrata, ou seja, as características do objeto que são levadas em consideração são apenas as que são fundamentais para o sistema. E aquilo que é importante será definido na classe.

#### O que é uma classe?
    É uma abstração das características relevantes de um grupo de coisas do mundo     real. A classe, em orientação a objeto, é criada para definir no sistema como o objeto vai ser criado, quais serão suas características (atributos) e suas ações (métodos). Já o objeto é o componente de software que representa o objeto do mundo real, reunindo atributos e métodos relacionados, e se relacionando entre si através de mensagens. Uma classe pode gerar vários objetos.  Chamamos de instância o ato de a classe criar um novo objeto. Em outras palavras, um objeto é uma instância de uma classe.

#### O que é um atributo?
    Os objetos possuem atributos, que são informações que definem seu estado. Os atribtos de cada objeto de uma classe têm seus próprios valores. Em uma classe,  podemos encontrar dois tipos de atributos: atributos de objeto e atributos de classe. 
    - Atributos de objeto: cada objeto tem seus atributos, e não compartilham com  os outros. 
    - Atributos de classe são aqueles que têm valores compartilhados por todos os objetos da classe.

### Método
    Os métodos são as ações que a objeto poderá realizar. É a descrição, em forma de código, das operações que um objeto executa quando recebe uma mensagem. Pode ser chamado por qualquer outro método para realizar alguma função específica. Por exemplo, vamos imaginar um aparelho de som. Sua função é reproduzir músicas, mas só a executa se receber uma ordem para isso. E essa ordem é passada pelo botão de ligar, que ao ser acionado, faz com que a música toque. Nesse caso, teríamos que implementar um método que tivesse a ação de fazer o som tocar. Perceba que um aparelho de som possui outros botões, cada um com suas responsabilidades diversas     como parar de tocar, gravar, aumentar volume, diminuir. 

### Construtores
    O construtor de uma classe é utilizado para a construção de um objeto pertencente àquela classe. Ao ser chamado, todas as inicializações do objeto são declaradas de     forma organizada. Deve ser criado com o mesmo nome da classe, e pode ou não receber um argumento, podendo inicializar, assim, já com algum tipo de informação 
    atrbuída.

### Encapsulamento
#### O que é Encapsulamento?
    Encapsulamento é um princípio da programação orientada a objeto que permite que determinados elementos de uma classe possam ser ocultados de outras classes.  Ou seja, encapsulando, conseguimos esconder dados contidos em uma classe, podendo ser acessados apenas por intermédio de métodos próprios.

#### Modificadores de Acesso
    Agora já sabemos que o encapsulamento nos dá a opção de esconder dados de objetos. Mas como? Podemos definir esse acesso aos dados de três formas: Público, Protegido e Particular.

##### Acesso Público (Public)
    No acesso público, os elementos da classe poderão ser acessados tanto de dentro como de fora da classe. Ou seja, qualquer objeto que interage com a classe poderá acessar seus elementos que estão públicos. 

##### Acesso Privado (Private)
    Já no acesso Privado, o atributo ou o método só poderá ser acessado internamente, apenas na classe que o definiu.

##### Acesso Protegido (Protected)
    Somente classes do mesmo pacote podem ter acesso aos atributos e métodos no modo protegido.

### Herança
#### O que é herança?
Uma das grandes vantagens do uso da orientação a objetos é justamente a utilização do conceito de herança. Com a herança o trabalho do programador pode ser otimizado, pois proporciona uma eficiente e segura política de reutilização de códigos, evitando assim o retrabalho. 
A herança nos permite que características que são comuns a diversas classes sejam reunidas em uma única classe base. A partir desta, outras classes herdam suas especificações, e nelas apenas é implementado o que lhes falta, a diferença.

####  Superclasse e Subclasse
Essa classe base, que reúne informações comuns a outras classes, é chamada de Superclasse. Já a Subclasse é uma classe mais específica, que herda as funcionalidades da Superclasse e ainda adiciona funcionalidades específicas que por ventura venha a ter.

####  Herança múltipla
Algumas linguagens de programação suportam a herança múltipla, que permite que uma subclasse tenha capacidade de herdar características de duas ou mais superclasses. Assim, uma única classe pode agrupar atributos e métodos de várias classes. Não é o caso de Java, que não permite essa funcionalidade.

### Polimorfismo
#### O que é polimorfismo?
A palavra Polimorfismo vem do grego, e significa muitas formas. Em orientação a objetos, é a capacidade de uma referência mudar de comportamento de acordo com o objeto a que se refere. Significa que um mesmo tipo de objeto, sob certas condições, pode se comportar de formas distintas ao receber uma mensagem. Ou seja, dependendo do contexto da execução, o sistema decidirá qual método será executado.

#### Sobrecarga de métodos
Sobrecarga de métodos é a propriedade que torna possível a criação de métodos com o mesmo nome, que executam funções diferentes. Ele saberá de qual maneira deverá se comportar através da quantidade de argumentos informada. A sobrecarga de métodos facilita a implementação, pois muitas vezes a mesma operação tem implementações diferentes para cada situação, e ao invés de criarmos nomes para cada uma delas, podemos diferenciar apenas através dos argumentos enviados.

#### Classes e métodos abstratos
Uma classe abstrata é uma superclasse criada apenas para representar entidades e conceitos abstratos, e dela não são gerados objetos, ou seja, a classe abstrata não é instanciada. 
Geralmente criamos uma classe com um propósito específico, porém, a classe abstrata tem outra função, ela é criada com a intenção de que outras classes herdem funcionalidades delas. É definida como um modelo genérico a ser utilizado pelas suas subclasses.
A utilização de classes abstratas nos proporciona uma redução de código e um ganho considerável na utilização do polimorfismo, pois com elas podemos criar métodos mais genéricos que se adaptam a diversos tipos de objetos.

### Interfaces
O Python não possui uma palavra reservada interface. Mesmo sem uma palavra reservada para a mesma, toda classe possui uma interface. Interfaces são os atributos públicos definidos (que em Python são tanto atributos quanto métodos) em uma classe - isso inclui os métodos especiais como __str__() e __add__().

Uma interface vista como um conjunto de métodos para desempenhar um papel é o que os programadores da SmallTalk chamavam de protocolo, e este termo foi disseminado em comunidades de programadores de linguagens dinâmicas. Esse protocolo funciona como um contrato.

Os protocolos são independentes de herança. Uma classe pode implementar vários protocolos, como os mix-ins. Protocolos são interfaces e são definidos apenas por documentação e convenções em linguagens dinâmicas, por isso são considerados informais. Os protocolos não podem ser verificados estaticamente pelo interpretador.

O método __str__(), por exemplo, é esperado que retorne uma representação do objeto em forma de string. Nada impede de fazermos outras coisas dentro do método como deletar algum conteúdo ou fazer algum cálculo; ao invés de retornarmos apenas a string. Mas há um entendimento prévio comum do que este método deve fazer e está presente na documentação do Python. Este é um exemplo onde o contrato semântico é descrito em um manual. Algumas linguagens de tipagem estática, como Java, possuem interfaces em sua biblioteca padrão e podem garantir este contrato em tempo de compilação.

## Arquivos .py
### tipos_primitivos.py
Mostra exemplos de como declarar variaveis em Python.

## Referências
- INFORMÁTICA - POO JAVA. [S. l.: s. n.], 2013.
- https://www.alura.com.br/apostila-python-orientacao-a-objetos/heranca-multipla-e-interfaces