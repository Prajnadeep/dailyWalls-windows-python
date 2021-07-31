import wget
import os
import ctypes
import time
import requests


# Prajnadeep

def displayTitle():
    print(" Daily Walls")
    print("    -by prajnadeep")
    print('')


# redirected url
def getURl():
    base_url = "https://source.unsplash.com/random/1920x1080"
    print("Fetching network image. .")
    print('')
    try:
        r = requests.get(base_url, allow_redirects=True)
        url = r.url
        print("Just a sec ..")
        # generate name from timestamp
        timeStamp = int(time.time())

        # make folder
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'Wallpapers')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        # save image
        dest_file = current_directory + '/Wallpapers/' + str(timeStamp) + '.jpg'
        image_filename = wget.download(url, dest_file)
        print('Image Successfully Downloaded: ', image_filename)

        # apply image
        path = os.path.abspath(dest_file)
        print(path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

    except requests.ConnectionError:
        print("Make sure you are connected to the Internet! ")
        time.sleep(5)


# delete image
# os.remove(path)
def main():
    displayTitle()
    getURl()


if __name__ == "__main__":
    main()
