import joblib
import pandas as pd

# Path ke model
MODEL_PATH = "../model/best_lgb_grid_adasyn.joblib"

# Daftar fitur yang dibutuhkan model (urut dan nama harus sesuai training)
FEATURE_NAMES = [
    'Garis Kemiskinan',
    'Indeks Pembangunan Manusia',
    'Jumlah Penduduk Miskin',
    'Indeks Kedalaman Kemiskinan',
    'Indeks Keparahan Kemiskinan',
    'Pengeluaran Perkapita Bahan Makanan Lainnya',
    'Pengeluaran Perkapita Bahan Minuman',
    'Pengeluaran Perkapita Buah-Buahan',
    'Pengeluaran Perkapita Daging',
    'Pengeluaran Perkapita Kacang-Kacangan',
    'Pengeluaran Perkapita Bahan Minyak dan Kelapa',
    'Pengeluaran Perkapita Padi-Padian',
    'Pengeluaran Perkapita Rokok dan Tembakau',
    'Pengeluaran Perkapita Telur dan Susu',
    'Pengeluaran Perkapita Umbi-Umbian',
    'Persentase Penduduk Miskin',
    'Prevalensi Konsumsi Pangan Tidak Cukup',
    'Rata-rata Lama Sekolah_Laki-laki',
    'Rata-rata Lama Sekolah_Perempuan',
    'NCPR',
    'Kemiskinan (%)',
    'Pengeluaran Pangan (%)',
    'Tanpa Listrik (%)',
    'Tanpa Air Bersih (%)',
    'Rasio Tenaga Kesehatan',
    'Angka Harapan Hidup',
    'Stunting (%)',
    'is_kota'
]

def get_user_input(feature_names):
    print("=== INPUT DATA ===")
    kabupaten = input("Nama Kabupaten/Kota: ")
    tahun = input("Tahun: ")

    data = {}
    for feat in feature_names:
        while True:
            try:
                value = float(input(f"- {feat}: "))
                data[feat] = value
                break
            except ValueError:
                print("Masukkan angka yang valid!")

    return kabupaten, tahun, pd.DataFrame([data])

def main():
    # Load model
    print("📦 Memuat model...")
    model = joblib.load(MODEL_PATH)

    # Input pengguna
    kabupaten, tahun, input_df = get_user_input(FEATURE_NAMES)

    # Prediksi
    print("\n🔍 Melakukan prediksi...")
    pred = model.predict(input_df)[0]
    hasil = "Tahan Pangan" if pred == 1 else "Rawan Pangan"

    print(f"\n📊 Kabupaten/Kota {kabupaten} pada tahun {tahun} diklasifikasikan sebagai: {hasil}")

if __name__ == "__main__":
    main()
