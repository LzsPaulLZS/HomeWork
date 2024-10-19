'''
===================== 第二堂課 練習題 =====================
修正完成時間: 2024/10/20 01:13
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

# L2 練習題
def test_process_time_v1():
    process_time_latest = [385, 400, 395, 375, 401]

    while True:
        user_Input = input("請輸入最新一次時間(ms) 或輸入 'exit'退出: ")
        print()

        if user_Input.lower() == "exit":
            break

        try:
            input_time = int(user_Input)
            # print(f"輸入的時間是: {input_time}")
            if input_time < 0:
                print("輸入的值不能小於 0，請重新輸入。")
            else:
                process_time_latest.append(input_time)
                latest_five = process_time_latest[-6:-1]
                sort_latest = sorted(latest_five)
                print(f'不包含本次，最新5筆時間為:{sort_latest}')
                if input_time < process_time_latest[2]:
                    print(f"此次時間數據{input_time}與最新5筆數據相比，排名於前3名，故pass")
                else:
                    print(f"此次時間數據{input_time}與最新5筆數據相比，落後前3名，故Fail")
                print(f'所有數據依時間排序為:{process_time_latest[:]}')
            print('-------------------------------------------------------------------')
        except ValueError:
            print("請輸入數字")

# 調用函數
# test_process_time_v1()


#%%
'''
===================== L2作業 =====================
以練習題為基礎, 調整功能如下:

1. 鍾QA發現有時主管會調整排名標準
→請將此程式從"前3名pass"改為一個"前n名pass"的函式, n為參數

2. 程式步驟調整如下:
    a. 使用者輸入數據
    b. 新增功能: 數據新增到csv
    c. 查看新數據與最新5筆數據相比，是否符合前n名標準

3. 補充: csv須保留所有舊數據, 不做任何刪除

加分題
查看前n名的邏輯時, 嘗試不使用sort()來達成. 請參考氣泡排序法檔案 (Bubble.py)
'''

import csv
import sys

# 以下請編寫您的L2作業

# L2 作業
# 不使用 bubble 排序
def test_process_time_with_csv_v1(n):

    if n > 5:
        print('n必須小於等於5')
        sys.exit()
        

    process_time_latest = []

    # 初始化CSV文件
    with open('new_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['編號', '時間數據time(ms)', '結果result', '不包含本次，最新5筆數據排序' ,'完整數據list'])

    def print_csv_content():
        with open('new_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
        print()  # 添加一個空行，以提高可讀性

    while True:
        user_Input = input("請輸入最新一次時間(ms) 或輸入 'exit'退出: ")
        print()

        if user_Input.lower() == "exit":
            break

        try:
            input_time = int(user_Input)
            # print(f"輸入的時間是: {input_time}")
            if input_time < 0:
                print("輸入的值不能小於 0，請重新輸入。")
            else:
                process_time_latest.append(input_time)
                if len(process_time_latest)< 6:
                    result = f"此次時間數據{input_time}未大於總數據5筆，故pass"
                    init_time = process_time_latest
                    sort_latest = sorted(init_time)
                    # print(f'所有數據依時間排序為:{process_time_latest[:]}')
                else:
                    latest_five = process_time_latest[-6:-1]
                    sort_latest = sorted(latest_five)
                    print(f'不包含本次，最新5筆時間為:{sort_latest}')
                    if input_time <= sort_latest[n-1]:
                        result = f"此次時間數據{input_time}與最新5筆數據相比，排名於前{n}名，故pass"

                    else:
                        result = f"此次時間數據{input_time}與最新5筆數據相比，落後前{n}名，故Fail"
                    print(f'所有數據依時間排序為:{process_time_latest[:]}')

                        # 將數據寫入CSV文件
            with open('new_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([len(process_time_latest), input_time, result, sort_latest, [str(process_time_latest[:])]])

            # 打印CSV的內容
            print("\nCSV 內容:")
            print_csv_content()


            print('-------------------------------------------------------------------')
        except ValueError:
            print("請輸入數字")

# 調用函數
# test_process_time_with_csv_v1(3)




# 使用 bubble 排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # 返回排序後的列表

def test_process_time_with_csv_v2(n):

    if n > 5:
        print('n必須小於等於5')
        sys.exit()
        

    process_time_latest = []

    # 初始化CSV文件
    with open('new_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['編號', '時間數據time(ms)', '結果result', '不包含本次，最新5筆數據排序' ,'完整數據list'])

    def print_csv_content():
        with open('new_data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
        print()  # 添加一個空行，以提高可讀性

    while True:
        user_Input = input("請輸入最新一次時間(ms) 或輸入 'exit'退出: ")
        print()

        if user_Input.lower() == "exit":
            break

        try:
            input_time = int(user_Input)
            # print(f"輸入的時間是: {input_time}")
            if input_time < 0:
                print("輸入的值不能小於 0，請重新輸入。")
            else:
                process_time_latest.append(input_time)
                if len(process_time_latest)< 6:
                    result = f"此次時間數據{input_time}未大於總數據5筆，故pass"
                    init_time = process_time_latest
                    sort_latest = bubble_sort(init_time)
                    # print(f'所有數據依時間排序為:{process_time_latest[:]}')
                else:
                    latest_five = process_time_latest[-6:-1]
                    sort_latest = bubble_sort(latest_five)
                    print(f'不包含本次，最新5筆時間為:{sort_latest}')
                    if input_time < sort_latest[n-1]:
                        result = f"此次時間數據{input_time}與最新5筆數據相比，排名於前{n}名，故pass"

                    else:
                        result = f"此次時間數據{input_time}與最新5筆數據相比，落後前{n}名，故Fail"
                    print(f'所有數據依時間排序為:{process_time_latest[:]}')

                        # 將數據寫入CSV文件
            with open('new_data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([len(process_time_latest), input_time, result, sort_latest, [str(process_time_latest[:])]])

            # 打印CSV的內容
            print("\nCSV 內容:")
            print_csv_content()


            print('-------------------------------------------------------------------')
        except ValueError:
            print("請輸入數字")

# 調用函數
# test_process_time_with_csv_v2(3)



# 測試git PR 因此多加此行 
# 再次多加一行
# 再多加一行，測試PR 分支:update-homework-L2




# %%
