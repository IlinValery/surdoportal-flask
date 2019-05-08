# This script for create tables in our database

#table user
# CREATE TABLE `surdoDB`.`user` (
#   `iduser` INT NOT NULL AUTO_INCREMENT,
#   `email` VARCHAR(225) NOT NULL,
#   `first_name` VARCHAR(100) NOT NULL,
#   `last_name` VARCHAR(100) NOT NULL,
#   `password` VARCHAR(225) NOT NULL,
#   `is_superuser` TINYINT(1) NOT NULL DEFAULT 0,
#   PRIMARY KEY (`iduser`),
#   UNIQUE INDEX `email_UNIQUE` (`email` ASC));

# CREATE TABLE `surdoDB`.`department` (
#   `iddepartment` INT NOT NULL,
#   `caption` VARCHAR(45) NULL,
#   `initials` VARCHAR(45) NULL,
#   PRIMARY KEY (`iddepartment`));