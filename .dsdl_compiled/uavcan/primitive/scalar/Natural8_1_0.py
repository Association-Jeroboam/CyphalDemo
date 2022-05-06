# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/primitive/scalar/Natural8.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.304804 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Natural8
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
class Natural8_1_0:
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
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.primitive.scalar.Natural8.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint8 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint8 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 255:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 255]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u8(max(min(self.value, 255), 0))
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.primitive.scalar.Natural8.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Natural8_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u8()
        self = Natural8_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.primitive.scalar.Natural8.1.0'
        assert isinstance(self, Natural8_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Natural8.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YW%W70X5S@_BBqlx>65O~jx{$cJ>du{Df*@nY!KgcFs&ALm4SgT<W0(;FW}z5pP)PX^{-xEKBoiaKo9?>Rb^4q-'
        ')n8YB|5@&we(8QYQ(oCZcytD=`2x~nA<Cv|8*c(qx^)m-EJJkoe%2zL(BmUIq@C0iHB_A6jxZ^qE?Q?Q6U+n)UxEc!41tTlKBu%M'
        'Cg{9rYSNvw`tfXkLW8A2=Q|xy+7J+eGcpGB^og!xb#aJN_mx4b7Hrmqf&e09ir1B2Fr>8kq4s86qk3Hj9HaYJ+J=xO2#fVNXd0|B'
        'cnLm;s!>RKE8QKP1Ld+}mvj3$#ezED=pCgk;RDnPoVpD3BTC&(-3i#p3|53{N=hAy64K@+{X)*>ojoMIt^1zYC~O^;5Kz%^x-CAN'
        'DJs!6E(oJ&nEJvu(Ur&vi=qX-E3M|m8cFHKh>e_%^4}BIw)BMW)=hS<7kC9vX?bh{rS;uetHJJJ)lj<EMrlnc9FC*SH!u3j1--fF'
        '41TGny}9p{`sdCU&x)r-c7j4~%cjuanV-WtWNRj-L^{?F^h553w2b@c+_**C_+YpiQ@Z)mgg2-00f%SCrDf5yJdoFc_*o?z7R5~V'
        'StO4|;5mHTqJz-5h5bEIYQw{&U!*%DP|DQf{|@QBoE=8Xif31|j4*fkC+!T@etF3+pq&HpI7P{FD^usm;tfpmW;IV2cRE+E3!Ju4'
        'pFWadlwL+z`~|yrqdv3)000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
