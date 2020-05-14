
def show_banner():

    path_file = "banner.txt"
    
    open_file = open(path_file, "r")
    banner = open_file.read()
    print(banner+"\n\tCoder: SoftPanG")
    
    open_file.close()

show_banner()

    
