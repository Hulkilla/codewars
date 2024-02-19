import re
ele1 = ("http://google.com")
ele2 = ("http://google.co.jp")
ele3 = ("https://123.net")
ele4 = ("https://hyphen-site.org")
ele5 = ("http://codewars.com")
ele6 = ("www.xakep.ru")
ele7 = ("https://youtube.com")
ele8 = ("http://www.codewars.com/kata/")
ele9 = ("icann.org")



def domain_name(url):
    
    if (re.search("://", url) != None) or (re.search("www.", url) != None):
        resultado = re.search(r'(://www.|www\.|://)([^/.]+)', url)
        return resultado.group(2)
    else:
        resultado = re.search(r'(www\.|://)?([^/.]+)', url)
        return resultado.group(2)


print(domain_name(ele9))

# Buenas prácticas

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]