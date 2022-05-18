# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector3.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:36.425191 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector3
# Version:       0.1
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
class Vector3_0_1:
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
                 value: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.service.actuator.common.sp.Vector3.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[3] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(3, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 3')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 3

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[3] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 3')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 3, 'self.value: saturated float16[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 48, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector3.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 3)
        assert len(_f0_) == 3, 'saturated float16[3]'
        self = Vector3_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 48, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector3.0.1'
        assert isinstance(self, Vector3_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector3.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8$gqTB0{?wf-)kH<5I+BQ?6|qqjr-7t+(Uo3A#7dJ1X>b8>u?a(=U(l^4J59rU5#(lXtj%0Ywikx=Ak79K?7F*-;Q?Au`l)Y'
        ';8?9R`ex>v@7q7-|Jhz_)jxN$7>QD-h?QU@SMqnBD2P~^XGLC03*N0g0wptAiYKE2{Hg!)wSVO|-6E4(gYnpMYx~wzsjUo5hAc46'
        'GlIBnU=UTpa1~LSW0^w4DV*EfM3gDZbyOD70i?8X$Gc^A45pO14%kZv<MpYJTk*_a{<U|jj9Y7DQdubdp`X^oyCCltx)PK)uWW@0'
        'ZaK4|T=&V8>&EbrcOP}-5X27XfyM8`)?|-s3>0Lb?HFuIErkgj%43SS(p5RPlPIe!k(Q}CiI3Y<U&>3%vRr`2n{K0jc0F8+w&|=F'
        'jshot`aLR=m6mJ4jkpN(hHx@I(9%{SBt9}kJ8@YO$KCOoFx<kuyLY#~@d2qy+!e}Q@KoB7kLTPxOBBU_e%97GJauT_fA{X{57IVd'
        '?bGYHK{v<p!n@8ikaCnIxss`O>pjSFA}y5mV*w^;<f7(Mlr%^D&V9HC1z34`+$?)Zwc|sIyS7^?#m(sbAi_H4ssjJF-;CRD%Y-_g'
        'XPMMK-U<so42z{Of=Y3^5YL3j*4vUug<-*Ut;*dh30HB&Ei`a+SLD=4i>Tyo{en_iGHU$r%HvPCQPR)_6b4dG-ts5z19lXY#){ln'
        'CWYU1*IAiYCIvcBzzR+ybxYx)WJ2TYlS7C7uzN~9&wNF>F%N#5Eu?oV+oJ-xdPIB%iB}2n%gBh-4dpx6KMi+|wn+uGLn*`9qa>0u'
        'ml9izPYJuELAJ+Ujkcn%qcBo$g9_If@{;N_!479AC%A|Ecn9y*wBxsUzZp_9ojw;r>cM|TNT(0zLr^rwK3*n{<9G{q=-(rl{yXAv'
        '6|Z6&uOE8c;P_-rE*_lV&%5{xpKsy|Jj7p+;jhRs!4w4o9^oLAjK9_8(VSsuscPSAwcQ5IrTOF;hQI|qYHyPf*PqhZ2O7j<ZD9ar'
        '!o~P$+`-TAi+CnD32(ij@}~5CV>{Pj?)p-p2MY$B6OZ(H+r(}I@i+*uLsFf9`go7)0sNmE7TL>M&%M?x-M9$0T<e~QZQ%}e9+-`n'
        '$1<-ehBBOX=(KamX}BEy3nOhkrA`I_00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
