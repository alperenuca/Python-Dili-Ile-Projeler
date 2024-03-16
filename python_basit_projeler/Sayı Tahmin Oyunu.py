import random

def guess_number():
    
    target_number = random.randint(1, 500)
    attempts = 0
    
    print("Tuttuğum sayıyı tahmin et :)")
    
    while True:
        
        guess = int(input("Tahmininizi girin: "))
        attempts += 1
        

        if guess < target_number:
            print("Daha yüksek")
        elif guess > target_number:
            print("Sanki biraz fazla oldu :D ")
        else:
            print(f"Bravo bu sefer şans seninleydi ama bir dahakine seni yeneceğim. {attempts} Denemede buldun.")
            break

if __name__ == "__main__":
    guess_number()
