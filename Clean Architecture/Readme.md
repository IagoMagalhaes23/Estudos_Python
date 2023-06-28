# Clean Architecture

## Tópicos de interesse:
   - A Clean Architecture (Arquitetura Limpa) é uma forma de desenvolver software, de tal forma que apenas olhando para o código fonte de um programa, você deve ser capaz de dizer o que o programa faz.

## Aplicação — Construiremos um exemplo de caso de uso para criar um Cliente. O Cliente tem os seguintes atributos:
- Primeiro nome
- Sobrenome
- E-mail
- Telefone

O núcleo do projeto de arquitetura limpa é composto do seguinte:
- camada de domínio
- Camada de caso de uso
- Camada do repositório
Vamos começar com a camada de Domínio. No exemplo acima, nosso Cliente é um domínio e precisamos criar uma entidade de domínio para o cliente.

**Domínio** — Usaremos o Pydantic para construir nossa entidade de domínio. Usar o Pydantic é puramente uma preferência e pode ser substituído por uma classe de dados ou uma classe Python simples

Pacotes necessários

    pytest == 7.2 . 1 
    pytest-cov == 4.0 . 0 
    pytest-django == 4.5 . 2 
    pytest-factoryboy == 2.5 . 1 
    pidantico == 1.10 . 5 
    djangorestframework == 3.14 . 0 
    django == 4.1 . 7 
    validador de e-mail == 1.3 . 1

**cliente/domínio/entidades.py**

    ```
    import re 
    import uuid 

    from pydantic import BaseModel, EmailStr, validator 

    from domain.exceptions import InvalidPhoneNumberException 


    class  Customer ( BaseModel ): 
        id : uuid.UUID = Field(default_factory= lambda : uuid.uuid4()) 
        first_name: str
        last_name: str
        email: EmailStr 
        phone: str 

        @validator( "phone" ) 
        def  phone_validation ( cls, v ):
            # Para referência - https://stackoverflow.com/questions/70414211/pydantic-custom-data-type-for-phone-number 
            # -value-error-missing
            regex = r"^(\+)[1-9] [0-9\-\(\)\.]{9,15}$" 
            if v e  não re.search(regex, v, re.I): 
                raise InvalidPhoneNumberException( "Número de telefone inválido." ) 
            return v
    ```

**cliente/domínio/exceções.py**

    ```
    classe  InvalidPhoneNumberException (Exceção): 
        ...
    ```

Portanto, temos nossa entidade de domínio para o cliente configurada. Podemos escrever um teste rápido para verificar se está funcionando conforme o esperado.

**cliente/testes/domínio/test_entities.py**

    ```
    import pytest 
    from pydantic import ValidationError 

    from customer.domain.entities import Customer 
    from customer.domain.exceptions import InvalidPhoneNumberException 

    def  test_customer_create (): 
        customer = Customer( 
            first_name= "test" , 
            last_name= "user" , 
            email= "xyz@example. com" , 
            phone= "+25499919191919"
        ) 

        assert customer 
        assert customer.first_name == "test" 
        assertcustomer.last_name == "user" 
        assert customer.email == "xyz@example.com" 
        assert customer.phone == "+25499919191919" 


    def  test_customer_create_throws_invalid_email_exception (): 

        with pytest.raises(ValidationError) as exc: 
            Customer( 
                first_name= "test" , 
                last_name= "user" , 
                email= "xyz@exampl" , 
                phone= "+25499919191919"
            ) 
        assert exc.value.errors()[ 0 ][ "loc" ][ 0] == "email" 
        assert exc.value.errors()[ 0 ][ "msg" ] == "value is not a valid email address" 


    def  test_customer_create_throws_invalid_phone_exception (): 
        with pytest.raises(InvalidPhoneNumberException) as exc: 
            Customer( 
                first_name= "test" , 
                last_name= "user" , 
                email= "xyz@exampl" , 
                phone= "+25499919"
            ) 
        assert  isinstance (exc.value, InvalidPhoneNumberException)
    ```

Bom. Terminamos nosso primeiro passo. Temos uma entidade configurada e também adicionamos nossos testes.

**Repositório** — Isso é o que vai interagir com sua camada de infraestrutura. Lembre-se de que a estrutura do repositório deve ser independente de infraestrutura. Deixe-me explicar com um pouco de código.

**cliente/repo/base.py**

    ```
    class  AbstractCustomerRepository ( ABC ): 
        @abstractmethod 
        def  insert ( self, cliente: CustomerEntity ) -> Opcional [CustomerEntity]: 
            ... 

        @abstractmethod 
        def  update ( self, cliente: CustomerEntity ) -> CustomerEntity: 
            ... 

        @abstractmethod 
        def  get_by_id ( self, customer_id ) -> Opcional [CustomerEntity]: 
            ... 

        @abstractmethod 
        def  delete ( self, customer_id ): 
            ...

        @abstractmethod 
        def  list ( self ) -> Opcional [ Sequence [CustomerEntity]]: 
            ...
    ```

**cliente/repo/cliente.py**

    ```
    class  CustomerRepository ( AbstractCustomerRepository ): 

        def  insert ( self, obj: CustomerEntity ) -> CustomerEntity: 
            pass 

        def  update ( self, obj: CustomerEntity ) -> CustomerEntity: 
            pass 

        def  get_by_id ( self, customer_id ) -> Opcional [CustomerEntity]: 
            pass 

        def  delete ( self, customer_id ) -> None : 
            pass 

        def  list ( self ) -> Opcional [ Sequence[CustomerEntity]]: 
            aprovado
    ```

Assim, temos uma interface de repositório base onde todas as operações básicas são definidas. Em seguida, definimos uma classe concreta que implementa a interface abstract repo. No nosso caso, vamos salvar nosso cadastro de cliente em nosso modelo Django. Vamos criar um modelo de cliente.

**cliente/modelos.py**

    ```
    class  TimeStampedModel (models.Model): 
        id = models.UUIDField(max_length= 34 , primary_key= True ) 
        class  Meta : 
            abstract = True 

    class  Customer ( TimeStampedModel ): 
        first_name = models.CharField(max_length= 120 ) 
        last_name = models.CharField( max_length= 120 ) 
        email = models.EmailField(unique= True ) 
        phone = models.CharField(max_length= 20 , unique= True ) 

        def  __str__ ( self): 
            return  f" {self.first_name}  {self.last_name} "
    ```

Vamos escrever nossa implementação para o repositório

Implementaremos a operação de inserção para o cliente

**cliente/repo/cliente.py**

    ```
    class  CustomerRepository ( AbstractCustomerRepository ): 

        def  insert ( self, obj: CustomerEntity ) -> CustomerEntity: 
            customer = Customer.objects.create(**obj. dict ()) 
            return CustomerEntity(**customer.__dict__)
    ```

Agora, vamos implementar a operação get_by_id para o cliente

    ```
    class  CustomerRepository (AbstractCustomerRepository): 

        def  insert ( self , obj: CustomerEntity ) -> CustomerEntity:
            customer = Customer.objects.create(**obj.dict()) 
            return CustomerEntity(**customer.__dict__) 

        def  get_by_id ( self , customer_id ) -> CustomerEntity: 
            if customer : = Customer.objects.filter(id=customer_id).first(): 
                return CustomerEntity(**customer.__dict__) 
            else: 
                return None
    ```

Assim, temos a operação insert e get_by_id implementada. Vamos escrever um teste para os métodos

Vamos criar uma classe de fábrica para o cliente

**cliente/testes/fábricas.py**

    ```
    class ClienteFactory (factory.django.DjangoModelFactory): 
        id = fábrica. LazyAttribute (lambda s: uuid. uuid4 ()) 
        first_name = factory. Faker ( "pystr" ) 
        last_name = fábrica. Faker ( "pystr" ) 
        email = fábrica. Faker ( "email" ) 
        telefone = "+9551370038"

        classe Meta: 
            modelo = Cliente
    ```

Vamos registrar esta fábrica em customer/tests/conftest.py

    ```
    from factories import CustomerFactory
    register(CustomerFactory, name="customer_factory")
    ```

Portanto, adicionamos uma classe de fábrica e registramos a classe de fábrica em conftest.py

Vamos criar um fixture para customer_repo pois iremos utilizá-lo em nossos testes.

**cliente/testes/conftest.py**

    ```
    from customer.repo.customer import CustomerRepository 
    @pytest.fixture 
    def  customer_repo (): 
        return CustomerRepository()
    ```

Agora, nosso código clichê está pronto para criarmos os testes para o repo.

**cliente/testes/repo/test_customer_repo.py**

    ```
    import pytest 

    from customer.domain.entities import CustomerEntity 

    pytestmark = pytest.mark.django_db 


    def  test_customer_repository_insert ( customer_factory, customer_repo ): 
        customer_data = customer_factory.build() 
        customer_entity = CustomerEntity(**customer_data.__dict__) 
        customer_repo.insert(customer_entity) 
        customer_obj = customer_repo.get_by_id(customer_entity. id ) 
        assert customer_obj. id == cliente_entidade. id 

    def  test_customer_repository_get_by_id ( customer_factory, customer_repo ):
        customer_data = customer_factory() 
        customer = customer_repo.get_by_id(customer_data. id ) 
        afirmar cliente 
        afirmar cliente. id == dados_cliente. id 
        assert customer.email == customer_data.email
    ```

Portanto, adicionamos os testes para insert e get_by_id. Em seguida, implementaremos a atualização

    ```
    class CustomerRepository (AbstractCustomerRepository): 

        def insert (self, obj: CustomerEntity) -> CustomerEntity: 
            customer = Customer.objects. create (**obj. dict ()) 
            return CustomerEntity (**customer.__dict__) 

        def update (self, obj: CustomerEntity): 
            Customer.objects. filtro (id=obj.id). atualização (**obj. dict ()) 
            cliente = Cliente.objetos. get (id=obj.id) 
            return CustomerEntity (**customer.__dict__) 

        def get_by_id(self, customer_id) -> Opcional[CustomerEntity]: 
            if customer := Customer.objects. filtro (id=customer_id). first (): 
                return CustomerEntity (**customer.__dict__) 
            else: 
                return None
    ```

Agora, vamos escrever um teste para a atualização

    ```
    def  test_customer_repository_update ( customer_factory, customer_repo ): 
        customer_data = customer_factory() 
        assert customer_data.first_name != "Test_1" 
        assert customer_data.last_name != "User_1" 
        assert customer_data.email != "abc@example.com"

        customer_entity = CustomerEntity(** customer_data.__dict__) 
        customer_entity.first_name = "Test_1"
        customer_entity.last_name = "User_1"
        customer_entity.email = "abc@example.com"

        customer = customer_repo.update(customer_entity) 
        afirma cliente 
        afirma cliente.id == cliente_entidade. id 
        assert customer.first_name == "Test_1" 
        assert customer_entity.last_name == "User_1" 
        assert customer_entity.email == "abc@example.com"
    ```

As duas últimas implementações que temos são obter todos os clientes e excluir um cliente. vamos mergulhar

    ```
    class  CustomerRepository (AbstractCustomerRepository): 

        def  insert ( self , obj: CustomerEntity ) -> CustomerEntity:
            customer = Customer.objects.create(**obj.dict()) 
            return CustomerEntity(**customer.__dict__) 

        def  update ( self , obj : CustomerEntity ) -> CustomerEntity:
            Customer.objects.filter(id=obj.id).update(**obj.dict()) 
            customer = Customer.objects.get(id=obj.id) 
            return CustomerEntity(**customer .__dict__) 

        def  get_by_id ( self, customer_id ) -> Opcional[CustomerEntity]: 
            if customer : = Customer.objects.filter(id=customer_id).first(): 
                return CustomerEntity(**customer.__dict__) 
            else: 
                return None 

        def  delete ( self , customer_id ) - > Nenhum:
            Customer.objects.get(id=customer_id).delete() 

        def  list ( self ) -> Opcional[Sequência[CustomerEntity]]: 
            clientes = Customer.objects.all() 
            return [CustomerEntity(**customer.__dict__ ) para cliente em clientes]
    ```

Agora, vamos adicionar testes para os métodos delete e list.

    ```
    def  test_customer_repository_delete ( customer_factory, customer_repo ): 
        customer_data = customer_factory() 
        customer_repo.delete(customer_data. id ) 
        customer = customer_repo.get_by_id(customer_data. id ) 
        assert  not customer 


    def  test_customer_repository_list ( customer_factory, customer_repo ): 
        customer_factory(phone= "+9551370037" ) 
        customer_factory(phone= "+9551370038" ) 
        customer_factory(phone= "+9551370039" ) 

        clientes = customer_repo. lista() 
        afirmar clientes 
        afirmar  len (clientes) == 3
    ```

Visão final do repositório e dos testes.

**cliente/repo/cliente.py**

    ```
    class  CustomerRepository (AbstractCustomerRepository): 

        def  insert ( self , obj: CustomerEntity ) -> CustomerEntity:
            customer = Customer.objects.create(**obj.dict()) 
            return CustomerEntity(**customer.__dict__) 

        def  update ( self , obj : CustomerEntity ): 
            Customer.objects.filter(id=obj.id).update(**obj.dict()) 
            customer = Customer.objects.get(id=obj.id) 
            return CustomerEntity(**customer.__dict__) 

        def  get_by_id ( self , customer_id) -> Opcional[CustomerEntity]: 
            if customer : = Customer.objects.filter(id=customer_id).first(): 
                return CustomerEntity(**customer.__dict__) 
            else: 
                return None 

        def  delete ( self , customer_id ) -> None :
            Customer.objects.get(id=customer_id).delete() 

        def  list ( self ) -> Opcional[Sequência[CustomerEntity]]: 

            clientes = Customer.objects.all() 
            return [CustomerEntity(**customer.__dict__) para cliente em clientes]
    ```

**cliente/testes/repo/test_customer_repo.py**

    ```
    def  test_customer_repository_insert ( customer_factory, customer_repo ): 
        customer_data = customer_factory.build() 
        customer_entity = CustomerEntity(**customer_data.__dict__) 
        customer_repo.insert(customer_entity) 
        customer_obj = customer_repo.get_by_id(customer_entity. id ) 
        assert customer_obj 
        assert customer_obj. id == cliente_entidade. id 


    def  test_customer_repository_get_by_id ( customer_factory, customer_repo ): 
        customer_data = customer_factory() 
        customer = customer_repo.get_by_id(customer_data. id )
        afirmar cliente 
        afirmar cliente. id == dados_cliente. id 
        assert customer.email == customer_data.email 


    def  test_customer_repository_update ( customer_factory, customer_repo ): 
        customer_data = customer_factory() 
        assert customer_data.first_name != "Test_1" 
        assert customer_data.last_name != "User_1" 
        assert customer_data.email != "abc@ exemplo.com"

        customer_entity = CustomerEntity(**customer_data.__dict__) 
        customer_entity.first_name = "Test_1"
        customer_entity.
        customer_entity.email = "abc@example.com"

        customer = customer_repo.update(customer_entity) 
        afirmar cliente 
        afirmar cliente. id == cliente_entidade. id 
        assert customer.first_name == "Test_1" 
        assert customer_entity.last_name == "User_1" 
        assert customer_entity.email == "abc@example.com" 


    def  test_customer_repository_delete ( customer_factory, customer_repo ): 
        customer_data = customer_factory() 
        customer_repo.delete(customer_data . id )
        customer = customer_repo.get_by_id(customer_data. id ) 
        assert  not customer 


    def  test_customer_repository_list ( customer_factory, customer_repo ): 
        customer_factory(phone= "+9551370037" ) 
        customer_factory(phone= "+9551370038" ) 
        customer_factory(phone= "+9551370039" ) 

        clientes = customer_repo. lista () 
        afirmar clientes 
        afirmar  len (clientes) == 3
    ```

Até agora, cobrimos dois dos principais componentes da arquitetura limpa
- Domínio.
- Repositório.

Agora, precisamos implementar a lógica de negócios que estará nos casos de uso. O caso de uso também é semelhante ao módulo de serviços.

**cliente/use_cases/base.py**

    ```
    from abc import ABC , 

    classe  abstractmethod AbstractCustomerUseCase ( ABC ): 
        @abstractmethod 
        def  get_by_id ( self , customer_id ): 
            ... 

        @abstractmethod 
        def  insert ( self , cliente: CustomerEntity ): 
            ... 

        @abstractmethod 
        def  update ( self , cliente: CustomerEntity ): 
            ... 

        @abstractmethod 
        def  delete ( self , customer_id): 
            ... 

        @abstractmethod 
        def  list ( self ): 
            ...
    ```

Agora, vamos criar a implementação concreta para este caso de uso para as operações do cliente.

**cliente/user_cases/cliente.py**

    ```
    class  CustomerUseCase (AbstractCustomerUseCase): 
        def  __init__ ( self , customer_repo ): 
            self .repo = customer_repo 

        def  get_by_id ( self , customer_id ): 
            return  self .repo.get_by_id(customer_id) 

        def  insert ( self , cliente: CustomerEntity ): 
            return  self .repo .insert(cliente) 

        def  update ( self , cliente: CustomerEntity ): 
            return  self.repo.update(cliente) 

        def  delete ( self , customer_id ): 
            self .repo.delete(customer_id) 

        def  list ( self ): 
            return  self .repo.list()
    ```

Ótimo, vamos adicionar alguns testes para nosso caso de uso

**cliente/testes/use_cases/test_customer.py**

    ```
    pytestmark = pytest.mark.django_db

    def  test_create_customer_use_case ( customer_factory, customer_repo ): 
        customer_use_case = CustomerUseCase(customer_repo=customer_repo) 
        customer_data = customer_factory.build() 
        customer_entity = CustomerEntity(**customer_data.__dict__) 
        customer = customer_use_case.insert(customer_entity) 
        afirmar cliente 
        assert customer.first_name == customer_data.first_name 
        assert customer.email == customer_data.email 
        assert customer.phone == customer_data.phone 


    def  test_update_customer_use_case ( customer_factory, customer_repo ):
        customer_use_case = CustomerUseCase(customer_repo=customer_repo) 
        customer_data = customer_factory() 
        customer_entity = CustomerEntity(**customer_data.__dict__) 
        customer_entity.first_name = "Test_1"
        customer_entity.last_name = "User_1"
        customer_entity.email = "abc@example.com"

        customer = customer_use_case.update(customer_entity) 
        assert customer 
        assert customer.first_name == "Test_1" 
        assert customer.last_name == "User_1" 
        assert customer.email == "abc@example.com" 


    def  test_get_customer_use_case (customer_factory, customer_repo ): 
        customer_use_case = CustomerUseCase(customer_repo=customer_repo) 
        customer_data = customer_factory() 
        customer = customer_use_case.get_by_id(customer_data. id ) 
        assert customer 
        assert customer.first_name == customer_data.first_name 
        assert customer.last_name == customer_data.last_name 
        assert customer .email == customer_data.email 


    def  test_list_customer_use_case ( customer_factory, customer_repo ): 
        customer_use_case = CustomerUseCase(customer_repo=customer_repo) 
        customer_factory(phone= "+9551370037" )
        customer_factory(phone= "+9551370038" ) 
        customer_factory(phone= "+9551370039" ) 
        customer = customer_use_case. list () 
        assert customer 
        assert  len ​​(customer) == 3 


    def  test_delete_customer_use_case ( customer_factory, customer_repo ): 
        customer_use_case = CustomerUseCase(customer_repo=customer_repo) 

        customer_data = customer_factory() 
        customer_use_case.delete(customer_data. id ) 

        customer = customer_use_case.get_by_id(customer_data. id ) 
        assert not customer
    ```

Incrível, concluímos todas as três camadas da Clean Architecture até agora. Adicionamos a camada de domínio que é nossa CustomerEntity. Em seguida, adicionamos a camada de repositório que é nosso CustomerRepository e, finalmente, adicionamos nossa camada UseCase, que é nossa classe CustomerUseCase.

Até agora conseguimos construir os componentes isoladamente e testá-los sem nenhum acoplamento. A classe de caso de uso para o cliente faz um repositório no método __init__ e é aí que está a verdadeira mágica. É aqui que podemos alternar facilmente os repositórios que interagem com o armazenamento em tempo de execução, se necessário. A estrutura do repositório base determina que qualquer outra classe de repositório concreta deve implementar os métodos declarados, e é por isso que esse design é tão incrível.

A última e última camada são as visualizações ou manipuladores ou rotas…

Vou demonstrar os pontos de vista, mas é bastante simples.

Vamos adicionar nossos serializadores…

**cliente/manipuladores/serializers.py**

    ```
    class  CustomerBaseSerializer (serializers.ModelSerializer): 
        class  Meta : 
            model = Customer 
            fields = [ "first_name" , "last_name" , "email" , "phone" , ] 


    class  CustomerCreateSerializer ( CustomerBaseSerializer ): 
        ... 


    class  CustomerPutOrPatchSerializer ( CustomerBaseSerializer ): 
        . .. 


    class  CustomerDetailSerializer ( CustomerBaseSerializer ): 
        ... 


    class  CustomerListSerializer (CustomerBaseSerializer ): 
        class  Meta : 
            model = 
            Campos do cliente = CustomerBaseSerializer.Meta.fields + [ "id" , ]
    ```

**cliente/manipuladores/web.py**

    ```
    class  CustomerAPIView (APIView): 
        def post(self, request): 
            customer_serializer = CustomerCreateSerializer( data =request. data ) 
            if not customer_serializer.is_valid(): 
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            customer_entity = CustomerEntity(* *customer_serializer.validated_data) 
            customer_repo = CustomerRepository() 
            customer = CustomerUseCase(customer_repo).insert(customer_entity) 
            return Response(customer.dict(), status=status.HTTP_201_CREATED) 

        def put(self, request, customer_id): 
            customer_repo = CustomerRepository( )
            customer = CustomerUseCase(customer_repo).get_by_id(customer_id) 
            if not customer: 
                return Response( 
                    { "message" : "Customer with that Id does not exist" }, 
                    status=status.HTTP_400_BAD_REQUEST, 
                ) 
            else : 
                customer_serializer = CustomerCreateSerializer( data =request. data ) 
                se não customer_serializer.is_valid(): 
                    return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
                customer_entity = CustomerEntity(**customer_serializer.validated_data)
                customer_entity.id = customer.id 
                customer_repo = CustomerRepository() 
                customer = CustomerUseCase(customer_repo).update(customer_entity) 
                return Response(customer.dict(), status=status.HTTP_200_OK) 

        def get (self, request, customer_id=None): 
            customer_repo = CustomerRepository() 
            if not customer_id: 
                if customers := CustomerUseCase(customer_repo).list(): 
                    customers_dict = [customer.__dict__ for customer in customers] 
                else : 
                    customers_dict = {} 
                return Response( 
                    {
                        "message" : customer_dict, 
                    }, 
                    status=status.HTTP_200_OK, 
                ) 
            else : 
                if customer := CustomerUseCase(customer_repo).get_by_id(customer_id): 
                    return Response(customer.dict(), status=status.HTTP_200_OK) 
                else : 
                    return Response ( 
                        { "mensagem" : "Cliente com esse Id não existe" }, 
                        status=status.HTTP_400_BAD_REQUEST, 
                    )
    ```

Então, o que está acontecendo nas visualizações/manipuladores/rotas?

1. A rota ou camada de visualização é a camada de apresentação.
2. Ele recebe um pedido de dados.
3. Os dados são passados ​​para os serializadores.
4. O serializador então retorna um valided_data que é um dicionário.
5. O dicionário é então mapeado para a entidade de domínio.
6. O objeto de Caso de Uso de Cliente Concreto é instanciado com uma instância de repositório concreta.
7. Em seguida, invocamos o método correto com base no método de rota. por exemplo, get_by_id, list, insert ou delete.
8. O caso de uso chama o método de repositório e retorna os dados.
9. Os dados retornados são então convertidos em um dict e passados ​​para a classe DRF Response com o status_code correto.

Pontos importantes a serem observados:

1. A estrutura limpa cria uma clara separação de interesses.
2. Ele separa as preocupações de infraestrutura do código do aplicativo.
3. O código desacoplado é mais fácil de manter e dimensionar.
4. Testar cada componente ou camada é fácil, pois não é acoplado a outras camadas.
5. A injeção de dependência e o IOC estão no centro da implementação acima.

## Referências:
- https://medium.com/@surajit.das0320/understanding-clean-architecture-in-python-deep-dive-on-the-code-17141dc5761a