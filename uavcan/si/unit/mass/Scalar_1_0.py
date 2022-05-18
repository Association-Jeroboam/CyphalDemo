# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/mass/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:07.880800 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.mass.Scalar
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
                 kilogram: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.mass.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param kilogram: saturated float32 kilogram
        """
        self._kilogram: float

        self.kilogram = kilogram if kilogram is not None else 0.0  # type: ignore

    @property
    def kilogram(self) -> float:
        """
        saturated float32 kilogram
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._kilogram

    @kilogram.setter
    def kilogram(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._kilogram = x
        else:
            raise ValueError(f'kilogram: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.kilogram):
            if self.kilogram > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.kilogram < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.kilogram)
        else:
            _ser_.add_aligned_f32(self.kilogram)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.mass.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "kilogram"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            kilogram=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.mass.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'kilogram=%s' % self.kilogram,
        ])
        return f'uavcan.si.unit.mass.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dxmvl0{?YWOHUL*5MJc52r3~E4|<T3z-8RWEG}0uds)Ga7;mQ2Gu>==?3wBGW3y{QA_t8mooGV&2mK{hv*03zxpehZ)mQaZ'
        'ef?$O*YEk-<rkjm3A0Qk#Bw94lAmd&ctY~3(3O>rLwI=XjL)4n{QX38xPaX=IE9_CNJ?6u|B0ugoR*1|i7%x~3Tka~oKr;&gk>_~'
        '#>%P$Q494CSM~+;=lZp8a0X$OQ0I)yyyF%=!d?CR4T7-PlU%V`A1j1WM~REg-IcD5EToeojJV%Z6?OkoStXftMDcRy1oXEMGN;y&'
        'qGBAxW_UcfPLFBH0s0Q33u)B8!aE3?#5!6sYS>Mn?}$^-A<o3JSop-y+#!97W9ePlh!M8iX`|I`wbQ-5cDK{&c02psX7gnuZFbvf'
        'H|;d{_FJ7aZ9uH$GqD(!KS@;$4J{xn5LV?7YUrS0<Hj&aHkmHy6vVbzw@8w4ZFo){XK)@KkrO%QjOfZZA{iWobz&=Ta*htgiKa*)'
        ')Z?LKhV2hf592}ndx0aHdx5n@6$NllO9(3m6D_EE&5H`cQ|&V)b7J_=t5|QgA|$^w6$~a?Ok9Yf!6V8B!rD|gNi%6AagpHSd^d=o'
        '7CSP$baAsInR7T7J7O34XA1M4U+;Z3e++cD?+_lmlJ3pr{TQ!T3JCM0(h#=p0<n`KtB??Oa)<;`RdIK3H8<2%W~QShk_(C26uq!E'
        'pp40K_+OCdNAHnWNON-AiwGmCJcl2!)8G1OGkidL3IzRSpCR2smQkW;&~Y^CQKmTMn7u;ySkv<IjUD;SW<E>)067|^J?#Sk00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)