-- MySQL dump 10.15  Distrib 10.0.28-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: mato_smartsensor    Database: mato_smartsensor
-- ------------------------------------------------------
-- Server version	10.0.28-MariaDB-2+b1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `measurements`
--

DROP TABLE IF EXISTS `measurements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `measurements` (
  `uuid` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_hash` varchar(32) NOT NULL,
  `sensor_type` varchar(32) NOT NULL,
  `data` float NOT NULL,
  `created_on_module` varchar(128) DEFAULT NULL,
  `created_on_server` datetime DEFAULT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `measurements`
--

LOCK TABLES `measurements` WRITE;
/*!40000 ALTER TABLE `measurements` DISABLE KEYS */;
INSERT INTO `measurements` VALUES (1,'a4cf127d8b2c','TEMP',284,'2050-2-9T19:5:3','2020-02-10 20:09:39'),(2,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:4:37','2020-02-10 20:09:39'),(3,'a4cf127d8b2c','LIGHT',0,'2050-2-9T19:5:1','2020-02-10 20:09:39'),(4,'a4cf127d8b2c','MOIST',726,'2050-2-9T19:4:40','2020-02-10 20:09:41'),(5,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:4:44','2020-02-10 20:09:43'),(6,'a4cf127d8b2c','MOIST',727,'2050-2-9T19:4:47','2020-02-10 20:09:45'),(7,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:4:51','2020-02-10 20:09:47'),(8,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:4:54','2020-02-10 20:09:49'),(9,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:4:58','2020-02-10 20:09:51'),(10,'a4cf127d8b2c','MOIST_CAL_LOW',726,'2050-2-9T19:13:55','2020-02-10 20:14:32'),(11,'a4cf127d8b2c','MOIST_CAL_HIGH',727,'2050-2-9T19:14:36','2020-02-10 20:14:36'),(12,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:22:17','2020-02-10 20:22:34'),(13,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:22:21','2020-02-10 20:22:38'),(14,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:22:24','2020-02-10 20:22:41'),(15,'a4cf127d8b2c','MOIST',726,'2050-2-9T19:22:28','2020-02-10 20:22:45'),(16,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:22:31','2020-02-10 20:22:47'),(17,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:22:35','2020-02-10 20:22:51'),(18,'a4cf127d8b2c','MOIST',726,'2050-2-9T19:22:38','2020-02-10 20:22:53'),(19,'a4cf127d8b2c','LIGHT',0,'2050-2-9T19:22:42','2020-02-10 20:22:57'),(20,'a4cf127d8b2c','TEMP',284,'2050-2-9T19:22:43','2020-02-10 20:22:59'),(21,'a4cf127d8b2c','MOIST',727,'2050-2-9T19:24:0','2020-02-10 20:24:07'),(22,'a4cf127d8b2c','MOIST',727,'2050-2-9T19:24:2','2020-02-10 20:24:11'),(23,'a4cf127d8b2c','MOIST',726,'2050-2-9T19:24:4','2020-02-10 20:24:14'),(24,'a4cf127d8b2c','MOIST',724,'2050-2-9T19:24:6','2020-02-10 20:24:18'),(25,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:24:8','2020-02-10 20:24:20'),(26,'a4cf127d8b2c','MOIST',726,'2050-2-9T19:24:10','2020-02-10 20:24:24'),(27,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:24:12','2020-02-10 20:24:26'),(28,'a4cf127d8b2c','LIGHT',0,'2050-2-9T19:24:14','2020-02-10 20:24:30'),(29,'a4cf127d8b2c','TEMP',286,'2050-2-9T19:24:15','2020-02-10 20:24:32'),(30,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:26:8','2020-02-10 20:26:20'),(31,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:26:10','2020-02-10 20:26:24'),(32,'a4cf127d8b2c','MOIST',727,'2050-2-9T19:26:12','2020-02-10 20:26:26'),(33,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:26:14','2020-02-10 20:26:29'),(34,'a4cf127d8b2c','MOIST',727,'2050-2-9T19:26:17','2020-02-10 20:26:33'),(35,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:26:21','2020-02-10 20:26:35'),(36,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:26:24','2020-02-10 20:26:39'),(37,'a4cf127d8b2c','LIGHT',0,'2050-2-9T19:26:28','2020-02-10 20:26:41'),(38,'a4cf127d8b2c','TEMP',286,'2050-2-9T19:26:29','2020-02-10 20:26:45'),(39,'a4cf127d8b2c','MOIST_CAL_LOW',725,'2050-2-9T19:27:19','2020-02-10 20:27:39'),(40,'a4cf127d8b2c','MOIST_CAL_HIGH',726,'2050-2-9T19:27:44','2020-02-10 20:27:41'),(41,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:28:8','2020-02-10 20:28:27'),(42,'a4cf127d8b2c','MOIST',726,'2050-2-9T19:28:12','2020-02-10 20:28:30'),(43,'a4cf127d8b2c','MOIST',728,'2050-2-9T19:28:16','2020-02-10 20:28:34'),(44,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:28:19','2020-02-10 20:28:36'),(45,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:28:23','2020-02-10 20:28:38'),(46,'a4cf127d8b2c','MOIST',725,'2050-2-9T19:28:27','2020-02-10 20:28:42'),(47,'a4cf127d8b2c','MOIST',724,'2050-2-9T19:28:30','2020-02-10 20:28:44'),(48,'a4cf127d8b2c','LIGHT',0,'2050-2-9T19:28:34','2020-02-10 20:28:48'),(49,'a4cf127d8b2c','TEMP',293,'2050-2-9T19:28:35','2020-02-10 20:28:50');
/*!40000 ALTER TABLE `measurements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor`
--

DROP TABLE IF EXISTS `sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sensor_hash` varchar(32) NOT NULL,
  `created_on_module` varchar(128) DEFAULT NULL,
  `created_on_server` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_sensor_sensor_hash` (`sensor_hash`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor`
--

LOCK TABLES `sensor` WRITE;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
INSERT INTO `sensor` VALUES (1,'a4cf127d8b2c','2050-2-9T19:5:3','2020-02-10 20:09:39');
/*!40000 ALTER TABLE `sensor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-10 20:31:02