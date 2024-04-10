CREATE DATABASE  IF NOT EXISTS `hospital` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `hospital`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `analytics`
--

DROP TABLE IF EXISTS `analytics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analytics` (
  `analytics_ID` int(11) NOT NULL AUTO_INCREMENT,
  `metric_ID` int(11) DEFAULT NULL,
  `value` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`analytics_ID`),
  UNIQUE KEY `analytic_ID_UNIQUE` (`analytics_ID`),
  KEY `metric_ID_analytics_idx` (`metric_ID`),
  CONSTRAINT `metric_ID_analytics` FOREIGN KEY (`metric_ID`) REFERENCES `quality` (`metric_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='this is to see the different trends in the use of this database.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `appoinments`
--

DROP TABLE IF EXISTS `appoinments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appoinments` (
  `appoinment_ID` int(11) NOT NULL AUTO_INCREMENT,
  `patient_ID` int(11) NOT NULL,
  `doctor_ID` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `appoinmentdate` date NOT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`appoinment_ID`),
  UNIQUE KEY `appoinment_ID_UNIQUE` (`appoinment_ID`),
  KEY `patient_ID_idx` (`patient_ID`),
  KEY `doctor_idx` (`doctor_ID`),
  CONSTRAINT `doctor_ID_appoinment` FOREIGN KEY (`doctor_ID`) REFERENCES `doctors` (`doctor_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `patient_ID_appointment` FOREIGN KEY (`patient_ID`) REFERENCES `patients` (`patient_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This table stores all the information related to appoinments, their status and time and who and for who it is assigned.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `billing`
--

DROP TABLE IF EXISTS `billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billing` (
  `billing_ID` int(11) NOT NULL AUTO_INCREMENT,
  `patient_ID` int(11) NOT NULL,
  `amount` double NOT NULL,
  `payment_status` int(11) NOT NULL,
  `insurance_and_remarks` tinytext,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`billing_ID`),
  UNIQUE KEY `trans_ID_UNIQUE` (`billing_ID`),
  KEY `patient_idx` (`patient_ID`),
  CONSTRAINT `patient_ID_bill` FOREIGN KEY (`patient_ID`) REFERENCES `patients` (`patient_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `communication`
--

DROP TABLE IF EXISTS `communication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communication` (
  `communication_ID` int(11) NOT NULL AUTO_INCREMENT,
  `sender_ID` int(11) NOT NULL,
  `receiver_ID` int(11) NOT NULL,
  `message` longtext,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`communication_ID`,`timestamp`),
  UNIQUE KEY `log_ID_UNIQUE` (`communication_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='this logs communication between different entities in the setup.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `doctorappoinments`
--

DROP TABLE IF EXISTS `doctorappoinments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctorappoinments` (
  `doctor_ID` int(11) NOT NULL,
  `appoinment_ID` int(11) NOT NULL,
  PRIMARY KEY (`doctor_ID`,`appoinment_ID`),
  KEY `appoinment_ID_idx` (`appoinment_ID`),
  CONSTRAINT `appoinment_ID` FOREIGN KEY (`appoinment_ID`) REFERENCES `appoinments` (`appoinment_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `doctor_ID_app` FOREIGN KEY (`doctor_ID`) REFERENCES `doctors` (`doctor_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_ID` int(11) NOT NULL DEFAULT '1',
  `contact_info` mediumtext NOT NULL,
  `speciality` varchar(45) DEFAULT NULL,
  `notes` longtext,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`doctor_ID`),
  UNIQUE KEY `doctor_ID_UNIQUE` (`doctor_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This table contains details about doctors, their contact info and specifications, if any.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `inventory_ID` int(11) NOT NULL AUTO_INCREMENT,
  `sku` int(11) NOT NULL,
  `item_name` varchar(45) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `latestExpirationDate` date DEFAULT NULL,
  `supplier_ID` int(11) NOT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`inventory_ID`),
  UNIQUE KEY `item_ID_UNIQUE` (`inventory_ID`),
  KEY `supplier_idx` (`supplier_ID`),
  CONSTRAINT `supplier_ID_inventory` FOREIGN KEY (`supplier_ID`) REFERENCES `supplier` (`supplier_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medical_records`
--

DROP TABLE IF EXISTS `medical_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_records` (
  `medical_records_ID` int(11) NOT NULL DEFAULT '1',
  `patient_ID` int(11) NOT NULL,
  `diagnosis` mediumtext NOT NULL,
  `treatment` longtext,
  `medications` longtext,
  `lab_results` longtext,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`medical_records_ID`),
  UNIQUE KEY `record_ID_UNIQUE` (`medical_records_ID`),
  KEY `patient_ID_idx` (`patient_ID`),
  CONSTRAINT `patient_ID_medicalrecords` FOREIGN KEY (`patient_ID`) REFERENCES `patients` (`patient_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This table contains records for patient''s medical records. A patient can have multiple unique records. \n';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_ID` int(11) NOT NULL DEFAULT '1' COMMENT 'A unique ID is assigned to the patients. This can be a register number which increments by 1 when new patient_ID is created.',
  `patient_name` varchar(60) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `medical_history` varchar(60) NOT NULL,
  `insurance_info` varchar(60) DEFAULT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`patient_ID`),
  UNIQUE KEY `patient_ID_UNIQUE` (`patient_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This table contains the patients info. It can create multiple relations to medical_records, appoinments and billing.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `quality`
--

DROP TABLE IF EXISTS `quality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quality` (
  `metric_ID` int(11) NOT NULL DEFAULT '1',
  `name` varchar(45) NOT NULL,
  `value` varchar(45) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`metric_ID`),
  UNIQUE KEY `metric_ID_UNIQUE` (`metric_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `student_grades`
--

DROP TABLE IF EXISTS `student_grades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_grades` (
  `student_ID` int(11) NOT NULL DEFAULT '1',
  `name` varchar(45) NOT NULL,
  `contact_info` varchar(45) NOT NULL,
  `grades` varchar(45) NOT NULL,
  PRIMARY KEY (`student_ID`),
  UNIQUE KEY `student_ID_UNIQUE` (`student_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplier_ID` int(11) NOT NULL DEFAULT '1',
  `name_and_contact` mediumtext NOT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`supplier_ID`),
  UNIQUE KEY `supplier_ID_UNIQUE` (`supplier_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This table contains all the suppliers for the phrmacy.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `training`
--

DROP TABLE IF EXISTS `training`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training` (
  `training_ID` int(11) NOT NULL DEFAULT '1',
  `title` varchar(45) NOT NULL,
  `desc` tinytext,
  `link` tinytext,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`training_ID`),
  UNIQUE KEY `material_ID_UNIQUE` (`training_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='This is a part of training module, it contains differernt training materials.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_ID` varchar(45) NOT NULL DEFAULT '1',
  `userpass` varchar(45) DEFAULT NULL,
  `priviledges` varchar(45) NOT NULL,
  `updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_ID`),
  UNIQUE KEY `user_ID_UNIQUE` (`user_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'hospital'
--

--
-- Dumping routines for database 'hospital'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-10 15:20:08
