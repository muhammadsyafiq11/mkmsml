<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<header>
  <h1>🌾 Data-Driven Prediction of Food Security Index Categories in Indonesia Using Machine Learning and GFSI-BPN Indicators
</h1>
  <img class="banner" src="img/BANNER Indeks Ketahanan pangan.png" alt="Banner Proyek IKP"/>
  <p>Proyek ini bertujuan untuk membangun model prediksi kategori Indeks Ketahanan Pangan (IKP) kabupaten/kota di Indonesia. Model dikembangkan dengan memanfaatkan 9 indikator utama dari Badan Pangan Nasional (BPN) dan indikator tambahan dari Global Food Security Index (GFSI) serta variabel sosial-ekonomi lainnya. Diharapkan model ini mampu memberikan insight berbasis data yang akurat untuk mendukung kebijakan ketahanan pangan nasional.
</p>
</header>

<h2>🇮🇩 Latar Belakang</h2>
<p>Ketahanan pangan merupakan isu strategis dalam pembangunan berkelanjutan Indonesia. World Food Summit (1996) mendefinisikan ketahanan pangan sebagai:</p>
<blockquote><em>“Situasi di mana setiap orang, setiap saat, memiliki akses fisik dan ekonomi terhadap pangan yang cukup, aman, dan bergizi untuk menjalani kehidupan yang sehat.”</em></blockquote>
<p>Food Security Index (FSI) atau Indeks Ketahanan Pangan (IKP) menilai kemampuan negara dalam menjamin ketersediaan, akses, dan pemanfaatan pangan. Menurut Global Food Security Index (2022), Indonesia menempati peringkat 63 dari 113 negara.</p>

<h2>🎯 Tujuan Penelitian</h2>
<ul>
  <li>Mengidentifikasi faktor utama ketahanan pangan Indonesia</li>
  <li>Menyeleksi variabel yang relevan untuk model prediksi IKP</li>
  <li>Membangun model prediksi berbasis Neural Network + GFSI</li>
  <li>Memprediksi IKP kabupaten/kota untuk tahun 2024-2025</li>
</ul>

<h2>📋 Data dan Variabel</h2>
<div align="center">
  <table>
  <tr>
    <td align="center">
      <img src="img/satudata.png" Height="90"><br>
      <strong>Satudata Indonesia</strong>
    </td>
    <td align="center">
      <img src="img/BPS.png" height="90"><br>
      <strong>Badan Pusat Statistik</strong>
    </td>
    <td align="center">
      <img src="img/GFSI.png" height="90"><br>
      <strong>Global Food Safety Initiative</strong>
    </td>
  </tr>
</table>
</div>
<h3><strong>Variabel Prediktor (X):</strong></h3>
<h4>Indikator Sosial dan Kesehatan</h4>
<ul>
  <li>Angka Harapan Hidup</li>
  <li>Rasio Tenaga Kesehatan</li>
  <li>Stunting (%)</li>
  <li>Tanpa Air Bersih (%)</li>
</ul>

<h4>Indikator Pendidikan</h4>
<ul>
  <li>Rata-rata Lama Sekolah Laki-laki</li>
  <li>Rata-rata Lama Sekolah Perempuan</li>
</ul>

<h4>Kemiskinan dan Ekonomi</h4>
<ul>
  <li>Garis Kemiskinan</li>
  <li>Jumlah Penduduk Miskin</li>
  <li>Kemiskinan (%)</li>
  <li>Persentase Penduduk Miskin</li>
  <li>Indeks Kedalaman Kemiskinan</li>
  <li>Indeks Keparahan Kemiskinan</li>
  <li>Indeks Pembangunan Manusia</li>
  <li>Prevalensi Konsumsi Pangan Tidak Cukup</li>
</ul>

<h4>Pengeluaran Konsumsi Pangan</h4>
<ul>
  <li>Pengeluaran Pangan (%)</li>
  <li>Pengeluaran Perkapita Padi-Padian</li>
  <li>Pengeluaran Perkapita Umbi-Umbian</li>
  <li>Pengeluaran Perkapita Kacang-Kacangan</li>
  <li>Pengeluaran Perkapita Buah-Buahan</li>
  <li>Pengeluaran Perkapita Telur dan Susu</li>
  <li>Pengeluaran Perkapita Daging</li>
  <li>Pengeluaran Perkapita Bahan Minuman</li>
  <li>Pengeluaran Perkapita Bahan Makanan Lainnya</li>
  <li>Pengeluaran Perkapita Bahan Minyak dan Kelapa</li>
  <li>Pengeluaran Perkapita Rokok dan Tembakau</li>
</ul>

<h4>Indeks Konsumsi Pangan</h4>
<ul>
  <li>NCPR</li>
</ul>
<p><strong>Variabel Target (Y):</strong> Kategori IKP disederhanakan menjadi 0 (Rentan: 1–3) & 1 (Tahan: 4–6)</p>

<h2>💡 Metodologi</h2>
<p align="center">
<img src="img/Flowchart.png" alt="Flowchart IKP" class="center" width="80%"/>
<br><em>Gambar 1. Flowchart Metode Indeks Ketahanan Pangan</em>
</p>
<p><strong>Tahapan Penelitian Indeks Ketahanan Pangan</strong></p>
<ol>
  <li>Pengumpulan Data</li>
  <li>Exploratory Data Analysis (EDA)</li>
  <li>Preprocessing Data</li>
  <li>Bangun Model Prediksi (Neural Network + Grid Search)</li>
  <li>Cross Validation untuk model terbaik</li>
  <li>Analisis indikator paling signifikan</li>
  <li>Evaluasi model: Accuracy, F1-score, Confusion Matrix</li>
  <li>Rekomendasi kebijakan</li>
</ol>

<h2>📋 Diagram Alur Proyek</h2>
<p align="center">
<img src="img/WorkFlow.png" alt="WorkFlow IKP" class="center" width="80%"/>
<br><em>Gambar 2. WorkFlow Indeks Ketahanan Pangan/Kota</em>
</p>
<h2>📂 Struktur Proyek</h2>
<pre>
ikp-prediction-model/
├── data/
├── notebooks/
├── src/
├── outputs/
├── model_ikp_binary.h5
├── requirements.txt
├── README.md
└── LICENSE
</pre>

<h2>🚀 Cara Menjalankan</h2>
<ol>
  <li>Clone repo: <br><code>git clone https://github.com/your-username/ikp-prediction-model.git</code></li>
  <li>Install dependensi: <br><code>pip install -r requirements.txt</code></li>
  <li>Jalankan notebook di <code>src/</code> atau <code>notebooks/</code></li>
</ol>

<h2>🎯 Hasil Prediksi</h2>
<table>
  <tr><th>Metrik</th><th>Nilai</th></tr>
  <tr><td>Accuracy</td><td>95%</td></tr>
  <tr><td>F1-Score</td><td>0.94</td></tr>
  <tr><td>R² Score</td><td>0.78</td></tr>
  <tr><td>Silhouette Score</td><td>0.62</td></tr>
  <tr><td>Calinski-Harabasz</td><td>470.1</td></tr>
</table>

<h2>📊 Cuplikan Visual</h2>
<p align="center">
  <img src="img/Sebaran IKP 2024.png" width="80%"/>
  <br><em>Gambar 3. Sebaran IKP 2024 Berdasarkan Kabupaten/Kota</em>
</p>

<p align="center">
  <img src="img/Peta IKP 2024.png" width="80%"/>
  <br><em>Gambar 4. Peta Sebaran IKP di Indonesia</em>
</p>

<p align="center">
  <img src="img/Peta IKP 2024.png" width="80%"/>
  <br><em>Gambar 4. Peta Sebaran IKP di Indonesia</em>
</p>

<h2>📊 Confusion Matrix</h2>
<img src="outputs/confusion_matrix.png" alt="Confusion Matrix" class="center"/>

<h2>🎉 Manfaat Penelitian</h2>
<ul>
  <li>Informasi strategis untuk kebijakan ketahanan pangan Indonesia</li>
  <li>Framework Machine Learning untuk prediksi daerah rentan</li>
  <li>Rekomendasi intervensi daerah berdasarkan model</li>
</ul>

<h2>🔎 Citation</h2>
<pre>
@article{Roisilmi2025IKP,
  title={Predicting Indonesia's Food Security Index with Deep Learning},
  author={Adib Roisilmi Abdullah et al.},
  year={2025},
  journal={Tugas Akhir Pembelajaran Mesin Statistika, IPB University}
}
</pre>

<h2>👥 Anggota Kelompok</h2>

<div align="center">
  <table>
    <tr>
      <td align="center">
        <img src="img/Ngurah.png" width="220"><br>
        <strong>I Gusti Ngurah Sentana Putra</strong><br>
        M0501241019
      </td>
      <td align="center">
        <img src="img/Syafiq.png" width="220"><br>
        <strong>Muhammad Syafiq</strong><br>
        M0501241005
      </td>
      <td align="center">
        <img src="img/Adib.png" width="220"><br>
        <strong>Adib Roisilmi Abdullah</strong><br>
        M0501241039
      </td>
      <td align="center">
        <img src="img/Yusran.png" width="220"><br>
        <strong>Muhammad Yusran</strong><br>
        M0501241064
      </td>
    </tr>
  </table>
</div>

<footer>
  <p>Lisensi: MIT License • IPB University, 2025</p>
</footer>

</body>
</html>
