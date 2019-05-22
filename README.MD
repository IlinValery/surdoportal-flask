# Surdoportal Flask Project

## Description
This project is based on task from Bauman University (course TDSP-2019).
## Virtualenv & etc.
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r req.txt
```

## Database
```bash
mysql -u root -p
```

```mysql
CREATE USER 'surdo_user'@'localhost' IDENTIFIED BY 'UserPass123)';
CREATE DATABASE surdoDB CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON surdoDB.* To 'surdo_user'@'localhost';
```
Then execute all scripts from docs/database_create.txt or reset database from surdoDB.sql
```bash
mysqldump -u surdo_user -p surdoDB > surdoDB.sql #save database
mysql -u surdo_user -p surdoDB < surdoDB.sql
```


## Links for description patterns
- Log in was created with the help of [this youtube link](https://www.youtube.com/watch?v=BNdIOnn-wik)
- Visitor Pattern with [this link](https://refactoring.guru/ru/design-patterns/visitor)
- Table Data Gateway Pattern with [this link](http://design-pattern.ru/patterns/table-data-gateway.html)
- Service Layer with [this link](http://design-pattern.ru/patterns/service-layer.html)