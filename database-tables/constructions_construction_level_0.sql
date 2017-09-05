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
-- Table structure for table `construction_level_0`
--

DROP TABLE IF EXISTS `construction_level_0`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `construction_level_0` (
  `code` varchar(45) NOT NULL,
  `sequence` text NOT NULL,
  `forward_primer` varchar(45) NOT NULL,
  `reverse_primer` varchar(45) NOT NULL,
  `3_end` varchar(10) NOT NULL,
  `5_end` varchar(10) NOT NULL,
  `vector` varchar(45) NOT NULL,
  `restriction_sites_0` varchar(45) NOT NULL DEFAULT '2',
  `comment` varchar(200) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`code`),
  KEY `f_primer_idx` (`forward_primer`),
  KEY `r_primer_idx` (`reverse_primer`),
  KEY `vector_idx` (`vector`),
  KEY `generated_idx` (`restriction_sites_0`),
  KEY `3end_idx` (`3_end`),
  KEY `5end_idx` (`5_end`),
  CONSTRAINT `3end` FOREIGN KEY (`3_end`) REFERENCES `pieces` (`number`) ON UPDATE CASCADE,
  CONSTRAINT `5end` FOREIGN KEY (`5_end`) REFERENCES `pieces` (`number`) ON UPDATE CASCADE,
  CONSTRAINT `cons_0_glyc` FOREIGN KEY (`code`) REFERENCES `glycerol` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `f_primer` FOREIGN KEY (`forward_primer`) REFERENCES `primers` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `r_primer` FOREIGN KEY (`reverse_primer`) REFERENCES `primers` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `restric_0` FOREIGN KEY (`restriction_sites_0`) REFERENCES `enzymes` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `vector_0` FOREIGN KEY (`vector`) REFERENCES `vector` (`code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `construction_level_0`
--

LOCK TABLES `construction_level_0` WRITE;
/*!40000 ALTER TABLE `construction_level_0` DISABLE KEYS */;
/*!40000 ALTER TABLE `construction_level_0` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-24 12:24:16
