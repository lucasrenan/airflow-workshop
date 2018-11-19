DROP DATABASE IF EXISTS crm;
DROP USER IF EXISTS db_owner;
DROP USER IF EXISTS oltp_read;
CREATE USER db_owner PASSWORD 'db_owner';
CREATE USER oltp_read PASSWORD 'oltp_read';

-- Create orders database
CREATE DATABASE crm;
\c crm;
CREATE SCHEMA crm AUTHORIZATION db_owner;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA crm TO db_owner;
GRANT USAGE ON SCHEMA crm TO oltp_read;

CREATE TABLE crm.order_info (
    order_id    INTEGER NOT NULL,
    customer_id VARCHAR(16) NOT NULL,
    create_dtm  TIMESTAMP NOT NULL
);

GRANT SELECT ON ALL TABLES IN SCHEMA crm TO oltp_read;

INSERT INTO crm.order_info (order_id, customer_id, create_dtm) VALUES (6,'CUST-004',current_timestamp - interval '1 day');
INSERT INTO crm.order_info (order_id, customer_id, create_dtm) VALUES (5,'CUST-001',current_timestamp - interval '2 day');
INSERT INTO crm.order_info (order_id, customer_id, create_dtm) VALUES (4,'CUST-002',current_timestamp - interval '2 day');
INSERT INTO crm.order_info (order_id, customer_id, create_dtm) VALUES (3,'CUST-003',current_timestamp - interval '3 days');
INSERT INTO crm.order_info (order_id, customer_id, create_dtm) VALUES (2,'CUST-001',current_timestamp - interval '5 days');
INSERT INTO crm.order_info (order_id, customer_id, create_dtm) VALUES (1,'CUST-001',current_timestamp - interval '6 days');
