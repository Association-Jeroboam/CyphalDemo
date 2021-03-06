# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/scalar/Real64.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:10.062910 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Real64
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
class Real64_1_0:
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
                 value: None | int | float | _np_.float64 = None) -> None:
        """
        uavcan.primitive.scalar.Real64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float64 value
        """
        self._value: float

        self.value = value if value is not None else 0.0  # type: ignore

    @property
    def value(self) -> float:
        """
        saturated float64 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | float | _np_.float64) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        self._value = float(x)  # Range check not required

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Saturation not required due to compatible native representation of "saturated float64"
        _ser_.add_aligned_f64(self.value)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of uavcan.primitive.scalar.Real64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Real64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_f64()
        self = Real64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of uavcan.primitive.scalar.Real64.1.0'
        assert isinstance(self, Real64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Real64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eui~o0{?YXU5gw=6rI(~ZrrFLB;-ZVc`|D>V|`b(Pr>NEj9HgNM37KacUPthdb*qL>SZPnFb|4>0);LAueWwK*)_5QO;vT>'
        'd+t4V&gtK-{c~?RIs1jrx=lHh^;{3OccykPOkUf$F4|Ss4$j*cK6>i=vG8MWf7*05p2ja;#h39QOm$;caR2FOP72e^yWXvwcPDl}'
        '6s9)){E0QSU@=_RC$=A4+r(-T_I^I!pT@<`V)93P6~hf}yzgB;dOO5t@v5HQ2E{Nvbha)pdfC^d@kaa9;8p2w`-|a&!@4#8zjSWs'
        '+<9HwX6dWAcnFY%8N6P#rH$2{aQFC4dP<u=g1g7*3TRAzk56K_qX%!A()8tJpg#d;WtNTeW0?v+?@i%>{s3b+Jl_MxFMMY*!7`H~'
        'qnI)!2*q3?g&8N35h^K`h*2(NrjSIia>5m3StfX<GAx-C3Z)z(kW>f}#i^14ag}kd1SL`kB^8#KGsMzc$}yvgFahw45=@CuDuW|d'
        '5Ud!KfCo`dCC4ID0zoy5xD=dYq6m_LFwQcBGDKBI2_!Qlp_t-GF$khG1MF0d5-K2y5Rx&41y@LMo>8buD6j>JKwS|*5W|c~AP>z_'
        '=vHEdGMtetQwkG~pm#(BRtyuS09UA(hCk-jG)zxSJ;IEy>9Q?iK;N%ny!B?*+pf2RZG4i!%r)LFL4x1Retkgh-{<tJ*_UVQGe9xn'
        '_9ZFme6yAK%UIp3ZVe!jGGP_Q+cLfmAM59CZA;y?z1OacN8y$p+OaPzT+~)~1_TiH(o(w|{`_Nb)cQERJq5w-d=0%;ZL-jNor_`r'
        '(Wa|R{heL4F?`aEdF=|_+vQlNdKUr*>FjPT2auOUy}Pwt3^%vNo8vi}CnH3k^m$uXW`Lf0m_%~Mi7RY;T^)o;8d+Wg?B{Qcb0J`e'
        '^zWWy`0!ije>gioh2yz}!uz`IVwhb8GHh0P3!I>p$G{P6nZ*BNXM5w@{=$g6x~LqOyE+Uvk4;&+X8FIMYLRY_#u^B3-n|8ctrY%>'
        '2aAV)4>^2+x-C##Tpx3wyK+tPIBd*1ZT6DSVbCdiU)yzOnzN78(U=eUn9u(O8<;UHG6ett'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
