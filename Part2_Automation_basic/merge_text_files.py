"""
# 회원 개인정보 파일 1천 개, 1초만에 텍스트 파일 하나로 합치기

아래 명령어를 실행하시면 됩니다.

> python merge_txt_files.py
"""
import time
import os

# 작업 시작 메시지를 출력합니다.
print("Process Start")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 하나로 합칠 파일들이 저장된 폴더 이름을 적어주세요.
directory = "personal_info"

# 결과물 파일의 이름을 정의합니다.
outfile_name = "merged_ID.txt"

# 결과물 파일을 생성합니다. 텅 빈 텍스트파일이 생성됩니다.
out_file = open(outfile_name, 'w', encoding = 'utf-8')

# 폴더의 내용물을 열람해 목록을 생성합니다.
input_files = os.listdir(directory)

# 폴더의 내용물을 하나하나 불러와 합치는 작업을 수행합니다.
# input_files에 저장된 파일 이름을 한 번에 하나씩 불러옵니다.
for filename in input_files:
    # 간혹 텍스트 파일이 아닌 파일이 섞여있을 수 있습니다. 이걸 걸러냅니다.
    if ".txt" not in filename:
        continue

    # 텍스트 파일이 맞다면, 파일을 읽어옵니다.
    file = open(directory + "/" + filename, encoding = 'utf-8')

    # 파일의 내용물을 문자열로 불러옵니다.
    content = file.read()

    # 파일의 내용물을 결과물 파일에 기재합니다.
    out_file.write(content + "\n\n")

    # 읽어온 파일을 종료합니다.
    file.close()

# 결과물 파일을 종료합니다.
out_file.close()

# 작업 종료 메시지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")