# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/unit/acceleration/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.500591 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.acceleration.Scalar
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
                 meter_per_second_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.acceleration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter_per_second_per_second: saturated float32 meter_per_second_per_second
        """
        self._meter_per_second_per_second: float

        self.meter_per_second_per_second = meter_per_second_per_second if meter_per_second_per_second is not None else 0.0  # type: ignore

    @property
    def meter_per_second_per_second(self) -> float:
        """
        saturated float32 meter_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second_per_second

    @meter_per_second_per_second.setter
    def meter_per_second_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._meter_per_second_per_second = x
        else:
            raise ValueError(f'meter_per_second_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.meter_per_second_per_second):
            if self.meter_per_second_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.meter_per_second_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.meter_per_second_per_second)
        else:
            _ser_.add_aligned_f32(self.meter_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.acceleration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter_per_second_per_second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            meter_per_second_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.acceleration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter_per_second_per_second=%s' % self.meter_per_second_per_second,
        ])
        return f'uavcan.si.unit.acceleration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YWOHUL*5MJadsDwbgaFBQqxQzRlh2<&+4-2>v<IQw>x|{7zdLHS=X4iy74jM^1(S-8<TFrvHVwhwy)l*ep)mQcP'
        '*SX)TbG4f%yr@Rpa-9$>jG|h7p_vv5VP#&GRyhIT>6tU0Id8<rQ6=CSb}!)qcEUU<Xpa7uo(>o-5~~tlD3?&igcgQ6RTjw^qna8B'
        'OJpF7#XlfxVe!+geGT22ZtXi<LRcZxIioV~goV%WP+xz8Aj}^rq4}hrWx}bW#Kk5bO0SH{l~V(ZczmQw>i(s)LNeuu7DeAl=x!k-'
        'qt=nU<O1YIc;359k7>yv`c9$?Y1F>K2M8O)I$CgQ_%zTD#K~zNXXAM+d~PU<!?8G)qgxv>!gedIH#^N%y0_Qrw40qy`=HZk?AOyq'
        'r<Hcnc4P0L*-q0s#9BU+^I<a=P8d?*YXvI{K4n6fBfMk~Y8Xqy`qX?$HX85l0_3(_v&fr^$_PfC;BXb5k#jW^2v!<L6o=EWMr`Q~'
        '6X?)_R1{f-#rV-GLq<K6%CHyzUgH#JUSn-pMr|xO{8A)3+gA?4^5LkGRKFE@31PGHnO2M#(f2x5p6m}37RIWA@W?8Ji^_uVWLjGg'
        'R>$f}8c98g+Xfexuudek*rO4Ji|ZdKCg4i$$X%RBrV;zqoj4{-!a#TbjP>3qcYJd`!{e<?!YnB(2wM+<*ioL9NDMnUL82(V*zNl&'
        'wq2Tu*cJ$r3I#0Rh1DMATowKQg5+`Zo_dWmNB6ymFreBC_z64RtzS07TUL#Mpu6NVq?@ZE>KF|=jK*TrGEO^YFB37WXmN89Pkm-H'
        'pCx|)vBKKV8Uz3U'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
