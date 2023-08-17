import sys

CHARS_PER_LINE = 16

def convert_file_to_array(input_file, output_file, array_name):
	num_bytes = 0
	with open(input_file, 'rb') as fp:
		bin_data = fp.read()
		num_bytes = len(bin_data)
		
		code = f"static const unsigned char {array_name}[{num_bytes}] = {{\n"
		for i, byte in enumerate(bin_data):
			code += f"0x{byte:02X}, "
			if (i + 1) % CHARS_PER_LINE == 0:
				code += "\n"
		code += "};"
		
		# UNIX utf-8
		with open(output_file, 'w', newline='\n', encoding='utf-8') as file:
			file.write(code)
	return num_bytes

if len(sys.argv) < 4:
	print("Usage: python bin2arr.py <input_file> <output_file> <array_name>")
else:
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	array_name = sys.argv[3]
	
	num_bytes = convert_file_to_array(input_file, output_file, array_name)
	print(f"Conversion successful, output has been written to {output_file}, {num_bytes} bytes.")