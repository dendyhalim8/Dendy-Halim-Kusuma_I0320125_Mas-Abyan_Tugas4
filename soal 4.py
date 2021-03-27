usia = int(input("Berapa usia kamu?"))
ujian = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)?")

if usia >= 21:
    usia = 1
else:
    usia = 0

if ujian == "Y":
    ujian = 1
elif ujian == "T":
    ujian = 0
else:
    print("Jawaban yang anda masukan salah")
    ujian = 0

hasil = usia+ujian
if hasil == 2:
    hasil = "Anda dapat mendaftar di kursus."
else:
    hasil = "Anda tidak dapat mendaftar di kursus."

print(hasil)
