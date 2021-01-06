# Klefki
A tool used to break down a Wii U OTP.

Klefki is a command-line tool which can be used to break down each value inside of a Wii U's OTP (one-time programable) dump. This is most commonly obtained through the [Wii U NAND Dumper](https://github.com/koolkdev/wiiu-nanddumper/releases), which can be run through homebrew access on the Wii U console. Values that can be found include Wii U, Wii, and vWii information such as common keys and private keys. Please do not share any values obtained from this program! Many are copyrighted and/or console-unique!

In order to properly use the tool, you will need to run it through the command-line. Call the executable file and provide the path to your dumped one-time programmable. By default, any unknown and/or unused values according to [WiiUBrew's Hardware/OTP webpage](https://wiiubrew.org/wiki/Hardware/OTP) are hidden in the program. In order to show these values, pass `-unknown` (or `-u`) as the final argument.

An example input may include: `Klefki.exe "C:\Users\Name\Desktop\otp.bin" -unknown`

This tool has been tested on a Windows operating system. An executable file has been provided for general use.