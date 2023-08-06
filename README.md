Question 1 :
	python script for generating exploit string   =>  factorial.py
	commands for running:
		1)  Generating exploit string     :    python factorial.py > factorial_exploit_string
		2)  Passing input to executable   :    ./lab_2_rop < factorial_exploit_string



Question 2 :
	python script for generating exploit string is   =>    cipher.py
	
	commands for running:
		1)  Generating exploit string     :   python cipher.py > cipher_exploit_string
		2)  Passing input to executable   :   ./lab_2_rop < cipher_exploit_string

	TO EDIT THE INPUT PLAINTEXT    :   Let the input string to be given as plaintext be "ABCDEFGHIJ",  inside cipher.py at Line 1,  change the value of variable  cipher_string_init to ABCDEFGHIJ as follows
					   cipher_string_init = 'ABCDEFGHIJ\n'

	TO CHANGE THE VALUE OF KEY     :   Let the desired value of key be 'n',  inside cipher.py at Line 6,  change the value of variable GA_key_value to 'n' in its hex format in Little Endian .
					   The current key value that is set in the submitted cipher.py script is 3.

					   GA_value_key :
						key = 1  => GA_value_key = '\x01' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 2  => GA_value_key = '\x02' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 3  => GA_value_key = '\x03' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 4  => GA_value_key = '\x04' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 5  => GA_value_key = '\x05' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 6  => GA_value_key = '\x06' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 7  => GA_value_key = '\x07' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 8  => GA_value_key = '\x08' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 9  => GA_value_key = '\x09' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 10 => GA_value_key = '\x0a' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 11 => GA_value_key = '\x0b' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 12 => GA_value_key = '\x0c' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 13 => GA_value_key = '\x0d' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 14 => GA_value_key = '\x0e' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 15 => GA_value_key = '\x0f' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 16 => GA_value_key = '\x10' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 17 => GA_value_key = '\x11' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 18 => GA_value_key = '\x12' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 19 => GA_value_key = '\x13' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 20 => GA_value_key = '\x14' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 21 => GA_value_key = '\x15' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 22 => GA_value_key = '\x16' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 23 => GA_value_key = '\x17' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 24 => GA_value_key = '\x18' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3
                                                key = 25 => GA_value_key = '\x19' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3 + '\x00' * 12 + '\x00' * 3

							 
