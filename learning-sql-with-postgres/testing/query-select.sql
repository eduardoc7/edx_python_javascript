/** O insert seria uma forma de escrever na tabela do banco de dados. E o select
seria uma forma de ler o que há na tabela.
Uma query é um pedido de uma informação ou de um dado, nesse caso, dentro de
uma tabela do banco de dados. Estabelecido através do comando SELECT

Para fazermos isso dentro de um banco de dados, usamos o comando:
SELECT (globing caracter *) FROM (nome da tabela). Listando assim todas as colunas
**/

/* EXEMPLOS DE QUERIES */
/* lendo dados do banco de dados: */
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3; /* todas as linhas da tabela com o id = 3 */
SELECT * FROM flights WHERE origin = 'New york';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' AND duration > 500;
SELECT * FROM flights WHERE destination = 'Paris' OR duration > 500;
SELECT AVG(duration) FROM flights WHERE origin = 'New York'; /* AVG é um função que retorna a media */
SELECT COUNT(*) FROM flights; /* funcão contadora, in this case retorna o numero de linhas da tabela */
SELECT COUNT(*) FROM flights WHERE origin = 'New York';
SELECT MIN(destination) FROM flights; /* e depois => */ SELECT * FROM flights WHERE destination = 245;
SELECT * FROM flights WHERE origin IN ('New York', 'Lima') /* Utilizando ranges */
SELECT * FROM flights WHERE origin LIKE '%a%'; /* isso seria qualquer texto */
SELECT * FROM flights LIMIT 2; /*  limitar a quantidade de linhas a serem exibidas */
SELECT * FROM flights ORDER BY duration ASC; /*  ordenar pela duração */
SELECT * FROM flights ORDER BY duration DESC; /* ordenação reversa */
SELECT origin, COUNT(*) FROM flights GROUP BY origin; /* a saida desse comando irá filtrar todos 
as origens da tabela e contar a quantidade de cada origin que ha dentro da tabela */
SELECT origin, COUNT(*) FROM flights GROUP by origin HAVING COUNT(*) > 1
/* HAVING é uma propriedade específica do GROUP BY, que funciona da mesma forma
 * que o where. Irá contar quantas ordenações existe e criar uma condição > 1 */


/* atualizando dados do banco de dados com o update: */
/* isso é feito com a keyword UPDATE do sql seguido com o nome da tabela: */
UPDATE flights
  SET duration = 430
  WHERE origin = 'New york'
  AND destination = 'London'

/*  deletando dados do banco de dados com o delete */
/* isso é feito com a keyword DELETE do sql seguido do nome da tabela: */
DELETE from flights
  WHERE destination = 'Tokyo'

