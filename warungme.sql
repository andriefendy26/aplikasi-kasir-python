-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Jan 2024 pada 05.14
-- Versi server: 10.4.28-MariaDB
-- Versi PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `warungme`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `auth`
--

CREATE TABLE `auth` (
  `id` int(10) NOT NULL,
  `username` varchar(60) NOT NULL,
  `tipeUser` varchar(50) NOT NULL,
  `pass` varchar(60) NOT NULL,
  `totalPembelian` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `auth`
--

INSERT INTO `auth` (`id`, `username`, `tipeUser`, `pass`, `totalPembelian`) VALUES
(1, 'andri', 'pembeli', 'andri26', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `laporan`
--

CREATE TABLE `laporan` (
  `id` int(5) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jumlah` int(50) NOT NULL,
  `total` int(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `laporan`
--

INSERT INTO `laporan` (`id`, `nama`, `jumlah`, `total`) VALUES
(1, 'Andri', 7, 200000),
(28, 'Andri', 4, 46000),
(29, 'andri', 4, 74000),
(30, 'andri', 3, 31000),
(31, 'andri', 1, 8000),
(32, 'adsada', 1, 5000),
(33, 'sfsfs', 3, 31000),
(34, 'ddg', 2, 30000),
(35, 'andri', 2, 10000),
(36, 'adas', 2, 44000),
(37, 'sfesfs', 3, 35000),
(38, 'adssad', 3, 18000),
(39, 'andri', 2, 40000),
(40, 'Andri', 2, 30000),
(41, 'sefsfs', 4, 36000),
(42, 'dgdgd', 3, 21000),
(43, 'adasadsa', 3, 51000),
(44, 'sfsfsdfsd', 3, 25000),
(45, 'andri', 3, 21000),
(46, 'andri', 3, 21000),
(47, 'Andri', 5, 63000),
(48, 'hayyuk', 5, 51000),
(49, 'hantu', 4, 58000),
(50, 'boboi', 2, 36000),
(51, 'winarti', 5, 51000),
(52, 'Winter', 4, 50000),
(53, 'Qris', 2, 26000),
(54, 'Julian', 5, 62000),
(55, 'Andri', 3, 34000),
(56, 'Winter', 5, 47000),
(57, 'Tiren', 3, 18000),
(58, 'Weter', 5, 54000),
(59, 'n', 8, 72000),
(60, 'adit', 1, 22000),
(61, 'AndriE', 2, 23000),
(62, 'aditya', 1, 18000),
(63, 'www', 4, 88000),
(64, 'andri', 2, 44000),
(65, 'rahmatullah', 4, 52000),
(66, 'mm', 2, 10000),
(67, 'Andri', 3, 24400);

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbbarang`
--

CREATE TABLE `tbbarang` (
  `IdMenu` varchar(5) NOT NULL,
  `kategori` varchar(50) NOT NULL,
  `namaMenu` varchar(50) NOT NULL,
  `harga` int(10) NOT NULL,
  `total` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tbbarang`
--

INSERT INTO `tbbarang` (`IdMenu`, `kategori`, `namaMenu`, `harga`, `total`) VALUES
('AN001', 'Makanan', 'Mie Goreng', 20000, 0),
('AN002', 'Makanan', 'Nasi Goreng', 22000, 0),
('AN003', 'Minuman', 'Es Teh', 5000, 0),
('AN004', 'Minuman', 'Es Jeruk', 8000, 0),
('AN005', 'Minuman', 'Jus Alpukat', 15000, 0),
('AN006', 'Makanan', 'Mie Ayam', 18000, 0),
('AN007', 'Makanan', 'Ayam Geprek', 22000, 0),
('AN008', 'Minuman', 'Matcha', 18000, 0),
('AN009', 'Makanan', 'Kwetiaw', 3200, 0),
('AN010', 'Minuman', 'Bakso', 16000, 0),
('AND01', 'Minuman', 'Teh Olong', 15000, 0);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `auth`
--
ALTER TABLE `auth`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `laporan`
--
ALTER TABLE `laporan`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `tbbarang`
--
ALTER TABLE `tbbarang`
  ADD PRIMARY KEY (`IdMenu`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `auth`
--
ALTER TABLE `auth`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `laporan`
--
ALTER TABLE `laporan`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
