

from network_config_module import config_functions

def main():
    # Menerima input dari pengguna
    user_input = input("Masukkan konfigurasi jaringan: ")

    # Memvalidasi input dari pengguna
    if config_functions.validate_input(user_input):
        # Menyimpan informasi konfigurasi jaringan yang telah diinput pengguna ke dalam list
        config_functions.save_configuration(user_input)
        print("Konfigurasi jaringan telah disimpan.")
    else:
        print("Format input tidak valid.")

    # Menampilkan informasi konfigurasi jaringan tertentu
    config_functions.display_configuration(0)  # Contoh: Menampilkan konfigurasi pertama

if __name__ == "__main__":
    main()
