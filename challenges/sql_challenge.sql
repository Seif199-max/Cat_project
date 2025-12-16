SELECT
    O.order_id,
    C.customer_name,
    O.order_total
FROM
    Orders AS O
INNER JOIN
    Customers AS C ON O.customer_id = C.customer_id;