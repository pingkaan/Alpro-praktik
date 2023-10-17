-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 01, 2023 at 05:34 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `percobaan_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `pembayaran`
--

CREATE TABLE `pembayaran` (
  `id_pembayaran` varchar(10) NOT NULL,
  `id_buku` varchar(10) NOT NULL,
  `tgl_keluar` datetime NOT NULL,
  `jumlah` int(3) NOT NULL,
  `metode` varchar(30) NOT NULL,
  `keterangan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pembayaran`
--

INSERT INTO `pembayaran` (`id_pembayaran`, `id_buku`, `tgl_keluar`, `jumlah`, `metode`, `keterangan`) VALUES
('JWKA1EZ39X', 'AA02', '2023-01-01 21:20:20', 1, 'COD', 'Pesanan Sedang Diproses'),
('VRHV2RRAWC', 'AA04', '2023-01-01 22:48:58', 1, 'Tansfer Bank', 'Pesanan Sedang Diproses'),
('ZOXOJROX7F', 'AA05', '2023-01-01 23:21:59', 1, 'COD', 'Pesanan Sedang Diproses');

--
-- Triggers `pembayaran`
--
DELIMITER $$
CREATE TRIGGER `bukuterbeli` AFTER INSERT ON `pembayaran` FOR EACH ROW BEGIN
	UPDATE tbl_daftar_buku SET jumlah_stok = jumlah_stok - NEW.jumlah
    WHERE id_buku = NEW.id_buku;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_daftar_buku`
--

CREATE TABLE `tbl_daftar_buku` (
  `id_buku` varchar(10) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `pengarang` varchar(50) NOT NULL,
  `harga` int(10) NOT NULL,
  `jumlah_stok` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_daftar_buku`
--

INSERT INTO `tbl_daftar_buku` (`id_buku`, `judul`, `penerbit`, `pengarang`, `harga`, `jumlah_stok`) VALUES
('AA01', 'Le Petit Prince (Pangeran Cilik)', 'Gramedia', 'Antoine De Saint-Exupery', 58000, 7),
('AA02', 'Colors in the Sky', 'LovRinz Publishing', 'Tenderlova', 99000, 9),
('AA03', 'Makassar (Mantra Tentang Hujan)', 'LovRinz Publishing', 'Windy Joana H', 99000, 6),
('AA04', 'Bibi Gill', 'Penerbit Sabakgrip', 'TereLiye', 72000, 10),
('AA05', 'Sagaras', 'Penerbit Sabakgrip', 'TereLiye', 72000, 11),
('AA06', 'Pramoedya', 'GagasMedia', 'Tenderlova', 88000, 5);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_keranjang`
--

CREATE TABLE `tbl_keranjang` (
  `id_buku` varchar(10) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `pengarang` varchar(50) NOT NULL,
  `harga` int(10) NOT NULL,
  `jumlah_stok` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_keranjang`
--

INSERT INTO `tbl_keranjang` (`id_buku`, `judul`, `penerbit`, `pengarang`, `harga`, `jumlah_stok`) VALUES
('AA02', 'Colors in the Sky', 'LovRinz Publishing', 'Tenderlova', 99000, 9);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `id_user` int(5) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`id_user`, `username`, `password`) VALUES
(1, 'admin', 'e10adc3949ba59abbe56e057f20f883e'),
(2, 'admin2', '234567');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pembayaran`
--
ALTER TABLE `pembayaran`
  ADD PRIMARY KEY (`id_pembayaran`);

--
-- Indexes for table `tbl_daftar_buku`
--
ALTER TABLE `tbl_daftar_buku`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `tbl_keranjang`
--
ALTER TABLE `tbl_keranjang`
  ADD PRIMARY KEY (`id_buku`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `id_user` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
