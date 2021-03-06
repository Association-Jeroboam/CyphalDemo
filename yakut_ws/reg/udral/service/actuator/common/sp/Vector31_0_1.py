# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector31.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:49.097897 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector31
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
class Vector31_0_1:
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
        reg.udral.service.actuator.common.sp.Vector31.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[31] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(31, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 31:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 31:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 31')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 31

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[31] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 31:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 31:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 31')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 31

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 31, 'self.value: saturated float16[31]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 496 <= (_ser_.current_bit_length - _base_offset_) <= 496, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector31.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector31_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 31)
        assert len(_f0_) == 31, 'saturated float16[31]'
        self = Vector31_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 496 <= (_des_.consumed_bit_length - _base_offset_) <= 496, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector31.0.1'
        assert isinstance(self, Vector31_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector31.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8NwtJx0{?wf-)|d55I(2*)uaK3KzQIGexM~FakMI}1fr^FDofGT!A(j)g0Sq}PCQHZerRtmvXLs$hoVMWiAq`iPyPgE@9ZXS'
        '<NCq3w=?t2%s2DhU-SR&E(Z0_ZWSX@3Kg;vwB$<u$zuf}OY*eHOKHH_wTGZ&N=NZzRDe5kpFelc+_qh0GRr_a4D8y0(N$t94bv_Q'
        'EaNFbe5qj&Rzh<XQkoN)K*-6Rn_P#KDb2I6EW$%b=;HP*XP4Ot=u+mH2VXiIpU+$rM6JKwb7xl>H%802GEllBH>-=+PR=fLB`9%T'
        '+6oigaAthH_LCXmTJw>!A9m#s#3RTC2EX@L(@m~1P>@1q#$YpQDYPe1o{-1YuFAQYMp<RCG)&b=T-2ue5?&gX<^mjU+0FhW+=qob'
        'Wb1j8=j4Ukry^NtcqX_O7lB?9PRa+FG?nm)k2Ud5T$aRfcYG!cyKwi;ots}fk5t9>D&;PCBF)G}TXvqsiu`X(+B%1)4$YhI&R%;U'
        'O+(fJy^b5SS6E&++nEJYj?y?+GI4gJ2Wd{E`O<zUK>H=RxO53hnj?N|KiG!?jJ(`$jy<K?@jm&zzgH>6_2^9}!aCuq0{4&Gj@qxv'
        'm^z<lsmxsOzm`AoVSQTiL#Py|kf`N-gI6Wd3d4eD^<M5(u@A--yU+kqu*j*EfXL)_<HD}8c+^PZnZw7pS<=`A6dDpv@^Yv4J$CGO'
        'jTN~zObWMW*IAiYIsq~$U<Ie4+9m%`GNys{Nu<NRzdfU_TVGLb%)R913hC_1&Zt1H9ulK|$*Y(cW~4>xhVq>&fW~`;u4xZyky3`S'
        'OleIfLM6T$sS<Wcqg<cJHM|+#3jI`_@r$^@ke5`b_KKLmoZ>zn;BCBHGmqckcg>ud0rj~MG8?=#MY7(bZ$Z(RU9?OjM>G<A<o|jE'
        ')PK!AuHrRp<NA@qO^#2-{Nmv${<Mcb<1gFzD<0u*$nbaM7-ND00grLui^f0d0%_DRG*q|i1#P=YqiH^TnjvsOk6PfQ#*H6o@`DV-'
        'Zf0NrdP>UpY1F~%_*vBQa>6fOQh75v|7a)A{OGewx83W|FFP?w-?(k;HW0gh2RpQ{Q&1o8^K1a`lEfl=+U#^NM-dmnmh0umC<=(#'
        'pzWEBmdBf3Qw*iIcF5Yf#Oi~?{{bpI%X(A>000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
