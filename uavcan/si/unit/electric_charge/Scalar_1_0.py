# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/electric_charge/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:07.988024 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.electric_charge.Scalar
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
                 coulomb: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.electric_charge.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param coulomb: saturated float32 coulomb
        """
        self._coulomb: float

        self.coulomb = coulomb if coulomb is not None else 0.0  # type: ignore

    @property
    def coulomb(self) -> float:
        """
        saturated float32 coulomb
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._coulomb

    @coulomb.setter
    def coulomb(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._coulomb = x
        else:
            raise ValueError(f'coulomb: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.coulomb):
            if self.coulomb > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.coulomb < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.coulomb)
        else:
            _ser_.add_aligned_f32(self.coulomb)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.electric_charge.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "coulomb"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            coulomb=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.electric_charge.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'coulomb=%s' % self.coulomb,
        ])
        return f'uavcan.si.unit.electric_charge.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8dxmvl0{?YWOK%e~5KieMeE?O}iVFvNfwq?=k4;Ih6y*|HB8s>n%e!{7mb`1rk0?Q^L=PY;SpuoUZ{^CkX-O&SUUux6`DVVE'
        '&tDdP{hqH~ec_p&Fw0~@EH{Em@tJ0lCnQ&;R#rF;;n9gRK6l>m4-?Jd686sF40gjJsc4D*=bnyoS|wH_z7j6slIPBdoa6;HL!O-E'
        'R8j+BnT)uxLRC=ILjB{leF^=!e(f8aLs%o!VPfVTx9|z>Ywd3kgvFlVlFeFLC5$>sT<r6{bZtZ_oETxmN>3{4{$;gBGU15i)zB5t'
        '-$uxsT1QI7I22pq$>1hErX`2yJBlu(QTqz-A#4%rXvL^uw}HMRPDzJ29?xRoQ$ury^ev91cWom^*lDMYR=3qo_xIb~POIDP9CVw_'
        'SB<pUZKvI|)7(F3b<(r}v6jz@#Zb?cm#WMlED)x02sON?Ve{53Nj90T>I{mVV#6Xw#<k%&b)3OPcuY>km@}f4aYQgU4jaTOZ*q<f'
        '$%&@OAk^be3M{lTKxK>v@%9oYHun;17b;5Offf)}4=1{y@(nK)gs0kP618CX(92kFwjt!cG?fk}T1;Gs@`12^M?iQpl~B@58cAF!'
        'xH#!eQc#P{8D6=#<B`ZYTok*-9*!cD2>;?n0kchDpu2m9@bI;8Z?DcLc)Zp^m?ug@*uD?MPRdLnH|*pHxuU+}7T;-Zs8eR9s3qhf'
        'P^CpLtPdz-q8k1eRP>|w*h{22x$8xQ5tW|957_N*|FjuCB|Qa#{<6=IZYioLRy6218uchx9C*xLC48)Db@kegeP%PCC4T@aZ5>tu'
        '1ONa'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
