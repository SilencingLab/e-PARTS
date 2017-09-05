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
-- Table structure for table `construction_level_p`
--

DROP TABLE IF EXISTS `construction_level_p`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `construction_level_p` (
  `code` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sequence` text NOT NULL,
  `comment` varchar(200) NOT NULL,
  `restriction_sites_P` varchar(45) NOT NULL DEFAULT '1',
  `vector` varchar(45) NOT NULL,
  PRIMARY KEY (`code`,`restriction_sites_P`,`vector`),
  KEY `restriction_p_idx` (`restriction_sites_P`),
  KEY `vector_p_idx` (`vector`),
  CONSTRAINT `P_gly` FOREIGN KEY (`code`) REFERENCES `glycerol` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `restriction_p` FOREIGN KEY (`restriction_sites_P`) REFERENCES `enzymes` (`code`) ON UPDATE CASCADE,
  CONSTRAINT `vector_p` FOREIGN KEY (`vector`) REFERENCES `vector` (`code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `construction_level_p`
--

LOCK TABLES `construction_level_p` WRITE;
/*!40000 ALTER TABLE `construction_level_p` DISABLE KEYS */;
/*!40000 ALTER TABLE `construction_level_p` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-24 12:24:10
