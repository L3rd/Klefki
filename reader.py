import os, sys
unknownMode = False

print("Klefki (Created by: NoahAbc12345) | Example Usage: Klefki.exe \"C:\\Users\\Name\\Desktop\\otp.bin\" -unknown")
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Before using this program, you first need to specify the path to your otp.bin!")
else:
    print("Please do not share any values obtained from this program! Many are copyrighted and/or console-unique!")    
    fileOTP = sys.argv[1]
    try: unknownMode = True if sys.argv[2] == "-u" or sys.argv[2] == "-unknown" else False
    except: pass

    try:
        if os.stat(fileOTP).st_size == 1024:
            with open(fileOTP, "rb") as OTP:
                WiiBoot1 = (OTP.read(20)).hex()
                WiiCommon = (OTP.read(16)).hex()
                WiiNGID = (OTP.read(4)).hex()
                WiiNGPrivate = (OTP.read(28)).hex()
                WiiNANDHMAC = (OTP.read(20)).hex()
                WiiNAND = (OTP.read(16)).hex()
                WiiRNG = (OTP.read(16)).hex()
                Unknown1 = (OTP.read(8)).hex()
                SecurityFlag = (OTP.read(4)).hex()
                IOStrengthConfig = (OTP.read(4)).hex()
                SEEPROMPulseLength = (OTP.read(4)).hex()
                SignatureType = (OTP.read(4)).hex()
                WiiUStarbuck = (OTP.read(16)).hex()
                WiiUSEEPROM = (OTP.read(16)).hex()
                Unknown2 = (OTP.read(16)).hex()
                Unknown3 = (OTP.read(16)).hex()
                vWiiCommon = (OTP.read(16)).hex()
                WiiUCommon = (OTP.read(16)).hex()
                Unknown4 = (OTP.read(16)).hex()
                Unknown5 = (OTP.read(16)).hex()
                Unknown6 = (OTP.read(16)).hex()
                SSLRSAEncrypt = (OTP.read(16)).hex()
                StorageSeedEncrypt = (OTP.read(16)).hex()
                Unknown7 = (OTP.read(16)).hex()
                WiiUXOR = (OTP.read(16)).hex()
                WiiURNG = (OTP.read(16)).hex()
                WiiUSLC = (OTP.read(16)).hex()
                WiiUMLC = (OTP.read(16)).hex()
                SHDDEncrypt = (OTP.read(16)).hex()
                DRHWLANEncrypt = (OTP.read(16)).hex()
                Unknown8 = (OTP.read(48)).hex()
                WiiUSLCHMAC = (OTP.read(20)).hex()
                Unknown9 = (OTP.read(12)).hex()
                Unknown10 = (OTP.read(16)).hex()
                Unknown11 = (OTP.read(12)).hex()
                WiiUNGID = (OTP.read(4)).hex()
                WiiUNGPrivate = (OTP.read(32)).hex()
                WiiUNSSCertPrivate = (OTP.read(32)).hex()
                WiiUOTPRNGSeed = (OTP.read(16)).hex()
                Unknown12 = (OTP.read(16)).hex()
                WiiURootCertMSID = (OTP.read(4)).hex()
                WiiURootCertCAID = (OTP.read(4)).hex()
                WiiURootCertNGID = (OTP.read(4)).hex()
                WiiURootCertNGSig = (OTP.read(60)).hex()
                Unknown13 = (OTP.read(24)).hex()
                Unknown14 = (OTP.read(32)).hex()
                WiiRootCertMSID = (OTP.read(4)).hex()
                WiiRootCertCAID = (OTP.read(4)).hex()
                WiiRootCertNGID = (OTP.read(4)).hex()
                WiiRootCertNGSig = (OTP.read(60)).hex()
                WiiKorean = (OTP.read(16)).hex()
                Unknown15 = (OTP.read(8)).hex()
                WiiNSSCertPrivate = (OTP.read(32)).hex()
                Unknown16 = (OTP.read(32)).hex()
                WiiUBoot1 = (OTP.read(16)).hex()
                Unknown17 = (OTP.read(16)).hex()
                Empty1 = (OTP.read(32)).hex()
                Empty2 = (OTP.read(4)).hex()
                OTPVersion = (OTP.read(4)).hex()
                OTPDateCode = (OTP.read(8)).hex()
                OTPString = (OTP.read(8)).hex()
                Empty3 = (OTP.read(4)).hex()
                JTagStatus = (OTP.read(4)).hex()
                
            print(f"{'Wii boot1 SHA-1 Hash:':<36} {WiiBoot1}")
            print(f"{'Wii Common Key:':<36} {WiiCommon}")
            print(f"{'Wii NG ID:':<36} {WiiNGID}")
            print(f"{'Wii NG Private Key:':<36} {WiiNGPrivate}")
            print(f"{'Wii NAND HMAC:':<36} {WiiNANDHMAC}")
            print(f"{'Wii NAND Key:':<36} {WiiNAND}")
            print(f"{'Wii RNG Key:':<36} {WiiRNG}")
            print(f"{'Unknown (Padding):':<36} {Unknown1}") if unknownMode else None
            print(f"{'Security Level Flag:':<36} {SecurityFlag}")
            print(f"{'IOStrength Configuration Flag:':<36} {IOStrengthConfig}")
            print(f"{'SEEPROM Manual CLK Pulse Length:':<36} {SEEPROMPulseLength}")
            print(f"{'Signature Type:':<36} {SignatureType}")
            print(f"{'Wii U Starbuck Ancast Key:':<36} {WiiUStarbuck}")
            print(f"{'Wii U SEEPROM Key:':<36} {WiiUSEEPROM}")
            print(f"{'Unknown (Unused):':<36} {Unknown2}") if unknownMode else None
            print(f"{'Unknown (Unused):':<36} {Unknown3}") if unknownMode else None
            print(f"{'vWii Common Key:':<36} {vWiiCommon}")
            print(f"{'Wii U Common Key:':<36} {WiiUCommon}")
            print(f"{'Unknown (Unused):':<36} {Unknown4}") if unknownMode else None
            print(f"{'Unknown (Unused):':<36} {Unknown5}") if unknownMode else None
            print(f"{'Unknown (Unused):':<36} {Unknown6}") if unknownMode else None
            print(f"{'SSL RSA Encryption Key:':<36} {SSLRSAEncrypt}")
            print(f"{'USB Storage Seed Encryption Key:':<36} {StorageSeedEncrypt}")
            print(f"{'Unknown (Used):':<36} {Unknown7}") if unknownMode else None
            print(f"{'Wii U XOR Key:':<36} {WiiUXOR}")
            print(f"{'Wii U RNG Key:':<36} {WiiURNG}")
            print(f"{'Wii U SLC (NAND) Key:':<36} {WiiUSLC}")
            print(f"{'Wii U MLC (eMMC) Key:':<36} {WiiUMLC}")
            print(f"{'SHDD Encryption Key:':<36} {SHDDEncrypt}")
            print(f"{'DRH WLAN Data Encryption Key:':<36} {DRHWLANEncrypt}")
            print(f"{'Unknown (Unused):':<36} {Unknown8}") if unknownMode else None
            print(f"{'Wii U SLC (NAND) HMAC:':<36} {WiiUSLCHMAC}")
            print(f"{'Unknown (Padding):':<36} {Unknown9}") if unknownMode else None
            print(f"{'Unknown (Unused):':<36} {Unknown10}") if unknownMode else None
            print(f"{'Unknown (Unused):':<36} {Unknown11}") if unknownMode else None
            print(f"{'Wii U NG ID:':<36} {WiiUNGID}")
            print(f"{'Wii U NG Private Key:':<36} {WiiUNGPrivate}")
            print(f"{'Wii U NSS Device Certificate Key:':<36} {WiiUNSSCertPrivate}")
            print(f"{'Wii U OTP RNG Seed:':<36} {WiiUOTPRNGSeed}")
            print(f"{'Unknown (Unused):':<36} {Unknown12}") if unknownMode else None
            print(f"{'Wii U Root Certificate MS ID:':<36} {WiiURootCertMSID}")
            print(f"{'Wii U Root Certificate CA ID:':<36} {WiiURootCertCAID}")
            print(f"{'Wii U Root Certificate NG Key ID:':<36} {WiiURootCertNGID}")
            print(f"{'Wii U Root Certificate NG Signature:':<36} {WiiURootCertNGSig}")
            print(f"{'Unknown (Unused):':<36} {Unknown13}") if unknownMode else None
            print(f"{'Unknown (Locked/Unused):':<36} {Unknown14}") if unknownMode else None
            print(f"{'Wii Root Certificate MS ID:':<36} {WiiRootCertMSID}")
            print(f"{'Wii Root Certificate CA ID:':<36} {WiiRootCertCAID}")
            print(f"{'Wii Root Certificate NG Key ID:':<36} {WiiRootCertNGID}")
            print(f"{'Wii Root Certificate NG Signature:':<36} {WiiRootCertNGSig}")
            print(f"{'Wii Korean Key:':<36} {WiiKorean}")
            print(f"{'Unknown (Unused):':<36} {Unknown15}") if unknownMode else None
            print(f"{'Wii NSS Device Certificate Key:':<36} {WiiNSSCertPrivate}")
            print(f"{'Unknown (Locked/Unused):':<36} {Unknown16}") if unknownMode else None
            print(f"{'Wii U boot1 Key (Locked):':<36} {WiiUBoot1}")
            print(f"{'Unknown (Locked/Unused):':<36} {Unknown17}") if unknownMode else None
            print(f"{'Empty Space:':<36} {Empty1}") if unknownMode else None
            print(f"{'Empty Space:':<36} {Empty2}") if unknownMode else None
            print(f"{'OTP Version & Revision:':<36} {OTPVersion}")
            print(f"{'OTP Date Code:':<36} {OTPDateCode}")
            print(f"{'OTP Version Name String:':<36} {OTPString}")
            print(f"{'Empty Space:':<36} {Empty3}") if unknownMode else None
            print(f"{'JTAG Status:':<36} {JTagStatus}")
        else: print("The path provided does not lead to a valid otp.bin!")
    except: print("The path provided does not lead to a valid otp.bin!")