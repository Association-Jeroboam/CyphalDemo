# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/duration/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:07.619203 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.duration.Scalar
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
class Scalar_1_0:
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
                 second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.duration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param second: saturated float32 second
        """
        self._second: float

        self.second = second if second is not None else 0.0  # type: ignore

    @property
    def second(self) -> float:
        """
        saturated float32 second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._second

    @second.setter
    def second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._second = x
        else:
            raise ValueError(f'second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.second):
            if self.second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.second)
        else:
            _ser_.add_aligned_f32(self.second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.duration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.duration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'second=%s' % self.second,
        ])
        return f'uavcan.si.unit.duration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dxmvl0{?YWTTc`*6kg;isDwa#F;SibUdFx5;_xbFUsiA<#y8V+rght-Gt>04*)<`N2aP06G~xIk{TZIJ;39^3nbV%@_nog_'
        '7JmJnZ(M%inVvAqR6;B_k}CO`=87kzs7qa2={SUkC(ii7dBfjNG=~e=JA+f$4U43rCHkLwIx1+DSef`rx`cT{ovf?mq@ao#2rFd7'
        'jl~-fjj;UT%D#a9T)*)R&LFH2>YS0ecih59xND}rK@b*uk}EcwWtA}MC~<MXyVA9hrF3$H5%+tlrtV)jYb2MBC|(Vnfc`d?EU0y)'
        'tQiNf6&??+(_>n4h`yufLKuy&@D9Qjv5r=Z8g{eLcdS#=A@br`Z2Za4B9dc~mfn?(HNs9OZML&^C*9xgWZia_bq}&u>t!=-Wt}uj'
        'yRH3$b~jC%5PSJtEQTe^i@IVE76_{g2o1cZVe<x+B%e%IbP8feY*>WIxHi0?jx#t9kH{xE=8WjtI3gJwhYezDZwihM#fhc}AS}n9'
        'k~t1PKt+rP@%91<n|p!1MI9w@PfG}^hZ8NRdd<rk!V~RtB@1Hs(5u*QwjhMQG?fe{T1;GsvOzwsg#%%IDxIX2G?TbWaFO9nBB;fw'
        '46j_=?MN0J&c&|SLk@C<b)R2vezpM&bhpnC9=ww7&E@$7k5?K9^Q6`gw(lxpCuLqED4gU7L87kWv~M-Xv1>C^(h@0zM0JW@SRYWv'
        'WHtORNc5xk*eirNx$VUYBdR=yAF$is{%Lc3LV8*V`YS$1xTUP3NYS9<Xe>veBGWN@mGH5q)#WQY_PNb{p8NsT{R5Tr0{{R'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
