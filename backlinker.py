import json,requests,re,sys

try:
  print("""
            _ ____             _    _ _       _             
           | |  _ \           | |  | (_)     | |            
 _   _ _ __| | |_) | __ _  ___| | _| |_ _ __ | | _____ _ __ 
| | | | '__| |  _ < / _` |/ __| |/ / | | '_ \| |/ / _ \ '__|
| |_| | |  | | |_) | (_| | (__|   <| | | | | |   <  __/ |   
 \__,_|_|  |_|____/ \__,_|\___|_|\_\_|_|_| |_|_|\_\___|_|   
                                              cupsss168     
  """)
  if (sys.version_info.major == 3):
    site = input(" => Inject Backlink \t: ")
  else:
    site = raw_input(" => Inject Backlink \t: ")
  with open("urlbacklinks.json", "r") as file:
    data = json.loads(file.read())
    for backlink in data:
      url = backlink['url'].replace("h4link.duckdns.org", site)
      try:
        r = requests.get(url).status_code
      except KeyboardInterrupt:
        sys.exit()
      except:
        r = "time out"
      print(site + " => Inject Backlink ==> "+re.search('http:\/\/.*?\/', url).group(0).replace("/", "").replace("http:","") + " status: "+str(r))
except:
  print("\n\n => exit\n")
