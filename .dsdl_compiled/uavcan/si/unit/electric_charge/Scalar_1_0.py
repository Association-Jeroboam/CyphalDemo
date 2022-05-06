# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/unit/electric_charge/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.527993 UTC
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YWOHUL*5MJc5JXAs;UOdP}fy=m$Sy--O@UVazG2Tq4XS&($q-T24kIk+Li5xVNbfO96|FxP07ctCbs=KPbs;}zn'
        'uXDd==4#hpcu|d+Whx<-8%dS?LNmn^lIx<<Ryq#h$*D6wci!-i<BG!->|DS(Y=?PL(gOW2Jssw>Osq_NDP6)9&z+Gu$ptk7o}A`X'
        'Q3GL-47ssVmmq4P{^`cPg5FH8_8l%DtPtujG4qaF_zVxV_BRN^{GsHEO<P(fj5<nO?DL`Y%E&@GImC#iL#3(vm(>c%q$7%#11F%j'
        'iI6$9jue`45F6oH|293QB?ss`jxMB8`vxB%Y!K^c$*5s>fqo!PK?gV<&tl;-Lvx4pEso{z#zu^=)lM6&ZmXT{?zX#~R=3;P?>3uz'
        'jkMWqr`@#E+}&?=(zF4wme0g|sOQ=%U1SjE2-7))8s5{eerJ{>8&6hs4q{8JS>(ugWq3{<XK)#wk~2Btj8xh<A{m^7HDa|lIY)=$'
        'q@u_m)Z<S{EVR@|WsLgq_6jF9^BQXl9i_0~@K2G{>_9pQ%Ln61Q1zA<8p89+X9`te_`s`JdAci1SeS?i!XqmYE(!_4>OCpp%|uK|'
        'GifAox!~f=*NLDO+cdm%aoa<gbGQ`SVh4wkDTIG@tA*)KFwosULwNi~x})p!DIRZB5oU?5AZ$JaV#h_MksEe$j9gJ^ai8xiZm82{'
        's;vd&AyKd5U0Cf?#$-A8FGw6k?}=APb9~>62t%qoho7+B+x%rSd{os02zrY?L%M}5qioTjqiEElbaCJ@dztW2Ma%1Vcj7af`7HSZ'
        '<NYS)3<LlG'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)