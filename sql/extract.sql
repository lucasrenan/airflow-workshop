SELECT
        order_id,
        customer_id
FROM
        crm.order_info
WHERE
        create_dtm >= '{{ds}}' AND create_dtm < '{{tomorrow_ds}}'