for _ in range(int(input())):
    d, m = map(int, input().split())
    d = int(d)
    m = int(m)
    if (d >= 21 and m == 3) or (d <= 19 and m == 4):
        print("Bach Duong")
    elif (d >= 20 and m == 4) or (d <= 20 and m == 5):
        print("Kim Nguu")
    elif (d >= 21 and m == 5) or (d <= 20 and m == 6):
        print("Song Tu")
    elif (d >= 21 and m == 6) or (d <= 22 and m == 7):
        print("Cu Giai")
    elif (d >= 23 and m == 7) or (d <= 22 and m == 8):
        print("Su Tu")
    elif (d >= 23 and m == 8) or (d <= 22 and m == 9):
        print("Xu Nu")
    elif (d >= 23 and m == 9) or (d <= 22 and m == 10):
        print("Thien Binh")
    elif (d >= 23 and m == 10) or (d <= 22 and m == 11):
        print("Thien Yet")
    elif (d >= 23 and m == 11) or (d <= 21 and m == 12):
        print("Nhan Ma")
    elif (d >= 22 and m == 12) or (d <= 19 and m == 1):
        print("Ma Ket")
    elif (d >= 20 and m == 1) or (d <= 18 and m == 2):
        print("Bao Binh")
    elif (d >= 19 and m == 2) or (d <= 20 and m == 3):
        print("Song Ngu")
