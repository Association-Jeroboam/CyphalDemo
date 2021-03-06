# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/array/Integer16.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:55.103837 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Integer16
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
class Integer16_1_0:
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
                 value: None | _NDArray_[_np_.int16] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Integer16.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int16[<=128] value
        """
        self._value: _NDArray_[_np_.int16]

        if value is None:
            self.value = _np_.array([], _np_.int16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.int16 and value.ndim == 1 and value.size <= 128:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.int16).flatten()
                if not value.size <= 128:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 128')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.int16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 128

    @property
    def value(self) -> _NDArray_[_np_.int16]:
        """
        saturated int16[<=128] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.int16] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.int16 and x.ndim == 1 and x.size <= 128:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.int16).flatten()
            if not x.size <= 128:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 128')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.int16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 128

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 128, 'self.value: saturated int16[<=128]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Integer16.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer16_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 128:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 128')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.int16, _len0_)
        assert len(_f0_) <= 128, 'saturated int16[<=128]'
        self = Integer16_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Integer16.1.0'
        assert isinstance(self, Integer16_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Integer16.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8i?xJe0{`t<OKcn073KVC%OA?}N3oNbacqZ99GXh}VVs{DCxwdJ<Fa-eXwhOcBqy3d`56p{0#zV@vS^_I1M~qN16pdSrIuQ1'
        'sil@`yU|ihEw$_&lKMrKZP}8Hwh{<&-n;jnd)|GIk2<;&>eD}^6YZbyvNv9Clq*@YVf(ICasO%+D|Xf_)vI2;;RbdTo_rkm%~H_x'
        '?LUlrcJw5=@l*6;lnFJnW>wjqZdzj{tCsbAx9SG&n4PtJ-x|;UrWV+vwm)z;3X|rT?Kj+dEpif}@qPFCNkkGQ{vQ1lg*~Pf1io8r'
        '26iL*bF>?)4W}s7e(l<o@+O<(X4wiXGl(gMmv#w{c}3xc?=7C?ncv#A(ZKmtJiC2qCr!IzSM6HR#oL9>#)_k`_pv)#v&-EzZ%6Af'
        'i*8_6+Q}kHG1ZdQ2+V4|Y)8(;@O)t%CJxI!U>jl+mnZSJ=us4&H5-9dD_eefE6`-K7#?FJ&nmgWctjK7nXbwFAudgaI^*~KvDVm?'
        'oO79yPTILbQk=@U7Ne?WvC@db>+6f&Ov>vIemRc96W_Q&r<9L**hLN%v+nWX*bSsHUM<!uZYc`;U{~v0(tyvz?>yVLg1Wz1Jl!lg'
        'E^oARCp`C{UMpFFU3;c$T#VS$w`+WYGVFi)VY5=P{P7*0x;bW5ns)S$C__onC_4AL#kkK=7am!)QTvhY*@3$orN5X}tHmYffN$E9'
        '&UZ0Zim}@DtGYGby!e6LkVu9`yxYx+6~~hl`z8d*-FKz^&YuNYklLNoHs(knRgm5p%ki_Z%|;sOf|A|1V>@hQ@EYm(Mm*2(xaXOE'
        'bc~J*I?=Hu<6I|q^`jm-A?VaLT%P5*)6b2elXOZ@s>`?cg}!u}>q=*K<Y5cX_q|j+_0kzZXFI+s+fT%?=UzIN`sl2n^UvhKR<>Q('
        '6BeDL^Md+2F{yYz-r93KU7&tJ7kA~v9&Eq#O1ShET@>{8wtBIZ@!ol5Ji0`03wrmteA$bAF27a|dWYT>l<wA6(0i|qMwclq=t>7C'
        '{XFh*=J)p{AH7Fc1YKRvxn&RH3SHZ`9P~b26?FZDyTTD^_GaG?_BA(Mqw9h)>+4K%B%iVy`<{b7pp2joUwWM!!Tui|2oJhJ9}2p;'
        'xwlstGqZJnKR&R$^by?@l-*MuIErI#9VjRIn6iR$>o+2Q-UbdlAKjvypilN(3y$QtPY;D34bUfoZtpxRHyJy(eqQbz8W;MMZVS5m'
        'N;TtXj=guNT<H$o6_nq+Uo!2w@g4Koq4S`7loxdWm21Zc9RK+n;Z2{>eL-LBehzPQj(mI;zkFl-=yUo)&{wZjUq)e!uixkz=u7%a'
        '(BQ^h$hS?CMWfyFtXf+*w=GD>NT^8YtS=~ql#G;$lul`+Wu#T4b;=<pBc~##(;x<A45}E^sepovf{KDpBN&k}qGCiR51tH9g{RX5'
        'CS**gn9xZ;$Pg-oPSco{F|A@+r&-L(m{l>W(>&&7%&VB!X%UMu7F8_jw2WmL%PN+2TE(i2RTZnuQ$j*PLPNqpN<vCON<+#(T0&Yu'
        'T0`1EPC`yWPD9SXpoBpMgBk`66eJWB6f_hJj7S(!Frs0^fG5FI;A!v-Oh}keFri_>fRG>*2o1u(w1jB|(;B7?%u1M5FsotKz`TTc'
        '1@ju_4J=AnRIsRF(ZI5VWd+L`mJO^*SXHp9Vbu`LqRm?I_biwnA(?a@|JP`_Wc*kB0c*MBk(O)MId!Dv4n)f(W5)Zc<<c+umN)<{'
        'm)^by|Fc>y-Twd4|Cg4F*L=0TyGL4XUCZ&OHm?1VmivX4+kRG#wA@~`T<3ntuq}0@<z7R}b-s^|wA^86x%OSiyWVu3wueZ{Nb0O4'
        'kW{gzp<hP7PW|ZTkwF<`WMouibjl;IA}=Ga(-4Ma45=8>X&A#YhE)vf<iL^PsBm<&_$5;dEtMuQDPvN_q)t<qk};)XN~amj$e2+v'
        'qthJbWX!3U(`f+<G8R-U=(L0-8A~dbbXviRj1?6tI@Xw!PHR|W&JvOek{Xf*`X%%$=x6c<GW?Q|QIOG)mylPG=LZ8r5{48EX&5pv'
        'EMZu|u!dm+js!=6qroxIlF(An($F$6DPdB<q=rcYQxc{WOlg=hFe70`!Hk9(19KAQ6wGOuGq50GLBWEC1p`YGmJ}>$STeAtU`4_T'
        '|JJa=Lx}}k+@Eu_Q0w&nLe(tSOHr7Jnnf$@+tPzJi{qW{_K%VCPp7vL_Lybc^X<6(SdM-UPnkcsExT-bbw4oOa`Z6lH5>J&U$WUy'
        'u}#kkoG3Knw~AYg!efPc!)+Df*(XsZlx}furyh6DWzUVm;}6C?$Etj5SL<=}x>>BaCDXS@o0T}<W@oz*g?gvk&X8NW&sw*$eP*NQ'
        'o*l^MvT^4%3gQ-WpXpc)X645{?S}1-xg|UL+4-0AZzt;vbXu6Vx3xh}7p!vGt&Q$zf3h_nCK;=3jwspOu8Eze4?A_v{s*x`o)>2z'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
