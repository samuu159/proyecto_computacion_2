-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: bxlfjozyadylicrojiil-mysql.services.clever-cloud.com:3306
-- Tiempo de generación: 13-03-2024 a las 10:23:03
-- Versión del servidor: 8.0.22-13
-- Versión de PHP: 8.2.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bxlfjozyadylicrojiil`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Arbitros`
--

CREATE TABLE `Arbitros` (
  `id` int NOT NULL,
  `arbitro` varchar(255) DEFAULT NULL,
  `partidos_jugados` int DEFAULT NULL,
  `penaltis_pitados` int DEFAULT NULL,
  `promedio_penalti` decimal(5,2) DEFAULT NULL,
  `tarjetas_amarillas` int DEFAULT NULL,
  `promedio_amarilla` decimal(5,2) DEFAULT NULL,
  `tarjetas_rojas` int DEFAULT NULL,
  `promedio_roja` decimal(5,2) DEFAULT NULL,
  `doble_amarilla` int DEFAULT NULL,
  `promedio_doble_amarilla` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `Arbitros`
--

INSERT INTO `Arbitros` (`id`, `arbitro`, `partidos_jugados`, `penaltis_pitados`, `promedio_penalti`, `tarjetas_amarillas`, `promedio_amarilla`, `tarjetas_rojas`, `promedio_roja`, `doble_amarilla`, `promedio_doble_amarilla`) VALUES
(23, 'César Soto Grado', 22, 3, 0.14, 118, 5.36, 4, 0.18, 0, 0.00),
(24, 'Jorge Figueroa Vázquez', 18, 2, 0.11, 70, 3.89, 7, 0.39, 0, 0.00),
(25, 'Pablo González Fuertes', 17, 7, 0.41, 67, 3.94, 5, 0.29, 0, 0.00),
(26, 'Miguel Ángel Ortiz Arias', 17, 3, 0.18, 66, 3.88, 7, 0.41, 0, 0.00),
(27, 'Guillermo Cuadra Fernández', 21, 4, 0.19, 114, 5.43, 7, 0.33, 0, 0.00),
(28, 'Jesús Gil Manzano', 24, 7, 0.29, 98, 4.08, 1, 0.04, 0, 0.00),
(29, 'Javier Iglesias Villanueva', 17, 5, 0.29, 76, 4.47, 1, 0.06, 0, 0.00),
(30, 'Juan Luis Pulido Santana', 16, 15, 0.94, 80, 5.00, 3, 0.19, 0, 0.00),
(31, 'Mateo Busquets Ferrer', 17, 4, 0.24, 93, 5.47, 7, 0.41, 0, 0.00),
(32, 'Alejandro Muñiz Ruiz', 19, 7, 0.37, 98, 5.16, 4, 0.21, 0, 0.00),
(33, 'José María Sánchez Martínez', 23, 2, 0.09, 119, 5.17, 3, 0.13, 0, 0.00),
(34, 'Ricardo De Burgos Bengoetxea', 20, 6, 0.30, 77, 3.85, 5, 0.25, 0, 0.00),
(35, 'Isidro Díaz de Mera Escuderos', 16, 5, 0.31, 77, 4.81, 3, 0.19, 0, 0.00),
(36, 'Víctor García Verdura', 16, 7, 0.44, 71, 4.44, 4, 0.25, 0, 0.00),
(37, 'Francisco José Hernández Maeso', 16, 4, 0.25, 76, 4.75, 1, 0.06, 0, 0.00),
(38, 'Jose Luis Munuera Montero', 18, 6, 0.33, 97, 5.39, 4, 0.22, 0, 0.00),
(39, 'Javier Alberola Rojas', 18, 7, 0.39, 58, 3.22, 2, 0.11, 0, 0.00),
(40, 'Alejandro Hernández Hernández', 18, 7, 0.39, 97, 5.39, 7, 0.39, 0, 0.00),
(41, 'Juan Martínez Munuera', 16, 6, 0.38, 65, 4.06, 5, 0.31, 0, 0.00),
(42, 'Mario Melero López', 14, 1, 0.07, 59, 4.21, 1, 0.07, 0, 0.00);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Equipos`
--

CREATE TABLE `Equipos` (
  `Id_equipo` int NOT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `Partidos` int DEFAULT NULL,
  `Victorias` int DEFAULT NULL,
  `Empates` int DEFAULT NULL,
  `Derrotas` int DEFAULT NULL,
  `Puntos` int DEFAULT NULL,
  `Jornada_1` int DEFAULT NULL,
  `Jornada_2` int DEFAULT NULL,
  `Jornada_3` int DEFAULT NULL,
  `Jornada_4` int DEFAULT NULL,
  `Jornada_5` int DEFAULT NULL,
  `Jornada_6` int DEFAULT NULL,
  `Jornada_7` int DEFAULT NULL,
  `Jornada_8` int DEFAULT NULL,
  `Jornada_9` int DEFAULT NULL,
  `Jornada_10` int DEFAULT NULL,
  `Jornada_11` int DEFAULT NULL,
  `Jornada_12` int DEFAULT NULL,
  `Jornada_13` int DEFAULT NULL,
  `Jornada_14` int DEFAULT NULL,
  `Jornada_15` int DEFAULT NULL,
  `Jornada_16` int DEFAULT NULL,
  `Jornada_17` int DEFAULT NULL,
  `Jornada_18` int DEFAULT NULL,
  `Jornada_19` int DEFAULT NULL,
  `Jornada_20` int DEFAULT NULL,
  `Jornada_21` int DEFAULT NULL,
  `Jornada_22` int DEFAULT NULL,
  `Jornada_23` int DEFAULT NULL,
  `Jornada_24` int DEFAULT NULL,
  `Jornada_25` int DEFAULT NULL,
  `Jornada_26` int DEFAULT NULL,
  `Jornada_27` int DEFAULT NULL,
  `Jornada_28` int DEFAULT NULL,
  `Jornada_29` int DEFAULT NULL,
  `Jornada_30` int DEFAULT NULL,
  `Jornada_31` int DEFAULT NULL,
  `Jornada_32` int DEFAULT NULL,
  `Jornada_33` int DEFAULT NULL,
  `Jornada_34` int DEFAULT NULL,
  `Jornada_35` int DEFAULT NULL,
  `Jornada_36` int DEFAULT NULL,
  `Jornada_37` int DEFAULT NULL,
  `Jornada_38` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Jugadores`
--

CREATE TABLE `Jugadores` (
  `Id_Jugador` int NOT NULL,
  `Id_usuario` int DEFAULT NULL,
  `Nombre` varchar(30) DEFAULT NULL,
  `Apellido` varchar(30) DEFAULT NULL,
  `Equipo` varchar(50) DEFAULT NULL,
  `Posicion` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Valor` decimal(10,2) DEFAULT NULL,
  `Puntos_totales` int DEFAULT NULL,
  `Media_total` decimal(5,2) DEFAULT NULL,
  `Partidos` int DEFAULT NULL,
  `Goles` int DEFAULT NULL,
  `Tarjetas` int DEFAULT NULL,
  `Media_en_casa` decimal(5,2) DEFAULT NULL,
  `Media_visitante` decimal(5,2) DEFAULT NULL,
  `Valor_subido_bajado` decimal(10,2) DEFAULT NULL,
  `Mercado` binary(50) DEFAULT NULL,
  `Puntos_predicción` decimal(20,6) DEFAULT NULL,
  `Valor_predicción` decimal(10,2) DEFAULT NULL,
  `Jornada_1` varchar(50) DEFAULT NULL,
  `Jornada_2` varchar(50) DEFAULT NULL,
  `Jornada_3` varchar(50) DEFAULT NULL,
  `Jornada_4` varchar(50) DEFAULT NULL,
  `Jornada_5` varchar(50) DEFAULT NULL,
  `Jornada_6` varchar(50) DEFAULT NULL,
  `Jornada_7` varchar(50) DEFAULT NULL,
  `Jornada_8` varchar(50) DEFAULT NULL,
  `Jornada_9` varchar(50) DEFAULT NULL,
  `Jornada_10` varchar(50) DEFAULT NULL,
  `Jornada_11` varchar(50) DEFAULT NULL,
  `Jornada_12` varchar(50) DEFAULT NULL,
  `Jornada_13` varchar(50) DEFAULT NULL,
  `Jornada_14` varchar(50) DEFAULT NULL,
  `Jornada_15` varchar(50) DEFAULT NULL,
  `Jornada_16` varchar(50) DEFAULT NULL,
  `Jornada_17` varchar(50) DEFAULT NULL,
  `Jornada_18` varchar(50) DEFAULT NULL,
  `Jornada_19` varchar(50) DEFAULT NULL,
  `Jornada_21` varchar(50) DEFAULT NULL,
  `Jornada_20` varchar(50) DEFAULT NULL,
  `Jornada_22` varchar(50) DEFAULT NULL,
  `Jornada_23` varchar(50) DEFAULT NULL,
  `Jornada_24` varchar(50) DEFAULT NULL,
  `Jornada_25` varchar(50) DEFAULT NULL,
  `Jornada_26` varchar(50) DEFAULT NULL,
  `Jornada_27` varchar(50) DEFAULT NULL,
  `Jornada_28` varchar(50) DEFAULT NULL,
  `Jornada_29` varchar(50) DEFAULT NULL,
  `Jornada_30` varchar(50) DEFAULT NULL,
  `Jornada_31` varchar(50) DEFAULT NULL,
  `Jornada_32` varchar(50) DEFAULT NULL,
  `Jornada_33` varchar(50) DEFAULT NULL,
  `Jornada_34` varchar(50) DEFAULT NULL,
  `Jornada_35` varchar(50) DEFAULT NULL,
  `Jornada_36` varchar(50) DEFAULT NULL,
  `Jornada_37` varchar(50) DEFAULT NULL,
  `Jornada_38` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `Jugadores`
--

INSERT INTO `Jugadores` (`Id_Jugador`, `Id_usuario`, `Nombre`, `Apellido`, `Equipo`, `Posicion`, `Valor`, `Puntos_totales`, `Media_total`, `Partidos`, `Goles`, `Tarjetas`, `Media_en_casa`, `Media_visitante`, `Valor_subido_bajado`, `Mercado`, `Puntos_predicción`, `Valor_predicción`, `Jornada_1`, `Jornada_2`, `Jornada_3`, `Jornada_4`, `Jornada_5`, `Jornada_6`, `Jornada_7`, `Jornada_8`, `Jornada_9`, `Jornada_10`, `Jornada_11`, `Jornada_12`, `Jornada_13`, `Jornada_14`, `Jornada_15`, `Jornada_16`, `Jornada_17`, `Jornada_18`, `Jornada_19`, `Jornada_21`, `Jornada_20`, `Jornada_22`, `Jornada_23`, `Jornada_24`, `Jornada_25`, `Jornada_26`, `Jornada_27`, `Jornada_28`, `Jornada_29`, `Jornada_30`, `Jornada_31`, `Jornada_32`, `Jornada_33`, `Jornada_34`, `Jornada_35`, `Jornada_36`, `Jornada_37`, `Jornada_38`) VALUES
(1, NULL, 'Jude', 'Bellingham', 'Real Madrid', '', 25042000.00, 210, 9.50, 22, 16, 6, 9.50, 9.60, -5000.00, NULL, NULL, NULL, '19', '12', '12', '4', '3', '', '14', '18', '6', '18', '7', '', '11', '5', '11', '12', '3', '4', '5', 'Sancionado', '10', '5', '18', 'Lesionado', 'Lesionado', '-1', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, NULL, 'Ante', 'Budimir', 'Osasuna', '', 16552000.00, 184, 6.80, 27, 14, 4, 8.00, 5.50, 68000.00, NULL, NULL, NULL, '3', '4', '2', '10', '3', '6', '10', '0', '16', '3', '16', '10', '4', '7', '8', '3', '2', '11', '2', '8', '4', '4', '10', '16', '2', '11', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, NULL, 'Borja', 'Mayoral', 'Getafe', '', 18773000.00, 175, 6.50, 27, 15, 2, 6.60, 6.40, -43000.00, NULL, NULL, NULL, '2', '10', '9', '3', '9', '2', '5', '12', '10', '3', '10', '9', '10', '2', '10', '10', '17', '3', '2', '10', '9', '3', '9', '2', '0', '2', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, NULL, NULL, 'Isco', 'Betis', '', 18928000.00, 174, 7.90, 22, 6, 7, 9.30, 6.50, -68000.00, NULL, NULL, NULL, '6', '11', '8', '2', '6', '6', '7', '5', '7', '15', '7', '9', '6', '2', '7', '7', 'Sancionado', '6', '12', '8', '18', '10', 'Lesionado', 'Lesionado', 'Lesionado', 'Lesionado', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, NULL, NULL, 'Savio', 'Girona', '', 20075000.00, 169, 6.30, 27, 7, 4, 7.60, 5.00, 12000.00, NULL, NULL, NULL, '6', '6', '5', '13', '13', '6', '1', '3', '10', '5', '5', '10', '7', '5', '5', '6', '6', '9', '3', '4', '9', '7', '1', '3', '16', '3', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, NULL, 'Takefusa', 'Kubo', 'Real Sociedad', '', 20855000.00, 168, 8.00, 21, 7, 2, 8.60, 7.20, 21000.00, NULL, NULL, NULL, '6', '5', '19', '9', '10', '', '13', '3', '7', '6', '7', '3', '5', '8', '14', '7', '6', '7', 'No convocado', 'No convocado', 'No convocado', 'No convocado', '6', '11', '4', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, NULL, 'Antoine', 'Griezmann', 'Atlético', '', 24876000.00, 166, 6.90, 24, 11, 3, 7.80, 6.10, -16000.00, NULL, NULL, NULL, '3', '13', '3', '1', '12', '10', '7', '10', '21', '5', '3', '12', '10', '4', '6', '1', '16', '5', '4', '6', '5', '5', '2', '', 'Lesionado', 'Lesionado', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(8, NULL, 'Inaki', 'Williams', 'Athletic Club', '', 20054000.00, 165, 6.90, 24, 9, 3, 7.20, 6.50, 10000.00, NULL, NULL, NULL, '9', '9', '3', '11', '11', '12', '4', '7', '4', '6', '12', '2', '11', '11', '9', '10', '7', '', 'No convocado', '2', 'No convocado', '5', '3', '10', '3', '3', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(9, NULL, 'Kirian', 'Rodriguez', 'Las Palmas', '', 16962000.00, 162, 6.20, 26, 6, 7, 7.90, 4.50, 54000.00, NULL, NULL, NULL, '4', '6', '3', '4', '13', '3', '6', '5', '4', '5', '13', '3', '6', '9', '11', '5', 'Sancionado', '5', '18', '2', '5', '3', '5', '1', '12', '6', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, NULL, 'Artem', 'Dovbyk', 'Girona', '', 19658000.00, 161, 6.40, 25, 14, 1, 7.40, 5.70, 10000.00, NULL, NULL, NULL, '2', '1', '3', '4', '10', '9', '3', '4', '16', '3', '13', '9', 'Lesionado', '2', '10', '16', '9', '5', '0', '3', '20', 'Lesionado', '1', '3', '1', '3', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, NULL, 'Alvaro', 'Valles', 'Las Palmas', '', 16251000.00, 161, 6.00, 27, 0, 1, 5.80, 6.10, -54000.00, NULL, NULL, NULL, '7', '7', '6', '8', '6', '8', '5', '5', '6', '5', '7', '9', '8', '7', '8', '9', '10', '4', '8', '5', '7', '3', '6', '0', '2', '2', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, NULL, 'Aleix', 'Garcia', 'Girona', '', 20548000.00, 159, 6.10, 26, 3, 4, 6.40, 5.90, -3000.00, NULL, NULL, NULL, '6', '10', '3', '5', '8', '9', '7', '13', '10', '7', '11', '5', '6', '8', '7', '6', '7', '4', '-5', '5', 'Sancionado', '5', '3', '3', '7', '4', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, NULL, NULL, 'Pepelu', 'Valencia', '', 17943000.00, 157, 6.00, 26, 4, 2, 7.20, 4.90, 70000.00, NULL, NULL, NULL, '6', '11', '7', '5', '6', '4', '5', '5', '10', '8', '5', '10', '5', '5', '4', '3', '7', '5', '16', '5', '3', '3', '5', '6', '3', '5', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(14, NULL, 'Ilkay', 'Gundogan', 'Barcelona', '', 20208000.00, 153, 5.70, 27, 5, 3, 5.60, 5.70, 31000.00, NULL, NULL, NULL, '6', '5', '6', '2', '5', '3', '6', '6', '4', '11', '5', '2', '4', '7', '10', '4', '3', '11', '2', '11', '6', '12', '4', '5', '6', '5', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, NULL, 'Jorgen Strand', 'Larsen', 'Celta', '', 14790000.00, 151, 5.60, 27, 9, 4, 4.90, 6.40, -79000.00, NULL, NULL, NULL, '2', '4', '9', '2', '11', '1', '8', '13', '6', '2', '3', '9', '4', '11', '0', '10', '10', '3', '4', '3', '3', '12', '9', '3', '3', '4', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, NULL, 'Lamine', 'Yamal', 'Barcelona', '', 15197000.00, 150, 5.80, 26, 3, 2, 5.40, 6.20, 65000.00, NULL, NULL, NULL, '8', '10', '5', '3', '2', '6', '5', '9', '3', '2', '3', '5', '6', '5', '3', '2', '3', '2', '7', '8', '11', '8', '16', '9', '', '5', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, NULL, 'Martin', 'Zubimendi', 'Real Sociedad', '', 16128000.00, 148, 5.70, 26, 4, 3, 6.00, 5.40, -25000.00, NULL, NULL, NULL, '5', '5', '11', '7', '4', '4', '6', '3', '3', '6', '6', '10', '6', '5', '12', '7', '5', '12', '2', '6', 'Lesionado', '3', '3', '4', '4', '4', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(18, NULL, 'Fede', 'Valverde', 'Real Madrid', '', 20438000.00, 147, 5.40, 27, 1, 2, 5.80, 5.10, 29000.00, NULL, NULL, NULL, '6', '7', '4', '10', '3', '4', '4', '9', '4', '6', '6', '5', '5', '6', '5', '7', '6', '6', '3', '4', '3', '6', '5', '7', '5', '6', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Partido`
--

CREATE TABLE `Partido` (
  `Id_partido` int NOT NULL,
  `Id_equipo_local` int DEFAULT NULL,
  `Id_equipo_visitante` int DEFAULT NULL,
  `Numero_jornada` int DEFAULT NULL,
  `Fecha` timestamp NULL DEFAULT NULL,
  `Goles_local` int DEFAULT NULL,
  `Goles_visitante` int DEFAULT NULL,
  `Id_arbitro` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuarios`
--

CREATE TABLE `Usuarios` (
  `Id_usuario` int NOT NULL,
  `ADMIN` binary(1) NOT NULL,
  `Nombre` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Apellido` varchar(30) DEFAULT NULL,
  `Correo` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Contraseña` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `Usuarios`
--

INSERT INTO `Usuarios` (`Id_usuario`, `ADMIN`, `Nombre`, `Apellido`, `Correo`, `Contraseña`) VALUES
(1, 0x31, 'Preditech', 'Uem', 'preditechinsightsuem@gmail.com', 'RealMadrid2024'),
(2, 0x30, 'Ivan', 'Garcia', 'ivangarciamoriones23@gmail.com', 'Cloe2016!');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Arbitros`
--
ALTER TABLE `Arbitros`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Equipos`
--
ALTER TABLE `Equipos`
  ADD PRIMARY KEY (`Id_equipo`);

--
-- Indices de la tabla `Jugadores`
--
ALTER TABLE `Jugadores`
  ADD PRIMARY KEY (`Id_Jugador`),
  ADD KEY `Id_usuario` (`Id_usuario`);

--
-- Indices de la tabla `Partido`
--
ALTER TABLE `Partido`
  ADD PRIMARY KEY (`Id_partido`),
  ADD KEY `Id_equipo_local` (`Id_equipo_local`),
  ADD KEY `Id_equipo_visitante` (`Id_equipo_visitante`),
  ADD KEY `fk_partidos_arbitros` (`Id_arbitro`);

--
-- Indices de la tabla `Usuarios`
--
ALTER TABLE `Usuarios`
  ADD PRIMARY KEY (`Id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Arbitros`
--
ALTER TABLE `Arbitros`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `Equipos`
--
ALTER TABLE `Equipos`
  MODIFY `Id_equipo` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Jugadores`
--
ALTER TABLE `Jugadores`
  MODIFY `Id_Jugador` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `Partido`
--
ALTER TABLE `Partido`
  MODIFY `Id_partido` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Usuarios`
--
ALTER TABLE `Usuarios`
  MODIFY `Id_usuario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Jugadores`
--
ALTER TABLE `Jugadores`
  ADD CONSTRAINT `Jugadores_ibfk_1` FOREIGN KEY (`Id_usuario`) REFERENCES `Usuarios` (`Id_usuario`);

--
-- Filtros para la tabla `Partido`
--
ALTER TABLE `Partido`
  ADD CONSTRAINT `fk_partidos_arbitros` FOREIGN KEY (`Id_arbitro`) REFERENCES `Arbitros` (`id`),
  ADD CONSTRAINT `Partido_ibfk_1` FOREIGN KEY (`Id_equipo_local`) REFERENCES `Equipos` (`Id_equipo`),
  ADD CONSTRAINT `Partido_ibfk_2` FOREIGN KEY (`Id_equipo_visitante`) REFERENCES `Equipos` (`Id_equipo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
