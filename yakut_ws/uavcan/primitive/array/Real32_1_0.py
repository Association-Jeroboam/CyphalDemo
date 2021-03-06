# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/array/Real32.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:55.272907 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Real32
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
class Real32_1_0:
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
                 value: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.primitive.array.Real32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float32[<=64] value
        """
        self._value: _NDArray_[_np_.float32]

        if value is None:
            self.value = _np_.array([], _np_.float32)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float32 and value.ndim == 1 and value.size <= 64:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float32).flatten()
                if not value.size <= 64:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 64')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float32  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 64

    @property
    def value(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[<=64] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size <= 64:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size <= 64:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 64')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float32  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 64

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 64, 'self.value: saturated float32[<=64]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Real32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Real32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 64:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 64')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, _len0_)
        assert len(_f0_) <= 64, 'saturated float32[<=64]'
        self = Real32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Real32.1.0'
        assert isinstance(self, Real32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Real32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8i?xJe0{`t<TW{M&78WVq94B!S=h7xk&8E31O`=$~Y%7<h>Si0bI6c`Q-7WTlfTpC0Ni1~%Ng37x1>A>SxWE8QAhU0M@S}f*'
        'AN@1DZ~hs3MwDZ#j*~dC9qg|4!r`3redn7qLrO<yLHpOUkxci)M_Qd)R15M>#6sT<{J*)CfaRTPv)*b(e#`_v_I(_-t8qJIzwfk|'
        'cp<L;Bz_b*t~(94PWFp!cdqI-@~zOX`>{XA@@^Qqo%~bg2IFIbTh1H{Bfr@YUWS`L^u{j)D3JMw_(||V$BpCAue4(piDzObNiUrQ'
        '*B|*TsBKC);?&&Obz-THU)TXIMG1cH2bX4P<~!DyjlHksZ2!8BIV@mx)`)w2JIHytT)_t(1x+{ZXBl)Ve(VI@AOdWXSaqY=sW)p('
        'c<1@qCmV1H%ReL=N)x3e^LO!7@Y7BdyN#L~*0vHY5>MToZTNA!CIdeY-D*tfj3~{IdSl|?*T##ZW2Le2;^gFbX=1EYnz&Oc6sAUt'
        'h0=JjRGcVG-Wi)H7Dt7Q)voXXQrB{;e%ujI=BIk$oaZvlX&OlL@E;nHKigonZyPb2Wntffy%DfH+q(pcr1Y*V607D^0#bH$BY~R>'
        'p<Kqlz8C!HZ~Qpjmhb7d$IP=%vn9B_6G_ymSDJxe6?_<3y-C|6lkmG13*ERGZf=O-R6U;#jd!1)dDv`J-Iz6A=_->UJww)@)0iXw'
        'p~vkYaKp|vPs5pWgEkZY6gjYxsNy~7CF5&CoqOswX4zBLVzIxIq`%T`&Qr<>@NIX}`%ZG%#MRAT-EYu=kOOkVjKxiPg4%&A@t{cG'
        'Oaf}}n(bccxl$9*dUN{AImm*RfRWy-a%}e5KnEiMtA`udW&@Mf2uEJxX@>3xU+D(}a3q1Fsm+qHj_v3NgK#u~<9)m|OLIf7#lSH*'
        'p1_Ho-ji?ig&{bRz^QF<$U^hOZ-s}Ga4Lb*sjo)%qY``Ot+6l+rxQ5)N)2Qs+qqqF!5KK4z(*T-CM_TD8V~2-qXf?HsEItte&L;X'
        ';bS<Tz$bnAA}jG-d}ltm0G}lA>1*|p7x|35R}8oapC(}U&evz}%>^U$T*IZ5$9|o18Ta!&i3gv-r35Z-#N4t2GCx=LECzfImlL@9'
        '#yuf~P2S{tZBJvv6}Xx}ZeyMFB*-&%ea~aSHOM9K#apkF5afSjUv$8A_#%Oun|phiICER~_tw6}g&S})f&8xWKq$i8-d9a<3-Sq!'
        'rZG;)=dG~s@!&R$CNQ?^To96Q;|HP-3NV&Har;@hN!+6w=Vju+w7@tN6PSFboDrI^QwORQCSWpw(&qam*UcNfW9}Td4w!;c0(ajz'
        'cf>&WdmltM+=06Z+~4^e7AZzap2aUem_E1%_Y-*VUil>!;`r)=t^vM;2MLsWxlY<tI<one+vt|x>Ffe#6kJd+qvC>!nJg}3F{9yv'
        'hBG>@={RHHnt?MWiC98g!6gN46_-@Bv$&K+Tf-#{GvsRGf{qyj7YxkM*n~2yU|GQx1<NX~s94V8N*2o+u4rhJtA$HC+6FEeXq&iX'
        '!VIk8jDl+l&ZxMi;!GCTvN)sRnucW^S9B~JxME=0#1%7XR~S`Wf25N0PiR@*pZ{yBAxr)a-sft_I;@7ezW_6b)zH3FL)IQwL-w2A'
        'v-?mD+5J24KU)pi>Hh-%SJjYQ^X2aD9#%se)sRJ~++j7ets3e-D~Hw4ZmXg6{gNZwiNk8>J*uJf`{=M5I*4kBa-6iiUucLq6PHN@'
        'S_&>Iu!xq5iz-@KT+E`S;i87C8cyrDs^hwX(*}Aft{S+m;<Slg7FSJDu#7ncmle#ZxU6C>i_2NeX}GMRr{TH=)3A!u3a%0Xp$SU3'
        'EKX}^5i5n#(K2w+K+D8M6W1vSag#|$k3yML;D86~=ure6mvzh;xNJ}fBzr`j&h@kh#WknatO}kH?TX8XxAat<N+)gA{wTaP?_|UW'
        'of>O}Ot!#k;%9!`dG61%n$v2AvE$doV}8<!n(eU4$Ph56<;I@iro04xMeu<q&B&jBB4=NS99M2rY_BO>!D`DF{K&&j%X5R@vU*cC'
        'W80O$uR0-{Z3i;mW~Vk1+(=u;M7gD#s`omzLums!U&xQ<W$RDGvM)O9cy2_JLfN2=SUBfbnfTfJH=q1w-mS(##}4J%A~MT9t?j41'
        '%IL2Bms^F&si~>4!sJc+#>ViO@Fu)c+IqX!*S;Hi;?`<@V|H8Hj;vpCizIZ-0<3m_CF=e1INh84e*iGxj=yLh000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
