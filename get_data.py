#https://www.google.com/search?sca_esv=559161989&rlz=1C1VDKB_enBD1058BD1058&hl=en&sxsrf=AB5stBi4CC9GlrRTh36hb5cKpyRVOyVvlQ:1692735531752&q=dog&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiRisagi_GAAxWG1TgGHQPMCUsQ0pQJegQICBAB&biw=1280&bih=610&dpr=1.5

import shutil
import requests
from bs4 import BeautifulSoup
import os



def makeimages(name):
    def get_images_from_webpage(url, num_images=500):
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            img_tags = soup.find_all('img')

            image_urls = []
            for img_tag in img_tags:
                if 'src' in img_tag.attrs:
                    img_url = img_tag['src']
                    if str(img_url).startswith('https://'):
                        image_urls.append(img_url)
                        print(img_url)
                    if len(image_urls) >= num_images:
                        break

            return image_urls
        except :
            return ''

    def download_image(url, save_path):
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)



    name=name
    name=name.replace(' ', '+')
    path=os.getcwd()
    mdp=os.path.join(path,name)
    try:
        os.mkdir(mdp)
    except :
        pass


    webpage_url = [f'https://www.google.com/search?sca_esv=559161989&rlz=1C1VDKB_enBD1058BD1058&hl=en&sxsrf=AB5stBi4CC9GlrRTh36hb5cKpyRVOyVvlQ:1692735531752&q={name}&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiRisagi_GAAxWG1TgGHQPMCUsQ0pQJegQICBAB&biw=1280&bih=610&dpr=1.5',f'https://www.bing.com/images/search?q={name}&form=HDRSC3&first=1',f'https://duckduckgo.com/?va=a&t=hq&q={name}&iax=images&ia=images',f'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDYsMSw0LDUsMiw4LDcsOQ%3D%3D&word={name}',f'https://www.ecosia.org/images?q={name}',
                            f'https://yandex.com/images/search?text={name}',f'https://search.brave.com/images?q={name}&source=web',
                            f'https://www.mojeek.com/search?q={name}&fmt=images']  # Replace with the actual webpage URL
    addext= ['from+little+distence','from+little+close+distence','up+shot','down+shot','around','in+hand','form+side']
    lis=[]
    print("output should be ",len(addext)*len(lis))
    for tag in addext:
        for url in webpage_url:
            url = url.replace(name,name+"+"+tag)
            #print(url)
            
            lis.append(url)
        
    for url in webpage_url:
        lis.append(url)
    
    #print(lis,len(lis))
    webpage_url=lis
    num_images_to_get = 1000
    idx = 0
    for i in webpage_url:
        image_urls = get_images_from_webpage(i, num_images_to_get)
        for img_url in image_urls:
            try:
                if str(img_url).endswith('.svg'):
                    print("NOT IMPLEMENTED")
                else:
                    print(f"Image {idx + 1}: {img_url}",type(img_url))
                    filename = os.path.join(mdp, name+f'{idx}.jpg')
                    download_image(img_url,filename)
                    
                    idx=idx + 1
            except:
                pass
        print("Done Section -----------------------------------------------------------------")



    
