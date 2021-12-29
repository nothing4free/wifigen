import itertools, sys, os.path


# defines the colors on the console, taken from blender:
# https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


numeric = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

alphanumeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabetic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def print_intro():
    print("")
    print(" ██╗    ██╗██╗███████╗██╗ ██████╗ ███████╗███╗   ██╗")
    print(" ██║    ██║██║██╔════╝██║██╔════╝ ██╔════╝████╗  ██║")
    print(" ██║ █╗ ██║██║█████╗  ██║██║  ███╗█████╗  ██╔██╗ ██║")
    print(" ██║███╗██║██║██╔══╝  ██║██║   ██║██╔══╝  ██║╚██╗██║")
    print(" ╚███╔███╔╝██║██║     ██║╚██████╔╝███████╗██║ ╚████║")
    print("  ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝  v.0.1")
    print("")
    print("     A simple Wifi password dictionary generator")
    print("      written by Jorge Martinez / nothing4free")
    print("")


def generate_dict(dict_type, password_len, filename):
    print(" [" + color.OKBLUE + "i" + color.ENDC + "] Generating dictionary with the following parameters:")
    if dict_type == alphanumeric:
        print("     > Dictionary type: alphanumeric")
    elif dict_type == alphabetic:
        print("     > Dictionary type: alphabetic")
    elif dict_type == numeric:
        print("     > Dictionary type: numeric")
    print("     > Password length: " + str(password_len))
    print("     > Writing to file: " + filename)
    print("")
    print(" [" + color.OKBLUE + "i" + color.ENDC + "] This process may take several minutes, please wait...")
    print("")
    f = open(filename, "w", newline='')
    counter = 0
    try:
        for p in itertools.product(dict_type, repeat=password_len):
            for i in p:
                counter = counter + 1
                if counter < password_len:
                    f.write(str(i))
                else:
                    f.write(str(i))
                    f.write("\n")
                    counter = 0
        print("[" + color.OKGREEN + 'i' + color.ENDC + "] Dictionary generated successfully, exiting now...")
    except:
        print(" [" + color.FAIL + "!" + color.ENDC + "] An error occurred while generating the dictionary, "
                                                     "exiting now...")

def check_files(file):
    if os.path.isfile(file):
        print(" [" + color.FAIL + "!" + color.ENDC + "] ERROR: File already exists.")
        quit()


def init_script():
    print_intro()
    dict_type = sys.argv[2]
    password_len = int(sys.argv[4])
    filename = sys.argv[6]
    check_files(filename)
    if dict_type == "alphanumeric":
        generate_dict(alphanumeric, password_len, filename)
    elif dict_type == "alphabetic":
        generate_dict(alphabetic, password_len, filename)
    elif dict_type == "numeric":
        generate_dict(numeric, password_len, filename)


if len(sys.argv) != 7:
    print(" [" + color.FAIL + "!" + color.ENDC + "] Invalid arguments.")
    print("     Usage: wifigen.py -t <type> -l <length> -o <filename>")
    print("     Supported types: alphanumeric, numeric, alphabetic")
else:
    init_script()