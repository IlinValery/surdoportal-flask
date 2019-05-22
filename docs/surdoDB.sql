-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: surdoDB
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `iddepartment` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(225) NOT NULL,
  `initials` varchar(45) NOT NULL,
  PRIMARY KEY (`iddepartment`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (8,'Системы обработки информации и управления','ИУ5'),(9,'Информационная безопасность','ИУ8'),(10,'Материаловедение','МТ8'),(11,'Компьютерные системы автоматизации производства','РК9');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discipline`
--

DROP TABLE IF EXISTS `discipline`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discipline` (
  `iddiscipline` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(225) NOT NULL,
  `semester` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`iddiscipline`),
  KEY `department_id_fk` (`department_id`),
  CONSTRAINT `department_id_fk` FOREIGN KEY (`department_id`) REFERENCES `department` (`iddepartment`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discipline`
--

LOCK TABLES `discipline` WRITE;
/*!40000 ALTER TABLE `discipline` DISABLE KEYS */;
INSERT INTO `discipline` VALUES (2,'Материаловедение',6,10),(3,'История',5,8);
/*!40000 ALTER TABLE `discipline` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `idlog` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user` int(11) NOT NULL,
  `table` varchar(45) NOT NULL,
  `element` int(11) NOT NULL,
  `action` varchar(45) NOT NULL,
  PRIMARY KEY (`idlog`)
) ENGINE=InnoDB AUTO_INCREMENT=200 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (158,'2019-05-21 23:42:39',3,'department',8,'add'),(159,'2019-05-22 00:44:17',3,'department',9,'add'),(160,'2019-05-22 00:44:38',3,'department',10,'add'),(161,'2019-05-22 00:45:01',3,'department',11,'add'),(162,'2019-05-22 00:47:26',3,'discipline',1,'add'),(163,'2019-05-22 00:47:51',3,'discipline',1,'delete'),(164,'2019-05-22 00:48:07',3,'discipline',2,'add'),(165,'2019-05-22 00:48:13',3,'discipline',2,'edit'),(166,'2019-05-22 01:17:58',3,'discipline',2,'edit'),(167,'2019-05-22 01:18:17',3,'teacher',1,'add'),(168,'2019-05-22 01:19:42',3,'term',1,'add'),(169,'2019-05-22 01:20:08',3,'media',1,'add'),(170,'2019-05-22 01:20:11',3,'term',1,'validate_1'),(171,'2019-05-22 01:24:16',3,'term',2,'add'),(172,'2019-05-22 01:24:27',3,'media',2,'add'),(173,'2019-05-22 01:24:32',3,'term',2,'validate_1'),(174,'2019-05-22 01:26:57',3,'term',3,'add'),(175,'2019-05-22 01:27:11',3,'media',3,'add'),(176,'2019-05-22 01:27:13',3,'term',3,'validate_1'),(177,'2019-05-22 01:29:53',3,'discipline',3,'add'),(178,'2019-05-22 01:44:37',3,'term',1,'edit'),(179,'2019-05-22 01:44:38',3,'term',1,'validate_1'),(180,'2019-05-22 09:22:31',4,'term',4,'add'),(181,'2019-05-22 09:22:44',3,'user',4,'delete'),(182,'2019-05-22 09:35:50',3,'user',5,'add'),(183,'2019-05-22 10:03:42',3,'term',1,'validate_0'),(184,'2019-05-22 10:03:43',3,'term',1,'validate_1'),(185,'2019-05-22 10:03:44',3,'term',1,'validate_0'),(186,'2019-05-22 10:03:45',3,'term',1,'validate_1'),(187,'2019-05-22 10:25:52',3,'user',5,'delete'),(188,'2019-05-22 10:26:21',3,'user',6,'add'),(189,'2019-05-22 10:27:26',3,'teacher',2,'add'),(190,'2019-05-22 10:27:50',3,'term',5,'add'),(191,'2019-05-22 10:28:12',3,'term',6,'add'),(192,'2019-05-22 10:29:09',6,'term',7,'add'),(193,'2019-05-22 10:29:35',6,'term',8,'add'),(194,'2019-05-22 10:29:57',6,'term',9,'add'),(195,'2019-05-22 10:30:18',6,'term',10,'add'),(196,'2019-05-22 10:31:26',3,'media',4,'add'),(197,'2019-05-22 10:31:29',3,'term',5,'validate_1'),(198,'2019-05-22 10:31:49',3,'media',5,'add'),(199,'2019-05-22 10:31:50',3,'term',10,'validate_1');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `media`
--

DROP TABLE IF EXISTS `media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `media` (
  `idmedia` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL,
  `youtube_id` varchar(45) NOT NULL,
  `term` int(11) NOT NULL,
  PRIMARY KEY (`idmedia`),
  KEY `fk_term_idx` (`term`),
  CONSTRAINT `fk_term` FOREIGN KEY (`term`) REFERENCES `term` (`idterm`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `media`
--

LOCK TABLES `media` WRITE;
/*!40000 ALTER TABLE `media` DISABLE KEYS */;
INSERT INTO `media` VALUES (1,1,'z5lGPVmUgDw',1),(2,1,'WlSXPzdj950',2),(3,1,'r_zO5bXWa88',3),(4,1,'4wcfKsinbdY',5),(5,1,'q5BmAliAJFw',10);
/*!40000 ALTER TABLE `media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `idteacher` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(145) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`idteacher`),
  KEY `department_id_teacher_idx` (`department_id`),
  CONSTRAINT `department_id_teacher` FOREIGN KEY (`department_id`) REFERENCES `department` (`iddepartment`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'Петров В.И.',10),(2,'Разумов А.Н.',8);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `term`
--

DROP TABLE IF EXISTS `term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `term` (
  `idterm` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(145) NOT NULL,
  `description` varchar(500) NOT NULL,
  `lesson` int(11) NOT NULL,
  `teacher` int(11) NOT NULL,
  `discipline` int(11) NOT NULL,
  `image_path` varchar(200) NOT NULL,
  `creator` int(11) NOT NULL,
  `changed` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_shown` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`idterm`),
  KEY `fk_teacher_idx` (`teacher`),
  KEY `fk_discipline_idx` (`discipline`),
  KEY `fk_creator_idx` (`creator`),
  CONSTRAINT `fk_creator` FOREIGN KEY (`creator`) REFERENCES `user` (`iduser`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_discipline` FOREIGN KEY (`discipline`) REFERENCES `discipline` (`iddiscipline`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_teacher` FOREIGN KEY (`teacher`) REFERENCES `teacher` (`idteacher`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `term`
--

LOCK TABLES `term` WRITE;
/*!40000 ALTER TABLE `term` DISABLE KEYS */;
INSERT INTO `term` VALUES (1,'Адгезия','Адге́зия — сцепление поверхностей разнородных твёрдых и/или жидких тел. Адгезия обусловлена межмолекулярными взаимодействиями в поверхностном слое и характеризуется удельной работой, необходимой для разделения поверхностей. В некоторых случаях адгезия может оказаться сильнее, чем когезия, то есть сцепление внутри однородного материала, в таких случаях при приложении разрывающего усилия происходит когезионный разрыв, то есть разрыв в объёме менее прочного из соприкасающихся материалов.',15,1,2,'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Drops_I.jpg/220px-Drops_I.jpg',3,'2019-05-22 10:03:45',1),(2,'Диффузия металлов','Диффузия – это перенос вещества, обусловленный беспорядочным тепловым движением диффундирующих частиц. ',10,1,2,'https://ds04.infourok.ru/uploads/ex/1142/000750b9-c7531694/img5.jpg',3,'2019-05-22 01:24:32',1),(3,'Замасливание','Процесс замасливания представляет собой процедуру нанесения специального покрытия на поверхность стекловолокон, которая способствует их слипанию, выравниванию сил трения вдоль волокон и нитей',15,1,2,'https://ua.all.biz/img/ua/catalog/16050364.jpeg',3,'2019-05-22 01:27:13',1),(5,'Битва','Би́тва (Генеральное сражение) — широкомасштабные военные действия (включающие боевые действия) между двумя сторонами, находящимися друг с другом в состоянии войны. Название битве, как правило, даётся по местности, где она состоялась.',7,2,3,'http://elitefon.ru/download.php?file=201211/2560x1600/elitefon.ru-26776.jpg',3,'2019-05-22 10:31:29',1),(6,'Власть','Вла́сть — это возможность навязать свою волю другим людям, даже вопреки их сопротивлению',13,2,3,'https://images.aif.ru/004/311/8acf3adbe57967bd143979f00ba3d696.jpg',3,'2019-05-22 10:28:12',0),(7,'Война','Война́ — конфликт между политическими образованиями — государствами, племенами, политическими группировками и так далее, — происходящий на почве различных претензий, в форме вооружённого противоборства, военных (боевых) действий между их вооружёнными силами.',11,2,3,'http://www.topoboi.com/pic/201310/1920x1200/topoboi.com-20938.jpg',6,'2019-05-22 10:29:09',0),(8,'Восстание','Восста́ние, или мяте́ж — один из видов массовых выступлений против существующей власти, как правило, не приводящих к смене политического строя в государстве, стране или регионе.',10,2,3,'https://i0.wp.com/ezoterik-page.com/wp-content/uploads/2018/10/C0knARKWgAE1AI7.jpg?w=874',6,'2019-05-22 10:29:35',0),(9,'Государство','Госуда́рство — политическая форма организации общества на определённой территории, политико-территориальная суверенная организация публичной власти, обладающая аппаратом управления и принуждения, которому подчиняется всё население страны.',5,2,3,'http://www.pyatigorsk-rf.ru/images/fizicheskaja-karta-rossii.jpg',6,'2019-05-22 10:29:57',0),(10,'Император','Импера́тор — титул монарха, главы империи. Изначально — титул предводителя римских легионов. Императри́ца — как правило, супруга правящего императора, иногда — правительница империи в своем праве.',14,2,3,'https://avatars.mds.yandex.net/get-pdb/1381183/2b1fd927-df5f-417f-ae14-c3b2a80e1759/s1200',6,'2019-05-22 10:31:50',1);
/*!40000 ALTER TABLE `term` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(225) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `password` varchar(225) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`iduser`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'val@bmstu.ru','Валерий','Ильин','pbkdf2:sha256:150000$D86HAOTM$2133faeb156e986ea17180e6d5300f4361a694091637e7f134aecc76745734a6',1),(6,'kos@bmstu.ru','Татьяна','Косян','pbkdf2:sha256:150000$lPcC5n6P$d02af62eb91434ebd247e8d8eeb449c39abe397e4e789ee02cb2c7a1b564cbbe',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-22 10:39:22
