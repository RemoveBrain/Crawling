import os
from pytube import YouTube
from moviepy.editor import *

# 폴더 이름 설정
folderName  = "유튜브 다운로드"

# 바탕화면에 폴더 생성
UserName = os.path.expanduser("~") 
folderPath = f"{UserName}/Desktop/{folderName}"  
if not os.path.isdir(folderPath): os.makedirs(folderPath)

# 유튜브 제목에서 다운로드 된 영상 이름 추출
print("편집할 영상을 선택해주세요.")

# 디랙토리 보기
_directory = os.listdir(folderPath)
for i in range(len(_directory)) :
    print(f"{i+1} 번 : {_directory[i]}")

# 파일 선택하기
while True : 
    try : 
        select = int(input("\n번호를 입력해주세요. "))-1
        if (0 <= select and select < len(_directory)) :
            print(f"\n{_directory[i-1]} 를 선택하셨습니다.");break
        else : print(f"1~{len(_directory)} 사이 번호를 입력해주세요.")
    except :
        print(f"1~{len(_directory)} 사이 번호를 입력해주세요.")
        
selected_file = f"{folderPath}/{_directory[select]}"

print("영상을 편집합니다. ")
#현재 하드코딩부분//크롤링으로 자료 수집 예정
t0 = ["이... 이름이","오프닝","AirTag","iMac with M1","iPad Pro 5th","이번 이벤트의 소감은?"]
t1 = [0,13,44,194,438,698] 
# ===========================

for i in range(len(t1)-1) : 
    videoclip = VideoFileClip(selected_file)
    videoclip = videoclip.subclip(t1[i],t1[i+1]) 
    videoclip.write_videofile(f"{folderPath}/{i}번_{t0[i]}.mp4")
    
os.startfile(folderPath) ## 완료후 폴더 오픈
