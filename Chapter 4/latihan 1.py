#tarif
tarifAwal=200000
tarifAkhir=10000

#waktu
jamMulai=6
jamSelesai=23
menitMulai=0
menitSelesai=50

totalJam=(jamSelesai-jamMulai)+((menitSelesai-menitMulai)//60)

#harga
harga=(10000*(totalJam-12))+200000

print ("total harga yang harus dibayarkan sebesar",harga, "ribu rupiah")
