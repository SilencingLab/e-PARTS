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
-- Table structure for table `resistance`
--

DROP TABLE IF EXISTS `resistance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resistance` (
  `vector_code` varchar(45) NOT NULL,
  `antibiotic_code` varchar(45) NOT NULL,
  `position` varchar(3) DEFAULT 'OUT',
  PRIMARY KEY (`vector_code`,`antibiotic_code`),
  KEY `antibiotic_code_idx` (`antibiotic_code`),
  CONSTRAINT `antibiotic_code` FOREIGN KEY (`antibiotic_code`) REFERENCES `antibiotic` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `vector_code` FOREIGN KEY (`vector_code`) REFERENCES `vector` (`code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resistance`
--

LOCK TABLES `resistance` WRITE;
/*!40000 ALTER TABLE `resistance` DISABLE KEYS */;
INSERT INTO `resistance` VALUES ('TA1','Kan','OUT'),('TA10','Kan','OUT'),('TA2','Spc','OUT'),('TA3','Spc','OUT'),('TA4','Cb','OUT'),('TA5','Kan','OUT'),('TA8','Spc','OUT'),('TB1','Spc','OUT'),('TB10','Kan','OUT'),('TB12','Kan','OUT'),('TB2','Spc','OUT'),('TB3','Cb','OUT'),('TB4','Cb','OUT'),('TB8','Spc','OUT'),('TC1','Spc','OUT'),('TC10','Kan','OUT'),('TC12','Kan','OUT'),('TC2','Spc','OUT'),('TC3','Cb','OUT'),('TC4','Cb','OUT'),('TC8','Spc','OUT'),('TD1','Spc','OUT'),('TD12','Kan','OUT'),('TD2','Spc','OUT'),('TD3','Cb','OUT'),('TD4','Cb','OUT'),('TD8','Spc','OUT'),('TE1','Spc','OUT'),('TE12','Kan','OUT'),('TE2','Spc','OUT'),('TE3','Cb','OUT'),('TE4','Cb','OUT'),('TE8','Spc','OUT'),('TE9','Kan','OUT'),('TF1','Spc','OUT'),('TF12','Kan','OUT'),('TF2','Spc','OUT'),('TF3','Cb','OUT'),('TF4','Cb','OUT'),('TF9','Kan','OUT'),('TG1','Spc','OUT'),('TG12','Spc','OUT'),('TG2','Spc','OUT'),('TG3','Cb','OUT'),('TG4','Cb','OUT'),('TG7','Spc','OUT'),('TG9','Kan','OUT'),('TH1','Spc','OUT'),('TH2','Spc','OUT'),('TH3','Cb','OUT'),('TH4','Kan','OUT'),('TH7','Spc','OUT'),('TH9','Kan','OUT');
/*!40000 ALTER TABLE `resistance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-24 12:24:11
