import cv2
import os
import glob
folder = "tarde3"
VIDEO_PATHS =  os.path.abspath(os.path.join('.', "Videos/"+folder))

VIDEO_PATHS_all = glob.glob(os.path.join(VIDEO_PATHS, "*.*"))
print(VIDEO_PATHS)
print(VIDEO_PATHS_all)
#"manha" MP5
#cont = 0 - 533
#"tarde1" mp4
#cont = 534 -817
#"tarde2" mp4 
# cont = 818 - 1524
#"tarde3" mp4
cont = 1525
def extract_images():
    local_cont = cont
    cont2 = 0
    for path in VIDEO_PATHS_all:

        print("\n\n ======= Extracting Video in "+ path +"  \n\n ======")
        cap = cv2.VideoCapture(path)
        cap.open(path)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        while length > 2:
            ret, frame = cap.read()
            length -= 1
            #Esse if serve pra quando houve problemas nos frames
            if ret:
                resize_and_save(frame,local_cont)
                #cv2.imshow("shown",frame)
                cont2 += 1
                if cont2 > 120:    
                    resize_and_save(frame,local_cont)
                    local_cont += 1
                    print(local_cont)
                    cont2 = 0
            k=cv2.waitKey(30) & 0xff
            if k == 27:
                break

def resize_and_save(frame, num):
    #print(frame.shape[0], frame.shape[1])
    width = 480
    height = int(frame.shape[0] * (width / frame.shape[1] ))
    dim = (width, height)
    img = cv2.resize(frame, dim)

    img_path = os.path.abspath(os.path.join('.', "Images/"+folder+"/"+str(num)+".png"))
    #print(img_path)
    #cv2.imshow("shown2",img)

    cv2.imwrite(img_path, img)


if __name__ == '__main__':  
  extract_images()