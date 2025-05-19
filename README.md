<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Proyek Prediksi IKP</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #fdfdfd;
      color: #333;
      margin: 40px;
      line-height: 1.6;
    }
    header {
      background-color: #2E86C1;
      color: white;
      padding: 25px;
      border-radius: 10px;
      text-align: center;
      margin-bottom: 30px;
    }
    h1, h2, h3 {
      color: #2E86C1;
    }
    img.banner {
      width: 100%;
      max-height: 320px;
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 30px;
    }
    pre, code {
      background-color: #f1f1f1;
      padding: 6px 10px;
      border-radius: 5px;
      display: block;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 25px 0;
    }
    th, td {
      padding: 10px;
      border: 1px solid #ccc;
      text-align: center;
    }
    th {
      background-color: #2E86C1;
      color: white;
    }
    ul, ol {
      padding-left: 25px;
    }
    .center {
      display: block;
      margin: 20px auto;
      max-width: 90%;
      border: 1px solid #ddd;
      border-radius: 8px;
    }
    footer {
      margin-top: 50px;
      font-size: 0.9em;
      text-align: center;
      color: #666;
    }
    .team-container {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      margin-top: 15px;
    }
    .team-member {
      flex: 1 1 
</head>
<body>
<header>
  <h1>🌾 Proyek Prediksi IKP</h1>
  <p>Klasifikasi Indeks Ketahanan Pangan Indonesia dengan Neural Network dan Cross Validation</p>
</header>

<img class="banner" src="outputs/banner.jpg" alt="Banner Proyek IKP"/>

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
<p><strong>Sumber data:</strong> Badan Pangan Nasional, <a href="https://data.go.id">data.go.id</a>, Global Food Security Index 2022.</p>
<p><strong>Variabel Prediktor (X):</strong></p>
<ul>
  <li>Rasio konsumsi normatif per kapita</li>
  <li>Penduduk di bawah garis kemiskinan</li>
  <li>Pengeluaran pangan rumah tangga &gt; 65%</li>
  <li>Akses listrik</li>
  <li>Lama sekolah perempuan &gt; 15 tahun</li>
  <li>Akses air bersih</li>
  <li>Rasio penduduk per tenaga kesehatan</li>
  <li>Stunting balita</li>
  <li>Angka harapan hidup</li>
</ul>
<p><strong>Variabel Target (Y):</strong> Kategori IKP disederhanakan menjadi 0 (Rentan: 1–3) & 1 (Tahan: 4–6)</p>

<h2>💡 Metodologi</h2>
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
<img src="outputs/flowchart_final.png" alt="Flowchart IKP" class="center"/>

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
<div class="team-container">

  <div class="team-member">
    <img src="outputs/foto_anggota/sentana.jpg" alt="Sentana">
    <p><strong>I Gusti Ngurah Sentana Putra</strong><br>NIM: M0501241019</p>
  </div>

  <div class="team-member">
    <img src="outputs/foto_anggota/syafiq.jpg" alt="Syafiq">
    <p><strong>Muhammad Syafiq</strong><br>NIM: M0501241005</p>
  </div>

  <div class="team-member">
    <img src="outputs/foto_anggota/adib.jpg" alt="Adib">
    <p><strong>Adib Roisilmi Abdullah</strong><br>NIM: M0501241039</p>
  </div>

  <div class="team-member">
    <img src="outputs/foto_anggota/yusran.jpg" alt="Yusran">
    <p><strong>Muhammad Yusran</strong><br>NIM: M0501241064</p>
  </div>

</div>

<footer>
  <p>Lisensi: MIT License • IPB University, 2025</p>
</footer>

</body>
</html>
