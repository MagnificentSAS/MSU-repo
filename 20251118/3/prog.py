import sys

try:
    buf = sys.stdin.buffer.read()
    if buf[:4] != b"RIFF":
        raise Exception
    Size = int.from_bytes(buf[4:8], 'little')
    Type = int.from_bytes(buf[20:22], 'little')
    Channels = int.from_bytes(buf[22:24], 'little')
    Rate = int.from_bytes(buf[24:28], 'little')
    Bits = int.from_bytes(buf[34:36], 'little')
    Data_Size = int.from_bytes(buf[40:44], 'little')
    print(f"{Size=}, {Type=}, {Channels=}, {Rate=}, {Bits=}, Data size={Data_Size}")

except:
    exit(0)