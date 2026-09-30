import tkinter as tk
import random

# じゃんけんの手
hands = ["グー", "チョキ", "パー"]

# スコア変数
total_games = 0
wins = 0
losses = 0
draws = 0

def play(player_choice):
    global total_games, wins, losses, draws

    computer_choice = random.randint(0, 2)
    player_hand.set(f"あなた: {hands[player_choice]}")
    computer_hand.set(f"コンピュータ: {hands[computer_choice]}")

    total_games += 1

    if player_choice == computer_choice:
        draws += 1
        result.set("あいこです！")
    elif (player_choice == 0 and computer_choice == 1) or \
         (player_choice == 1 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 0):
        wins += 1
        result.set("あなたの勝ち！")
    else:
        losses += 1
        result.set("あなたの負け…")

    update_score()

def update_score():
    score.set(f"試合数: {total_games} | 勝ち: {wins} | 負け: {losses} | 引き分け: {draws}")

def reset_score():
    global total_games, wins, losses, draws
    total_games = wins = losses = draws = 0
    player_hand.set("")
    computer_hand.set("")
    result.set("")
    update_score()

# ウィンドウ作成
root = tk.Tk()
root.title("じゃんけんゲーム")
root.geometry("500x400")  # ウィンドウサイズ


# 表示用変数
player_hand = tk.StringVar()
computer_hand = tk.StringVar()
result = tk.StringVar()
score = tk.StringVar(value="試合数: 0 | 勝ち: 0 | 負け: 0 | 引き分け: 0")

# スコア表示（上部中央）
tk.Label(root, textvariable=score, font=("Arial", 14, "bold")).pack(expand=True)

# タイトル
tk.Label(root, text="手を選んでください", font=("Arial", 14)).pack(pady=5)

# 画像読み込み（サイズ調整）
gu_img = tk.PhotoImage(file="gu.png").subsample(3, 3)      # ← 2→3 に変更
choki_img = tk.PhotoImage(file="choki.png").subsample(3, 3)
pa_img = tk.PhotoImage(file="pa.png").subsample(3, 3)

# ボタン配置（画像ボタン）
frame_buttons = tk.Frame(root)
frame_buttons.pack(expand=True)
tk.Button(frame_buttons, image=gu_img, command=lambda: play(0)).pack(side="left", expand=True)
tk.Button(frame_buttons, image=choki_img, command=lambda: play(1)).pack(side="left", expand=True)
tk.Button(frame_buttons, image=pa_img, command=lambda: play(2)).pack(side="left", expand=True)

# 結果表示
tk.Label(root, textvariable=player_hand, font=("Arial", 12)).pack()
tk.Label(root, textvariable=computer_hand, font=("Arial", 12)).pack()
tk.Label(root, textvariable=result, font=("Arial", 14, "bold")).pack(expand=True)

# リセットボタン
tk.Button(root, text="スコアリセット", font=("Arial", 12), command=reset_score).pack(expand=True)

root.mainloop()
