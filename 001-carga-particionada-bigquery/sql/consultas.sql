-- O filtro na coluna de particionamento permite partition pruning.
SELECT data_pedido, COUNT(*) AS pedidos, SUM(valor) AS receita
FROM `SEU_PROJETO.dados.pedidos`
WHERE data_pedido BETWEEN DATE '2026-08-01' AND DATE '2026-08-04'
GROUP BY data_pedido
ORDER BY data_pedido;
