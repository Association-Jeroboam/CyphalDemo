# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/unit/volume/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.537261 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.volume.Scalar
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
                 cubic_meter: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.volume.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param cubic_meter: saturated float32 cubic_meter
        """
        self._cubic_meter: float

        self.cubic_meter = cubic_meter if cubic_meter is not None else 0.0  # type: ignore

    @property
    def cubic_meter(self) -> float:
        """
        saturated float32 cubic_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._cubic_meter

    @cubic_meter.setter
    def cubic_meter(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._cubic_meter = x
        else:
            raise ValueError(f'cubic_meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.cubic_meter):
            if self.cubic_meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.cubic_meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.cubic_meter)
        else:
            _ser_.add_aligned_f32(self.cubic_meter)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.volume.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "cubic_meter"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            cubic_meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.volume.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'cubic_meter=%s' % self.cubic_meter,
        ])
        return f'uavcan.si.unit.volume.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YWOHUL*5MJadsDwbgXd)+p%eaqO9Ij&Uuz(ve-b|-^y4~rdXL{0)&8`WF95j-2q6y_M^$%Fhf{PgDGSyvGU)5Lj'
        '^_RI{zh@hlUwBrJx#cP$Rv1Z@{7jh=3CVR?Yb%|A@bJVLpF3~F`*AJc0(Q>e6t=@Wsc4D*r=AXTS|wH{zLG8(YUN9joa9td17V2_'
        'g|SjsP&C5ghb#L6dNaMoH#mc^La1{_GVg?ik8oE<e}f>*A4sA2w3B7RsiVZj_U=lrjVz^;LyWk8pfq*=l35{4I-*21a0T=>5i+ON'
        'ky3L3#YTACzfO;7$v*myq6=v>zQQ{Q8^k(VaccNYpznxN(g9Az^H}(kp}9l)7RPdMWg|w|>ZHwf*6yUcyPd4t&a&=a)@r?Mrmd`#'
        'W@)#zyVvffX%k{C&x-l5l6xj|QVJ(<#&d-096|$qG_2p4Ct>5smQJDAD%LFW<f1krr%rG<50A(vITD=I+BhOP9EUYxwKusyhZ3Zw'
        '$RaGppOOq2^idR}e!RWFsm;8=+J%lPSaA5KNNjc>9falmaa~aLT9g{XliD+d-5N3QDpsEE3lkP5`hjrIN`#9V!pn(@AgoSwl(dp&'
        '688!&j(eRH)M9r=R4y)hD02bl#dfiSvtSBQpI^&hx(*C<x6cqByprzl@_d5FD?x-=qH747cY)Y($uv^JPL7ZwiY%`3Z7mFS+Dv7&'
        'K=MMOREsxZwNE*h)!@IN;xKxTy+WGf+g?N%Qso8wfbHJqPs{K<)e|7-EqR7?OIbz5qCrQ|Sd6O0Imhf}B1Sc>E}z`7XO?-E`~e!Z'
        '?fw1(000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
