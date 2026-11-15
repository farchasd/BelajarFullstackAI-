import sys 
import requests
import bs4


# if len(sys.argv)>1:
#     query =" ".join(sys.argv[1:])
# else:
#     query="python programming language"

# print(f"sedang mencari artikel wikipedia untu : {query}")

url = f"https://en.wikipedia.org/wiki/Indonesian_cuisine"

try:
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    res = requests.get(url, headers=header)
    res.raise_for_status()

except Exception as exc:
    print(f"gagal mengunduh {exc}")
    # sys.exit()

soup = bs4.BeautifulSoup(res.text, "html.parser")

link_elems = soup.select('p')

# 6. Memeriksa apakah hasil pencarian ditemukan
if not link_elems:
    print('Tidak ditemukan artikel yang sesuai dengan kata kunci tersebut.')
else:
    
    # Mengambil maksimal 5 hasil teratas
    num_results = min(20, len(link_elems))
    for i in range(num_results):
        title = link_elems[i].getText()
        # Menambahkan domain wikipedia karena link bawaannya berupa link relatif (/wiki/...)
        
        
        print(f"{title}")
        

  


