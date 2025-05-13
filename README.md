<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyek Prediksi IKP</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f9f9f9; color: #333; margin: 40px; line-height: 1.6; }
        h1, h2, h3 { color: #2E86C1; }
        header { background-color: #2E86C1; color: white; padding: 20px; text-align: center; }
        img.banner { width: 100%; max-height: 300px; object-fit: cover; }
        pre, code { background-color: #eee; padding: 5px; border-radius: 4px; display: block; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #2E86C1; color: white; }
        ul { margin-left: 20px; }
    </style>
</head>
<body>

<header>
    <h1>🌾 Proyek Prediksi IKP</h1>
    <p>Klasifikasi Indeks Ketahanan Pangan Indonesia dengan Neural Network dan Cross Validation</p>
</header>

<img class="banner" src="outputs/banner.jpg" alt="Banner Proyek IKP">

<h2>🇮🇩 Latar Belakang</h2>
<p>Ketahanan pangan merupakan isu strategis dalam pembangunan berkelanjutan Indonesia. World Food Summit (1996) mendefinisikan ketahanan pangan sebagai: 
<em>"Situasi di mana setiap orang, setiap saat, memiliki akses fisik dan ekonomi terhadap pangan yang cukup, aman, dan bergizi untuk menjalani kehidupan yang sehat."</em></p>
<p>Food Security Index (FSI) atau Indeks Ketahanan Pangan (IKP) menilai kemampuan negara dalam menjamin ketersediaan, akses, dan pemanfaatan pangan. Menurut Global Food Security Index (2022), Indonesia menempati peringkat 63 dari 113 negara.</p>

<h2>🎯 Tujuan Penelitian</h2>
<ul>
    <li>Mengidentifikasi faktor utama ketahanan pangan Indonesia</li>
    <li>Menyeleksi variabel yang relevan untuk model prediksi IKP</li>
    <li>Membangun model prediksi berbasis Neural Network + GFSI</li>
    <li>Memprediksi IKP kabupaten/kota untuk tahun 2024-2025</li>
</ul>

<h2>📋 Data dan Variabel</h2>
<p><b>Sumber data:</b> Badan Pangan Nasional, data.go.id, Global Food Security Index 2022.</p>
<p><b>Variabel X:</b></p>
<ul>
    <li>Rasio konsumsi normatif per kapita</li>
    <li>Penduduk di bawah garis kemiskinan</li>
    <li>Pengeluaran pangan rumah tangga >65%</li>
    <li>Akses listrik</li>
    <li>Lama sekolah perempuan >15 tahun</li>
    <li>Akses air bersih</li>
    <li>Rasio penduduk per tenaga kesehatan</li>
    <li>Stunting balita</li>
    <li>Angka harapan hidup</li>
</ul>
<p><b>Variabel Y (Kategori IKP):</b> 1=Sangat Rentan ... 6=Sangat Tahan → Disederhanakan jadi: 0 (1-3) & 1 (4-6)</p>

<h2>💡 Metodologi</h2>
<ol>
    <li>Pengumpulan Data</li>
    <li>Exploratory Data Analysis (EDA)</li>
    <li>Preprocessing Data</li>
    <li>Bangun Model Prediksi (Neural Network + Grid Search)</li>
    <li>Cari Model Terbaik (Cross Validation)</li>
    <li>Analisis Indikator Terpenting</li>
    <li>Evaluasi Model (Accuracy, F1-score, Confusion Matrix)</li>
    <li>Berikan Hasil dan Rekomendasi</li>
</ol>

<h2>📋 Diagram Alur Proyek</h2>
<img src="outputs/flowchart_final.png" alt="Flowchart Proyek IKP" style="width:90%; display:block; margin:auto; border:1px solid #ccc;">

<h2>📂 Struktur Project</h2>
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
    <li>Clone repository:<br><code>git clone https://github.com/your-username/ikp-prediction-model.git</code></li>
    <li>Install dependensi:<br><code>pip install -r requirements.txt</code></li>
    <li>Jalankan notebook atau script di folder <code>src/</code> atau <code>notebooks/</code></li>
</ol>

<h2>🎯 Hasil Prediksi (Masih Coba-coba)</h2>
<table>
    <tr><th>Metrik</th><th>Nilai</th></tr>
    <tr><td>Accuracy</td><td>95%</td></tr>
    <tr><td>F1-Score</td><td>0.94</td></tr>
    <tr><td>R² Score</td><td>0.78</td></tr>
    <tr><td>Silhouette Score</td><td>0.62</td></tr>
    <tr><td>Calinski-Harabasz</td><td>470.1</td></tr>
</table>

<h2>📊 Contoh Confusion Matrix</h2>
<img src="outputs/confusion_matrix.png" alt="Confusion Matrix" style="width:60%; display:block; margin:auto; border:1px solid #ccc;">

<h2>🎉 Manfaat Penelitian</h2>
<ul>
    <li>Informasi strategis untuk kebijakan pangan Indonesia</li>
    <li>Framework prediksi berbasis Machine Learning untuk instansi</li>
    <li>Alat bantu prioritas intervensi daerah rawan pangan</li>
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

<h2>👤 Anggota: Mungkinkah Kumiliki</h2>
<ul>
    <li>I Gusti Ngurah Sentana Putra</li>
    <li>Muhammad Syafiq</li>
    <li>Adib Roisilmi Abdullah</li>
    <li>Muhammad Yusran</li>
</ul>

<h2>📄 Lisensi</h2>
<p>Proyek ini dilisensikan dengan <b>MIT License</b>.</p>

</body>
</html>
