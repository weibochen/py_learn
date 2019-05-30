#!/usr/bin/env python
# coding=utf-8

import random

# 创建单词序列
WORDS = (
    "python",
    "jumble",
    "easy",
    "different",
    "answer",
    "continue",
    "phone",
    "position",
    "pose",
    "game",
)


def guess_word_game():
    # 开始游戏
    print(
        """
            欢迎参加猜单词游戏
        把字母组合成一个正确的单词。
        """
    )

    is_continue = "y"

    while is_continue == "y" or is_continue == "Y":
        word = random.choice(WORDS)
        word_list = list(word)
        new_word_list = []
        while len(word_list):
            letter = random.choice(word_list)
            new_word_list.append(letter)
            word_list.remove(letter)

        new_word = "".join(new_word_list)
        print(new_word)

        guess = input("\n请你猜：")
        while guess != word and guess != "":
            print("猜错了！")
            guess = input("继续猜：")

        if guess == word:
            print("恭喜你，猜对了！")

        is_continue = input("\n是否继续(y/Y): ")


if __name__ == "__main__":
    guess_word_game()
