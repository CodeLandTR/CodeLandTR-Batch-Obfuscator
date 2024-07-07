import os
import base64

def encrypt_and_obfuscate_batch_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Dosya bulunamadı: {file_path}")
        return

    try:
        with open(file_path, "r") as f:
            original_code = f.read()

        # Kodu Base64 ile şifrele
        encoded_code = base64.b64encode(original_code.encode()).decode()

        # Yeni bir şifrelenmiş batch dosyası oluştur
        encrypted_file_path = os.path.join(os.path.dirname(file_path), "encrypted_" + os.path.basename(file_path))

        # Şifrelenmiş kodu yeni batch dosyasına yaz
        with open(encrypted_file_path, "w") as f:
            f.write("@echo off\n")
            f.write(":: Şifrelenmiş Batch Dosyası\n\n")
            f.write(f"set \"encoded={encoded_code}\"\n")
            f.write("certutil -decode %encoded% %~n0_decoded.bat >nul 2>&1\n")
            f.write("call %~n0_decoded.bat\n")
            f.write("del %~n0_decoded.bat >nul 2>&1\n")

        print(f"Şifrelenmiş dosya yolu: {encrypted_file_path}")

        # Orijinal batch dosyasını sil
        try:
            os.remove(file_path)
            print(f"Orijinal batch dosyası silindi: {file_path}")
        except OSError as e:
            print(f"Hata: Orijinal batch dosyası silinemedi - {str(e)}")

    except Exception as e:
        print(f"Hata: {str(e)}")

def main():
    file_path = input("Lütfen şifrelemek ve obfuscate etmek istediğiniz batch dosyasının yolunu girin: ")
    encrypt_and_obfuscate_batch_file(file_path)

if __name__ == "__main__":
    main()