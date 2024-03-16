def check_password(password):
    if len(password) != 7:
        print("Şifre 7 karakter uzunluğunda olmalıdır.")
        return False
    
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        print("Şifrede en az bir sayı olmalıdır.")
        return False       
    return True

while True:
    password = input("Lütfen şifrenizi oluşturunuz(En az bir sayı içermeli ve 7 karakterden oluşmalı!): ")
    if check_password(password):
        print("Şifreniz Onaylanmıştır")
        break
    else:
        print("Şifrenizi istenilene uygun şekilde oluşturmalısınız")
