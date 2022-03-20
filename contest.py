class Solution:
    @staticmethod
    def minimum_white_tiles(floor: str, carpets: int, size: int) -> int:
        floor = floor + '0' * len(floor)
        # 0 is black, 1 is white
        floor = list(floor)
        n = len(floor)
        w = sum(tile == '1' for tile in floor)
        # print('===', floor)

        # keep finding the best position of placing the carpet
        # try to cover all whites, starting with a white
        while carpets > 0 and w > 0:
            keep = 0
            # print('finding best carpet position')
            max_whites = 0
            for i in range(n):
                whites_here = 0
                if floor[i] == '1':
                    for j in range(i, i + size):
                        if floor[j] == '1':
                            whites_here += 1
                # print('whites', i, whites_here)
                if whites_here > max_whites:
                    max_whites = whites_here
                    keep = i

            # print('best carpet', keep, keep + size)
            for i in range(keep, keep + size):
                if floor[i] == '1':
                    w -= 1
                floor[i] = '0'
            carpets -= 1

            # print(floor)

        # print(''.join(floor))
        # return white visible tiles now
        return w


_floor = "000000000010000000000100000011000000010010000000001111000001100000000"
"""
000000000010000000000100000011000000010010000000001111000001100000000
00000000001000000000010000001100000001001000000000xxxx000001100000000
"""
assert Solution.minimum_white_tiles(_floor, carpets=1, size=4) == 8
_floor = "10110101"
"""
10110101
10xx01
"""
assert Solution.minimum_white_tiles(floor=_floor, carpets=2, size=2) == 2
_floor = "11111"
assert Solution.minimum_white_tiles(floor=_floor, carpets=2, size=3) == 0
# assert
_floor = "1" * 1000
assert Solution.minimum_white_tiles(_floor, 1, 256) == 8
