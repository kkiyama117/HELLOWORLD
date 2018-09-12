if __name__ == '__main__':
    # 原作準拠によりとても冗長になっております
    hello_world_letters = ("1001000",
                           "1100101",
                           "1101100",
                           "1101100",
                           "1101111",
                           "100000",
                           "1010111",
                           "1101111",
                           "1110010",
                           "1101100",
                           "1100100")
    hello_world = ""
    for letter in hello_world_letters:
        # 文字列を2進数にする
        bin_letter = int(letter, 2)
        # 2進数を16進数に変換
        hex_letter = hex(bin_letter)
        # (int -> bytes経由で)unicodeに
        x = int(hex_letter, 16)
        hello_world += str(
            int(hex_letter, 16).to_bytes((x.bit_length() + 7) // 8, 'big'),
            'utf-8')
    print(hello_world)
