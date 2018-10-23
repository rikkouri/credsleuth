import credsleuth

#config = credsleuth.ConfigEngine()
#config.verbose = True

print(credsleuth.check_string("string of data\npassword=123\nsome more text"))
print(credsleuth.check_file('sample.txt'))


