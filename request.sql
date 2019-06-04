
CREATE TABLE IF NOT EXISTS `Product` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `barcode` BIGINT NOT NULL,
  `url` VARCHAR(255) NOT NULL,
  `grade` VARCHAR(1) NOT NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Category` (
  `category_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Store` (
  `Store_id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Store_id`))
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Product_Category` (
  `Product_id` INT NOT NULL,
  `Category_id` INT NOT NULL,
  PRIMARY KEY (`Product_id`, `Category_id`),
  INDEX `fk_Product_has_Category_Category1_idx` (`Category_id` ASC) VISIBLE,
  INDEX `fk_Product_has_Category_Product_idx` (`Product_id` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Category_Product`
    FOREIGN KEY (`Product_id`)
    REFERENCES `Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Category_Category1`
    FOREIGN KEY (`Category_id`)
    REFERENCES `Category` (`Category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Product_Store` (
  `Product_id` INT NOT NULL,
  `Store_id` INT NOT NULL,
  PRIMARY KEY (`Product_id`, `Store_id`),
  INDEX `fk_Product_has_Store_Store1_idx` (`Store_id` ASC) VISIBLE,
  INDEX `fk_Product_has_Store_Product1_idx` (`Product_id` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Store_Product1`
    FOREIGN KEY (`Product_id`)
    REFERENCES `Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Store_Store1`
    FOREIGN KEY (`Store_id`)
    REFERENCES `Store` (`Store_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `Favorite` (
  `substitute_product_id` INT NOT NULL,
  `substituted_product_id` INT NOT NULL,
  PRIMARY KEY (`substitute_product_id`, `substituted_product_id`),
  INDEX `fk_Product_has_Product_Product2_idx` (`substituted_product_id` ASC) VISIBLE,
  INDEX `fk_Product_has_Product_Product1_idx` (`substitute_product_id` ASC) VISIBLE,
  CONSTRAINT `fk_Product_has_Product_Product1`
    FOREIGN KEY (`substitute_product_id`)
    REFERENCES `Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Product_Product2`
    FOREIGN KEY (`substituted_product_id`)
    REFERENCES `Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
