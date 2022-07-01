#-*-coding:euc-kr
import time
import os

# �ϳ��� ��ĥ ���ϵ��� ����� ���� �̸��� �����ּ���.
directory = "personal_info"

# ����� ������ �̸��� �����մϴ�.
outfile_name = "simple_merged_ID.csv"

# ����� ������ �����մϴ�. �� �� �ؽ�Ʈ������ �����˴ϴ�.
out_file = open(outfile_name, 'w', encoding = 'utf-8')

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ ���빰�� �ϳ��ϳ� �ҷ��� ��ġ�� �۾��� �����մϴ�.
# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �ؽ�Ʈ ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".txt" not in filename:
        continue

    # �ؽ�Ʈ ������ �´ٸ�, ������ �о�ɴϴ�.
    file = open(directory + "/" + filename, encoding = 'utf-8')

    # ������ ���빰�� ���ڿ��� �ҷ��ɴϴ�.
    content = file.read()

    # ������ ���빰�� ����� ���Ͽ� �����մϴ�.
    out_file.write(content + "\n\n")

    # �о�� ������ �����մϴ�.
    file.close()

# ����� ������ �����մϴ�.
out_file.close()

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")