SHOW TABLES; -- Para saber quais tabelas existem no SCHEMA

SELECT -- Escolhi a tabela pedido para realiza o inner join por conta que ela que mostra os dados que preciso para fazer o dashboard
	*
FROM 
	pedidos;

SELECT -- Combinando a tabela pedidos, lojas produtos e clientes
	p.ID_Pedido,
    p.Data_Venda,
	l.Loja,
    pr.Nome_Produto,
	pr.Marca_Produto,
    c.Nome,
    c.Sobrenome,
    p.Qtd_Vendida,
    p.Receita_Venda,
    p.Custo_Venda,
    pr.Preco_Unit,
    pr.Custo_Unit,
    l.Gerente,
    l.Endereco,
    l.Num_Funcionarios
FROM
	pedidos p
INNER JOIN
	produtos pr ON pr.ID_Produto=p.ID_Produto
INNER JOIN
	lojas l ON l.ID_Loja=p.ID_Loja
INNER JOIN
	clientes c ON c.ID_Cliente=p.ID_Cliente;