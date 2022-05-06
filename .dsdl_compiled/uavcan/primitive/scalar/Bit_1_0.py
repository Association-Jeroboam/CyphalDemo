# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/primitive/scalar/Bit.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.291318 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Bit
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
class Bit_1_0:
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
                 value: None | bool = None) -> None:
        """
        uavcan.primitive.scalar.Bit.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated bool value
        """
        self._value: bool

        self.value = value if value is not None else False

    @property
    def value(self) -> bool:
        """
        saturated bool value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: bool) -> None:
        self._value = bool(x)  # Cast to bool implements saturation

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_unaligned_bit(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.primitive.scalar.Bit.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Bit_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_unaligned_bit()
        self = Bit_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.primitive.scalar.Bit.1.0'
        assert isinstance(self, Bit_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Bit.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YWO=}cE5Z#dMCMJFm61;dYdXRV-^%n$^;APFa81W`e^>n-4&@<ii$FeH~%t2wHK_MmnU8{GKY>Z?sQ$5x7s@{7w'
        '-`0NrS?$c9{M1cF5T;^5dJRT@1#V=;YTGy)bd;DMoJODOn7sTrbrLV|<vE_=e(tgs8p=OOFs`AkoY#$xdMv9@g8^S1>WF!RjinFT'
        'wx~LJ{nKT9f&G<!=Leo+-eM4=*E~fT@H5^u(DfzE-M3mAu^eQR35dXAneMLg>*1*3p|wUr`!Aa<#&u*ywxg(MI0CI9MAld#QSIi('
        '!z+MNRvl69q@;*Q=R1DDyvss_R)7~bfo6%TZtjl3B<j4zgsm}mFmcE`H+VBXU5I&xYENwknnp<HWergZoaKk?i=Ifqob{1ufrGrw'
        'f=#}blrWMxpk8^syo~0U?+wYj$*_FAAZ{zKsJF7ktX`xy1k9_W;?CyL)G08>vaw{OOWf$1c{xg^bYAL81-*sM1b#!y-ok3k_sQ()'
        'P4&7e;$tj|>@Wp^M)R_b#f`D9CC=0{^_+y@h9F;Dd9_rGF2>vE1^T=B`IL^Ap5;|$9p=5eK*F@)miW*lC&Z67A=2u-chW<&e(8LV'
        ')k@Pose}Az2tw#~^xq|QT(W~?i0t%smJk*O|HS?N%CEp_>D>Yd`x}W9-A1<*mH;LtSTBo3BA4n-CMOQs`F}A;Jn+P;zmHI^F`@$i'
        '00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)