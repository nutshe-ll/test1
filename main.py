meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "FR": "Digunakan untuk menyatakan kebenaran terhadap sesuatu yang dikatakan"
    ""
}

while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

    if word.upper() in meme_dict.keys():
        print(meme_dict[word.upper()])
    else:
        print("Kata tidak ditemukan!")
