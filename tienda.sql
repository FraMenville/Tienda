-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2024 a las 20:37:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tienda`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin_window`
--

CREATE TABLE `admin_window` (
  `Usuario` varchar(10) NOT NULL,
  `contraseña` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `admin_window`
--

INSERT INTO `admin_window` (`Usuario`, `contraseña`) VALUES
('Admin', 123456);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--
-- Error leyendo la estructura de la tabla tienda.productos: #1932 - Table &#039;tienda.productos&#039; doesn&#039;t exist in engine
-- Error leyendo datos de la tabla tienda.productos: #1064 - Algo está equivocado en su sintax cerca &#039;FROM `tienda`.`productos`&#039; en la linea 1

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos1`
--

CREATE TABLE `productos1` (
  `id` int(10) NOT NULL,
  `Articulo` varchar(50) NOT NULL,
  `Precio` float NOT NULL,
  `Descripcion` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos1`
--

INSERT INTO `productos1` (`id`, `Articulo`, `Precio`, `Descripcion`) VALUES
(1, 'Sandia', 500, 'Sandia traida desde el Vaticano, vendecida por los mismos dioses\n'),
(2, 'Patilla', 100, 'Patilla del campo comun\n'),
(3, 'Arroz', 50, 'Arroz tipo 1\n'),
(4, 'Perico', 50, 'Pajaro de dudosa procedencia\n');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos1`
--
ALTER TABLE `productos1`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos1`
--
ALTER TABLE `productos1`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
