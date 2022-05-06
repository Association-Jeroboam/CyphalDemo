# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/primitive/Unstructured.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.241874 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.Unstructured
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
class Unstructured_1_0:
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
                 value: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.primitive.Unstructured.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint8[<=256] value
        """
        self._value: _NDArray_[_np_.uint8]

        if value is None:
            self.value = _np_.array([], _np_.uint8)
        else:
            value = value.encode() if isinstance(value, str) else value  # Implicit string encoding
            if isinstance(value, (bytes, bytearray)) and len(value) <= 256:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._value = _np_.frombuffer(value, _np_.uint8)  # type: ignore
            elif isinstance(value, _np_.ndarray) and value.dtype == _np_.uint8 and value.ndim == 1 and value.size <= 256:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.uint8).flatten()
                if not value.size <= 256:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 256')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.uint8  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 256

    @property
    def value(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=256] value
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .value.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 256:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._value = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 256:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 256:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 256')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.uint8  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 256

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 256, 'self.value: saturated uint8[<=256]'
        _ser_.add_aligned_u16(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 2064, \
            'Bad serialization of uavcan.primitive.Unstructured.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Unstructured_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u16()
        assert _len0_ >= 0
        if _len0_ > 256:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 256')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f0_) <= 256, 'saturated uint8[<=256]'
        self = Unstructured_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
            'Bad deserialization of uavcan.primitive.Unstructured.1.0'
        assert isinstance(self, Unstructured_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % repr(bytes(self.value))[1:],
        ])
        return f'uavcan.primitive.Unstructured.1.0({_o_0_})'

    _EXTENT_BYTES_ = 258

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{`t=No*VE73S=;<%QlAFY&}%=tQCEHB90pN?jBxUO$I*+CZ0LG$hBGLAeZuLzgNLKsmHffB`y%r+|(+>ZqfRI_juf'
        'b<|Nu9d+#cMQUMWd6$eP(q(4e`u*=ckoq`pT>a0#FQ?Z2qKp1mrCF)wtfmuqcGdg4U8*`ctK6vhjiwhmNp$$TFld#-R^a?;%y*Kf'
        '$@L$TAChdOS#`U{`U@@lN!hOF{J^Vuq4&he{kh&;cc~;%+Ir#yO|MZ;+*D+I-@SjDkVL6}CO;-opJj((;FVgT(@g%7>;!4UD2cS+'
        'c}}&m3FV+wu|wMm1-|Iq4(>r<k0sHW?`@W{<PT1LG<3fa(%y3&ww$U{bLwF?-VSg!j+;a$_`u$1-KqS(9y+5=&>OGMDtVz*T}zix'
        'n!%RsW@yzK6(@1eMyHGGfrMM`0qY=CT%goHl1E8&(rSiwy<!KIt$`+5rRV@h^6j!0jwMJ*(ebX%dMv8bLGPaLpl~lz#x>nbB#D^r'
        'RpG8$rD`*YuC1SMGddqN{P}Yd9r}$IcB=LrKX%U-DOSTzB6Fu8&9PdkQT57PB{;PPS1;uDf9pGe9X5i^D(P0)^|+_*?da5lM!jr@'
        'PW_pt;?%-2aOylPS++m=uvM+v!PquS-FjkITTb$?BukmNS#s}oi&0>&Gmq^0sPoA2ozU9}(qFBb-4?ZFkHIym`#=OsbFj4n*1S5m'
        'N!+a2r6WW1wN<r60Fs1lDkiymRo1RN_i{{XSEg;qNFg;Qz4I)Kd!t838tE~myM70@>BwMQba2C;CH&m?OglP22V*+a(WOPM!#mnh'
        'A03M6NKagrvh3({edsV9i7C^~5!103TGLT(6CK}{i8U-g@lyVDjE={2vSX{V{*drJ_0qm{f=<SC`k5G5%ephK6pK#L>6rT0E6rHm'
        'du4w*L;W$G-4PR8u>Ra@#ijS?Y)t2S>cv`)cj2|;(K$LF)BDfG%T{c2@r`oO1$sXwbECEb^#^YpkuH)M)1^)v^LhA1_RDW2AALZV'
        'V!E=Pb4wpYm9D<E9CVqk#B}Y2ona4?t=aa&x0;)-(zTef>*wtD?D|{JK_5~!rjK6wob18&AMXkdx=tU(G_cv*D;zVswZEV2T3-5?'
        '24c#+QXSZfeQxY3Ci;YOG37VsAlsRQo4cNsZcsj^Td!OZ_GG`?dxDQ{(yf^8Y@e6`j-6khn!9_3g>KWGnC`t+&DfiLKiyNTbeHbM'
        'ROp?qyqK@g_8bR&N`;s{f9=|F1or>po#3X==<}HF?>vWhI7dOu;+O9XAALdhWBTfi>dR3$#@Fxk4D=;^71Q9hndR=cm@+zT->$C_'
        '=QRtYWTaH2bmknCMp{N%#j1w1P8nomWK?8y>PNqfeii*XRt+*?$}m-!I%ScSkyVk^DUZC2yo$U|1r%fyR1|a?#Gs5p6@xkrVMxZ1'
        'iXokfD9R|RDC#tfVHv|JhIJajh>Q^xBRaWoWw<I_oqYH*d=<V<ZM0>yRkU>)$GD7f72`ThU_!=(iV2-!#4=(Pu}+hilrgDdQl}|Q'
        '$(T|xrPDN~WlXD>)@cSaGG<iF=roI28M7*8b(+JRj5!r^I?ZEV#=MGooffblV?o7&PK#KSv8ZBErzI@OSW>a1(=wK2EUQ@7X$31X'
        'R#dF$w2D<3t6Wd6u7s3=l!lanw1l*RG#A-GMnXnGMnlFxzl44T{TliWm=a6{rUuhMRzg-mRzuc6UP4|$UPInMK|(=6K|{g7poBpM'
        'gBk`63`rPLFr;C~Kv6<bK~Y1|z_5g21;ZMK4U9+_Q81!m#DFWoRp4rH4fqm#1-=H~KwCmvL0d!Hz_^5Q1>+jV4NORwP%xok!ayt`'
        'RuF554NOXyR4}Pw(!i92DFss+rVLC=m{u^YVcNiqgc$`h8fFa4N|;qJt6|o_oP;?Aa~kFh%uAS8Ft1_Wz=DJY1q&J$3@l1mRIsXG'
        'QNyBvB?(IkmNYCGSeCG?U|GYmffWfW3RX0%7+96!R>@(){w-zPA~I?BkN-D(IxTqAKA+wLKAq{*VV_U$0-xsp#yi!0t9;sg(RcJN'
        '@M*KR55HJGZEpSs@~h#~;>=e#a<;d>ziK`$YLZ=_gnd5!Gd|rrG5dV_Rrz%1Qzpy0%s!uf13umPR@&#&d%>qSKM}ip+I`C6trVJh'
        'Gt%jG4lQ>%w9dpsFlj-e*T}T`E@?E=XXep@OsmhP(SkmAne;x5{-x6B4u@tk{n9jAys37zNb9@`k5sGDC?`=WX_f5g#Fotqt2EYG'
        '==dRV|LY!WMtxSr@dHP^iLWF-MMtd1UfZcyej^AiuaZ2Bj#<q{D=0gxs5+K!hi(!X;!^cWNpzstXnO6UkUmYak#vJ|yA820qKAC7'
        'n@OaMdSMbBd@$y_cJ;STts#~-TBWL2wgP9gRTY^xH#^ut@2r||@GaXHr?#$}<ZkBjIkAb5gkpE%gyq^zh8Bo*j;0el@ybr}le-w*'
        '|E6xXw)mOlMz!jc#Ug;&cx;x&xFQ3llN-$qn1TH_v*gw7V9fMt_NbFf+yVDSXC2^H&rZS7qFt$Y_0es+1gyOmr5VVYI-zu{_qPrA'
        '>BCN^a{mK1bDqSUBLDy'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
