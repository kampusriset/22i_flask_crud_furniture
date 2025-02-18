-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 18, 2025 at 03:35 PM
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
-- Database: `instyle_furniture`
--

-- --------------------------------------------------------

--
-- Table structure for table `furniture`
--

CREATE TABLE `furniture` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `kategori` enum('Sofa','Meja','Kursi','Lemari','Dekorasi','Rak','Lampu','Karpet','Wallpaper') NOT NULL,
  `bahan` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `furniture`
--

INSERT INTO `furniture` (`id`, `name`, `kategori`, `bahan`, `price`, `stock`) VALUES
(1, 'Meja Makan Minimalis', 'Meja', 'Kayu Jati', 3500000.00, 10),
(2, 'Sofa Kulit Premium', 'Sofa', 'Kayu Jati, Kulit', 7800000.00, 5),
(3, 'Lemari Kayu Jati', 'Lemari', 'Kayu Jati', 6200000.00, 8),
(4, 'Lampu Gantung Modern', 'Dekorasi', 'Kaca, Baja', 2100000.00, 15),
(5, 'Kursi Bar Industrial', 'Kursi', 'Kayu Jati, Besi', 1500000.00, 12),
(6, 'Meja Kerja Marmer', 'Meja', 'Besi, Marmer', 4800000.00, 7),
(7, 'Rak Dinding Minimalis', 'Lemari', 'Rotan, Bambu', 1200000.00, 20),
(8, 'Cermin Aesthetic', 'Dekorasi', 'Kaca, Baja', 180000.00, 10),
(9, 'Karpet Wol Premium', 'Dekorasi', 'Wol', 2500000.00, 6),
(10, 'Kitchen Set Modern', 'Lemari', 'Kayu Jati, Marmer', 9500000.00, 3),
(11, 'Meja Kopi Skandinavia', 'Meja', 'Kayu Oak, Besi', 2200000.00, 9);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password_hash`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$msLB3I6GX8eCEoH9$6c8ae3b3a94c275b83d91af080464585605d2703e0acf6fbc370d52209233f9c');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `furniture`
--
ALTER TABLE `furniture`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `furniture`
--
ALTER TABLE `furniture`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
