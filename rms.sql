-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2023 at 06:59 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rms`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `user_id`, `phone`, `address`, `created_at`, `updated_at`) VALUES
(1, 5, 3453637531, 'Korangi DHA', '2023-07-17 08:54:19', '2023-07-17 06:08:47'),
(2, 5, 9876543210, '456 Elm Avenue', '2023-07-17 08:54:19', '2023-07-17 06:06:51'),
(3, 7, 5555555555, '789 Oak Road, ', '2023-07-17 08:54:19', '2023-07-17 06:04:43'),
(4, 5, 1111111111, '321 Pine Lane, Hamlet', '2023-07-17 08:54:19', '2023-07-17 08:54:19'),
(5, 4, 9999999999, '777 Maple Drive, Suburb', '2023-07-17 08:54:19', '2023-07-17 08:54:19');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `item_name` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `item_name`, `price`, `description`, `created_at`, `updated_at`) VALUES
(3, 'Veggie Burger', '7.49', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(4, 'Spicy Chicken Burger', '8.75', 'Crispy chicken fillet with spicy sauce and coleslaw.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(5, 'Mushroom Swiss', '10.20', 'Beef patty topped with sautéed mushrooms and Swiss cheese.', '2023-07-16 08:03:19', '2023-07-16 16:29:43'),
(8, 'Double Cheeseburger', '12.99', 'Two beef patties with double cheese and all the fixings.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(9, 'Hawaiian Teriyaki Burger', '10.75', 'Grilled pineapple, teriyaki sauce, and ham on a beef patty.', '2023-07-16 08:03:19', '2023-07-16 08:03:19'),
(10, 'Zinger burger', '8.80', 'hello', '2023-07-16 08:03:19', '2023-07-16 16:26:36'),
(12, 'Double Zinger', '8.00', 'very good', '2023-07-16 13:52:09', '2023-07-16 13:52:09'),
(13, 'Double Zinger', '8.99', 'very good', '2023-07-16 14:55:31', '2023-07-16 14:55:31'),
(15, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:48:49', '2023-07-16 15:48:49'),
(16, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:51:10', '2023-07-16 15:51:10'),
(17, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:51:16', '2023-07-16 15:51:16'),
(18, 'Veggie Burger', '7.00', 'Plant-based patty with fresh veggies and vegan mayo.', '2023-07-16 15:52:58', '2023-07-16 15:52:58'),
(19, 'Double Zinger', '8.99', 'normal', '2023-07-17 05:02:03', '2023-07-17 06:48:08');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `role` enum('customer','employee') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `role`, `created_at`, `updated_at`) VALUES
(3, 'Michael Johnson', 'customer', '2023-07-16 22:14:48', '2023-07-17 04:35:38'),
(4, 'Emily Davis', 'customer', '2023-07-16 22:14:48', '2023-07-16 22:14:48'),
(5, 'Robert Lee', 'employee', '2023-07-16 22:14:48', '2023-07-16 22:14:48'),
(7, 'Abbas Rizvi', 'employee', '2023-07-17 04:47:14', '2023-07-17 04:47:14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
