import requests

base_url = "https://api.openweathermap.org/data/2.5/"

def months():
    for i in range(1, 13):
        if i < 10:
            month = f"0{i}"
            days(month)
        else:
            month = str(i)
            days(month)

def days(month):
    for i in range(1, 32):
        if i < 10:
            day = f"0{i}"
            file = f"{month}-{day}.json"
            get_page(file)
        else:
            day = str(i)
            file = f"{month}-{day}.json"
            get_page(file)

def get_page(file):
    url = base_url + file
    r = requests.get(url)
    status_code = r.status_code
    if status_code != 400:
        print(url)
        download_file(r, file)
        
def download_file(r, file):
    f = open(file, "wb")
    f.write(r.content)
    f.close()

if __name__ == '__main__':
    months()