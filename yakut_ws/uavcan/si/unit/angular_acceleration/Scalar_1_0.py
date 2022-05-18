# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/angular_acceleration/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:58.292990 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.angular_acceleration.Scalar
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
                 radian_per_second_per_second: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.angular_acceleration.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param radian_per_second_per_second: saturated float32 radian_per_second_per_second
        """
        self._radian_per_second_per_second: float

        self.radian_per_second_per_second = radian_per_second_per_second if radian_per_second_per_second is not None else 0.0  # type: ignore

    @property
    def radian_per_second_per_second(self) -> float:
        """
        saturated float32 radian_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian_per_second_per_second

    @radian_per_second_per_second.setter
    def radian_per_second_per_second(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian_per_second_per_second = x
        else:
            raise ValueError(f'radian_per_second_per_second: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.radian_per_second_per_second):
            if self.radian_per_second_per_second > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian_per_second_per_second < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian_per_second_per_second)
        else:
            _ser_.add_aligned_f32(self.radian_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.angular_acceleration.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "radian_per_second_per_second"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            radian_per_second_per_second=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.angular_acceleration.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'radian_per_second_per_second=%s' % self.radian_per_second_per_second,
        ])
        return f'uavcan.si.unit.angular_acceleration.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8j<tkh0{?YWOHUL*5MFe72r3~EE}F<mz{9wYSzNAS_OgN-G2Tq4X1dwwr00=-Y<5jZ<e-tH6HO@puhlHLh%%R{?s|S-ef_2W'
        'YqMUv{QR?O!VOmuGeS#H@-rk#L@X`ysx;CH^pB3McByq*e3(=MFL3t^PjSc3vjTGRzi=>0p@@u(Tp?`)#n36x4AN96p~1?sh>laB'
        'JM>FzB($L$%xZq|<CT4Z{keYa8=j$GVPLJ6iL=7sC%kLEKSAi{dr~Mqn`@bIu)u5>_OA3w%UoJHqKF4QRf7E++6qggWl9u7n_+*8'
        'N~T~e%S$dW+whx%>-3No9gy!ZxCln=E51j+!Hk81gXT92eWyA(42dJhL*o+-X&}cCExjw7YWVGT+-P-M?Ramm-R-ox-Ohfu*?iTA'
        'o85NYjXTY~{Z=QA8yI@IB%Ak7HE;<9tAr+?X<6_aCi*(#Ws1H=!Qj_#5X_Rvbcv^!ZD(tSfOAo4k%AQ*&;4U|BFBP?mD)1N@yM?+'
        'Q#zdrawx$nAXt7e{FF=x(ttEG9)#NqqH*pe_0Gy5l6#dzzkD#MGEi?sUZQ_exkSm7X%XZ?{bp+;LKdc?qC`W9^&l*w^?%Yrzd99H'
        ')QlQYST@?QgLRgHp$WApY}o!trUK8iootu*NEG#Weyxq!jwsOHKBIs5TH3dl=VLlvsl?xBWrcq0t|DfVCnW)-Ne&4xDKAX>t_ow9'
        'dZx7nmS&RloAvza063S$@SmWpAG}9S5zNVLFI5<Uasq$gPJipCN$8PP(?Zx^atXoBWf5dd28@HT7^F;0hU{e~#uXHo@9@YaCUHsh'
        '8(>4XVj%<o00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
