# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/angle/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:26.567628 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.angle.Scalar
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
                 radian: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.angle.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param radian: saturated float32 radian
        """
        self._radian: float

        self.radian = radian if radian is not None else 0.0  # type: ignore

    @property
    def radian(self) -> float:
        """
        saturated float32 radian
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian

    @radian.setter
    def radian(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian = x
        else:
            raise ValueError(f'radian: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.radian):
            if self.radian > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian)
        else:
            _ser_.add_aligned_f32(self.radian)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.angle.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "radian"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            radian=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.angle.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'radian=%s' % self.radian,
        ])
        return f'uavcan.si.unit.angle.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8zOaO10{?YWOHUL*5MJc52r3~EFCOG1a2fY8i_2BaURH1;#+&KXOgB57^gPm!&8`WF95j-2q6y_6^p{w@3oc@q%T#w&eN|u8'
        '*I$-?{a&n1KmWX%aKlx^jL;I4{0xZ_5lhRwDvh)P{o_-sU22^cA10N+E8M@pbKLXGtbm;S&m4?WC?X>xS4bN{F(ic36clLmt865+'
        'k!68d&DTF(+gI3M=-0mC1^RUc)@qqJD-3?Z`x^Qignqdvh2rx@)))s1%!cmnORu!drIjO!c-T`V*nhdKvqV~^L@~4(_IC&}1!GxW'
        'a)H^le>%8H4{6a6`Hq8&Xw<&qd-U7PSSUDXejDgJ;p8x+p*S82pJ_-f(Kj@f-nC5_ezzSrTHRJVJ~(K1JFRZFbJ%S*Up3-pw;gxm'
        'PV?Zf)rsQ<hFUJkmi>wbE}=lb#CVyauhBL5ty`mH$z-;lbIf+LO+ys9sI*AI3XYfl2|JTx!C6&m%OuAWzsXGLbSlW91gn4u_<Hy$'
        'nNafslEZiqZm(!y3oog5R)+mQs3iKeqe+#4dL#0Z6j8ZE$&_g^bSl)FFNmnG%=AKuh7y;8W@x8V)u7*)=_YDMjVSC9Z5Zzs%fL`e'
        'S`;=cb|h1Qm)TynPXkC4fxfs|`+WQqXz!lUKYA_g+v)j~j@JV4i>$2B@7xDsCV5g4BkJUs7?P;M>fTjCgDv%3Mk_4MBuO*t`HcZ^'
        'E{oxRL0La|Pn;r}le=C*7=dyEf8bt!=ch^N{Zum`?610n=;pEr3MB)^!Keq7(wIZ`8WZCRis=(OafwM>68!-g>k5SJ0{{R'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
