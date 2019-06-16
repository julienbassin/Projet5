CREATE TABLE IF NOT EXISTS Favorites (
        id_product BIGINT REFERENCES Products(barcode),
        id_substitute BIGINT REFERENCES Products(barcode),
        PRIMARY KEY (id_product, id_substitute));

CREATE TABLE IF NOT EXISTS Products (
                          barcode BIGINT UNSIGNED UNIQUE PRIMARY KEY,
                          name_product VARCHAR(150),
                          url VARCHAR(255),
                          grade CHAR(1));

CREATE TABLE IF NOT EXISTS Categories (
                          id BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          category VARCHAR(125) UNIQUE);

CREATE TABLE IF NOT EXISTS Stores (
                          id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          store VARCHAR(150) UNIQUE);

CREATE TABLE IF NOT EXISTS Products_categories (
                          id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_id BIGINT REFERENCES Products(barcode),
                          category_id MEDIUMINT REFERENCES Category(id));

CREATE TABLE IF NOT EXISTS Products_stores (
                          id MEDIUMINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                          product_id BIGINT REFERENCES Products(barcode),
                          store_id MEDIUMINT REFERENCES Stores(id));

