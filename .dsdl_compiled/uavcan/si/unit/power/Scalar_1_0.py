# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/unit/power/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.548053 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.power.Scalar
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
                 watt: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.power.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param watt: saturated float32 watt
        """
        self._watt: float

        self.watt = watt if watt is not None else 0.0  # type: ignore

    @property
    def watt(self) -> float:
        """
        saturated float32 watt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._watt

    @watt.setter
    def watt(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._watt = x
        else:
            raise ValueError(f'watt: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.watt):
            if self.watt > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.watt < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.watt)
        else:
            _ser_.add_aligned_f32(self.watt)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.power.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "watt"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            watt=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.power.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'watt=%s' % self.watt,
        ])
        return f'uavcan.si.unit.power.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YWO-~d-5MAU`Pzix}@gOIG%eWu2xLn2HVF5Q{yqQk-bhFb*&-A1}mR%DPIcOy5L=(zC>94SQ7hJ?Jm+9{6dR4F9'
        '>o0S^e$Up%UwB@PxaBG#Rv1Z@{7jh=3CVO(X)B$8@c6_TpE+;DhfyWq3U)5w9Ja$eDQSW6XPyo+S|(N|zLYMh^qDZpNk$bl5SGY5'
        '7%O!Nc`Yn{yk1{HccxqW1{V-k2zAa#=AE$c3GQp??<ENH2T~|LZDg5n>L_usyZh2BBMa%|0B<}zP@1}bxvUT-9Z{m}yBxZk2$@mq'
        'NTIoad?P&V-K58~WFKQkF@!W~U*SE34PqTFIW_z?(09ZsXdj2-c`STtXy%Z<#jzY*uMs0`wbFXC(`==?yRA;U+3B?RI*rDwdfMo;'
        '(oWiL?Cv$&X<CO^%d>nw%$?ypAj}c2GYB<2q+$KmAPE~y)H#QID_^rnkc-NQj5@*LGCU!taws^dv~fgoI1X#XYHu=u0VPO9vHh?Z'
        'e@ZfJy@zHP_TuRkj%(&6*3NZQf5G9OBBR;9#EzEtM^#SM8&PO<M&+5388M>oRjfP}3KJG4zJc(-N`#BvL2bwGfv`I9Ptr*0Nz@Zu'
        '9P>KKsm11uC|wkIATt4%`F6g8qhJa_U);z)l>slhyL$+aUQ2g4-k;$1+6ZBm=nBH-eIRyJFpZ3`lOtq^=86)&tAwFWo2i`^NR~^q'
        'X#O^=_9*AF?EiNuKaA01uaM^GZWIv)RCxhEV7t5d(=vQV)dUE-OP(R!LYC2~xS+$hSd4DPF~{s>B8C+$$4~9pGs`?n{s2<$bAR;%'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
