from whatsappStats import main, printStats
import sys

if len(sys.argv) != 2:
	print ('Incorrect number of arguments provided.')
	sys.exit()
else:
	file_name = str(sys.argv[1])
        main(file_name)
        printStats()
