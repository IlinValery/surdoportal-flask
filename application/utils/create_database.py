from application.gateway.connection import *
import time
from tqdm import tqdm
requests_database = []

# user:
requests_database.append({"user" : """CREATE TABLE `surdoDB`.`user` (
  `iduser` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(225) NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `password` VARCHAR(225) NOT NULL,
  `is_superuser` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`iduser`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC));
"""})

# log:
requests_database.append({"log" : """CREATE TABLE `surdoDB`.`log` (
  `idlog` INT NOT NULL AUTO_INCREMENT,
  `date_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user` INT(11) NOT NULL,
  `table` VARCHAR(45) NOT NULL,
  `element` INT(11) NOT NULL,
  `action` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idlog`));"""})

# department:
requests_database.append({"department" : """CREATE TABLE `surdoDB`.`department` (
  `iddepartment` INT NOT NULL AUTO_INCREMENT,
  `caption` VARCHAR(225) NOT NULL,
  `initials` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`iddepartment`));"""})

# discipline:
requests_database.append({"discipline" : """CREATE TABLE `surdoDB`.`discipline` (
  `iddiscipline` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(225) NOT NULL,
  `semester` INT NOT NULL,
  `department_id` INT(11) NOT NULL,
  PRIMARY KEY (`iddiscipline`),
  INDEX `department_id_fk` (`department_id` ASC),
  CONSTRAINT `department_id_fk`
    FOREIGN KEY (`department_id`)
    REFERENCES `surdoDB`.`department` (`iddepartment`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);"""})

# teacher:
requests_database.append({"teacher" : """CREATE TABLE `surdoDB`.`teacher` (
  `idteacher` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(145) NOT NULL,
  `department_id` INT(11) NOT NULL,
  PRIMARY KEY (`idteacher`),
  INDEX `department_id_teacher_idx` (`department_id` ASC),
  CONSTRAINT `department_id_teacher`
    FOREIGN KEY (`department_id`)
    REFERENCES `surdoDB`.`department` (`iddepartment`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""})

# term_base:
requests_database.append({"term_base" : """CREATE TABLE `surdoDB`.`term` (
  `idterm` INT NOT NULL AUTO_INCREMENT,
  `caption` VARCHAR(145) NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `lesson` INT NOT NULL,
  `teacher` INT(11) NOT NULL,
  `discipline` INT(11) NOT NULL,
  `image_path` VARCHAR(200) NOT NULL,
  `creator` INT(11) NOT NULL,
  `changed` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_shown` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idterm`));"""})

# term_keys:
requests_database.append({"term add FK" : """
ALTER TABLE `surdoDB`.`term`
ADD INDEX `fk_teacher_idx` (`teacher` ASC),
ADD INDEX `fk_discipline_idx` (`discipline` ASC),
ADD INDEX `fk_creator_idx` (`creator` ASC);
"""})
# term_keys2:
requests_database.append({"term attach FK" : """
ALTER TABLE `surdoDB`.`term`
ADD CONSTRAINT `fk_teacher`
  FOREIGN KEY (`teacher`)
  REFERENCES `surdoDB`.`teacher` (`idteacher`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
ADD CONSTRAINT `fk_discipline`
  FOREIGN KEY (`discipline`)
  REFERENCES `surdoDB`.`discipline` (`iddiscipline`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
ADD CONSTRAINT `fk_creator`
  FOREIGN KEY (`creator`)
  REFERENCES `surdoDB`.`user` (`iduser`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
"""})

# media:
requests_database.append({"media" : """CREATE TABLE `surdoDB`.`media` (
  `idmedia` INT NOT NULL AUTO_INCREMENT,
  `type` INT NOT NULL,
  `youtube_id` VARCHAR(45) NOT NULL,
  `term` INT(11) NOT NULL,
  PRIMARY KEY (`idmedia`),
  INDEX `fk_term_idx` (`term` ASC),
  CONSTRAINT `fk_term`
    FOREIGN KEY (`term`)
    REFERENCES `surdoDB`.`term` (`idterm`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);"""})

def create_tables():
    connection = DatabaseConnection()
    cursor = connection.db.cursor()
    count = len(requests_database)
    for request in tqdm(requests_database):
        for key in request.keys():
            #print(key, request[key])
            req = request[key].replace("\n","")
            try:
                cursor.execute(request[key])
                connection.db.commit()
                result = "Table {0} created successfully!".format(key)
            except IntegrityError:
                result =  cursor.fetchall()
            print(result)
        time.sleep(1)

def drop_all_tables():
    connection = DatabaseConnection()
    cursor = connection.db.cursor()
    req = "DROP TABLE `surdoDB`.`department`, `surdoDB`.`discipline`, `surdoDB`.`log`, `surdoDB`.`media`, `surdoDB`.`teacher`, `surdoDB`.`term`, `surdoDB`.`user`;"
    cursor.execute(req)
    connection.db.commit()
    res = cursor.fetchall()
    if len(res) == 0:
        print("Success!")
    else:
        print(res)
