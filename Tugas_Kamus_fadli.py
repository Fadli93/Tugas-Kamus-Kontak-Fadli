kamus = {
    "manggis": "buah berwarna ungu yang kulitnya memiliki manfaat untuk kesehatan wajah",
    "semangka": "buah berwarna hijau yang musim di saat musim kemarau dan bermanfaat untuk menurunkan kolesterol dalam darah",
    "rambutan": "buah musiman yang mempunyai serat yang bisa membantu melancarkan pencernaan",
    "durian": "buah yang memiliki cipta rasa dan aroma yang sangat khas dan memiliki manfaat untuk menjaga daya tahan tubuh"}

kata = input("masukan kata yang ingin dicari arti dan manfaatnya: ").lower()

if kata in kamus:
    print(f"Arti dari {kata} adalah {kamus[kata]}")
else:
    print(f"Maaf, arti dari {kata} tidak ditemukan dalam kamus.")
        
