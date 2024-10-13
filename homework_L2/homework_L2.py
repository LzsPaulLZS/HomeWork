'''
===================== 第二堂課 練習題 =====================
'''

#%%
'''
===================== 練習一 =====================
鍾QA正在測試某程式不同版本執行時間, 
他有一個串列:process_time_latest, 存放A程式執行毫秒的數據(最新一筆置於最後)
ex: process_time_latest = [385, 400, 395, 375, 401]
分別代表近五次A程式執行時間, 最新一次為401毫秒

程式步驟:
1. 您的程式開始時, 能讓使用者再輸入一筆最新測試結果, 例如 389
2. 若該結果與最新5筆數據相比排前三名(時間越短, 排名越高), 則顯示pass, 否則顯示fail
3. 顯示完成後, 這筆數據須加入process_time_latest串列, 並置放於最新的一筆; 
以本範例來說, 執行後process_time_latest: [385, 400, 395, 375, 401, 389]
下一回合執行時, 重新從步驟1開始, 並會跟最新的五筆 (從400這筆~389這筆)比較

其他功能:
若於程式步驟1, 使用者輸入exit, 則終止本程式

範例:
第一回合
process_time_latest = [385, 400, 395, 375, 401]
使用者輸入389 
因389跟最新五筆比較, 列為前三名, 終端機顯示pass
第二回合
process_time_latest = [385, 400, 395, 375, 401, 389]
使用者輸入399
因399跟最新五筆比較, 列為前四名, 排在前三以外, 故終端機顯示fail

提示:
1. 請考慮使用者有意/無意輸入不符格式, 造成例外的狀況
2. 可用list.sort()來排序 (增加及刪除也放到提示)
'''

# L2 第一題
def test_process_time_sort_v1():
    process_time_latest = [385, 400, 395, 375, 401]

    while True:
        user_Input = input("請輸入最新一次時間(ms): ")

        if user_Input.lower() == "exit":
            break
        else:
            try:
                input_time = int(user_Input)
                process_time_latest.append(input_time)
                process_time_latest.sort()
                if input_time < process_time_latest[2]:
                    print("pass")
                else:
                    print("fail")
                print(process_time_latest[:5])
            except ValueError:
                print("請輸入數字")

# 調用函數
test_process_time_sort_v1()


#%%
'''
===================== L2作業 =====================
以練習題為基礎, 調整功能如下
0. 鍾QA發現有時主管會調整排名標準, 請將此程式從"前3名pass"改為一個"前n名pass"的函式, n為參數
1. 程式步驟調整如下
    a. 使用者輸入數據
    b. 數據新增到csv
    c. 查看新數據是否符合前n名標準
2. csv須保留所有舊數據, 不做任何刪除
3. 加分題: 查看前n名的邏輯時, 嘗試不使用sort()來達成. 請參考氣泡排序法檔案 (Bubble.zip)
'''

import csv

# 以下請編寫您的L2作業

# L2 第二題
# 不使用 bubble 排序
def test_process_time_sort_v2(n):

    process_time_latest = []

    # 初始化CSV文件
    with open('new_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['index', 'time(ms)', 'result', 'list'])

    def print_csv_content():
        with open('new_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
        print()  # 添加一個空行，以提高可讀性

    while True:
        user_Input = input("請輸入最新一次時間(ms): ")

        if user_Input.lower() == "exit":
            break
        else:
            try:
                input_time = int(user_Input)
                process_time_latest.append(input_time)
                process_time_latest.sort()
                
                if len(process_time_latest) < n:
                    result = "pass"
                elif input_time <= process_time_latest[n-1]:
                    result = "pass"
                else:
                    result = "fail"
                
                print(result)
                print(process_time_latest[:n])

                # 將數據寫入CSV文件
                with open('new_data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([len(process_time_latest), input_time, result,[str(process_time_latest[:n])]])

                # 打印CSV的內容
                print("\nCSV 內容:")
                print_csv_content()

            except ValueError:
                print("請輸入數字")

# 調用函數
# test_process_time_sort_v2(6)


# 使用 bubble 排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def test_process_time_sort_v3(n):
    process_time_latest = []

    # 初始化CSV文件
    with open('new_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['index', 'time', 'result', 'list'])

    def print_csv_content():
        with open('new_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
        print()  # 添加一個空行，以提高可讀性

    while True:
        user_Input = input("請輸入最新一次時間(ms): ")

        if user_Input.lower() == "exit":
            break
        else:
            try:
                input_time = int(user_Input)
                process_time_latest.append(input_time)
                bubble_sort(process_time_latest)  # 使用冒泡排序替代 sort()
                
                if len(process_time_latest) < n:
                    result = "pass"
                elif input_time <= process_time_latest[n-1]:
                    result = "pass"
                else:
                    result = "fail"
                
                print(result)
                print(process_time_latest[:n])

                # 將數據寫入CSV文件
                with open('new_data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([len(process_time_latest), input_time, result, str(process_time_latest[:n])])

                # 打印CSV的內容
                print("\nCSV 內容:")
                print_csv_content()

            except ValueError:
                print("請輸入數字")

# 調用函數
# test_process_time_sort_v3(6)
