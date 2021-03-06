# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/energy/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:26.737782 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.energy.Scalar
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
                 joule: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.energy.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param joule: saturated float32 joule
        """
        self._joule: float

        self.joule = joule if joule is not None else 0.0  # type: ignore

    @property
    def joule(self) -> float:
        """
        saturated float32 joule
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._joule

    @joule.setter
    def joule(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._joule = x
        else:
            raise ValueError(f'joule: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.joule):
            if self.joule > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.joule < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.joule)
        else:
            _ser_.add_aligned_f32(self.joule)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.energy.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "joule"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            joule=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.energy.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'joule=%s' % self.joule,
        ])
        return f'uavcan.si.unit.energy.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8zOaO10{?YWOHUL*5MG1@1eFko7fs|Oa2fY8i^EmSURH1;#+&JMPd7VldLHS=X2*m?4jM^1(S-6B`bVs0!9@&nnd+{puj;G%'
        '`pd$v-}8;j&p)ebZn%nw5n56uKU1beMA9;^N+YcR|M1vqms+RA`??Zv0lQ~#3Ol|@3Yw$;siWhR7Lk#WE2ND?A@rz@j#H|r2ER<k'
        'LK|5YkTv|$hb#L626KbPH#h^oN~pD3GG~Q>k8oE<e}lj``%)-A>tuy+YALayy}QyYEput*7$ffYRY~o?WL622mMBq-YzBiZgiNWi'
        'BrmyuY|}p;UZ;n&=m33(!G$y$U*R42O=2u9IMw_n(09bi=?JIdcqn|LX=;(a!LjtOY{c-}-MH0BI^B40ubcEbNz&U-+U=LExSe$4'
        'B<{8M_B*{eZb7K!Sl0B-Po+}`xj=ZCf^Xn0^&2-PNmxDI&naZv*}6f7TvS@5)Cvyg{t-Em6TwMUYD*-CBfm~e>2xa4p#-TY_V1U%'
        'Pf3Qo4^a-2VYt1(dCk4R+F2R)f3K3@R}Shbqw2NDOYl!B$CONo79*!Zz1e<{`QlVBm}oF@A!r6Kr>X(JHq}kkj#^RJBiJzB4U$oV'
        'J!w(cu-LIo1)OI)*)C3iDMWpKz4qDoG0@&VgMaW!+BcWyV?167z|WJi0>5<^h^cc{A|>qP5GkUl!s^~uLQ`AnnT!@mnn{#q*7s{e'
        '%DF5?{{>}(;5~8*Y1X&Bh%lzg3HSj!gRP&2;rpqkKrmQ#4C&^w2nt1mPJ*!%REl#B*(*d$Dq37Vu_MO}b1eD;1QOt7?gIb-'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
