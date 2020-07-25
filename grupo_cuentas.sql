-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.13-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para grupo_cuentas
CREATE DATABASE IF NOT EXISTS `grupo_cuentas` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `grupo_cuentas`;

-- Volcando estructura para tabla grupo_cuentas.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla grupo_cuentas.grupo: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`id`, `descripcion`) VALUES
	(1, 'Activos'),
	(2, 'Pasivos'),
	(3, 'Patrimonio'),
	(4, 'Ingreso'),
	(5, 'Prueba'),
	(6, '11111');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla grupo_cuentas.pcuenta
CREATE TABLE IF NOT EXISTS `pcuenta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT NULL,
  `grupo` int(11) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `naturaleza` varchar(50) DEFAULT NULL,
  `estado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grupo` (`grupo`),
  CONSTRAINT `FK_Pcuenta_grupo` FOREIGN KEY (`grupo`) REFERENCES `grupo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla grupo_cuentas.pcuenta: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `pcuenta` DISABLE KEYS */;
INSERT INTO `pcuenta` (`id`, `codigo`, `grupo`, `descripcion`, `naturaleza`, `estado`) VALUES
	(1, '0', 1, 'Caja', 'D', 1);
/*!40000 ALTER TABLE `pcuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
