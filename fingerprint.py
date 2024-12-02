import win32com.client

def main():
    try:
        wbf = win32com.client.Dispatch("WinBio.BiometricIdentity")
        enrolled_identities = wbf.EnumBiometricUnits()
        
        if not enrolled_identities:
            print("Tidak ada sidik jari yang terdaftar di laptop ini.")
            return
        
        for identity in enrolled_identities:
            print("Mengidentifikasi sidik jari untuk unit:", identity)
            result = wbf.Identify(identity)
            
            if result:
                print("Identifikasi sidik jari berhasil.")
            else:
                print("Sidik jari tidak cocok.")
    
    except Exception as e:
        print("Terjadi kesalahan:", str(e))

if __name__ == "__main__":
    main()
