# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector8.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.430064 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector8
# Version:       0.1
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
class Vector8_0_1:
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
        reg.udral.service.actuator.common.sp.Vector8.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[8] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(8, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 8:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 8:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 8')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 8

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[8] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 8:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 8:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 8')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 8

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 8, 'self.value: saturated float16[8]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 128, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector8.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector8_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 8)
        assert len(_f0_) == 8, 'saturated float16[8]'
        self = Vector8_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 128, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector8.0.1'
        assert isinstance(self, Vector8_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector8.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
        'ABzY8Q-pP50{?wfU2hyU6y2oxYSO@#KzQJx`@l!2&`<=e0D%ysTB(|Bx+Eo3f?zyjXRej`lE)M6B2`KsK#gRHN-_VJ<C#s9Em>At'
        'jmN(C_}+WYnbU=T9xrv8pS@F#MJ3XJRZ=USsy}#?%7Dd1Ru+{q(%JQgGF2It;>oy_?%aL++&yz!c8RGxm)cRsuJ0RN$EMbDI%JXM'
        'JOjihS|&j)G*1IubE0AyaD;PH=m0lmMIKaTa3EuBeCg~8JCV9lMeebe4<_q#7k0wAzua?Y*BCcOtEe`za))kK6R(1tUF<8Fip$DY'
        'nc#*q<IA=0%}CdpkDYzHuSQbr$UHIhz2BPdah=IjW->Puuo<<K+Rsp(AmU~}Ex4IRS!0nhENw1vVHfqqyfQ2+gmiSrZVoTfeOj=M'
        'vw=VIGx^i)p-5I4o(rzURiGEZ$#{}0Qwx9bk;d3D%L+5@Pu9S&ix2MKzxRdnNOfdy;_i~i%8XsOVi#DHBL2gRwl3k(p?Uq?*;_v-'
        '(++DNuagGt4OW!S_GW=p<18vt6+62zkXeDD`O+SjQhSYD)m%&pJkr<ptvy*vqppveXUC|WzC+xbyLFm!J$^k1SSLKKrTg1$h257`'
        'gw7XOrg9ga`UM~P#j>ZMPB{|7IUm`1Sz)MhRPwx0<!&AMR9dx*EgW)1fkrwQCAS+_l**!U>xXBKex%I`qzhSU8FP5co!K|okyjck'
        '3vHMZZr9#sRZ;6$;vki*<e=0p`$wuG&^d%dM?=4Rj-KZ}#obhRzbzR&Ias@qC{VJxJuZo-4>4IU_Bz6(87zsuaPy@Td;+$ihsLY8'
        'YvNYO<-)H3ZyoFGd<9Co6W0d!g3kg^t}|Yb8;p2`inTY!1<D!i(LQ}n4;ljKEBdCTtL16Pg;06&A2M<JEj|fldkk7J?Jzv09sCD?'
        '8NQ-`*60>>>Gq+cO-@fHW2S>M`gxb0(l1-|D;?5r#OQb86j4lqBpp#g<cp@`ra*8mM+SAfL8ogs!BPA9(~Kk+cr-qTDK~zC1d?2e'
        'N4b%S)KiY8_ro52Kp%y3-c@w>1qz(e`8(T1?lq8KD|&B7uX#)opSmsTw-ArK7<-WI6x6$WJWu5RIb(?(H`*R_=8<s~Y^Cu4M%$qs'
        'bna&xu1qA~3|UtGw1?B)HK#r~_!laDB)wV&000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
