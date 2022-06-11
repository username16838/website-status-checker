import requests
from threading import Thread

print('if program comes back with <Response [200]>')
print('that means wbsite is up')

def ping():
    
    # check known search engines 
    
    print('checking search engines...')
    go = requests.get('https://google.com')
    du = requests.get('https://duckduckgo.com')
    st = requests.get('https://www.startpage.com/en/')
    se = requests.get('https://searx.thegpm.org/')
    ec = requests.get('https://www.ecosia.org/?c=en')
    print("\n")
    print('google')
    print(go)
    print("\n")
    print('duckduckgo')
    print(du)
    print("\n")
    print('startpage')
    print(st)
    print("\n")
    print('searX')
    print(se)
    print("\n")
    print('ecosia')
    print(ec)
    print("\n")
    #check known wiki
    
    print("checking wiki's...")
    wiki = requests.get('https://en.wikipedia.org/wiki/Main_Page')
    print("\n")
    print('Wikipedia')
    print(wiki)
    print("\n")
    # check known programing sites

    print('checking programming sites...')
    ph = requests.get('https://www.php.net/')
    py = requests.get('https://www.python.org/')
    cpp = requests.get('https://m.cplusplus.com/')
    print("\n")
    print('php')
    print(ph)
    print("\n")
    print('python')
    print(py)
    print("\n")
    print('c++')
    print(cpp)
    print("\n")
    print("feel free to submit known websites that are not malware domains")
   
# create threads 

th_1 = Thread(target=ping)
# start threads

th_1.start()

# wait for threads to complete

th_1.join()

