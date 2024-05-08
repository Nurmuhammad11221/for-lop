# mehmonlar = ["Anvar", "Husan", "Hasan", "Toshmat", "Humoyun"]

# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}! sizni 20 chida bolib otadigan kechaga chaqiraman")
# print("Hurmat bilan Muzap chort!")
# sonlar = list(range(1, 11))
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for son in sonlar: 
#     print(f"{son} ning kvadrati {son ** 2} ga teng")

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# sonlar = list(range(11))
# sonlar_kv = [] 
# for son in sonlar:
#     sonlar_kv.append(son ** 2)

# print(sonlar)
# print(sonlar_kv)

# 1

# ismlar = ["muzap", "rizo", "jovo", "habi", "mustaf"]
# for ism in ismlar:
#     print(f"{ism} salom!")

# # 2

# print(f"Kod {len(ismlar)} mart Takrorlandi")

# # 3

# sonlar = list(range(11, 101, 2))
# sonlar_kb = []
# for son in sonlar:
#     nums = son ** 3
#     sonlar_kb.append(nums)

# print(sonlar)
# print(sonlar_kb)

# # 4

# kinolar = []

# for i in range(5):
#     kinolar.append(input(f"{i}-kinoni kiriting"))
 
# print(kinolar)

a = int(input(f"Bugun necha kishi bn suhbat qildingiz?: "))
suhbatlashgan = []
for suhbat in range(a):
    
    suhbatlashgan.append(input(f"{suhbat + 1}-suhbat qilgan odamingiz kim edi: "))
print(suhbatlashgan)