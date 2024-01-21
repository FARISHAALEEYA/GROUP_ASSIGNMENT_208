-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 21, 2024 at 02:14 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `login`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `First_Name` text NOT NULL,
  `Last_Name` text NOT NULL,
  `User_Email` varchar(30) NOT NULL,
  `User_Password` varchar(20) NOT NULL,
  `User_Gender` varchar(7) NOT NULL,
  `Date_of_Birth` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_login`
--

INSERT INTO `user_login` (`First_Name`, `Last_Name`, `User_Email`, `User_Password`, `User_Gender`, `Date_of_Birth`) VALUES
('Putra', 'Syazz', 'putraa123@gmail.com.my', 'PutraA2002', 'Male', '2000-03-03'),
('Daniel', 'Low', 'niell19@gmail.com.my', 'NIEL1900', 'Male', '2001-07-27'),
('Lilyee', 'Misan Lee', 'lilyy123', 'Lilyy00', 'Female', '2002-02-08');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
