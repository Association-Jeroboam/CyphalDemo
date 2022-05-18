# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/volumetric_flow_rate/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:07.822495 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.volumetric_flow_rate.Scalar
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
                 cubic_meter_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.volumetric_flow_rate.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param cubic_meter_per_second: saturated float32 cubic_meter_per_second
        """
        self._cubic_meter_per_second: float

        self.cubic_meter_per_second = cubic_meter_per_second if cubic_meter_per_second is not None else 0.0  # type: ignore

    @property
    def cubic_meter_per_second(self) -> float:
        """
        saturated float32 cubic_meter_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._cubic_meter_per_second

    @cubic_meter_per_second.setter
    def cubic_meter_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._cubic_meter_per_second = x
        else:
            raise ValueError(f'cubic_meter_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.cubic_meter_per_second):
            if self.cubic_meter_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.cubic_meter_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.cubic_meter_per_second)
        else:
            _ser_.add_aligned_f32(self.cubic_meter_per_second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.volumetric_flow_rate.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "cubic_meter_per_second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            cubic_meter_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.volumetric_flow_rate.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'cubic_meter_per_second=%s' % self.cubic_meter_per_second,
        ])
        return f'uavcan.si.unit.volumetric_flow_rate.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dxmvl0{?YW%}*0S6far?K}7=L;z3RV9@c(rv0TOUQo%-yH#3>p8M>3q?ri3xwk9NU&`2_gCOrRN-%zlKvdL!O?EC!v-fzCt'
        'e?6|(E}rnTnsCciLaZ>7D*2f*B@&Y9qS9760pa11Gd^?Pi1(99z&Y%k!U=4Lc~a5>{m(reWwcDJOnfO_GSbQy!Wo&7W2HY4L!C&D'
        'GODP7ut-M2SgA|MYhmHTrF{<lxqj^%oI+S8)L}03PFVN|x6St_2*P|%3dLu0EfG!~B`ywoTY6<=A)Opy#QmPq)cp-@nK0>y66Mh4'
        '(BH(88MTfSnhVI+!^Yq$J*Fl5=sSomgi-qn?;xxb>uAZT;nxd&$2tWaB1fLb#>a+c4&hs*rFUs#jj+{D8?A1uo$l_oyPa0I+u7?j'
        'n=cz_v)fL)X{Win*XpEc17a`F^7*ild4_Z&>%x!<Un??QatL+8bq1k^VKl5=qn5DAbbTj~Z{@2NA#+g~k>Rp9oP|f^SdIlJl{St@'
        '4u@ftSnW+F(4hpWC;|!#@uMU|FauP}co6@dBY|@-uy?MbJnmEy!qWbv%BgxS3Ju{&<(a~9jTm|r`^^@HRNR}&2@@?Q)}y45(Eo`F'
        '!pc-uNi%6Aan0Z&`)eep7AG{KbaC$^nF%<{xAPt3gDLFs>`E20?O>q0d4}-dm2__|&PRB>)JM2WbOmAawjy>?FpU6lk^=;cnv0u#'
        'i+iC?o0-b)kt~;}+`Jc729$GI4*v<t`_X&o6~dg{^kRh(RbIdk*zRxsv<$CTH7x}FMb8j!A<HOWH0U@Q3sJ<#ddyxTVqDSk;szdi'
        'W|?QnZ-SDjlp6#900'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
