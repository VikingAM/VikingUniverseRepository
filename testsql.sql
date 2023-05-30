/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 10.4.19-MariaDB : Database - viking_universe
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`viking_universe` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;

USE `viking_universe`;

/*Table structure for table `accounts_address_info` */

DROP TABLE IF EXISTS `accounts_address_info`;

CREATE TABLE `accounts_address_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `street` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `state` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `code` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `country` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address_type` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `zip_code` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_account_address_info_userId_id_df473da1_fk_auth_user_id` (`userId_id`),
  CONSTRAINT `accounts_account_address_info_userId_id_df473da1_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_address_info` */

insert  into `accounts_address_info`(`id`,`street`,`city`,`state`,`code`,`country`,`address_type`,`create_date`,`update_date`,`history`,`userId_id`,`zip_code`) values (24,'block 18 lot 35','Davao City','',NULL,'Philippines',NULL,'2023-03-11 15:34:36.132201','2023-03-11 15:34:36.132201',NULL,25,'8000');

/*Table structure for table `accounts_credit_score` */

DROP TABLE IF EXISTS `accounts_credit_score`;

CREATE TABLE `accounts_credit_score` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `amount` int(11) DEFAULT NULL,
  `paid` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `credit` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_credit_score_userId_id_5449c7b5_fk_auth_user_id` (`userId_id`),
  CONSTRAINT `accounts_credit_score_userId_id_5449c7b5_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_credit_score` */

insert  into `accounts_credit_score`(`id`,`amount`,`paid`,`create_date`,`status`,`userId_id`,`credit`) values (1,500,1,'2023-04-27 01:39:20.167055',1,25,500);

/*Table structure for table `accounts_details` */

DROP TABLE IF EXISTS `accounts_details`;

CREATE TABLE `accounts_details` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `middle_name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `last_name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `business_phone` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `company_name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `website` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `account_type_id` bigint(20) DEFAULT NULL,
  `industry_type_id` bigint(20) DEFAULT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `photo_path` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `business_description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_account_det_industry_type_id_120bcaa0_fk_accounts_` (`industry_type_id`),
  KEY `accounts_account_details_userId_id_edd2cca4_fk_auth_user_id` (`userId_id`),
  KEY `accounts_details_account_type_id_82a87080_fk_accounts_types_id` (`account_type_id`),
  CONSTRAINT `accounts_account_det_industry_type_id_120bcaa0_fk_accounts_` FOREIGN KEY (`industry_type_id`) REFERENCES `accounts_industry_type` (`id`),
  CONSTRAINT `accounts_account_details_userId_id_edd2cca4_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `accounts_details_account_type_id_82a87080_fk_accounts_types_id` FOREIGN KEY (`account_type_id`) REFERENCES `accounts_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_details` */

insert  into `accounts_details`(`id`,`first_name`,`middle_name`,`last_name`,`email`,`phone`,`business_phone`,`company_name`,`title`,`website`,`status`,`create_date`,`update_date`,`history`,`account_type_id`,`industry_type_id`,`userId_id`,`photo_path`,`business_description`) values (24,'william',NULL,'crumb','william.crumb@vikingassetmanagement.com','09663308394',NULL,'sample company',NULL,'','verified','2023-03-11 15:34:36.129686','2023-03-11 23:36:04.443752',NULL,NULL,NULL,25,'',NULL);

/*Table structure for table `accounts_industry_type` */

DROP TABLE IF EXISTS `accounts_industry_type`;

CREATE TABLE `accounts_industry_type` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_industry_type` */

insert  into `accounts_industry_type`(`id`,`name`,`is_delete`) values (1,'Ratail Trade',0);

/*Table structure for table `accounts_invoice` */

DROP TABLE IF EXISTS `accounts_invoice`;

CREATE TABLE `accounts_invoice` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create_date` datetime(6) NOT NULL,
  `payment_method` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `product_description` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `product_name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_invoice_userId_id_93432640_fk_auth_user_id` (`userId_id`),
  CONSTRAINT `accounts_invoice_userId_id_93432640_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_invoice` */

insert  into `accounts_invoice`(`id`,`create_date`,`payment_method`,`status`,`userId_id`,`amount`,`product_description`,`product_name`,`quantity`) values (1,'2023-04-27 01:39:20.170782','Card',1,25,500,'Custom 500 Credit','Custom Credit',1);

/*Table structure for table `accounts_password_category` */

DROP TABLE IF EXISTS `accounts_password_category`;

CREATE TABLE `accounts_password_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_password_category` */

insert  into `accounts_password_category`(`id`,`name`,`is_delete`) values (1,'Social Media',0);

/*Table structure for table `accounts_password_manager` */

DROP TABLE IF EXISTS `accounts_password_manager`;

CREATE TABLE `accounts_password_manager` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `url` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_password_ma_category_id_b28eadc6_fk_accounts_` (`category_id`),
  KEY `accounts_password_manager_userId_id_a47d6544_fk_auth_user_id` (`userId_id`),
  CONSTRAINT `accounts_password_ma_category_id_b28eadc6_fk_accounts_` FOREIGN KEY (`category_id`) REFERENCES `accounts_password_category` (`id`),
  CONSTRAINT `accounts_password_manager_userId_id_a47d6544_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_password_manager` */

insert  into `accounts_password_manager`(`id`,`name`,`username`,`password`,`description`,`url`,`create_date`,`update_date`,`history`,`category_id`,`userId_id`,`status`) values (1,'sample password name','sample username','password','sample2x','www.sampleurl.com/login.php','2023-03-16 15:43:45.657555','2023-03-16 15:43:45.657555',NULL,1,25,1),(2,'wswsawa','wsawaw','waswadaw','wadawsawdaw','sawdawawa','2023-04-29 10:35:22.436945','2023-04-29 10:35:22.436945',NULL,NULL,25,1);

/*Table structure for table `accounts_password_reset_code` */

DROP TABLE IF EXISTS `accounts_password_reset_code`;

CREATE TABLE `accounts_password_reset_code` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `userId_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_password_reset_code_userId_id_56c0caeb_fk_auth_user_id` (`userId_id`),
  CONSTRAINT `accounts_password_reset_code_userId_id_56c0caeb_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_password_reset_code` */

/*Table structure for table `accounts_types` */

DROP TABLE IF EXISTS `accounts_types`;

CREATE TABLE `accounts_types` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_types` */

/*Table structure for table `accounts_user_validation` */

DROP TABLE IF EXISTS `accounts_user_validation`;

CREATE TABLE `accounts_user_validation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `verification_code` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_user_validation_userId_id_354bfe17_fk_auth_user_id` (`userId_id`),
  CONSTRAINT `accounts_user_validation_userId_id_354bfe17_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `accounts_user_validation` */

insert  into `accounts_user_validation`(`id`,`verification_code`,`status`,`update_date`,`userId_id`,`create_date`) values (23,'69474916fdd94592b088c7ccba2df19f',1,'2023-03-11 23:36:04.549017',25,'2023-03-11 15:34:36.134658');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add industry_type',7,'add_industry_type'),(26,'Can change industry_type',7,'change_industry_type'),(27,'Can delete industry_type',7,'delete_industry_type'),(28,'Can view industry_type',7,'view_industry_type'),(29,'Can add account_address_info',8,'add_account_address_info'),(30,'Can change account_address_info',8,'change_account_address_info'),(31,'Can delete account_address_info',8,'delete_account_address_info'),(32,'Can view account_address_info',8,'view_account_address_info'),(33,'Can add account_type',9,'add_account_type'),(34,'Can change account_type',9,'change_account_type'),(35,'Can delete account_type',9,'delete_account_type'),(36,'Can view account_type',9,'view_account_type'),(37,'Can add account_details',10,'add_account_details'),(38,'Can change account_details',10,'change_account_details'),(39,'Can delete account_details',10,'delete_account_details'),(40,'Can view account_details',10,'view_account_details'),(41,'Can add address_info',8,'add_address_info'),(42,'Can change address_info',8,'change_address_info'),(43,'Can delete address_info',8,'delete_address_info'),(44,'Can view address_info',8,'view_address_info'),(45,'Can add details',10,'add_details'),(46,'Can change details',10,'change_details'),(47,'Can delete details',10,'delete_details'),(48,'Can view details',10,'view_details'),(49,'Can add types',9,'add_types'),(50,'Can change types',9,'change_types'),(51,'Can delete types',9,'delete_types'),(52,'Can view types',9,'view_types'),(53,'Can add password_category',11,'add_password_category'),(54,'Can change password_category',11,'change_password_category'),(55,'Can delete password_category',11,'delete_password_category'),(56,'Can view password_category',11,'view_password_category'),(57,'Can add password_manager',12,'add_password_manager'),(58,'Can change password_manager',12,'change_password_manager'),(59,'Can delete password_manager',12,'delete_password_manager'),(60,'Can view password_manager',12,'view_password_manager'),(61,'Can add issue',13,'add_issue'),(62,'Can change issue',13,'change_issue'),(63,'Can delete issue',13,'delete_issue'),(64,'Can view issue',13,'view_issue'),(65,'Can add issue_comment',14,'add_issue_comment'),(66,'Can change issue_comment',14,'change_issue_comment'),(67,'Can delete issue_comment',14,'delete_issue_comment'),(68,'Can view issue_comment',14,'view_issue_comment'),(69,'Can add issue_type',15,'add_issue_type'),(70,'Can change issue_type',15,'change_issue_type'),(71,'Can delete issue_type',15,'delete_issue_type'),(72,'Can view issue_type',15,'view_issue_type'),(73,'Can add task',16,'add_task'),(74,'Can change task',16,'change_task'),(75,'Can delete task',16,'delete_task'),(76,'Can view task',16,'view_task'),(77,'Can add task_category',17,'add_task_category'),(78,'Can change task_category',17,'change_task_category'),(79,'Can delete task_category',17,'delete_task_category'),(80,'Can view task_category',17,'view_task_category'),(81,'Can add task_comment',18,'add_task_comment'),(82,'Can change task_comment',18,'change_task_comment'),(83,'Can delete task_comment',18,'delete_task_comment'),(84,'Can view task_comment',18,'view_task_comment'),(85,'Can add tast_file',19,'add_tast_file'),(86,'Can change tast_file',19,'change_tast_file'),(87,'Can delete tast_file',19,'delete_tast_file'),(88,'Can view tast_file',19,'view_tast_file'),(89,'Can add task_responders',20,'add_task_responders'),(90,'Can change task_responders',20,'change_task_responders'),(91,'Can delete task_responders',20,'delete_task_responders'),(92,'Can view task_responders',20,'view_task_responders'),(93,'Can add task_comment_file',21,'add_task_comment_file'),(94,'Can change task_comment_file',21,'change_task_comment_file'),(95,'Can delete task_comment_file',21,'delete_task_comment_file'),(96,'Can view task_comment_file',21,'view_task_comment_file'),(97,'Can add issue_responders',22,'add_issue_responders'),(98,'Can change issue_responders',22,'change_issue_responders'),(99,'Can delete issue_responders',22,'delete_issue_responders'),(100,'Can view issue_responders',22,'view_issue_responders'),(101,'Can add issue_file',23,'add_issue_file'),(102,'Can change issue_file',23,'change_issue_file'),(103,'Can delete issue_file',23,'delete_issue_file'),(104,'Can view issue_file',23,'view_issue_file'),(105,'Can add issue_comment_file',24,'add_issue_comment_file'),(106,'Can change issue_comment_file',24,'change_issue_comment_file'),(107,'Can delete issue_comment_file',24,'delete_issue_comment_file'),(108,'Can view issue_comment_file',24,'view_issue_comment_file'),(109,'Can add task_file',19,'add_task_file'),(110,'Can change task_file',19,'change_task_file'),(111,'Can delete task_file',19,'delete_task_file'),(112,'Can view task_file',19,'view_task_file'),(113,'Can add user_validation',25,'add_user_validation'),(114,'Can change user_validation',25,'change_user_validation'),(115,'Can delete user_validation',25,'delete_user_validation'),(116,'Can view user_validation',25,'view_user_validation'),(117,'Can add password_reset_code',26,'add_password_reset_code'),(118,'Can change password_reset_code',26,'change_password_reset_code'),(119,'Can delete password_reset_code',26,'delete_password_reset_code'),(120,'Can view password_reset_code',26,'view_password_reset_code'),(121,'Can add credit_score',27,'add_credit_score'),(122,'Can change credit_score',27,'change_credit_score'),(123,'Can delete credit_score',27,'delete_credit_score'),(124,'Can view credit_score',27,'view_credit_score'),(125,'Can add invoice',28,'add_invoice'),(126,'Can change invoice',28,'change_invoice'),(127,'Can delete invoice',28,'delete_invoice'),(128,'Can view invoice',28,'view_invoice'),(129,'Can add task_cetegory_theme',29,'add_task_cetegory_theme'),(130,'Can change task_cetegory_theme',29,'change_task_cetegory_theme'),(131,'Can delete task_cetegory_theme',29,'delete_task_cetegory_theme'),(132,'Can view task_cetegory_theme',29,'view_task_cetegory_theme'),(133,'Can add task_services',30,'add_task_services'),(134,'Can change task_services',30,'change_task_services'),(135,'Can delete task_services',30,'delete_task_services'),(136,'Can view task_services',30,'view_task_services');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$390000$EqfYzGtmtELgPzo88broNc$JwrIJB1tgL2Abm0xF9RFyswXSV6p4aUcgt4dgyPVxhU=','2023-05-18 21:12:13.864833',1,'poliam','','','poliamcrumb@gmail.com',1,1,'2023-02-13 07:23:14.386164'),(25,'pbkdf2_sha256$390000$AVGwhG2VhqmKY46CU6Pt81$WD+7AQsLhiIb59c71cM42xoDzhfXSBqq/UQq04PQzqY=','2023-05-18 21:14:13.239603',0,'poliamusername','william','crumb','william.crumb@vikingassetmanagement.com',0,1,'2023-03-11 15:34:35.766204');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `django_admin_log` */

insert  into `django_admin_log`(`id`,`action_time`,`object_id`,`object_repr`,`action_flag`,`change_message`,`content_type_id`,`user_id`) values (1,'2023-05-02 01:48:57.543358','1','task_cetegory_theme object (1)',1,'[{\"added\": {}}]',29,1),(2,'2023-05-02 01:48:58.503992','2','task_cetegory_theme object (2)',1,'[{\"added\": {}}]',29,1),(3,'2023-05-02 01:49:18.464440','1','task_cetegory_theme object (1)',3,'',29,1);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (8,'accounts','address_info'),(27,'accounts','credit_score'),(10,'accounts','details'),(7,'accounts','industry_type'),(28,'accounts','invoice'),(11,'accounts','password_category'),(12,'accounts','password_manager'),(26,'accounts','password_reset_code'),(9,'accounts','types'),(25,'accounts','user_validation'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(13,'tickets','issue'),(14,'tickets','issue_comment'),(24,'tickets','issue_comment_file'),(23,'tickets','issue_file'),(22,'tickets','issue_responders'),(15,'tickets','issue_type'),(16,'tickets','task'),(17,'tickets','task_category'),(29,'tickets','task_cetegory_theme'),(18,'tickets','task_comment'),(21,'tickets','task_comment_file'),(19,'tickets','task_file'),(20,'tickets','task_responders'),(30,'tickets','task_services');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2023-02-08 01:18:12.056805'),(2,'auth','0001_initial','2023-02-08 01:18:12.576438'),(3,'admin','0001_initial','2023-02-08 01:18:12.710056'),(4,'admin','0002_logentry_remove_auto_add','2023-02-08 01:18:12.728855'),(5,'admin','0003_logentry_add_action_flag_choices','2023-02-08 01:18:12.742861'),(6,'contenttypes','0002_remove_content_type_name','2023-02-08 01:18:12.824282'),(7,'auth','0002_alter_permission_name_max_length','2023-02-08 01:18:12.888609'),(8,'auth','0003_alter_user_email_max_length','2023-02-08 01:18:12.917739'),(9,'auth','0004_alter_user_username_opts','2023-02-08 01:18:12.930743'),(10,'auth','0005_alter_user_last_login_null','2023-02-08 01:18:12.984743'),(11,'auth','0006_require_contenttypes_0002','2023-02-08 01:18:12.996045'),(12,'auth','0007_alter_validators_add_error_messages','2023-02-08 01:18:13.009745'),(13,'auth','0008_alter_user_username_max_length','2023-02-08 01:18:13.040719'),(14,'auth','0009_alter_user_last_name_max_length','2023-02-08 01:18:13.071329'),(15,'auth','0010_alter_group_name_max_length','2023-02-08 01:18:13.101218'),(16,'auth','0011_update_proxy_permissions','2023-02-08 01:18:13.124216'),(17,'auth','0012_alter_user_first_name_max_length','2023-02-08 01:18:13.149223'),(18,'sessions','0001_initial','2023-02-08 01:18:13.200147'),(19,'accounts','0001_initial','2023-02-13 04:41:00.857314'),(20,'accounts','0002_rename_account_address_info_address_info_and_more','2023-02-13 07:13:01.885791'),(21,'accounts','0003_password_category_details_photo_path_and_more','2023-02-13 07:38:25.436090'),(22,'accounts','0004_details_business_description_and_more','2023-02-13 10:30:41.250282'),(23,'tickets','0001_initial','2023-02-13 10:30:42.290882'),(24,'tickets','0002_task_comment_task_id','2023-02-13 13:48:13.229252'),(25,'tickets','0003_issue_issue_type_issue_comment_issue_id','2023-02-13 13:54:04.221816'),(26,'tickets','0004_rename_issue_id_issue_comment_issue_and_more','2023-02-13 14:00:41.165724'),(27,'tickets','0005_rename_tast_file_task_file','2023-02-13 14:02:47.452464'),(28,'accounts','0005_user_validation','2023-03-01 01:38:44.541493'),(29,'accounts','0006_user_validation_create_date','2023-03-01 07:58:12.557622'),(30,'accounts','0007_address_info_zip_code','2023-03-05 04:08:53.601564'),(31,'accounts','0008_password_reset_code','2023-03-08 05:19:07.549685'),(32,'accounts','0009_password_manager_status','2023-03-16 15:40:47.635904'),(33,'tickets','0006_issue_create_date_issue_history_issue_update_date','2023-03-24 14:28:23.028442'),(34,'accounts','0010_credit_score','2023-04-19 09:50:01.203413'),(35,'accounts','0011_alter_credit_score_amount','2023-04-19 09:50:01.218744'),(36,'accounts','0012_credit_score_credit','2023-04-19 09:50:01.282889'),(37,'accounts','0013_invoice','2023-04-19 09:50:01.355413'),(38,'accounts','0014_invoice_amount_invoice_product_description_and_more','2023-04-19 09:50:01.438526'),(39,'accounts','0015_remove_invoice_product_purchase','2023-04-19 09:50:01.461277'),(40,'tickets','0007_task_cetegory_theme_task_category_parent_and_more','2023-05-02 01:44:27.866822'),(41,'tickets','0008_task_category_status','2023-05-23 06:31:25.501919'),(42,'tickets','0009_task_end_date','2023-05-24 13:52:08.399743'),(43,'tickets','0010_task_owner','2023-05-29 06:47:37.366883'),(44,'tickets','0011_alter_task_urgency','2023-05-29 06:59:23.505751'),(45,'tickets','0012_alter_task_status','2023-05-29 07:01:58.360509'),(46,'tickets','0013_task_task_percentage','2023-05-29 16:47:23.699621');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('3czq7ntp7ycz7dpy60nxlt6uh32sy8uz','.eJxVjEEOwiAQRe_C2pApZQK4dO8ZyDBMpWogKe3KeHdt0oVu_3vvv1SkbS1x67LEOauzMqhOv2MifkjdSb5TvTXNra7LnPSu6IN2fW1ZnpfD_Tso1Mu3DmCNjC54DAg4DexBgngkFic0YQY0LoNjTB7YUjAI1oFJ4yDAzqj3B-0iN0g:1pzkwv:Ygzt9rnooUpLtS95-Ds4evBytO6eY8cVUmYmBJGS2EA','2023-06-01 21:14:13.243906'),('gzd1nm7vs4in7p7bgq2zph56snq27hdl','.eJxVjDsOwjAQBe_iGllZ_0NJzxmstXeNA8iR4qRC3B0ipYD2zcx7iYjbWuPWeYkTibMAcfrdEuYHtx3QHdttlnlu6zIluSvyoF1eZ-Ln5XD_Dir2-q0DuOw16qQsWgUDF0oF2AePhTgRhJINKbJu1A7DoAjAjoa0UQGDAvH-APDfN8k:1pRTBW:YSqRvHMiFPHXfkT4tOyjf7pZsHSzXl53sNTQXcjIfUM','2023-02-27 07:23:34.732359'),('som1vkbqou869fnu7r18a69jjtr1c5dy','.eJxVjEEOwiAQRe_C2pApZQK4dO8ZyDBMpWogKe3KeHdt0oVu_3vvv1SkbS1x67LEOauzMqhOv2MifkjdSb5TvTXNra7LnPSu6IN2fW1ZnpfD_Tso1Mu3DmCNjC54DAg4DexBgngkFic0YQY0LoNjTB7YUjAI1oFJ4yDAzqj3B-0iN0g:1pgXf2:bezXrMH3JagHMAl2zHHH_1dF7NjK2yDOQs65Ed3YzJw','2023-04-09 21:12:20.203785');

/*Table structure for table `tickets_issue` */

DROP TABLE IF EXISTS `tickets_issue`;

CREATE TABLE `tickets_issue` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `userId_id` int(11) DEFAULT NULL,
  `issue_type_id` bigint(20) DEFAULT NULL,
  `create_date` datetime(6) DEFAULT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `update_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_issue_userId_id_64e34315_fk_auth_user_id` (`userId_id`),
  KEY `tickets_issue_issue_type_id_5f4c35df_fk_tickets_issue_type_id` (`issue_type_id`),
  CONSTRAINT `tickets_issue_issue_type_id_5f4c35df_fk_tickets_issue_type_id` FOREIGN KEY (`issue_type_id`) REFERENCES `tickets_issue_type` (`id`),
  CONSTRAINT `tickets_issue_userId_id_64e34315_fk_auth_user_id` FOREIGN KEY (`userId_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_issue` */

insert  into `tickets_issue`(`id`,`title`,`description`,`is_delete`,`userId_id`,`issue_type_id`,`create_date`,`history`,`update_date`) values (2,'Cannot pay my plan','Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.',0,NULL,1,'2023-03-24 14:41:33.854463',NULL,'2023-03-24 14:41:33.854463'),(3,'Cannot pay my plan','Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.',0,NULL,1,'2023-03-24 14:41:47.321106',NULL,'2023-03-24 14:41:47.321106');

/*Table structure for table `tickets_issue_comment` */

DROP TABLE IF EXISTS `tickets_issue_comment`;

CREATE TABLE `tickets_issue_comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `comment` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `issue_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_issue_comment_owner_id_52740d5e_fk_auth_user_id` (`owner_id`),
  KEY `tickets_issue_comment_issue_id_a5dfd0a7_fk_tickets_issue_id` (`issue_id`),
  CONSTRAINT `tickets_issue_comment_issue_id_a5dfd0a7_fk_tickets_issue_id` FOREIGN KEY (`issue_id`) REFERENCES `tickets_issue` (`id`),
  CONSTRAINT `tickets_issue_comment_owner_id_52740d5e_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_issue_comment` */

/*Table structure for table `tickets_issue_comment_file` */

DROP TABLE IF EXISTS `tickets_issue_comment_file`;

CREATE TABLE `tickets_issue_comment_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `comment_file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `comment_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_issue_commen_comment_id_7deb010d_fk_tickets_i` (`comment_id`),
  CONSTRAINT `tickets_issue_commen_comment_id_7deb010d_fk_tickets_i` FOREIGN KEY (`comment_id`) REFERENCES `tickets_issue_comment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_issue_comment_file` */

/*Table structure for table `tickets_issue_file` */

DROP TABLE IF EXISTS `tickets_issue_file`;

CREATE TABLE `tickets_issue_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `issue_file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `issue_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_issue_file_issue_id_c6e140b4_fk_tickets_issue_id` (`issue_id`),
  CONSTRAINT `tickets_issue_file_issue_id_c6e140b4_fk_tickets_issue_id` FOREIGN KEY (`issue_id`) REFERENCES `tickets_issue` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_issue_file` */

/*Table structure for table `tickets_issue_responders` */

DROP TABLE IF EXISTS `tickets_issue_responders`;

CREATE TABLE `tickets_issue_responders` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `issue_id` bigint(20) DEFAULT NULL,
  `responder_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_issue_responders_responder_id_2dce4fd1_fk_auth_user_id` (`responder_id`),
  KEY `tickets_issue_responders_issue_id_0cfbff20_fk_tickets_issue_id` (`issue_id`),
  CONSTRAINT `tickets_issue_responders_issue_id_0cfbff20_fk_tickets_issue_id` FOREIGN KEY (`issue_id`) REFERENCES `tickets_issue` (`id`),
  CONSTRAINT `tickets_issue_responders_responder_id_2dce4fd1_fk_auth_user_id` FOREIGN KEY (`responder_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_issue_responders` */

/*Table structure for table `tickets_issue_type` */

DROP TABLE IF EXISTS `tickets_issue_type`;

CREATE TABLE `tickets_issue_type` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_issue_type` */

insert  into `tickets_issue_type`(`id`,`name`,`is_delete`) values (1,'Billing',0);

/*Table structure for table `tickets_task` */

DROP TABLE IF EXISTS `tickets_task`;

CREATE TABLE `tickets_task` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `due_date` datetime(6) DEFAULT NULL,
  `urgency` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `status` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `task_percentage` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_task_category_id_9d27844c_fk_tickets_task_category_id` (`category_id`),
  KEY `tickets_task_owner_id_f2f65557_fk_auth_user_id` (`owner_id`),
  CONSTRAINT `tickets_task_category_id_9d27844c_fk_tickets_task_category_id` FOREIGN KEY (`category_id`) REFERENCES `tickets_task_category` (`id`),
  CONSTRAINT `tickets_task_owner_id_f2f65557_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task` */

insert  into `tickets_task`(`id`,`title`,`description`,`due_date`,`urgency`,`create_date`,`update_date`,`status`,`is_delete`,`category_id`,`end_date`,`owner_id`,`task_percentage`) values (1,'sample','sample',NULL,'Low','2023-05-29 07:12:56.404229','2023-05-29 07:12:56.404229','Pending',0,15,NULL,25,0),(2,'Bag Design','Bag design Descriptions',NULL,'Low','2023-05-29 16:33:41.815858','2023-05-29 16:33:41.815858','Open',0,27,NULL,25,0),(3,'Email','Email Design Description',NULL,'Low','2023-05-29 16:34:54.984123','2023-05-29 16:34:54.984123','In Progress',0,21,NULL,25,40),(4,'Education Title','Education Description',NULL,'Low','2023-05-29 16:35:18.725196','2023-05-29 16:35:18.725196','Complete',0,28,NULL,25,100);

/*Table structure for table `tickets_task_category` */

DROP TABLE IF EXISTS `tickets_task_category`;

CREATE TABLE `tickets_task_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `short_description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `parent` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `theme_id` bigint(20) DEFAULT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_task_categor_theme_id_5620036a_fk_tickets_t` (`theme_id`),
  CONSTRAINT `tickets_task_categor_theme_id_5620036a_fk_tickets_t` FOREIGN KEY (`theme_id`) REFERENCES `tickets_task_cetegory_theme` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=313 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_category` */

insert  into `tickets_task_category`(`id`,`name`,`short_description`,`is_delete`,`parent`,`theme_id`,`status`) values (1,'Branding','Branding',0,'0',2,1),(2,'2D Logo Design','2D Logo Design',0,'1',2,1),(3,'3D Logo Design','3D Logo Design',0,'1',2,1),(4,'Business Card Design','Business Card Design',0,'1',2,1),(5,'Tag and Label Desgin','Tag and Label Desgin',0,'1',2,1),(6,'2D Packaging Design','2D Packaging Design',0,'1',2,1),(7,'3D Packaging Design','3D Packaging Design',0,'1',2,1),(8,'Letterhead Design','Letterhead Design',0,'1',2,1),(9,'Envelope Design','Envelope Design',0,'1',2,1),(10,'Font and Typography','Font and Typography',0,'1',2,1),(11,'QR Code Design','QR Code Design',0,'1',2,1),(12,'Reports and Presentation','Reports and Presentation',0,'0',2,1),(13,'Presentation Design','Presentation Design',0,'12',2,1),(14,'Documentation Design','Documentation Design',0,'12',2,1),(15,'Infographic Design','Infographic Design',0,'12',2,1),(16,'Outdoor and Signage','Outdoor and Signage',0,'0',2,1),(17,'Signage Design','Signage Design',0,'16',2,1),(18,'Automobile Wraps','Automobile Wraps',0,'16',2,1),(19,'Trade Show Booth Design','Trade Show Booth Design',0,'16',2,1),(20,'Business and Marketing','Business and Marketing',0,'0',2,1),(21,'Email Design','Email Design',0,'20',2,1),(22,'Social Media Design','Social Media Design',0,'20',2,1),(23,'Advertising Design','Advertising Design',0,'20',2,1),(24,'Merchandise Design','Merchandise Design',0,'0',2,1),(25,'T-Shirt Merchandise','T-Shirt Merchandise',0,'24',2,1),(26,'Party Supplies','Party Supplies',0,'24',2,1),(27,'Bag Design','Bag Design',0,'24',2,1),(28,'Educational','Educational',0,'24',2,1),(29,'Promotional Gifts','Promotional Gifts',0,'24',2,1),(30,'Gadget Accessories','Gadget Accessories',0,'24',2,1),(31,'Print Design','Print Design',0,'0',2,1),(32,'Card Design','Card Design',0,'31',2,1),(33,'Poster Design','Poster Design',0,'31',2,1),(34,'Book & Magazines Design','Book & Magazines Design',0,'31',2,1),(35,'Sticker Design','Sticker Design',0,'31',2,1),(36,'Banner Design','Banner Design',0,'31',2,1),(37,'Flyer Design','Flyer Design',0,'31',2,1),(38,'Gift Certificates & Tickets Design','Gift Certificates & Tickets Design',0,'31',2,1),(39,'Fashion Design','Fashion Design',0,'0',2,1),(40,'Costume Design','Costume Design',0,'39',2,1),(41,'Line Sheet Design','Line Sheet Design',0,'39',2,1),(42,'2D Fashion Design','2D Fashion Design',0,'39',2,1),(43,'3D Fashion Design','3D Fashion Design',0,'39',2,1),(44,'PHOTO EDITING','PHOTO EDITING',0,'0',2,1),(45,'Image Enhancement','Image Enhancement',0,'44',2,1),(46,'Image Editing','Image Editing',0,'44',2,1),(47,'Photo Manipulation','Photo Manipulation',0,'44',2,1),(48,'Photo Clipping','Photo Clipping',0,'44',2,1),(49,'Photo Retouching','Photo Retouching',0,'44',2,1),(50,'Photo Colorization','Photo Colorization',0,'44',2,1),(51,'Photo Restoration','Photo Restoration',0,'44',2,1),(52,'Photo Montage','Photo Montage',0,'44',2,1),(53,'RAW Image Conversion','RAW Image Conversion',0,'44',2,1),(54,'Panoramic Photo Stitching','Panoramic Photo Stitching',0,'44',2,1),(55,'Portrait Editing','Portrait Editing',0,'44',2,1),(56,'Digital Art & Illustration','Digital Art & Illustration',0,'0',2,1),(57,'3D Icon Design','3D Icon Design	',0,'56',2,1),(58,'2D Character','2D Character\r\n',0,'56',2,1),(59,'2D Flat Illustration','2D Flat Illustration\r\n\n',0,'56',2,1),(60,'3D Modeling','3D Modeling',0,'56',2,1),(61,'3D Character','3D Character',0,'56',2,1),(62,'3D Sculpting Design','3D Sculpting Design',0,'56',2,1),(63,'Vector Design','Vector Design',0,'56',2,1),(64,'Hand Drawn','Hand Drawn',0,'56',2,1),(65,'Character Illustration','Character Illustration',0,'56',2,1),(66,'Storyboards','Storyboards',0,'56',2,1),(67,'Tattoo Design','Tattoo Design',0,'56',2,1),(68,'NFT Art','NFT Art',0,'56',2,1),(69,'Editorial Illustration','Editorial Illustration',0,'56',2,1),(70,'Product Design And Engineering','Product Design And Engineering',0,'0',2,1),(71,'Civil & Structural Engineering Design','Civil & Structural Engineering Design',0,'70',2,1),(72,'Mechanical Engineering Design','Mechanical Engineering Design',0,'70',2,1),(73,'Industrial Product Design','Industrial Product Design',0,'70',2,1),(74,'Electrical & Electronics Design','Electrical & Electronics Design',0,'70',2,1),(75,'Architectural Design','Architectural Design',0,'0',2,1),(76,'3D Rendering','3D Rendering',0,'75',2,1),(77,'2D Interior & Exterior Design','2D Interior & Exterior Design',0,'75',2,1),(78,'3D Interior & Exterior Design','3D Interior & Exterior Design',0,'75',2,1),(79,'Diagrams and Mapping','Diagrams and Mapping',0,'75',2,1),(80,'Conceptual Design','Conceptual Design',0,'75',2,1),(81,'Digital Design','Digital Design',0,'0',2,1),(82,'Web and App Design','Web and App Design',0,'81',2,1),(83,'Game Design','Game Design',0,'81',2,1),(84,'VIDEO EDITING','VIDEO EDITING',0,'0',3,1),(85,'Business & Marketing','Business & Marketing',0,'84',3,1),(86,'Informational','Informational',0,'84',3,1),(87,'Entertainment','Entertainment',0,'84',3,1),(88,'Events','Events',0,'84',3,1),(89,'Social content','Social content',0,'84',3,1),(90,'ANIMATION','ANIMATION',0,'0',3,1),(91,'Web Animation','Web Animation',0,'90',3,1),(92,'2D Animation','2D Animation	',0,'90',3,1),(93,'3D Animation','3D Animation',0,'90',3,1),(94,'Stop Motion Animation','Stop Motion Animation',0,'90',3,1),(95,'VFX SERVICES','VFX SERVICES',0,'0',3,1),(96,'Compositing','Compositing',0,'95',3,1),(97,'Matte painting','Matte painting',0,'95',3,1),(98,'3D modeling','3D modeling',0,'95',3,1),(99,'Motion graphics','Motion graphics',0,'95',3,1),(100,'Rotoscoping','Rotoscoping',0,'95',3,1),(101,'Simulation','Simulation',0,'95',3,1),(102,'Texturing','Texturing',0,'95',3,1),(103,'MUSIC AND AUDIO','MUSIC AND AUDIO',0,'0',3,1),(104,'Podcast Editing & Production','Podcast Editing & Production',0,'103',3,1),(105,'Voice-over','Voice-over',0,'103',3,1),(106,'Audio Ads Production','Audio Ads Production',0,'103',3,1),(107,'Audiobook Production','Audiobook Production',0,'103',3,1),(108,'Dialogue Editing','Dialogue Editing',0,'103',3,1),(109,'Music Production & Composition','Music Production & Composition',0,'103',3,1),(110,'Music Transcription','Music Transcription',0,'103',3,1),(111,'Producer Tags','Producer Tags',0,'103',3,1),(112,'Audio Logo & Sonic Branding','Audio Logo & Sonic Branding',0,'103',3,1),(113,'Content Writing','Content Writing',0,'0',4,1),(114,'Advertisement and Sales','Advertisement and Sales',0,'113',4,1),(115,'Social Media','Social Media',0,'113',4,1),(116,'Articles & Blogs','Articles & Blogs',0,'113',4,1),(117,'Book & E-book','Book & E-book',0,'113',4,1),(118,'E-Learning','E-Learning',0,'113',4,1),(119,'Creative','Creative',0,'113',4,1),(120,'Website & Chatbot Content','Website & Chatbot Content',0,'113',4,1),(121,'Email Writing','Email Writing',0,'113',4,1),(122,'Scriptwriting','Scriptwriting',0,'113',4,1),(123,'Speech Writing','Speech Writing',0,'113',4,1),(124,'Professional & Business Writing','Professional & Business Writing',0,'0',4,1),(125,'Careers','Careers',0,'124',4,1),(126,'Legal','Legal',0,'124',4,1),(127,'Technical','Technical',0,'124',4,1),(128,'Business Reports','Business Reports',0,'124',4,1),(129,'Business Proposals','Business Proposals',0,'124',4,1),(130,'Business Letters','Business Letters',0,'124',4,1),(131,'Journalism Writing','Journalism Writing',0,'0',4,1),(132,'News','News',0,'131',4,1),(133,'Sports','Sports',0,'131',4,1),(134,'Editorials','Editorials',0,'131',4,1),(135,'Features','Features',0,'131',4,1),(136,'Proofreading & Editing','Proofreading & Editing',0,'0',4,1),(137,'Proofreading','Proofreading',0,'136',4,1),(138,'Editing','Editing',0,'136',4,1),(139,'Translation & Transcription','Translation & Transcription	',0,'0',4,1),(140,'Translation','Translation',0,'139',4,1),(141,'Transcription','Transcription',0,'139',4,1),(142,'Subtitling','Subtitling',0,'139',4,1),(143,'Human Resource Management & Recruitment','Human Resource Management & Recruitment',0,'0',5,1),(144,'Payroll & Compensation Management','Payroll & Compensation Management',0,'143',5,1),(145,'Recruitment and Selection','Recruitment and Selection',0,'143',5,1),(146,'Organizational Development','Organizational Development',0,'143',5,1),(147,'Performance Management','Performance Management',0,'143',5,1),(148,'Benefits and Rewards Management','Benefits and Rewards Management',0,'143',5,1),(149,'Employee Training & Development','Employee Training & Development',0,'143',5,1),(150,'Ecommerce Store Management','Ecommerce Store Management',0,'0',5,1),(151,'Store Set Up','Store Set Up',0,'150',5,1),(152,'Channel Management','Channel Management',0,'150',5,1),(153,'Order Management','Order Management',0,'150',5,1),(154,'Product Management','Product Management',0,'150',5,1),(155,'Inventory Management','Inventory Management',0,'150',5,1),(156,'Customer Segmentation','Customer Segmentation',0,'150',5,1),(157,'Customer Service and Support','Customer Service and Support',0,'150',5,1),(158,'Project Management & Coordination','Project Management & Coordination',0,'0',5,1),(159,'Project Planning & Scheduling','Project Planning & Scheduling',0,'158',5,1),(160,'Team Management','Team Management',0,'158',5,1),(161,'Resource Management','Resource Management',0,'158',5,1),(162,'Quality Management','Quality Management',0,'158',5,1),(163,'Change Management','Change Management',0,'158',5,1),(164,'Risk Management','Risk Management',0,'158',5,1),(165,'Configuration Management','Configuration Management',0,'158',5,1),(166,'Integration Management','Integration Management',0,'158',5,1),(167,'Transition Management','Transition Management',0,'158',5,1),(168,'Business Development','Business Development',0,'0',5,1),(169,'Expansion and Growth Strategy','Expansion and Growth Strategy',0,'168',5,1),(170,'Business Development','Business Development',0,'168',5,1),(171,'Business Optimization','Business Optimization',0,'168',5,1),(172,'Sales Pipeline Management','Sales Pipeline Management',0,'0',5,1),(173,'Sales Process Automation','Sales Process Automation',0,'172',5,1),(174,'Community Management & Content Moderation','Community Management & Content Moderation',0,'0',5,1),(175,'Community Management','Community Management',0,'174',5,1),(176,'Content Moderation & Review','Content Moderation & Review',0,'174',5,1),(177,'Event & Travel Management','Event & Travel Management',0,'0',5,1),(178,'Event Planning','Event Planning',0,'177',5,1),(179,'Travel Planning','Travel Planning',0,'177',5,1),(180,'Administrative Support','Administrative Support',0,'0',5,1),(181,'Calendar and E-mail Management','Calendar and E-mail Management',0,'180',5,1),(182,'Document creation and File management','Document creation and File management',0,'180',5,1),(183,'Sales Administration','Sales Administration',0,'180',5,1),(184,'Customer service','Customer service',0,'180',5,1),(185,'Data Collection','Data Collection',0,'0',5,1),(186,'Web Research','Web Research',0,'185',5,1),(187,'Data Mining','Data Mining',0,'185',5,1),(188,'Database Building','Database Building',0,'185',5,1),(189,'Data Verification','Data Verification',0,'185',5,1),(190,'Data Processing','Data Processing',0,'0',5,1),(191,'Database creation and management','Database creation and management',0,'190',5,1),(192,'Data Entry','Data Entry',0,'190',5,1),(193,'Data Annotation','Data Annotation',0,'190',5,1),(194,'Data Conversion & Digitization','Data Conversion & Digitization',0,'190',5,1),(195,'Forms Processing','Forms Processing',0,'190',5,1),(196,'Data Cleansing and Formatting','Data Cleansing and Formatting',0,'190',5,1),(197,'Scanning and Indexing','Scanning and Indexing',0,'190',5,1),(198,'Data Transcription','Data Transcription',0,'190',5,1),(199,'SEARCH ENGINE OPTIMIZATION (SEO)','SEARCH ENGINE OPTIMIZATION (SEO)',0,'0',6,1),(200,'On-Page SEO','On-Page SEO',0,'199',6,1),(201,'Off-Page SEO','Off-Page SEO',0,'199',6,1),(202,'SEO Audit','SEO Audit',0,'199',6,1),(203,'Geo Targeted SEO','Geo Targeted SEO',0,'199',6,1),(204,'Technical SEO','Technical SEO',0,'199',6,1),(205,'Keyword Research','Keyword Research',0,'199',6,1),(206,'Paid Advertising','Paid Advertising',0,'0',6,1),(207,'Display Ads','Display Ads',0,'206',6,1),(208,'Awareness Ads','Awareness Ads',0,'206',6,1),(209,'In-Stream Ads','In-Stream Ads',0,'206',6,1),(210,'Search Ads','Search Ads',0,'206',6,1),(211,'Social Media Ads','Social Media Ads',0,'206',6,1),(212,'Amazon Ads','Amazon Ads',0,'206',6,1),(213,'Addressable Ad Services','Addressable Ad Services',0,'206',6,1),(214,'Media Advertising','Media Advertising',0,'206',6,1),(215,'Social Media Marketing','Social Media Marketing',0,'0',6,1),(216,'Social Media Management','Social Media Management',0,'215',6,1),(217,'Social Media Promotion','Social Media Promotion',0,'215',6,1),(218,'Influencer Marketing','Influencer Marketing',0,'215',6,1),(219,'Content Marketing','Content Marketing',0,'0',6,1),(220,'Lead Magnets','Lead Magnets',0,'219',6,1),(221,'Content Distribution','Content Distribution',0,'219',6,1),(222,'Content Audit','Content Audit',0,'219',6,1),(223,'Guest Posting','Guest Posting',0,'219',6,1),(224,'Affiliate Marketing','Affiliate Marketing',0,'0',6,1),(225,'Affiliate program setup and management','Affiliate program setup and management',0,'224',6,1),(226,'Affiliate Recruitment Management','Affiliate Recruitment Management',0,'224',6,1),(227,'Affiliate Program Audit','Affiliate Program Audit',0,'224',6,1),(228,'Email Marketing','Email Marketing',0,'0',6,1),(229,'Email List Building and Management','Email List Building and Management',0,'228',6,1),(230,'Email Automation','Email Automation',0,'228',6,1),(231,'Email Segmentation and Personalization','Email Segmentation and Personalization',0,'228',6,1),(232,'Email Compliance and Deliverability','Email Compliance and Deliverability',0,'228',6,1),(233,'Email campaign management','Email campaign management',0,'228',6,1),(234,'Marketing Strategy and Research','Marketing Strategy and Research',0,'0',6,1),(235,'Marketing Strategy & Plans','Marketing Strategy & Plans',0,'234',6,1),(236,'Market and Audience Research','Market and Audience Research',0,'234',6,1),(237,'Crowdfunding','Crowdfunding',0,'0',6,1),(238,'Campaign creation and management','Campaign creation and management',0,'237',6,1),(239,'Lead Generation','Lead Generation',0,'0',6,1),(240,'Appointment Setting','Appointment Setting',0,'239',6,1),(241,'Click Funnels','Click Funnels',0,'239',6,1),(242,'Accounting','Accounting',0,'0',7,1),(243,'Bookkeeping','Bookkeeping',0,'242',7,1),(244,'Financial Statement Report & Preperation','Financial Statement Report & Preperation',0,'242',7,1),(245,'Tax Accounting and Preparation','Tax Accounting and Preparation',0,'242',7,1),(246,'Forensic Accounting','Forensic Accounting',0,'242',7,1),(247,'Audits & Assurance','Audits & Assurance',0,'242',7,1),(248,'Budgeting & Forecasting','Budgeting & Forecasting',0,'242',7,1),(249,'Financial Analysis and Valuation','Financial Analysis and Valuation',0,'0',7,1),(250,'Financial Modeling & Forecasting','Financial Modeling & Forecasting',0,'249',7,1),(251,'Credit Analysis','Credit Analysis',0,'249',7,1),(252,'Debt & Loan Valuation','Debt & Loan Valuation',0,'249',7,1),(253,'Equity & Fixed Asset Valuation','Equity & Fixed Asset Valuation',0,'249',7,1),(254,'Financial Analysis','Financial Analysis',0,'249',7,1),(255,'Investment research','Investment research',0,'249',7,1),(256,'Data Warehousing','Data Warehousing',0,'0',8,1),(257,'Data Warehouse Development & Implementation','Data Warehouse Development & Implementation',0,'256',8,1),(258,'Data warehouse migration','Data warehouse migration',0,'256',8,1),(259,'Data warehouse testing','Data warehouse testing',0,'256',8,1),(260,'Data Visualization','Data Visualization',0,'0',8,1),(261,'Data Platform Development','Data Platform Development',0,'260',8,1),(262,'Reports and Dashboards Development and Optimization','Reports and Dashboards Development and Optimization',0,'260',8,1),(263,'Data Engineering','Data Engineering',0,'0',8,1),(264,'Data Processing','Data Processing',0,'263',8,1),(265,'Data Storage','Data Storage',0,'263',8,1),(266,'Data Preparation and ETL/ELT','Data Preparation and ETL/ELT',0,'263',8,1),(267,'Data Lake Implementation','Data Lake Implementation',0,'263',8,1),(268,'Modern Data Pipelines','Modern Data Pipelines',0,'263',8,1),(269,'Data Science','Data Science',0,'0',8,1),(270,'Machine Learning Implementation','Machine Learning Implementation',0,'269',8,1),(271,'NLP, Voice & Image\nAnalytics','NLP, Voice & Image\r\nAnalytics',0,'269',8,1),(272,'Statistical Analysis & Optimization','Statistical Analysis & Optimization',0,'269',8,1),(273,'Business Analytics','Business Analytics',0,'0',8,1),(274,'Marketing Analytics','Marketing Analytics',0,'273',8,1),(275,'Sales Analytics','Sales Analytics',0,'273',8,1),(276,'Financial Analytics','Financial Analytics',0,'273',8,1),(277,'Operations Analytics','Operations Analytics',0,'273',8,1),(278,'Ecommerce Analytics','Ecommerce Analytics',0,'273',8,1),(279,'IT Analytics','IT Analytics',0,'273',8,1),(280,'Design and Art Analyrtics','Design and Art Analyrtics',0,'273',8,1),(281,'Blockchain Development','Blockchain Development',0,'0',9,1),(282,'Blockchain Development','Blockchain Development\r\n',0,'281',9,1),(283,'NFT Development','NFT Development',0,'281',9,1),(284,'Game Development','Game Development',0,'0',9,1),(285,'Cross Platform Game Development','Cross Platform Game Development',0,'284',9,1),(286,'Web-Based Game Development','Web-Based Game Development',0,'284',9,1),(287,'Mobile Game Development','Mobile Game Development',0,'284',9,1),(288,'PC Game Development','PC Game Development',0,'284',9,1),(289,'Web3 Game Development','Web3 Game Development',0,'284',9,1),(290,'Immersive Technology Game Development','Immersive Technology Game Development',0,'284',9,1),(291,'Game Testing','Game Testing',0,'284',9,1),(292,'Web & Software Development','Web & Software Development ',0,'0',9,1),(293,'Mobile Application Dvelopment','Mobile Application Dvelopment',0,'292',9,1),(294,'Development for Streamers','Development for Streamers',0,'292',9,1),(295,'Desktop Application Development','Desktop Application Development',0,'292',9,1),(296,'Website and Software Development','Website and Software Development',0,'292',9,1),(297,'QA Testing','QA Testing',0,'292',9,1),(298,'Software Architecture','Software Architecture',0,'0',9,1),(299,'System Design and Architecture','System Design and Architecture',0,'298',9,1),(300,'Artificial Inteligence Development','Artificial Inteligence Development',0,'0',9,1),(301,'Machine Learning Development','Machine Learning Development',0,'300',9,1),(302,'Natural Language Processing Development','Natural Language Processing Development',0,'300',9,1),(303,'Computer Vision Development','Computer Vision Development',0,'300',9,1),(304,'Robotic Process Automation Development','Robotic Process Automation Development',0,'300',9,1),(305,'Recommender System Development','Recommender System Development	',0,'300',9,1),(306,'IT Support','IT Support',0,'0',9,1),(307,'Technical Support','Technical Support',0,'306',9,1),(308,'Cloud Support','Cloud Support',0,'306',9,1),(309,'Application Support','Application Support',0,'306',9,1),(310,'Network Support','Network Support',0,'306',9,1),(311,'Database Support','Database Support',0,'306',9,1),(312,'Security Support','Security Support',0,'306',9,1);

/*Table structure for table `tickets_task_cetegory_theme` */

DROP TABLE IF EXISTS `tickets_task_cetegory_theme`;

CREATE TABLE `tickets_task_cetegory_theme` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `short_description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_cetegory_theme` */

insert  into `tickets_task_cetegory_theme`(`id`,`name`,`short_description`,`is_delete`) values (2,'DESIGN AND ART','DESIGN AND ART',0),(3,'CONTENT CREATION','CONTENT CREATION',0),(4,'CONTENT & CREATIVE WRITING','CONTENT & CREATIVE WRITING',0),(5,'BUSINESS & OPERATIONAL ASSISTANCE','BUSINESS & OPERATIONAL ASSISTANCE',0),(6,'MARKETING','MARKETING',0),(7,'ACCOUNTING AND FINANCE','ACCOUNTING AND FINANCE',0),(8,'DATA ANALYTICS','DATA ANALYTICS',0),(9,'TECHNOLOGY & DEVELOPMENT','TECHNOLOGY & DEVELOPMENT',0);

/*Table structure for table `tickets_task_comment` */

DROP TABLE IF EXISTS `tickets_task_comment`;

CREATE TABLE `tickets_task_comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `comment` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `task_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_task_comment_owner_id_1db30347_fk_auth_user_id` (`owner_id`),
  KEY `tickets_task_comment_task_id_39a92026_fk_tickets_task_id` (`task_id`),
  CONSTRAINT `tickets_task_comment_owner_id_1db30347_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `tickets_task_comment_task_id_39a92026_fk_tickets_task_id` FOREIGN KEY (`task_id`) REFERENCES `tickets_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_comment` */

/*Table structure for table `tickets_task_comment_file` */

DROP TABLE IF EXISTS `tickets_task_comment_file`;

CREATE TABLE `tickets_task_comment_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `comment_file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `comment_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_task_comment_comment_id_6678fcee_fk_tickets_t` (`comment_id`),
  CONSTRAINT `tickets_task_comment_comment_id_6678fcee_fk_tickets_t` FOREIGN KEY (`comment_id`) REFERENCES `tickets_task_comment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_comment_file` */

/*Table structure for table `tickets_task_file` */

DROP TABLE IF EXISTS `tickets_task_file`;

CREATE TABLE `tickets_task_file` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `issue_file` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `task_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_tast_file_task_id_2f1f242c_fk_tickets_task_id` (`task_id`),
  CONSTRAINT `tickets_tast_file_task_id_2f1f242c_fk_tickets_task_id` FOREIGN KEY (`task_id`) REFERENCES `tickets_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_file` */

/*Table structure for table `tickets_task_responders` */

DROP TABLE IF EXISTS `tickets_task_responders`;

CREATE TABLE `tickets_task_responders` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  `history` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `responder_id` int(11) DEFAULT NULL,
  `task_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_task_responders_responder_id_1508ba69_fk_auth_user_id` (`responder_id`),
  KEY `tickets_task_responders_task_id_1b5dc036_fk_tickets_task_id` (`task_id`),
  CONSTRAINT `tickets_task_responders_responder_id_1508ba69_fk_auth_user_id` FOREIGN KEY (`responder_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `tickets_task_responders_task_id_1b5dc036_fk_tickets_task_id` FOREIGN KEY (`task_id`) REFERENCES `tickets_task` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_responders` */

/*Table structure for table `tickets_task_services` */

DROP TABLE IF EXISTS `tickets_task_services`;

CREATE TABLE `tickets_task_services` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `short_description` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_task_service_category_id_8b41e46a_fk_tickets_t` (`category_id`),
  CONSTRAINT `tickets_task_service_category_id_8b41e46a_fk_tickets_t` FOREIGN KEY (`category_id`) REFERENCES `tickets_task_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Data for the table `tickets_task_services` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
