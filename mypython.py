import os
import random
import string

def main():
	cur_dir = os.getcwd()
	
	open_write_print_contents('{}/file1'.format(cur_dir), generate_random_chars(10)) 
	open_write_print_contents('{}/file2'.format(cur_dir), generate_random_chars(10)) 
	open_write_print_contents('{}/file3'.format(cur_dir), generate_random_chars(10)) 

	rand1 = random.randint(1, 42)
	rand2 = random.randint(1, 42)
	print(rand1)
	print(rand2)
	print(rand1*rand2)


def open_write_print_contents(filename, contents):
	file1 = create_file(filename)
	file1.write('{}\n'.format(contents))
	file1.seek(0)
	print(file1.read(), end='')
	file1.close()

def create_file(filename):
	return open(filename, 'w+')

def generate_random_chars(numChars):
	return ''.join([random.choice(string.ascii_lowercase) for n in range(numChars)])

if __name__ == "__main__":
	main()
