/* é um método que utilizaremos para conectar multiplas tabelas.
As tabelas relacionam-se umas as outras através de chaves.
Uma chave é um conjunto de um ou mais atributos que determinam a unicidade de cada registro.
Temos dois tipos de chaves:
    Chave primária: (PK - Primary Key) é um identificador exclusivo de todas as informações de cada registro dando-lhe unicidade. A chave primária nunca se repetirá.[1]
    Chave Estrangeira: (FK - Foreign Key) é a chave formada através de um relacionamento com a chave primária de outra tabela. Define um relacionamento entre as tabelas
    e pode ocorrer repetidas vezes. Caso a chave primária seja composta na origem, a chave estrangeira também o será.
    CHAVE ESTRANGEIRA: é uma maneira chique de dizer que estamos referenciando a key de uma diferente tabela.

É uma boa forma de dividir as tabelas, em tabelas menores que serão usadas por outras tabelas
Eliminando a redundância de informações dentro no relacionamento das tabela.
E quando for preciso daquela informações buscamos o ID da informação na sua respectiva tabela*/

CREATE TABLE passagens (
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);

/* a partir deste momento em que criamos uma tabela de passageiros 
e referenciamos ela a nossa tabela voos, ela criaram um relacionamento.

de modo básico para sabermos as informações do voo de um determinado passageiro,
teriamos que digitar 2 queries. Pra resolver esse problema existe o JOIN do SQL. 
o JOIN serve para juntar duas tabelas para conseguirmos buscar simultamente nas duas usando apenas uma querie com um unico select
EXEMPLO:

primeiro selecionamos as colunas que queremos
e a primeira tabela
após isso usamos o JOIN para juntar a tabela flights com o passengers
o último passo, é dizer como é o relacionamento dessas tabelas
neste caso, estamos dizendo que flight_id do passengers é o mesmo que
flights_id da tabela flights  
e assim juntamos uma única saida correspondendo a 2 tabelas

Existem alguns tipos de JOIN:

INNER JOIN: o padrão quando usamos JOIN
LEFT JOIN: irá trazer as correspondências estabelecidas, mas também irá trazer as outras linhas 
que correspondem da tabela que está sendo referenciada no lado esquerdo
RIGHT JOIN: o mesmo que o left, entretanto referencia a tabela do lado direito
*/

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights INNER JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights LEFT OUTER JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights RIGHT OUTER JOIN passengers ON passengers.flight_id = flights.id;
