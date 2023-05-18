# Extração e Tratamento de Dados

## Tópicos objetivos:
   - A extração de dados é o processo de coleta ou recuperação de tipos diferentes de dados de uma variedade de fontes, muitos dos quais podem estar mal organizados ou completamente desestruturados.
   - Obter os dados que serão analisados
   - Tratar os dados obtidos, transformando-os, alterando sua estrutura e valores a fim de deixar a base de dados mais coerente e garantir que os dados que serão trabalhados estejam nas melhores condições para serem analisados
   - Utilizar as bibliotecas Pandas e Scikit-learn para tratar os dados

## Estudo da arte

### O que é ETL?
Extrair, transformar e carregar (ETL) é o processo que as organizações orientadas a dados usam para coletar dados de várias fontes e reuni-los para dar suporte à descoberta, à geração de relatórios, à análise e à tomada de decisões.

As origens de dados podem ser muito diversas em tipo, formato, volume e confiabilidade, de modo que os dados precisam ser processados para serem úteis quando reunidos. Os armazenamentos de dados de destino podem ser bancos de dados, data warehouses ou data lakes, dependendo das metas e da implementação técnica.

### As três etapas distintas do ETL
#### Extrair
Durante a extração, o ETL identifica os dados e os copia de suas origens, de forma que possa transportar os dados para o armazenamento de dados de destino. Os dados podem vir de fontes estruturadas e não estruturadas, incluindo documentos, emails, aplicações de negócios, bancos de dados, equipamentos, sensores, terceiros e muito mais.

#### Transformar
Como os dados extraídos são brutos em sua forma original, eles precisam ser mapeados e transformados para prepará-los para o armazenamento de dados eventual. No processo de transformação, o ETL valida, autentica, desduplica e/ou agrega os dados de formas que tornam os dados resultantes confiáveis e consultáveis.

#### Carregar
O ETL move os dados transformados para o armazenamento de dados de destino. Esta etapa pode implicar o carregamento inicial de todos os dados de origem ou pode ser o carregamento de alterações incrementais nos dados de origem. Você pode carregar os dados em tempo real ou em lotes programados.

### Casos de uso ETL
O processo ETL é fundamental para muitos setores por causa de sua capacidade de ingerir dados de forma rápida e confiável em data lakes para ciência de dados e análise, criando modelos de alta qualidade. As soluções ETL também podem carregar e transformar dados transacionais em escala para criar uma visão organizada de grandes volumes de dados. Isso permite que as empresas visualizem e prevejam tendências do setor. Vários setores contam com o ETL para permitir insights acionáveis, tomada de decisões rápida e maior eficiência.

#### Serviços financeiros
As instituições de serviços financeiros coletam grandes quantidades de dados estruturados e não estruturados para obter insights sobre o comportamento do consumidor. Esses insights podem analisar o risco, otimizar os serviços financeiros dos bancos, melhorar as plataformas online e até mesmo fornecer caixas eletrônicos com dinheiro.

#### Setores de petróleo e gás
Os setores de petróleo e gás usam soluções ETL para gerar previsões sobre uso, armazenamento e tendências em áreas geográficas específicas. O ETL funciona para reunir o máximo de informações possível de todos os sensores de um site de extração e processar essas informações para facilitar a leitura.

#### Automotivo
As soluções de ETL permitem que as concessionárias e os fabricantes entendam os padrões de vendas, calibrem suas campanhas de marketing, reabram o estoque e acompanhem os leads dos clientes.

#### Telecomunicações
Com o volume e a variedade sem precedentes de dados produzidos hoje, os provedores de telecomunicações contam com soluções ETL para melhor gerenciar e entender esses dados. Uma vez processados e analisados esses dados, as empresas podem usá-los para melhorar a publicidade, a mídia social, o SEO, a satisfação do cliente, a lucratividade e muito mais.

#### Assistência Médica
Com a necessidade de reduzir custos e também melhorar a assistência médica, o setor de assistência médica emprega soluções ETL para gerenciar registros de pacientes, coletar informações de seguros e atender a requisitos regulatórios em evolução.

#### Ciências biológicas
Os laboratórios clínicos contam com soluções ETL e inteligência artificial (IA) para processar vários tipos de dados que estão sendo produzidos por instituições de pesquisa. Por exemplo, colaborar no desenvolvimento de vacinas requer que grandes quantidades de dados sejam coletados, processados e analisados.

#### Setor público
Com o surgimento dos recursos de Internet das Coisas (IoT), as cidades inteligentes estão usando o ETL e o poder da IA para otimizar o tráfego, monitorar a qualidade da água, melhorar o estacionamento e muito mais.

## Referências
- https://www.oracle.com/br/integration/what-is-etl/
- https://youtu.be/ANkrrduTtu0