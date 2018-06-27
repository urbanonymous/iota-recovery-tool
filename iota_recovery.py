from iota import Iota
from string import ascii_uppercase


char_set = ascii_uppercase + "9"

# Generates addresses of a given seed using the "get_new_addresses()" function
def addressGenerator(seed, iota_node, n_addresses):
	api = Iota(iota_node, seed) 
	gna_result = api.get_new_addresses(count=n_addresses) # This is the actual function to generate the address.
	addresses = gna_result['addresses']
	total = 0
	i = 0
	while i < n_addresses:
		address = [addresses[i]]
		balance = addressBalance(address, iota_node)
		print ("Address " + str(address[0]) + " has a balance of: " + str(balance))
		total += balance
		i += 1
	if total > 0:
		print ("The above addresses have a total balance of " + str(total) + " Iota tokens!!!")
		return True
	else:
		print ("No balance on those addresses!")
		return False

# Sends a request to the IOTA node and gets the current confirmed balance
def addressBalance(address, iota_node):
	api = Iota(iota_node)
	gb_result = api.get_balances(address)
	balance = gb_result['balances']
	return (balance[0])


def generateSeedAddresses(iota_target_seed, n_addresses, iota_node):
	money_found = False
	for idx, character in enumerate(iota_target_seed):
		idxp = idx+1
		print("\n----Current step: {} letter replaced {}".format(idx, character))
		for new_char in char_set:
			print("--Using", new_char)
			working_seed = iota_target_seed[:idx] + new_char + iota_target_seed[idxp:]
			
			if addressGenerator(working_seed, iota_node, n_addresses):
				money_found = True
				print("MONEY FOUND!!! ")
				print("\n\n\n\n\n\n")
				break

		if money_found:
			break

			
def main():
	# Get the target seed
	iota_target_seed = str(input("Target seed: "))
	#iota_target_seed = "MXJBHQOCOPWUWGKE9ZMYUDPUKLKICORJAFTMXKAHSXZ9BDHKBZNNVVZQHXNLLDUXTFOAQOYNEUQCAOFQA"
					    
	n_addresses = int(input("Number of addresses: "))
	#n_addresses = 100

	iota_node = "https://nodes.iota.cafe:443" # NODE SERVER

	print ("This can take a while...")
	print("\n\n\n")
	#addressGenerator(iota_target_seed, iota_node, n_addresses)
	generateSeedAddresses(iota_target_seed, n_addresses, iota_node)
 
if __name__ == '__main__':
	main()