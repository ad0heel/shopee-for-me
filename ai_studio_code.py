import sys

def print_rgb(text, r, g, b):
    """
    使用 ANSI Escape Codes 輸出指定 RGB 顏色的文字
    格式: \033[38;2;R;G;Bm文字\033[0m
    """
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")

def get_input(prompt, allow_empty=False):
    """
    處理輸入:
    1. 檢查是否輸入 'exit'
    2. 檢查是否為數字
    3. 處理留空預設值
    """
    while True:
        user_input = input(prompt).strip()
        
        # 檢查是否為離開指令 (不分大小寫)
        if user_input.lower() == "exit":
            return None

        # 如果允許留空且輸入為空，回傳 0
        if allow_empty and user_input == "":
            return 0.0
        
        # 嘗試轉換為浮點數
        try:
            return float(user_input)
        except ValueError:
            print("❌ 輸入錯誤，請輸入有效的數字，或輸入 'exit' 離開程式。")

def main():
    print("--- 費用計算器 ---")
    
    while True:
        print("\n" + "="*30) # 分隔線，區分每一次新的計算
        
        # 1. 要求用戶輸入資訊 (若輸入 exit 會收到 None，則跳出迴圈)
        sell_price = get_input("請輸入想販賣的售價 : ")
        if sell_price is None: break
        
        cost = get_input("請輸入 '羽台成本': ")
        if cost is None: break
        
        replenishment = get_input("請輸入 '回補' (留空默認0): ", allow_empty=True)
        if replenishment is None: break

        # 2. 計算 temp_result_1 (11% + 60)
        temp_result_1 = (sell_price * 0.11) + 60

        # 3. 計算 temp_result_2 (13% + 60)
        temp_result_2 = (sell_price * 0.13) + 60

        # 4. 最終計算
        # result_1: 售價 - 成本 + 回補 - temp_result_1
        result_1 = sell_price - cost + replenishment - temp_result_1
        
        # result_2: 售價 - 成本 - 回補 - temp_result_2
        result_2 = sell_price - cost + replenishment - temp_result_2

        print("\n--- 計算結果 ---")

        # 5. 輸出結果與顏色判斷
        
        # 處理 Result 1 (11%-60)
        output_text_1 = f"方案 (11%-60) 結果: {result_1:.2f}"
        if result_1 >= 0:
            print_rgb(output_text_1, 0, 200, 0) # 綠色
        else:
            print_rgb(output_text_1, 200, 0, 100) # 紫紅色

        # 處理 Result 2 (13%-60)
        output_text_2 = f"方案 (13%-60) 結果: {result_2:.2f}"
        if result_2 >= 0:
            print_rgb(output_text_2, 0, 200, 0) # 綠色
        else:
            print_rgb(output_text_2, 200, 0, 100) # 紫紅色

        # 6. 新增：輸入備註
        print("") # 空一行美觀
        memo = input("請輸入備註: ")
        # 備註顯示顏色: RGB(100, 150, 200)
        if memo:
            print("備註內容: ", end="")
            print_rgb(memo, 100, 150, 200)
        
        # 迴圈將自動回到開頭，無需額外代碼

    print("程式已關閉。")

if __name__ == "__main__":
    main()