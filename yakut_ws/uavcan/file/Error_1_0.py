# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/Error.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:56.387553 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.file.Error
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Error_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    OK:             int = 0
    UNKNOWN_ERROR:  int = 65535
    NOT_FOUND:      int = 2
    IO_ERROR:       int = 5
    ACCESS_DENIED:  int = 13
    IS_DIRECTORY:   int = 21
    INVALID_VALUE:  int = 22
    FILE_TOO_LARGE: int = 27
    OUT_OF_SPACE:   int = 28
    NOT_SUPPORTED:  int = 38

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.file.Error.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.value, 65535), 0))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.file.Error.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Error_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u16()
        self = Error_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.file.Error.1.0'
        assert isinstance(self, Error_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.file.Error.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jJ1Sf0{@j&U2hyU6y1a-*`!TKl&TUS=zsvV5losyX%R0F_5&@O&aC#MEe~LMW}Lm2X2&Djvt*G#6baNymOzU60sH`7_=Q|='
        'HXltlLc0&M9$)+1b3MoB{&M55zn4nmpShcl5|yMrQA~20@*ioGGM~g^kPF2%vu3rUWfAK_vhFBn_Qc+QZhx}(%mT^i0OK149mX{C'
        'k2r3uNhzc?Win(^agkXlnWZO_@riBDHA}zS=hoaLRBOqjLNjH*L$qsnoUgKGq0U*FT;yLN3DuNnN9wxmx#R<``4CrZ_A<r$8A}?O'
        'W_>1KE#@YPxF#vf`WkF=9l>L&G#QA5S-5TPw9bIsHot<g$1a2wm435rYi<*zX_io#Tn2hkM6h5MhBPgZ!3~m#*qV~X*)>zHh|KNL'
        '=Okbg?o38+HP_*7cn|KLBFu+P3-7}RW|2&=-aV_A9p{oMcf7AuTW(X0b2L3ehb^;wBx&qs6~^n6F~-f@1M7-V5hnZa|G2F7f@Tmt'
        '4M?rs4%=f|umzt^lEAK6c(}j6w?6~oau9Y&J?sV5DQI)MGa!{4;kC5pW}&otP^r{99a60YjoLI?^E-Ppz};#fRHI$1bi?+yh-SWM'
        '_{{&rLv^!3u36$qMw9IyBwjdAWFGZ$s=?DhwU-N?Y2|5wvk8|h)<TZ#6*jv&vlQ0|o*W!Dssx|Cnxpfm=J%0~yTP8j)E-w}CbWlQ'
        '<B4}9BvN6Xrn1lU=_)l+Nc}Y$vwW<zdgHK0x?xBT587YXrXBL`qgf6)>~%?4C!N+oWjfktvmBBWWvAC_h3)Qi1?*kGF|&Ee&qy>n'
        'wMGZ)!3NxikKl872vztJ0{8}=K^G$U9tObS7&QC}KZAi61-eke@H)p7C1GEhHFCs{SweClHQ|X3%mz`SkTE0fBM>JNYnI$!$|Gx*'
        'TWHzGEjN3Do;J6Qo&&;p^nA{(S*eV2plOv2gf;KvMU?WGNY*b>m+!(&(H<60JstPEMAod0ecj*jANbC8tahHaNq{OOAz7xK?+$s)'
        '>`Ro>cEFSqwFC24+DsLx_QVki_>y)!kuy0qDc@ORlw#VC&s^=oLlIbCeYfV;S6m;C-#hHwK+PLO<kooCfvC|S5?C`be~f2<J;G%V'
        '$272Mo%e!85(CFh1OJ#eTQo^{)_-jg{Oh7Yk)~9Ru0~<&4|}h<{-=tt5$2}|wplJBtaHFK*I#fzkKJI&^%(pDj{k~tbDE8NWl%&;'
        'S^j@0RTRgp2LJ#'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
