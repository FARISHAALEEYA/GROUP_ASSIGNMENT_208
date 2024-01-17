-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 17, 2024 at 06:26 AM
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
-- Database: `book_rent2`
--

-- --------------------------------------------------------

--
-- Table structure for table `book_entry_form`
--

CREATE TABLE `book_entry_form` (
  `book_id` int(10) NOT NULL,
  `book_title` text NOT NULL,
  `book_price` varchar(10) NOT NULL,
  `date_borrow` text NOT NULL,
  `book_type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book_entry_form`
--

INSERT INTO `book_entry_form` (`book_id`, `book_title`, `book_price`, `date_borrow`, `book_type`) VALUES
(23456, 'Authority Work', 'RM 20', '2/3/2024', 'Journal'),
(43256, 'Subject Heading', 'RM45.00', '1/1/2024', 'Encyclopedia');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
