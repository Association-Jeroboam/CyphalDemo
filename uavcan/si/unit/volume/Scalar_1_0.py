# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/volume/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:07.746133 UTC
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dxmvl0{?YWOHUL*5MJadsDwbgXd)+p%eaqO9Ij&avVt2i-b|-^y4~)i=aGJFc1=j+ppm2#O(=h)|H5h(T*NS!sqU)!s=lhP'
        'zbyRvJ>R(e!n1n9E!PRL!YHcMXUeolNM03nWt9^U9-cVkbLWkCKdA*=z}^|0!fse3B`whZ)YDN;%fzb0m&zrhO8Y`2Cpp#BKv*Fo'
        'VXUf3kd3hX;mW>%{#?KD4bC8}5$c>#%sXM>Biz-|-yjH!JtZ`sb+Sr0b(FZ+-d*XnQH649gc0|9x}xr1GHZk>N3<x1PC|bhA#-XS'
        'DJm{NZiUB#>-3nG9HQ?ix{yZWE4+iSMXaMGr-t7I`i?jS9pY3xkA*)OnmeR#aV)(n8!^I8CvCQ~b|>B6?_}L}mUR!ZR_kRmZDpM_'
        'OS`T8gLXGfn-FVxCKtn6?wQI-A)LS&FA!ek5E|&CVe`g337br}bP94uZdl~WMQub*o#1dD9+6LKEI6qv<A~yL95#rpyvYSRv>-J_'
        '7GXL5v|`9$fT9==;_U@aZSDoumQ_^2y;?z7J)G2%>er&EAUvr()7YaCL$71K*_M$1(o{8=XfbgiDhDs8+JUe>RZr4Nnn~OyxH#lZ'
        'BB{lmj3`}P??~kW&gHJ$!wE2rsL!vLKU)F@y4z<64_+zv=JI@k$153xc~aF7w(kP5lY&)92|GDLiYTqPz_+z9)Kz9CrX`X~g#wkm'
        'us)!it8(~XknBhAvDZj*a@&gtBdWcCAF$is{%IM$qIwDh{T0uUZlTJkQ#9x}8p~0uIOmwXO2oLP<>f;=_RKQRl0V>$uZ;8q000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)