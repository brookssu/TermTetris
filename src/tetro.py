# -*- coding: utf-8 -*-

"""Pre-defines the constant instances of all types and shapes of the tetrominos.
"""

import random

from cursor import putmsg, v_composing
from unicon import UnicodeIcon as UIcon


_P1 = ':{0}\x1b2hj'
_P01 = '2l:{0}\x1b4hj'
_P10 = _P1
_P11 = '2:{0}\x1b4hj'
_P001 = '4l:{0}\x1b6hj'
_P010 = _P01
_P011 = '2l2:{0}\x1b6hj'
_P100 = _P1
_P101 = ':{0}\x1b2l:{0}\x1b6hj'
_P110 = _P11
_P111 = '3:{0}\x1b6hj'
_P1111 = '4:{0}'


_SHAPE_I0 = v_composing(_P1 * 4)
_SHAPE_I1 = v_composing(_P1111)
_SHAPE_J0 = v_composing(f'{_P01 * 2}{_P11}')
_SHAPE_J1 = v_composing(f'{_P111}{_P001}')
_SHAPE_J2 = v_composing(f'{_P11}{_P10 * 2}')
_SHAPE_J3 = v_composing(f'{_P100}{_P111}')
_SHAPE_L0 = v_composing(f'{_P10 * 2}{_P11}')
_SHAPE_L1 = v_composing(f'{_P001}{_P111}')
_SHAPE_L2 = v_composing(f'{_P11}{_P01 * 2}')
_SHAPE_L3 = v_composing(f'{_P111}{_P100}')
_SHAPE_O0 = v_composing(f'{_P11 * 2}')
_SHAPE_S0 = v_composing(f'{_P011}{_P110}')
_SHAPE_S1 = v_composing(f'{_P10}{_P11}{_P01}')
_SHAPE_T0 = v_composing(f'{_P111}{_P010}')
_SHAPE_T1 = v_composing(f'{_P10}{_P11}{_P10}')
_SHAPE_T2 = v_composing(f'{_P010}{_P111}')
_SHAPE_T3 = v_composing(f'{_P01}{_P11}{_P01}')
_SHAPE_Z0 = v_composing(f'{_P110}{_P011}')
_SHAPE_Z1 = v_composing(f'{_P01}{_P11}{_P10}')


class Tetro:
    """Data structure description of the tetrominos.

    All types and shapes of tetrominos are pre-defined as constants and
    their instances are stored in a pool, in order of alphabetically
    sorted.
    """
    SQUARE_I = UIcon.GREEN_SQUARE
    SQUARE_J = UIcon.BLUE_SQUARE
    SQUARE_L = UIcon.ORANGE_SQUARE
    SQUARE_O = UIcon.YELLOW_SQUARE
    SQUARE_S = UIcon.GREEN_SQUARE
    SQUARE_T = UIcon.MAGENTA_SQUARE
    SQUARE_Z = UIcon.RED_SQUARE


    def __init__(  # pylint: disable=too-many-arguments
        self,
        height: int,
        width: int,
        bits: int,
        square: str,
        shape: str,
    ):
        self.height = height
        self.width = width
        self.bits = bits
        self.square = square
        self.shape = shape


    def show(self, row: int, col: int, square: str):
        """Shows tetro on the specified coordinate by using the 'square' as
        the composing unit.
        """
        putmsg(row, col, self.shape.format(square))


    def rotate(self):
        """Returns a new instance of rotating shape of the tetro.
        """
        i = TETRO_POOL.index(self)
        return TETRO_POOL[(i & 0xfc) | ((i + 1) & 0x03)]


    @staticmethod
    def choice():
        """Returns a random choiced tetro instance from the pool of tetrominos.
        """
        return random.choice(TETRO_POOL)


TETRO_I_0 = Tetro(4, 1, 0x0f, Tetro.SQUARE_I, _SHAPE_I0)
TETRO_I_1 = Tetro(1, 4, 0x0f, Tetro.SQUARE_I, _SHAPE_I1)
TETRO_I_2 = TETRO_I_0
TETRO_I_3 = TETRO_I_1

TETRO_J_0 = Tetro(3, 2, 0x3a, Tetro.SQUARE_J, _SHAPE_J0)
TETRO_J_1 = Tetro(2, 3, 0x27, Tetro.SQUARE_J, _SHAPE_J1)
TETRO_J_2 = Tetro(3, 2, 0x17, Tetro.SQUARE_J, _SHAPE_J2)
TETRO_J_3 = Tetro(2, 3, 0x39, Tetro.SQUARE_J, _SHAPE_J3)

TETRO_L_0 = Tetro(3, 2, 0x35, Tetro.SQUARE_L, _SHAPE_L0)
TETRO_L_1 = Tetro(2, 3, 0x3c, Tetro.SQUARE_L, _SHAPE_L1)
TETRO_L_2 = Tetro(3, 2, 0x2b, Tetro.SQUARE_L, _SHAPE_L2)
TETRO_L_3 = Tetro(2, 3, 0x0f, Tetro.SQUARE_L, _SHAPE_L3)

TETRO_O_0 = Tetro(2, 2, 0x0f, Tetro.SQUARE_O, _SHAPE_O0)
TETRO_O_1 = TETRO_O_0
TETRO_O_2 = TETRO_O_0
TETRO_O_3 = TETRO_O_0

TETRO_S_0 = Tetro(2, 3, 0x1e, Tetro.SQUARE_S, _SHAPE_S0)
TETRO_S_1 = Tetro(3, 2, 0x2d, Tetro.SQUARE_S, _SHAPE_S1)
TETRO_S_2 = TETRO_S_0
TETRO_S_3 = TETRO_S_1

TETRO_T_0 = Tetro(2, 3, 0x17, Tetro.SQUARE_T, _SHAPE_T0)
TETRO_T_1 = Tetro(3, 2, 0x1d, Tetro.SQUARE_T, _SHAPE_T1)
TETRO_T_2 = Tetro(2, 3, 0x3a, Tetro.SQUARE_T, _SHAPE_T2)
TETRO_T_3 = Tetro(3, 2, 0x2e, Tetro.SQUARE_T, _SHAPE_T3)

TETRO_Z_0 = Tetro(2, 3, 0x33, Tetro.SQUARE_Z, _SHAPE_Z0)
TETRO_Z_1 = Tetro(3, 2, 0x1e, Tetro.SQUARE_Z, _SHAPE_Z1)
TETRO_Z_2 = TETRO_Z_0
TETRO_Z_3 = TETRO_Z_1

TETRO_POOL = (
    TETRO_I_0, TETRO_I_1, TETRO_I_2, TETRO_I_3,
    TETRO_J_0, TETRO_J_1, TETRO_J_2, TETRO_J_3,
    TETRO_L_0, TETRO_L_1, TETRO_L_2, TETRO_L_3,
    TETRO_O_0, TETRO_O_1, TETRO_O_2, TETRO_O_3,
    TETRO_S_0, TETRO_S_1, TETRO_S_2, TETRO_S_3,
    TETRO_T_0, TETRO_T_1, TETRO_T_2, TETRO_T_3,
    TETRO_Z_0, TETRO_Z_1, TETRO_Z_2, TETRO_Z_3,
)
