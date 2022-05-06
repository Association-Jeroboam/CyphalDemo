# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/Health.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.187675 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.Health
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Health_1_0:
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
    NOMINAL:  int = 0
    ADVISORY: int = 1
    CAUTION:  int = 2
    WARNING:  int = 3

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.node.Health.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint2 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint2 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 3:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 3]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 3), 0), 2)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.node.Health.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Health_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(2)
        self = Health_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.node.Health.1.0'
        assert isinstance(self, Health_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.Health.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{@j&ZEIUM6n4@kaow$@ODSw)s|xE#=yIKxy+HTLb;)LuIBAl0FEE7em9C{tSGq{Lc03rYA2tXGHi-5c_BVIrm&9q8'
        'jRt~cOFHLyo^#HlU$6i5uwEPe`TOONS}GH4nGr;apGhiNf-_x|+6u>lfBVRpDsz=#$HS6^v#|Oy{1R6D0#>Ae{dX$T&xlHtrY!lI'
        '5$SmFb=+sh3atXK`K1?=^;y`N+o}B?UIu>?6X%RbE5~g30m5AY<os0d3)_N8dI6w;DRBh5i0Z2Ar4fa2q7NsQpDQbRiqVd8tjEk{'
        'HaBr99F|P=0RGNA1kZ?dxByat-}Uznrh($Mqz!v}aSIsLehY`e-^JDuMTw!afljNGFZhK%krg1gj;YRquLbz^man(9ig(;O2)@kk'
        'O;+#j%=7p7hy4CH!cupCuhVVq2L8aWA9IFA^-)YYBrM7+l{wH?s2(bfE}4--w4!t&6p^b*@QZkY;Df13?4&fz#-d!(sD4OdAR?!j'
        '_#=NKH)Isv!v6MT4f}p>Jw)m@1&AO0AA@@9>5I<M{^56#!rv{F8AzECiArLijT|#*5b5X&{&QrA>M^7Za+k<5mFWt~XBb5U0Y5mA'
        '6Ct5F;Usa0YG#qr4s>9BxY3CBZI#-gb*w<S(FFp1a&3yJ7E!~PO*o4TbncoH1v{71CP1Gj6CL=LpWAo?!b|Pe^W)BbH}dTt{}&7L'
        ';|vSvp;*!xj6%U7%6f)SI3F7_>H<1h5tn21l#P2E$yiJB@9;O@1pYUz!)~YhRfPZjW%#zr^9lAG22cV6In`{6zfy7jkkeBpBa{M2'
        'tH@${{56PM=Mb4+p0Nm=4###Ap(1{VukwfdOa2Al=1=%DzE{BjQwBxPh+{OI`dc^`Cye4!8;1oAU4I8#U73u*hGe)T(WaK-hZJe>'
        'Hx9t=P7dO)XJ7|&O&C|MqrWXW_$1K$*LuPQ-)Ij@PUKTo=-}Tkt5k{%8`i62%zR-<aA9%mj1Vb$WAL}f?wD*O>q#8L;G%OZV@@pK'
        'F`#X9ufE7wIOPw%6?3&(E440;+>HEu6a=)4vW_a9piVv-l$d5JxJ5-JohYFSab){2ZZH}v;17N1o0(n3+(4V3&?L28{iG3VHAw>w'
        '<tmFT*OjC&B)MdOW;9jf9X(DBA*@@Q9j$TFXhfG2tR{_ZEu|jV#|?zIbESRUYz_v4M3O<0X``5w38Pgr%T3d<6W84Mw7I#JY;0|A'
        'zH%ccB<bmX6MVHQK%8BX8e)dcf>A-5E!r1Wn;~uslR<q<v(?6%pN#^oZ6qbl0n@l`KacL5N+{aLQ;WQ?aj1%W^?UGdJrQnq^!<pP'
        'd$_-bbs0RmDu^8xsfLb$vhP6$!7~-p?}Ki{X>;)$E#iy|c<i|Iw+{%Vpy+Fd_%QBvD+$boukP|ke}t8t`9Ez6Z*e(}5O(TS3Ou1c'
        'u#5|G5*JJHnFD<y{ziNnh#EcDUGPnq#N;2>7g_)?2mk;'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
