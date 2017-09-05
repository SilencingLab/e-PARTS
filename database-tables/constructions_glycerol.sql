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
-- Table structure for table `glycerol`
--

DROP TABLE IF EXISTS `glycerol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `glycerol` (
  `id` varchar(20) NOT NULL,
  `type` varchar(45) NOT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `glycerol_construction_0__idx` (`comment`,`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `glycerol`
--

LOCK TABLES `glycerol` WRITE;
/*!40000 ALTER TABLE `glycerol` DISABLE KEYS */;
INSERT INTO `glycerol` VALUES ('PA1','level0','MoClo Plan Parts Kit',NULL),('PA10','level0','MoClo Plan Parts Kit',NULL),('PA11','level0','MoClo Plan Parts Kit',NULL),('PA12','level0','MoClo Plan Parts Kit',NULL),('PA2','level0','MoClo Plan Parts Kit',NULL),('PA3','level0','MoClo Plan Parts Kit',NULL),('PA4','level0','MoClo Plan Parts Kit',NULL),('PA5','level0','MoClo Plan Parts Kit',NULL),('PA6','level0','MoClo Plan Parts Kit',NULL),('PA7','level0','MoClo Plan Parts Kit',NULL),('PA8','level0','MoClo Plan Parts Kit',NULL),('PA9','level0','MoClo Plan Parts Kit',NULL),('PB1','level0','MoClo Plan Parts Kit',NULL),('PB10','level0','MoClo Plan Parts Kit',NULL),('PB11','level0','MoClo Plan Parts Kit',NULL),('PB12','level0','MoClo Plan Parts Kit',NULL),('PB2','level0','MoClo Plan Parts Kit',NULL),('PB3','level0','MoClo Plan Parts Kit',NULL),('PB4','level0','MoClo Plan Parts Kit',NULL),('PB5','level0','MoClo Plan Parts Kit',NULL),('PB6','level0','MoClo Plan Parts Kit',NULL),('PB7','level0','MoClo Plan Parts Kit',NULL),('PB8','level0','MoClo Plan Parts Kit',NULL),('PB9','level0','MoClo Plan Parts Kit',NULL),('PC1','level0','MoClo Plan Parts Kit',NULL),('PC10','level0','MoClo Plan Parts Kit',NULL),('PC11','level0','MoClo Plan Parts Kit',NULL),('PC12','level0','MoClo Plan Parts Kit',NULL),('PC2','level0','MoClo Plan Parts Kit',NULL),('PC3','level0','MoClo Plan Parts Kit',NULL),('PC4','level0','MoClo Plan Parts Kit',NULL),('PC5','level0','MoClo Plan Parts Kit',NULL),('PC6','level0','MoClo Plan Parts Kit',NULL),('PC7','level0','MoClo Plan Parts Kit',NULL),('PC8','level0','MoClo Plan Parts Kit',NULL),('PC9','level0','MoClo Plan Parts Kit',NULL),('PD1','level0','MoClo Plan Parts Kit',NULL),('PD10','level0','MoClo Plan Parts Kit',NULL),('PD11','level0','MoClo Plan Parts Kit',NULL),('PD12','level0','MoClo Plan Parts Kit',NULL),('PD2','level0','MoClo Plan Parts Kit',NULL),('PD3','level0','MoClo Plan Parts Kit',NULL),('PD4','level0','MoClo Plan Parts Kit',NULL),('PD5','level0','MoClo Plan Parts Kit',NULL),('PD6','level0','MoClo Plan Parts Kit',NULL),('PD7','level0','MoClo Plan Parts Kit',NULL),('PD8','level0','MoClo Plan Parts Kit',NULL),('PD9','level0','MoClo Plan Parts Kit',NULL),('PE1','level0','MoClo Plan Parts Kit',NULL),('PE10','level0','MoClo Plan Parts Kit',NULL),('PE11','level0','MoClo Plan Parts Kit',NULL),('PE12','level0','MoClo Plan Parts Kit',NULL),('PE2','level0','MoClo Plan Parts Kit',NULL),('PE3','level0','MoClo Plan Parts Kit',NULL),('PE4','level0','MoClo Plan Parts Kit',NULL),('PE5','level0','MoClo Plan Parts Kit',NULL),('PE6','level0','MoClo Plan Parts Kit',NULL),('PE7','level0','MoClo Plan Parts Kit',NULL),('PE8','level0','MoClo Plan Parts Kit',NULL),('PE9','level0','MoClo Plan Parts Kit',NULL),('PF1','level0','MoClo Plan Parts Kit',NULL),('PF10','level0','MoClo Plan Parts Kit',NULL),('PF11','level0','MoClo Plan Parts Kit',NULL),('PF12','level0','MoClo Plan Parts Kit',NULL),('PF2','level0','MoClo Plan Parts Kit',NULL),('PF3','level0','MoClo Plan Parts Kit',NULL),('PF4','level0','MoClo Plan Parts Kit',NULL),('PF5','level0','MoClo Plan Parts Kit',NULL),('PF6','level0','MoClo Plan Parts Kit',NULL),('PF7','level0','MoClo Plan Parts Kit',NULL),('PF8','level0','MoClo Plan Parts Kit',NULL),('PF9','level0','MoClo Plan Parts Kit',NULL),('PG1','level0','MoClo Plan Parts Kit',NULL),('PG10','level0','MoClo Plan Parts Kit',NULL),('PG11','level0','MoClo Plan Parts Kit',NULL),('PG12','level0','MoClo Plan Parts Kit',NULL),('PG2','level0','MoClo Plan Parts Kit',NULL),('PG3','level0','MoClo Plan Parts Kit',NULL),('PG4','level0','MoClo Plan Parts Kit',NULL),('PG5','level0','MoClo Plan Parts Kit',NULL),('PG6','level0','MoClo Plan Parts Kit',NULL),('PG7','level0','MoClo Plan Parts Kit',NULL),('PG8','level0','MoClo Plan Parts Kit',NULL),('PG9','level0','MoClo Plan Parts Kit',NULL),('PH1','level0','MoClo Plan Parts Kit',NULL),('PH10','level0','MoClo Plan Parts Kit',NULL),('PH11','level0','MoClo Plan Parts Kit',NULL),('PH12','level0','MoClo Plan Parts Kit',NULL),('PH2','level0','MoClo Plan Parts Kit',NULL),('PH3','level0','MoClo Plan Parts Kit',NULL),('PH4','level0','MoClo Plan Parts Kit',NULL),('PH5','level0','MoClo Plan Parts Kit',NULL),('PH6','level0','MoClo Plan Parts Kit',NULL),('PH7','level0','MoClo Plan Parts Kit',NULL),('PH8','level0','MoClo Plan Parts Kit',NULL),('PH9','level0','MoClo Plan Parts Kit',NULL),('TA1','vector','MoClo Tool Kit',NULL),('TA10','vector','MoClo Tool Kit',NULL),('TA12','level 1','MoClo Tool Kit',NULL),('TA2','vector','MoClo Tool Kit',NULL),('TA3','vector','MoClo Tool Kit',NULL),('TA4','vector','MoClo Tool Kit',NULL),('TA5','vector','MoClo Tool Kit',NULL),('TA6','level 1','MoClo Tool Kit',NULL),('TA7','level 1','MoClo Tool Kit',NULL),('TA8','vector','MoClo Tool Kit',NULL),('TB1','vector','MoClo Tool Kit',NULL),('TB10','vector','MoClo Tool Kit',NULL),('TB12','vector','MoClo Tool Kit',NULL),('TB2','vector','MoClo Tool Kit',NULL),('TB3','vector','MoClo Tool Kit',NULL),('TB4','vector','MoClo Tool Kit',NULL),('TB5','level 1','MoClo Tool Kit',NULL),('TB6','level 1','MoClo Tool Kit',NULL),('TB7','level 1','MoClo Tool Kit',NULL),('TB8','vector','MoClo Tool Kit',NULL),('TC1','vector','MoClo Tool Kit',NULL),('TC10','vector','MoClo Tool Kit',NULL),('TC11','level 1','MoClo Tool Kit',NULL),('TC12','vector','MoClo Tool Kit',NULL),('TC2','vector','MoClo Tool Kit',NULL),('TC3','vector','MoClo Tool Kit',NULL),('TC4','vector','MoClo Tool Kit',NULL),('TC5','level 1','MoClo Tool Kit',NULL),('TC6','level 1','MoClo Tool Kit',NULL),('TC7','level 1','MoClo Tool Kit',NULL),('TC8','vector','MoClo Tool Kit',NULL),('TD1','vector','MoClo Tool Kit',NULL),('TD11','level 1','MoClo Tool Kit',NULL),('TD12','vector','MoClo Tool Kit',NULL),('TD2','vector','MoClo Tool Kit',NULL),('TD3','vector','MoClo Tool Kit',NULL),('TD4','vector','MoClo Tool Kit',NULL),('TD5','level 1','MoClo Tool Kit',NULL),('TD6','level 1','MoClo Tool Kit',NULL),('TD7','level 1','MoClo Tool Kit',NULL),('TD8','vector','MoClo Tool Kit',NULL),('TE1','vector','MoClo Tool Kit',NULL),('TE11','level 1','MoClo Tool Kit',NULL),('TE12','vector','MoClo Tool Kit',NULL),('TE2','vector','MoClo Tool Kit',NULL),('TE3','vector','MoClo Tool Kit',NULL),('TE4','vector','MoClo Tool Kit',NULL),('TE5','level 1','MoClo Tool Kit',NULL),('TE6','level 1','MoClo Tool Kit',NULL),('TE7','level 1','MoClo Tool Kit',NULL),('TE8','vector','MoClo Tool Kit',NULL),('TE9','vector','MoClo Tool Kit',NULL),('TF1','vector','MoClo Tool Kit',NULL),('TF11','level 1','MoClo Tool Kit',NULL),('TF12','vector','MoClo Tool Kit',NULL),('TF2','vector','MoClo Tool Kit',NULL),('TF3','vector','MoClo Tool Kit',NULL),('TF4','vector','MoClo Tool Kit',NULL),('TF5','level 1','MoClo Tool Kit',NULL),('TF6','level 1','MoClo Tool Kit',NULL),('TF7','level 1','MoClo Tool Kit',NULL),('TF9','vector','MoClo Tool Kit',NULL),('TG1','vector','MoClo Tool Kit',NULL),('TG11','level 1','MoClo Tool Kit',NULL),('TG12','vector','MoClo Tool Kit',NULL),('TG2','vector','MoClo Tool Kit',NULL),('TG3','vector','MoClo Tool Kit',NULL),('TG4','vector','MoClo Tool Kit',NULL),('TG5','level 1','MoClo Tool Kit',NULL),('TG6','level 1','MoClo Tool Kit',NULL),('TG7','vector','MoClo Tool Kit',NULL),('TG9','vector','MoClo Tool Kit',NULL),('TH1','vector','MoClo Tool Kit',NULL),('TH11','level 1','MoClo Tool Kit',NULL),('TH2','vector','MoClo Tool Kit',NULL),('TH3','vector','MoClo Tool Kit',NULL),('TH4','vector','MoClo Tool Kit',NULL),('TH5','level 1','MoClo Tool Kit',NULL),('TH6','level 1','MoClo Tool Kit',NULL),('TH7','vector','MoClo Tool Kit',NULL),('TH9','vector','MoClo Tool Kit',NULL);
/*!40000 ALTER TABLE `glycerol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-24 12:24:14
