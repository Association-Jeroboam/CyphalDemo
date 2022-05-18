# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/array/Integer64.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:55.141000 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.array.Integer64
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
class Integer64_1_0:
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
                 value: None | _NDArray_[_np_.int64] | list[int] = None) -> None:
        """
        uavcan.primitive.array.Integer64.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int64[<=32] value
        """
        self._value: _NDArray_[_np_.int64]

        if value is None:
            self.value = _np_.array([], _np_.int64)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.int64 and value.ndim == 1 and value.size <= 32:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.int64).flatten()
                if not value.size <= 32:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} <= 32')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.int64  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) <= 32

    @property
    def value(self) -> _NDArray_[_np_.int64]:
        """
        saturated int64[<=32] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.int64] | list[int]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.int64 and x.ndim == 1 and x.size <= 32:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.int64).flatten()
            if not x.size <= 32:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} <= 32')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.int64  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) <= 32

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.value) <= 32, 'self.value: saturated int64[<=32]'
        _ser_.add_aligned_u8(len(self.value))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2056, \
            'Bad serialization of uavcan.primitive.array.Integer64.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer64_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 32:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 32')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.int64, _len0_)
        assert len(_f0_) <= 32, 'saturated int64[<=32]'
        self = Integer64_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2056, \
            'Bad deserialization of uavcan.primitive.array.Integer64.1.0'
        assert isinstance(self, Integer64_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.primitive.array.Integer64.1.0({_o_0_})'

    _EXTENT_BYTES_ = 257

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8i?xJe0{`t<TW=dh6!zVlCT)_Y>AlqS>Rxb@lD47T3<VT)m{MBk8(OXHA-iII(e65GkdVRyC`co*Qm6kXkNFG0pW)2Tj%U}7'
        'o94m;5|I_#Gv|EgI^%D4HVUs=XEV_syVzTA`7O6*`qXnQ*ZIk6xU^<AyX{`rcLK`U(Px3zZw7sje!JeI{3XBf3;&r{S<&oRZJe+4'
        't+l4rsr5Xk?F7ymty!LDt=GQn1ay^p_m?;`%r)xyPPfDD3@bm6KfmOVh0JgK7tSV4D+oNN(GRH4zvtt;8VGS#{KBDbOM7#~Y*~S2'
        '2Es*lZj8F{i?dVDEgZ#>uV`mAus;!_>Cldv)TM3O31Yl4?hGR4Z1$P6+M%sD<}})**>D2Wjf`=qqpMBJ56pJAMY(;JoqVETgj($p'
        '&Ji(%>B;=cpK^A>^aHEYvb<IjXtUp76NuEanoh9Jp~8;GQ|1pMHPUs&pZl)kk9E$z2!>s;FF{tAvabr%g4u9=&aSDTwNZ>e82--L'
        ')Td4$Q~3<P#>gyhc6-<y<3RlNcBAV$P0r>BZFe!H0rte#J?dFO*VD->nN8clLfiM){G)ECX$7>iqo_!Rko0H=JE)5C(~tYEYkBJ<'
        'k|lG^a{HA3!K+||e#3qcC*vV%oqB3@R_RmPqk%Kdr60|<^#W6l3ZF)U_U8htj#yFt+D-?HCqAGU$r!9Gs@-=jp$}Ohn+YKozvrWO'
        'Tno7n3h`KRFa~)jgiw;-bK-M3H3vl~g<!;b6C-m_#u(wqKp#i&`{a&tFabwGn38jbuyu5-98AJg2**;mIErJ_uhoI0a4dwG*x%V*'
        'Wnmg-LO4ER2WN16?v3<e7LJE-Ldq6!eoE-hzp*aN!HEz~?&t%~;@qh{VZl6{4B@oYnGy9kvuAxc1*bzeJJu(Z!1;6g!i6(%HiYx3'
        'eBmtOUD!7soP+Zry!BdtQ3_=)9>@k<fVV=Z#QpX5fwABsR6@8UaVoF#T-d!lY)@NzLtF4RTngcevX{ud$jw!apNwWSmQnN=8!p3@'
        '5U%Z72lS?b(kOd9Z8M#}=}2odo(qwFY!9x&wGgT*CIfY_mu`&4qHt9tbCEw1Rpm&bA|_miY6v&qI2P1E`CC$cw@w(UiHbwmgd1=('
        'gxe~fD`>fzuG2dzHq~`TB4f&ij!fCPG_Y|4Zo%ykYI}+eZVH_{N+%y_l?S$UPUllOmGMc-QEc!I)IwNL`xEy6qQ=y9k~tI6%tzjw'
        'iTqJD5_mFK7zrZYfrSw6?l~T)3B7lBUdO{#8(v9qtzr)_rln-f44j?9nFU?9d&!<0u9{v|%1_maalM4Ea2J+BxWBJBrS1c@@9OoP'
        'j8m^M-IqGXyYMb7!9BPi!m?g(Rn%P&Ywo=?w(5M<^J=$H$SQv|Q9W1`xbOg$LwLCF_z(g0-`9DTo+LX|?j_O}SxLF}2E7?Y8Ts*n'
        '-Y2gN>M3G9ftF6gvZ(2Yx_9MDoEYpevysR1aZUBECG1^~Y%QRr`|uuo5W+_XiWwdXjE@iL_oyy^-}-o%pf7q>Cpu6?V<eM>4YH9X'
        'nH<R!$OgXfL!NBpNv23PiX>Aa8zqt{lZ`UeVT;tWWGhSRIZ`i>E&QJ+Tlgv<Z6)<0*(#EHiENcfy-c>sVZT9<FMorFhNr|Z>}UTO'
        'K5K}s|Cjl!@jsu9@;viDpZ!<(tZ~SEwzAu9wgaCn?ZE%WG0tH=TS;d>!DmO&ld<f~E)T|Mvtw+gv!{L+hMAz|vz6$iJdV$%V;SXr'
        '=Le{YUGAUH4o9?GC+y5;MLe1tjq=&tfK%#I$4nw$3SY;iY}`B$pUn=qr;$1%NXtn!o6M(V47U?})<DT>iq9rFvaXWMmxxB6IW$8)'
        'Ts}Lxeut|yeEN`V>~73wlQp{?Rc#@~XR{IW(cL&)vGn=l+JG~Q7#9VfJOn<Q?9AlaPDZNNmuBsYiqXb=R<5^d#Mwvrtj1P7uex0^'
        'WrZAP@R0ee@Iz)<dXel-xrazUWE~}AmwpIl{V?XUa-V!XpUt9#>RP!5^=Vn1!(>G-54u*^yA#=3hW8JV&+hs6XZSoF^I0S8+pq8g'
        'G0J2UgCj<kY-VAT7&&4T$R@sWWV=9Cie$S;R!U^ML{`dVyG)Ec+04TVY?GBN+0K%c99b!lZTz1n+j(LX$!3ulC9+vU)`}!nJg2pb'
        'tSFxYvx3>`HaW}ie#2sOiMt51u`X{pe&+U{_N>n)%@*x>R6K@m@!#1o^9SbzZJE8U7nn|qKW4M0-|c%%iW4q1dsbj`Ru*rr)8K64'
        'N!NE?JQ1TWd6i}Fpl!P=Zc%bQhqEJ()_b<)en#6}af#7yxK7jb=xW~;_Vf*h&sj;{x*%lY7NQv6a2y}pz0?+K3pMcso(JM8Va~KI'
        'AHDL#-G)!SHK$4W@AhBz-*(Mjl#jBPQjf!@pIEJy(^(yP434wQ%s{MYnuF0#p9}0)k7b@~{{T*=-v@6R000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)