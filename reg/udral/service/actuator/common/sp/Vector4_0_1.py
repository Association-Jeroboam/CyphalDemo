# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector4.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:37.646231 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector4
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
class Vector4_0_1:
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
        reg.udral.service.actuator.common.sp.Vector4.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[4] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(4, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 4:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 4:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 4')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 4

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[4] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 4:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 4:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 4')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 4

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 4, 'self.value: saturated float16[4]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector4.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector4_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 4)
        assert len(_f0_) == 4, 'saturated float16[4]'
        self = Vector4_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector4.0.1'
        assert isinstance(self, Vector4_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector4.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8U50gH0{?wfU2haO6y1b;k&v=9ZTip$_MsnXg$61<q*fqkgH}S5O}7aRmD*rD<D0z(k7wlZM7u~x<)IakEEOs4|Lyh6hGc1$'
        'l~&`iug|^r+;is7xqmkoTJ_IeEk>dgDq<xV$(4M`69o}V^Q_2AX~DbIhoEFeOYwMAfIs%%y!NmBhFf4#YcL*LZgtn1Dz%k?$&h)b'
        'c}5V|3=E=57_K5pb0|}YIE8bYn}{-HxsJ*r+JlrfZh5!F4#AW%*8zKRZ@fPCaVwtr+rRd1g>h?*Oezbd-}lp+co*c|d{=@Jr<E-;'
        '!7XPtl<Pj9a@`m{^6rza9D>*aJ+Sy=*qZEdm4Si`v>k&@siiQ1LwQIM7rQFwb`oWUCDJlgC-HHc>PvZPS(Xd%c-5`<Pp*e+(I%bs'
        '!cpMlFTX=YveI%bxDjW8-Vjd42U^-ngv1AiXeTa9;<!6r6Na0=bNlv<TRtFFiMvR-3!X|l^6{LTV~L{puTI)Jg{Kbf`|sXe`bpY`'
        'tX+B?H|Q>~yzs6w4Wt}pNv>q--C7T_oJb3${ak<v8ab=E6eZ0Oe{dh~Kmk^sA2-WhQ0;i1;x2DjN^vuKKZvjnxvIeb<2T~=+cKff'
        '=U67Sj~|2uABM$Z7(t~tU5IBwWb187q{6V^x>n_Om4vIf?B*Ldx+`*Oq(xM6w{}LUEEzR^c;)dITrX+p0ty2uCvW*9_Ype?N@GQC'
        'ER(`-yDO~BE0Y2pC}0Jrk-Ek3P%@!$_Q|2ce%L*xo@cI8Zp?$<W((=v^5&>Ot{xJfLE=?H{4z2kbwl}1^-sgSK-;8(+M$$T>`@ZQ'
        'iA#yC#;1f`(jePouSPeb@1ihLZ-WZg81j<pG{FuhC`Y)1yLc1t)U@OGc()l+Go3ycLh8Z)Mo6dk=tEF6$39*nj^p?NZqdI-F#UJL'
        ';|gBFHeT8HxX$tMm|WaD!YAAK8~(n5f8ahoMTXCiV}dCP1U$e&C>fvE<<XpBXsK%7Yqi}v&87L|8HT_GJ!)^05!ZgDu@5weN7}*w'
        '%!G^ai@1Yd;@9y^a1ws|hRU1L_oth=4s+M%3O!gb=$v?@&)Wue8;D0ifE|+R1k`6cTo2$wZdhP1YCZQ_vvlJu*ix-~BDRHF)Olbw'
        'UK-21rWnd_+M(0VIj7-r^dCpENYzdT000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)