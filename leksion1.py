#imports
from urllib.request import urlopen
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

url_find_title = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/poseidon"

def find_title(url):
    #Define webpage.
    

    #Open webpage.
    page = urlopen(url)
    #print(page)

    #Extract informationn from the html.
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    #print the structure of the html%%%
    #print(html)

    #Find the html position of the title tag.
    title_index = html.find("<title>")
    #print the position of the title%%%
    #print(title_index)

    #Find the start position of the title index indstead of the title tag.
    start_index = title_index + len("<title>")
    #Print the title start_index.
    #print(start_index)%%%

    #Find the end postion of the title index.
    end_index = html.find("</title>")
    #Print the title end_index.
    #print(end_index)%%%


    #Extract title by slicing the index.
    title = html[start_index:end_index]
    #print title and url.
    print(f"Website url = {url}")
    print(f"Title = {title}")



#Call find title function
find_title(url_find_title)

def record_audio():
    fs = 44000  # Sample rate
    seconds = 10  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('myaudio.wav', fs, myrecording)  # Save as WAV file 


    pass

def audio():
    print("Step 1: Recording audio")
    record_audio()
    print("Step 1: Audio recorded(Completed)")
    print("Step 2: Playing audio")
    playsound('myaudio.wav')
    print("Step 2: Play audio(Completed)")

audio()