# Proyek Deteksi Penyakit Daun Kelapa Sawit

Proyek ini berfokus pada deteksi penyakit pada daun kelapa sawit menggunakan *deep learning*. Model yang telah dilatih kemudian disajikan melalui aplikasi FastAPI. Sebuah Dockerfile juga disediakan untuk kemudahan *deployment*.

**DagsHub** juga diintegrasikan ke dalam proyek ini untuk mencatat dan melacak pelatihan model, memungkinkan reproduktifitas dan kolaborasi yang lebih baik.

## Struktur Proyek

Berikut adalah penjelasan mengenai direktori dan file utama dalam repositori ini:

* **`.dvc`**: Berisi file-file terkait DVC (Data Version Control) untuk mengelola dan melacak *dataset*.
* **`app`**: Direktori ini berisi kode aplikasi FastAPI yang bertanggung jawab untuk menyajikan model *deep learning*.
* **`data_tf`**: Direktori ini berisi model *deep learning* yang telah dipilih karena mendapatkan akurasi tertinggi, disimpan dalam format SavedModel.
* **`notebooks`**: Direktori ini menampung Jupyter Notebook, digunakan untuk eksperimen, pelatihan model, dan analisis data. Isi dari folder ini adalah:
    * `master-notebook.ipynb`: Notebook utama yang mengkoordinasikan atau merangkum proses pelatihan dan evaluasi model.
    * `notebook.ipynb`: Notebook tambahan untuk eksperimen atau eksplorasi data tertentu.
    * `requirements.txt`: Daftar dependensi Python spesifik yang dibutuhkan untuk menjalankan notebook di dalam folder ini.
    * `upload-data-to-repository.ipynb`: Notebook yang digunakan untuk mengunggah atau mengelola data ke dalam repositori, kemungkinan dengan DVC atau DagsHub.
* **`.dockerignore`**: Menentukan file dan direktori yang harus diabaikan saat membangun *image* Docker.
* **`.env`**: (Kemungkinan) Berisi variabel lingkungan untuk proyek, seperti kunci API atau pengaturan konfigurasi.
* **`.gitattributes`**: Mengkonfigurasi atribut Git, berpotensi untuk menangani file besar dengan Git LFS.
* **`.gitignore`**: Menentukan file dan direktori yang harus diabaikan oleh Git.
* **`Dockerfile`**: Mendefinisikan *image* Docker untuk aplikasi FastAPI, memungkinkan *deployment* dalam kontainer.
* **`README.md`**: File dokumentasi ini, menyediakan gambaran umum proyek.
* **`palm-disease-dataset.dvc`**: File DVC yang menunjuk ke *dataset* penyakit kelapa sawit.
* **`requirements.txt`**: Mencantumkan dependensi Python utama yang diperlukan untuk proyek.

## Cara Menjalankan Aplikasi FastAPI

Anda memiliki dua pilihan utama untuk menjalankan aplikasi FastAPI: menggunakan Uvicorn secara langsung atau membangun dan menjalankan *image* Docker.

### Opsi 1: Menjalankan dengan Uvicorn (Pengembangan Lokal)

1.  **Instal Dependensi**:
    Pertama, pastikan Anda telah menginstal semua paket Python yang diperlukan.
    ```bash
    pip install -r requirements.txt
    ```

2.  **Masuk ke Direktori `app`**:
    ```bash
    cd app
    ```

3.  **Jalankan aplikasi FastAPI dengan Uvicorn**:
    Dengan asumsi file aplikasi FastAPI utama Anda adalah `main.py` di dalam direktori `app`, Anda dapat menjalankannya menggunakan Uvicorn. Ganti `main` dengan nama *instance* aplikasi FastAPI Anda jika berbeda.
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
    * `main:app`: Mengacu pada objek `app` di dalam file `main.py`. Sesuaikan `main` jika nama file Anda berbeda.
    * `--host 0.0.0.0`: Membuat aplikasi dapat diakses dari semua antarmuka jaringan.
    * `--port 8000`: Menentukan *port* tempat aplikasi akan berjalan.
    * `--reload`: (Opsional, untuk pengembangan) Secara otomatis memuat ulang aplikasi saat perubahan kode terdeteksi.

    Anda sekarang dapat mengakses dokumentasi API (Swagger UI) di `http://localhost:8000/docs` dan dokumentasi alternatif (ReDoc) di `http://localhost:8000/redoc`.

### Opsi 2: Menjalankan dengan Docker

Menggunakan Docker menyediakan lingkungan yang konsisten dan terisolasi untuk aplikasi Anda.

1.  **Bangun *Image* Docker**:
    Dari direktori utama proyek (tempat `Dockerfile` berada), bangun *image* Docker:
    ```bash
    docker build -t palm-disease-detector .
    ```
    * `-t palm-disease-detector`: Memberi tag pada *image* dengan nama `palm-disease-detector`. Anda dapat memilih nama apa pun yang Anda inginkan.
    * `.`: Menentukan konteks *build*, yaitu direktori saat ini.

2.  **Jalankan Kontainer Docker**:
    Setelah *image* dibangun, Anda dapat menjalankan kontainer darinya:
    ```bash
    docker run -p 8000:8000 palm-disease-detector
    ```
    * `-p 8000:8000`: Memetakan *port* 8000 di mesin *host* Anda ke *port* 8000 di dalam kontainer Docker. Ini adalah *port* di mana aplikasi FastAPI akan diekspos.

    Aplikasi FastAPI Anda sekarang akan berjalan di dalam kontainer Docker, dan Anda dapat mengaksesnya di `http://localhost:8000/docs` atau `http://localhost:8000/redoc`.

## Model dan Data

* **Model *Deep Learning***: Proyek ini menggunakan teknik *deep learning* untuk deteksi penyakit. Untuk pembuatan model, *library* utama yang digunakan adalah **TensorFlow** dan **Keras**.
    Pada proyek ini, telah dicoba untuk membuat **4 jenis model**, yaitu:
    1.  **Arsitektur CNN Mandiri**: Sebuah model Convolutional Neural Network (CNN) yang dibangun dari awal.
    2.  **MobileNetV2**: Model *transfer learning* berdasarkan arsitektur MobileNetV2.
    3.  **ResNet50V2**: Model *transfer learning* berdasarkan arsitektur ResNet50V2.
    4.  **Xception**: Model *transfer learning* berdasarkan arsitektur Xception.

    Model yang telah dilatih dan mendapatkan akurasi tertinggi dari keempat percobaan ini disimpan dalam format SavedModel di direktori `data_tf`.

* **Dataset**: File `palm-disease-dataset.dvc` menunjukkan bahwa DVC digunakan untuk mengelola *dataset* penyakit kelapa sawit, memastikan kontrol versi dan reproduktifitas.

## DagsHub Integration

Proyek ini menggunakan **DagsHub** untuk manajemen eksperimen dan pelacakan model. Dengan DagsHub, Anda dapat:

* **Melacak Parameter dan Metrik**: Catat parameter pelatihan, metrik evaluasi (akurasi, *loss*, dll.), dan artefak model untuk setiap eksperimen.
* **Version Control Model**: DagsHub memungkinkan Anda untuk *versioning* model yang dilatih, sehingga Anda dapat dengan mudah kembali ke versi sebelumnya atau membandingkan kinerja model yang berbeda.
* **Melihat Riwayat Eksperimen**: Jelajahi riwayat pelatihan model Anda melalui antarmuka DagsHub.

## Pengembangan Lanjut

* Jelajahi direktori `notebooks` untuk detail lebih lanjut tentang pelatihan dan evaluasi model, serta bagaimana data diunggah ke repositori. Anda dapat melihat bagaimana keempat jenis model (CNN Mandiri, MobileNetV2, ResNet50V2, Xception) dibangun dan dilatih di sana.
* Lihat direktori `app` untuk memahami implementasi FastAPI dalam menyajikan model.
* Manfaatkan `Dockerfile` untuk *deployment* yang mulus di lingkungan produksi.
* Gunakan **DagsHub** untuk mengelola dan memantau eksperimen pelatihan model Anda secara efektif.