from bs4 import BeautifulSoup
import requests
# number = [i for i in range(0, 127)]
numberstr = 1
numbersite = 1
imgnumbers = 1
for i in range(120):
    imageurl = []
    user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
    url = "https://wallhaven.cc/user/RaidyHD/uploads?page=" + str(numberstr)
    page = requests.get(url, headers={'User-Agent': user_agent})
    print(page.status_code)
    print("Сайт готов взаимодействовать")
    soup = BeautifulSoup(page.text, "html.parser")
    for link in soup.find_all('a', class_='preview', href=True):
        imageurl.append(link['href'])
    if page.status_code == 200:
        numberstr=numberstr+1
        print(numberstr)
        print(url)
        print(imageurl)
        numbersite = 1
    for r in range(23):

        number_url_img = (imageurl[numbersite])
        page1 = requests.get(number_url_img)
        print(page.status_code)
        print('скачивание изображения номер'+str(imgnumbers))
        soup1 = BeautifulSoup(page1.text, "html.parser")
        nbr = soup1.find_all(class_='scrollbox')
        nbr = soup1.find(id="wallpaper")
        imagelink = (nbr['src'])
        p = requests.get(imagelink)
        out = open(r"C:\Users\ilyua\PycharmProjects\img"+str(imgnumbers)+".jpg", "wb")
        out.write(p.content)
        out.close()
        imgnumbers=imgnumbers+1
        numbersite=numbersite+1
    imageurl.clear()










