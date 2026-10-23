# M77 — amendmen kapasitas: tiga peran, satu model Gemini

Pada15Oktober2026UTC+7, owner menjawab pilihan eksplisit antara mempertahankan
Groq/Gemini atau memakai Gemini untuk seluruh peran dengan arahan memilih yang
cepat dan mudah. Opsi kedua diterapkan pada **binding eksperimen**, tanpa
mengganti default operasional panel, konfigurasi tersimpan atau key.

## Yang diukur

Rancangan tetap40kasus native buatan milik owner, satu repetisi, B0/B1/B2/P.
Empat puluh kasus, input, prompt, schema, oracle, split, riskcap1–5%, analisis,
seed7501 dan batas output512/deadline15detik/framing4096 sama denganM75.
Teknikal, risiko dan makro kini memakai **Gemini3.5Flash-Lite yang sama**, dengan
prompt peran masing-masing. Jangan mengklaim tiga model independen atau
keunggulan ensemble lintas model.

Empat puluh slot makroM75 sudah teramati sebelum perubahan provider ini:
39VALID/1FAILED. Semua dipertahankan sebagai observasi utama dengan path/hash/
source_job_id aslinya, termasuk kegagalan dan usageUNKNOWN. Tidak ada penyalinan
yang mengubah identitas receipt, pengulangan macrocall, atau promosi pilot.
MainM73 lima attempt tetap terpisah dan tidak masukM77.

FreezeM77 dilakukan **sebelum120respons teknikal/risiko yang belum teramati**.
Perubahan ini mengikuti exposure40macro, sehingga desainGemini-saja tidak boleh
diklaim sudah dipreregistrasi penuh sebelum seluruh hasil utama. Alasan perubahan
adalah kapasitas/waktu free plan. Sampel dan prompt tidak dipilih ulang dari
respons yang menguntungkan. AnalisisM75 sudah dipin sebelum macrocall dan tidak
dituning setelah respons tersebut.

## Gratis dan batas operasi

Total unik tetap160attempt:40macro asli ditambah120call baru Gemini. Snapshot
publik Gemini terverifikasi sama untuk seluruh peran pada g1/r1/configr1.
Binding percall memilih konfigurasiGemini yang sama dan mencantumkan role yang
sesuai; tidak mengganti role dengan nama lain di prompt. Payload memakai schema
role yang sesuai, harga nol, tools/grounding tidak dipakai, satu attempt dan
tidak ada paid fallback. Konstruksi request/capsule/provider parser tetap
releaseM72 exact-pinned. Inference tidak memakai capsule diagnostikM76.

Semua sejarah konfigurasi dihitung. Ceiling kumulatif baru hanya menambah
120attempt/reservasi untuk slot yang belum pernah dikirim, tetap di bawah
review lama600attempt/4jutatoken. QuotaGemini400RPD/12RPM/200.000TPM/2jutatoken
harian lokal tidak dinaikkan. Batas akun/project global dan biaya aktual tetap
memerlukan bukti tersendiri; sumber harga free bukan invoice.
[Harga resmi](https://ai.google.dev/gemini-api/docs/pricing),
[semantik batas project](https://ai.google.dev/gemini-api/docs/rate-limits).

## Kegagalan dan stopping yang dipin sebelum peran baru

Respons tidak sah tetap ditolak oleh Runtime dan dicatat FAILED dengan usage
UNKNOWN/full reserve; teks yang ditolak tidak pernah menjadi keputusan valid.
Untuk120slot baru, satu envelope rejection diperlakukan sebagai outcome gagal
tanpa retry; **tiga kegagalan transport berturut-turut** menghentikan batch.
Ini perubahan prospective dari review per rejectionM75 dan dinyatakan sebelum
call teknikal/risiko. Tidak ada relabeling kegagalan lama.

DENIED, authentication/permission/billing denial, credential echo, capability
failure atau dispatch ambigu tetap menghentikan run segera. Quota/resource/
batas waktu memicu pause sebelum intent berikutnya. P hanya menggunakan tiga
artefakB2 berurutan yang sama, tanpa call tambahan, dan menjaga prioritas
known-input-violation→REJECT serta incompleteevidence→ABSTAIN sesuai policy.

## Interpretasi ilmiah

Korelasi tiga peran yang berbagi satu backbone harus diakui. ModelID adalah
label respons provider, bukan pin bobot/backend. Waktu macro dan peran baru
dicatat karena layanan tetap mungkin berubah. Missing usage tidak dianggap0;
semua attempt, termasuk failure, masuk denominator yang sesuai.

Empat kelompok heldout berisi10kasus dan sensitivitas guard tidak digunakan
untuk tuning. Primary pairingP–B2 tetap sama; grid tidak diberi klaim signifikansi
tambahan atau threshold terbaik. Bootstrap adalah envelope resampling
kondisional untuk desain40kasus tetap/nonrandom, bukan confidence guarantee atas
populasi pasar. McNemar adalah sensitivitasIID, bukan bukti generalisasi pasar.

Guard menegakkan aturan yang juga membentuk oracle. Tidak adanya known-invalid
ACCEPT olehP adalah sifat enforcement software yang diperiksa dengan artefak
aktual; tidak membuktikan prediksi market, profit EA atau kelayakan akun riil.
Source broker, pilot lama, n8n/OpenClaw/9Router dan order broker tidak dijadikan
hasil eksperimen sintetis ini. Naskah final harus mengganti metode lama400kasus/
duamodel dengan seluruh disclosure amendmenM73/M75/M77 ini.

[Freeze dan lineage](source-freeze-m77.json),
[hasil terkini](README.md).
