# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/angular_velocity/Vector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:07.724938 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.angular_velocity.Vector3
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
class Vector3_1_0:
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
    def __init__(self,
                 radian_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.unit.angular_velocity.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param radian_per_second: saturated float32[3] radian_per_second
        """
        self._radian_per_second: _NDArray_[_np_.float32]

        if radian_per_second is None:
            self.radian_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(radian_per_second, _np_.ndarray) and radian_per_second.dtype == _np_.float32 and radian_per_second.ndim == 1 and radian_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._radian_per_second = radian_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                radian_per_second = _np_.array(radian_per_second, _np_.float32).flatten()
                if not radian_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'radian_per_second: invalid array length: not {radian_per_second.size} == 3')
                self._radian_per_second = radian_per_second
            assert isinstance(self._radian_per_second, _np_.ndarray)
            assert self._radian_per_second.dtype == _np_.float32  # type: ignore
            assert self._radian_per_second.ndim == 1
            assert len(self._radian_per_second) == 3

    @property
    def radian_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] radian_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second

    @radian_per_second.setter
    def radian_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._radian_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'radian_per_second: invalid array length: not {x.size} == 3')
            self._radian_per_second = x
        assert isinstance(self._radian_per_second, _np_.ndarray)
        assert self._radian_per_second.dtype == _np_.float32  # type: ignore
        assert self._radian_per_second.ndim == 1
        assert len(self._radian_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.radian_per_second) == 3, 'self.radian_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.radian_per_second)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of uavcan.si.unit.angular_velocity.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "radian_per_second"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f0_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            radian_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of uavcan.si.unit.angular_velocity.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'radian_per_second=%s' % _np_.array2string(self.radian_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.unit.angular_velocity.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dxmvl0{?YXTTc@~6fRKiq9VozeUK-?m$jEIEWRnGnk>`?3~y$f-5EL)_m<h&rfWhX4;o1(k%Z&#@vnKNEppLr((LS<+jqWm'
        'zJ9I#`dzIIAM-RTS<WJd<XlM_$uBgBxI@A;&eB|J4rb+0t0L5e;vdS4!v#D)g%j8`vm~K0+BXW?4{74$(kT+D9h&rth$_<OQ5s5J'
        'I!8RzscM2*z&n-8GyzdD^GD<J1^82b<vW~$Ste9#C4)lq96rJ%aDSb^%(f+u*cGTH!l<T1Tcqa6gm9&33Fcv24mjK6Nl%Mc_UdMP'
        'D}+Zp=7}CBn}8)#GL~BQ(POb4rBvU{vP=T0Ni-}1{yO3dX|73}G7jRgdDOiOw_(mM+V-spIjMYu0|ZHOO%p~HyPoI==80(!*)EtZ'
        'e5`1wk;@!8ZjaBH!)!F&TElBJ-L0*r*J^lPYsahCw`*?QYr3A>s&DNyTCQ6ITdN4nBBINv9UAyErb>bcGd{a){0abapl^SJx$|1;'
        '5uJzlIi|qOkTe6cJ}F6F#z7j%5X{;>k5i=8f`6ZJMR94ah@2y#kT_}4G7k=T#<l#v-!%D**u_iqyVofqT*UIW6XxpEsNnDuHvRSU'
        'JiyMYB$f&IpX`AS>|x#x2^Sdy{3+{MInR-HKFDY?+}lnO*ibQRRuyHECIstXQ(>Agz&tF)rYcA)HEY-Qngr!YI42<X#A=Q!!g!{5'
        'NHu40X6}+>yO$(Ol_ruw$E=b(EmX+S5OI=GTmUm~Uy%%O_+8ZLplfe0u>YwSSX-o4nA4dAv$R`gf<|wUTPuhnK(2}6R-#z%N-a3('
        'xsi}DFvq~E6*HLox8;miV?jH0r{>tHg0`!=Mg+|fp0b)jk@RKA;Y{p{j&MYM$h>gH_GnI{0d*;3GU@#@MYMYOZ;_46;4dJ}ZU2*a'
        'i@$f6#vgO<`~g_6P`1hh000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
