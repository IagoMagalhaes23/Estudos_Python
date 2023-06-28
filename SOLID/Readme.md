# SOLID

## Tópicos objetivos:
   - O Solid possui cinco princípios considerados como boas práticas no desenvolvimento de software que ajudam os programadores a escrever os códigos mais limpos, separando as responsabilidades, diminuindo acoplamentos, facilitando na refatoração e estimulando o reaproveitamento do código.

## O que é SOLID?
SOLID é um acrônimo criado por Michael Feathers , após observar que cinco princípios da orientação a objetos e design de código — Criados por Robert C. Martin ( aka Uncle Bob) e pensado no artigo The Principles of OOD — poderia se encaixar nesta palavra.

## SOLID: Os 5 princípios da POO
S — Princípio da Responsabilidade Única (Princípio da responsabilidade única)
O — Princípio Aberto-Fechado (Princípio Aberto-Fechado)
L — Princípio da substituição de Liskov (Princípio da substituição de Liskov)
I — Princípio da Segregação da Interface
D — Princípio da Inversão da Dependência (Princípio da inversão da dependência)
Esses princípios ajudam o programador a escrever códigos mais limpos , separando responsabilidades, acompanhando-os, facilitando na refatoração e estimulando o reaproveitamento do código.

## 1. SRP - Princípio de Responsabilidade Única:
Princípio da Responsabilidade Única — Uma classe deve ter um, e somente um, motivo para mudar.

Esse princípio declara que uma classe deve ser especializada em um único assunto e possuir apenas uma responsabilidade dentro do software, ou seja, a classe deve ter uma única tarefa ou ação para executar.

Quando estamos aprendendo programação orientada a objetos, sem sabermos, damos a uma classe mais de uma responsabilidade e acabamos criando classes que fazem de tudo — God Class* . Num primeiro momento isso pode parecer eficiente, mas como as responsabilidades acabam se misturando, quando há necessidade de realizar mudanças nessa classe, será difícil modificar uma dessas responsabilidades sem comprometer as outras. Toda alteração acaba sendo orientada com um certo nível de interação em nosso sistema — principalmente se não existirem testes automatizados!

A violação do Princípio da Responsabilidade Única pode gerar alguns problemas, sendo eles:
- Falta de coesão — uma classe não deve assumir responsabilidades que não são suas;
- Alto abrigo — Mais responsabilidades geradas um nível maior de dependências, deixando o sistema engessado e frágil para alterações;
- Dificuldades na implementação de testes concluídos — É difícil de “mockar” esse tipo de classe;
- Dificuldades para reaproveitar o código;

O princípio da responsabilidade única não se limita somente a classes, ele também pode ser aplicado em métodos e funções, ou seja, tudo que é responsável por executar uma ação, deve ser responsável por apenas aquilo que se propõe a fazer.

Considera o SRP um dos princípios mais importantes, ele acaba sendo a base para outros princípios e padrões porque aborda temas como acomodação e coesão, características que todo código orientado a objetos deve ter.

Aplicando esse princípio, automaticamente você estará escrevendo um código mais limpo e de fácil manutenção! Se você tem interesse nesse assunto, recomendo a leitura das boas práticas para escrever códigos positivos.

## 2. OCP — Princípio Aberto-Fechado:
Princípio Aberto-Fechado — Objetos ou entidades devem estar abertos para extensão, mas fechados para modificados , ou seja, quando novos comportamentos e recursos precisam ser adicionados no software, estendidos e não alterar o código fonte original.

## 3. LSP— Princípio da Substituição de Liskov :
Princípio da substituição de Liskov — Uma classe derivada deve ser substituível por sua classe base .

O princípio da substituição de Liskov foi apresentado por Barbara Liskov em sua conferência “Data abstraction” em 1987. A definição formal de Liskov diz que:

    Se para cada objeto o1 do tipo S há um objeto o2 do tipo T de forma que, para todos os programas P definidos em termos de T, o comportamento de P é inalterado quando o1 é substituído por o2 então S é um subtipo de T

Um exemplo dessa definição mais simples e de fácil compreensão. Série:

    se S é um subtipo de T, então os objetos do tipo T, em um programa, podem ser substituídos pelos objetos do tipo S sem que seja necessário alterar as propriedades deste programa. — Wikipédia.

Exemplos de violação do LSP:

- Sobrescrever/implementar um método que não faz nada;
- Lançar uma exceção inesperada;
- Retornar valores de tipos diferentes da classe base;

Para não violar o Princípio de Substituição de Liskov, além de estruturar muito bem as suas abstrações, em alguns casos, você precisará usar a injeção de dependência e também usar outros princípios do SOLID, como por exemplo, o Princípio Aberto-Fechado e o Princípio de Segregação de Interface — será satisfatório no próximo tópico.

Seguir o LSP nos permite usar o polimorfismo com mais confiança. Podemos chamar nossas classes derivadas referindo-se à sua classe base sem preocupações com resultados inesperados.

## 4. ISP — Princípio de Segregação de Interface:
Princípio da Segregação da Interface — Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar.

Esse princípio basicamente diz que é melhor criar interfaces mais específicas ao compor de termos uma única interface genérica.

## 5. DIP - Princípio de Inversão de Dependência:
Princípio da Inversão de Dependência — Dependa de abstrações e não de implementações.

De acordo com Uncle Bob, esse princípio pode ser definido da seguinte forma:

    1. Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender da abstração.

    2. As abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.

No contexto da programação orientada a objetos, é comum que as pessoas confundem a Inversão de Dependência com a Injeção de Dependência , porém são coisas distintas, mas que relacionam entre si com um proposito em comum, deixam o código desacoplado.

**Importante: Inversão de Dependência não é igual a Injeção de Dependência, fique ciente disso ! AI nversão de Dependência é um princípio (Conceito) e Injeção de Dependência é um padrão de projeto (Design Pattern).**

## Referências
- https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530