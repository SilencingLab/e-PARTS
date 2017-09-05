-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 138.4.138.24    Database: constructions
-- ------------------------------------------------------
-- Server version	5.7.16-log

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
-- Table structure for table `has`
--

DROP TABLE IF EXISTS `has`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `has` (
  `vector_code` varchar(45) NOT NULL,
  `marker_code` varchar(45) NOT NULL,
  `position` varchar(3) NOT NULL,
  KEY `marker_code_idx` (`marker_code`),
  KEY `vector_code_marker_idx` (`vector_code`),
  CONSTRAINT `marker_code` FOREIGN KEY (`marker_code`) REFERENCES `marker` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `vector_code_marker` FOREIGN KEY (`vector_code`) REFERENCES `vector` (`code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `has`
--

LOCK TABLES `has` WRITE;
/*!40000 ALTER TABLE `has` DISABLE KEYS */;
INSERT INTO `has` VALUES ('TA1','LacZ','IN'),('TA10','LacZ','IN'),('TA2','LacZ','IN'),('TA3','LacZ','IN'),('TA4','LacZ','IN'),('TA5','Can','IN'),('TA8','LacZ','IN'),('TB1','LacZ','IN'),('TB10','LacZ','IN'),('TB12','LacZ','IN'),('TB2','LacZ','IN'),('TB3','LacZ','IN'),('TB4','LacZ','IN'),('TB8','LacZ','IN'),('TC1','LacZ','IN'),('TC10','LacZ','IN'),('TC2','LacZ','IN'),('TC3','LacZ','IN'),('TC4','LacZ','IN'),('TC8','LacZ','IN'),('TD1','LacZ','IN'),('TD2','LacZ','IN'),('TD3','LacZ','IN'),('TD4','LacZ','IN'),('TD8','LacZ','IN'),('TE1','LacZ','IN'),('TE12','LacZ','IN'),('TE2','LacZ','IN'),('TE3','LacZ','IN'),('TE4','LacZ','IN'),('TE8','LacZ','IN'),('TE9','LacZ','IN'),('TF1','LacZ','IN'),('TF12','LacZ','IN'),('TF2','LacZ','IN'),('TF3','LacZ','IN'),('TF4','LacZ','IN'),('TF9','LacZ','IN'),('TG1','LacZ','IN'),('TG12','LacZ','IN'),('TG2','LacZ','IN'),('TG3','LacZ','IN'),('TG4','LacZ','IN'),('TG7','LacZ','IN'),('TG9','LacZ','IN'),('TH1','LacZ','IN'),('TH2','LacZ','IN'),('TH3','LacZ','IN'),('TH4','Can','IN'),('TH7','LacZ','IN'),('TH9','LacZ','IN'),('TC12','LacZ','IN'),('TD12','LacZ','IN');
/*!40000 ALTER TABLE `has` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-24 12:24:18
