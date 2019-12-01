import re, os

def html_to_txt(dataset):
    
    files = os.listdir(dataset+'html/')
    txt = os.listdir(dataset+'txt/')
    
    if len(files) == len(txt):
        print("Dataset adquirido com sucesso")
        return
    
    for f in files:
        
        file = open(str(dataset+'html/'+f), "r")
        text = file.read()
        file.close()
        
        songStart = [i for i in range(len(text)) if text.startswith("<pre", i)]
        songEnd = [i for i in range(len(text)) if text.startswith("</pre>", i)]
        
        song = text[songStart[0]:songEnd[0]]
        
        chords = re.findall('<b>(.*?)</b>', song)
        
        new_file_path = str(dataset + 'txt/' + f[:-4] + 'txt')
        
        txt = open(new_file_path, "w+")
            
        for k in chords:
            txt.write(k+" ")
            
        txt.close()
        
    print("Dataset adquirido com sucesso")