/** O insert seria uma forma de escrever na tabela do banco de dados. E o select
seria uma forma de ler o que há na tabela.
Uma query é um pedido de uma informação ou de um dado, nesse caso, dentro de
uma tabela do banco de dados. Estabelecido através do comando SELECT

Para fazermos isso dentro de um banco de dados, usamos o comando:
SELECT (globing caracter *) FROM (nome da tabela). Listando assim todas as colunas
**/

/* EXEMPLOS DE QUERIES */
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


