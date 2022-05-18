# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/scalar/Integer64.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:09.951241 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer64
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
class Integer64_1_0:
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
                 value: None | int | _np_.int64 = None) -> None:
        """
        uavcan.primitive.scalar.Integer64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int64 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated int64 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.int64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -9223372036854775808 <= x <= 9223372036854775807:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-9223372036854775808, 9223372036854775807]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i64(max(min(self.value, 9223372036854775807), -9223372036854775808))
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.primitive.scalar.Integer64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i64()
        self = Integer64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.primitive.scalar.Integer64.1.0'
        assert isinstance(self, Integer64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eTH>n0{?YW&1)1f6yMrzx3+#zTfBI%^&s^!Du_oZRs>nQE>^rrNG8usATty4vFr*3dr&L{6!v-cU-e~o+pU$(Ws-Tx@BKdB'
        'd|mndXSp?f(tSIYUYde=aGD$ag$n}(E1SwTUI)N*^C-AjhUnnK*aA-Q(Fq>oUTU+NS5)7Pd|2|juufMx=phuo<c7QAO&wqW?)fuJ'
        'YitP4>!wE4N}Z4M^#r?1-PU(J!L-462u_O_z~d*piq`odOzqbij9k!JXOaibLgskY^>d1tHjnh6207>Wud)p$bYKSRK~UJ;C+L#<'
        'z^X<9s_k^Qe+HAU6$ey1%q5c3`iAc@Z8INuExD5yfqq1x+NnL{CQ|<uCYusd3!~s^>w<bF#xrA&QSGQrPi!Pu2PF?6@ig6HpY;eN'
        'vyBT(OYEgh=9}nBpn?HrIrU1N{4!c#y56T8NB#VDLfV!dQ*YJe;I3JXY5ibq6*sS-YB1fiQ5an^2ZLyGzlEnB)9Nf}g1q44>MU$b'
        'ch2K3o)%AvY(IwV#uiiD6D<dI$axHP33#e@)dMm?7y^EHme#^8Iv6hRG2M8n!`tcph_>^*(lTo-rk$%m{J0VgsUjwaq>^SK(D1#p'
        ';CN`<BK1{PDoqomUZmT7E~Tyq{~b~Xx!Q|{B#$pw31JrQPu%P7|MG&y-p+uqyA}n>t#q9SiWYp77o9v*WOcs1&R}GDJ^eF!QFswW'
        '@fY3SS<k8i000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
