
#-*- coding: utf-8 -*-

class TriangleChecker:
    def can_make_triangle(self, len1, len2, len3):
        # type: (float,float,float) -> bool
        '''
        与えられた3つの辺の長さから、三角形が成立するかを判定する関数\n
        三角形が作れるならばTrueを返す\n
        a, b, cにおいて
        a + b > c かつ
        b + c > a かつ
        c + a > b

        Parameters
        ----------
        len1 : float
            辺1の長さ
        len2 : float
            辺2の長さ
        len3 : float
            辺3の長さ
        '''

        if len1 + len2 <= len3:
            return False

        if len2 + len3 <= len1:
            return False

        if len3 + len1 <= len2:
            return False

        return True

if __name__ == "__main__":
    tc = TriangleChecker()
    print(tc.can_make_triangle(3,4,5)) # True
    print(tc.can_make_triangle(3,4,7)) # False
