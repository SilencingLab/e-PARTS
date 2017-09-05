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
-- Table structure for table `level0_dna`
--

DROP TABLE IF EXISTS `level0_dna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `level0_dna` (
  `position` int(11) NOT NULL,
  `DNA_inserted_code` varchar(45) NOT NULL,
  `DNA_inserted_copy` varchar(45) NOT NULL,
  `construction_0` varchar(45) NOT NULL,
  PRIMARY KEY (`position`,`DNA_inserted_code`,`DNA_inserted_copy`,`construction_0`),
  KEY `L0_DNA_DNA_copy_idx` (`DNA_inserted_copy`),
  KEY `L0_DNA_DNA_copy2_idx` (`DNA_inserted_copy`),
  KEY `L0_DNA_copyDNA_idx` (`DNA_inserted_copy`),
  KEY `L0_DNA_cons_idx` (`construction_0`),
  KEY `L0_DNA_DNA_code_idx` (`DNA_inserted_code`,`DNA_inserted_copy`),
  CONSTRAINT `L0_DNA_DNA_code` FOREIGN KEY (`DNA_inserted_code`, `DNA_inserted_copy`) REFERENCES `dna_inserted` (`DNA_code`, `copy`) ON UPDATE CASCADE,
  CONSTRAINT `L0_DNA_cons` FOREIGN KEY (`construction_0`) REFERENCES `construction_level_0` (`code`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `level0_dna`
--

LOCK TABLES `level0_dna` WRITE;
/*!40000 ALTER TABLE `level0_dna` DISABLE KEYS */;
/*!40000 ALTER TABLE `level0_dna` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-24 12:24:12
