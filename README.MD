# surdoportal Flask project

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
CREATE USER 'surdo_user'@'localhost' IDENTIFIED BY 'user_password'; # UserPass123)
CREATE DATABASE surdoDB CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON surdoDB.* To 'surdo_user'@'localhost';
```

## Link for tutorial
For this project I'm going to build app with [this youtube link](https://www.youtube.com/watch?v=BNdIOnn-wik)

Visitor Pattern: 
- https://youtu.be/axWaE7vTrjU
- https://tavianator.com/the-visitor-pattern-in-python/
- https://github.com/realistschuckle/pyvisitor
- https://www.youtube.com/watch?v=iNt_UAHOvAE
- https://www.youtube.com/watch?v=vc2Ay_IzEwM