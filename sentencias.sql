use db_snc;

describe erp_employee;
select * from erp_employee;

delete from erp_product WHERE ID > 0;
delete from erp_category WHERE ID > 0;

INSERT INTO erp_category (name) VALUES ('Prueba');
SELECT * FROM erp_category ORDER BY id;
ALTER TABLE erp_category AUTO_INCREMENT = 1;
ALTER TABLE erp_product AUTO_INCREMENT = 1;
SELECT * FROM erp_product

