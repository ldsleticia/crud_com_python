# Estudo de CRUD

<p>O objetivo deste projeto é o estudo da realização de CRUD's na linguagem Python com a ferramenta MySQL para a criação
e gerenciamento do banco de dados.</p>

<p>Os dados apresentados são fictícios e não têm relação com a realidade em valores dos produtos aqui apresentados</p>

<p>Para utilizar de forma correta o valor dentro da query do SQL, mesmo após colocar o valor em uma variável, é preciso
colocar entre <i>" "</i> para que o SQL entenda que o que estamos passando ali dentro é uma string e não um valor. 
Segue exemplo:</p>

~~~
produto = "Toddynho"
valor = 3

create_value = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{produto}", {valor})'
~~~

<p>O connection que setamos no código, cria a conexão com o banco de dados. Para que a conexão seja realizada da maneira 
correta, ele precisa de três parâmetros sendo eles o host, user, password e database. A exemplo, usaremos valores 
default:</p>

~~~ 
connection = mysql.connector.connect(
    host="localhost", user="root", password="root", database="bdyoutube"
)
~~~

<p>Após selecionar a connection, criamos um cursor que irá executar os comandos da minha execução. 
Segue exemplo:</p>

~~~
cursor = connection.cursor()
~~~

<p>Para executar os comandos de determinada parte do código que possui uma query, precisamos usar o comando execute:</p>

~~~
cursor.execute(create_value) 
~~~

<p>Após isso, no caso de CREATE é necessário executar o comando de commit para que seja inserida sua alteração no 
banco de dados:</p>

~~~
connection.commit()
~~~

<p>Caso queira ler os dados do banco de dados, o comando fetchall deverá ser executado:</p>

~~~
result = cursor.fetchall()
~~~

Lembrando que é necessário executar o comando <i>cursor.execute(create_value) </i> para que o comando seja executado de 
fato

<p>É importante se lembrar também que após a realização do seu CRUD, é preciso fechar a conexão com o banco de dados e a
execução do cursor. Para isso, utilize os seguintes comandos:</p>

~~~
cursor.close()
connection.close()
~~~