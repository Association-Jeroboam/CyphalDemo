# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/Unstructured.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:09.606566 UTC
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


def _restore_constant_(encoded_string: str) -> object:
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8eTH>n0{`t=No*VE73S=;<%PDqFka$`x6p|~(`%T-NtC)MRJ?u;>$HI`#b`*5HG^^)42LRNAb@gcs{jM^2RsFI)KNzrb<|Nu'
        '-KwLGI_jun|6imQMwV^al8h$OWoF*`{qH@H`Z#Y~{m;LyCD#6;D}KA&C|9yp!wEdQ;{Dw&R-CL=s#pDb!wa1_I{sZ4G)rMKaQ@Wx'
        'o%nft>&N(qI1_1B&8~9&<)%GWvTIpC@Ty+ujXBvr*Ba|C<v2=OV@}ZU>b2NSM8@~s`{yx9l=x@-V;uEab{Ga;u^Bpz_%HEJkT#6s'
        'Nc)}VRLYxBj#_0qw5?F!i!Scq9t3tfj?RB?b19en!Ksag?l(f(d#>Y_Q*o+JE$qhI0nWy8<EWn>*c+`m<=@vrXVeLL<MmlZFSIIa'
        '>0(N9uqC?@TGe{liQNm)xx#uN;g)^Obr33Epu|7or*U+~YJ_&JYzO77fhL;8=m?MG+a)h-$4E%g>8{RtCaTjx?_TPlaIa9xHQlQu'
        'iJ0yU;jUW6N+XVLuAgr+IzMXo^XE7^_8TwkRP8(d*gapQSam;+%$<TX+SOvc;+1%n;8g3pdLeKBx4skDVLjNal5Uk;kN4EQ7oB}v'
        'ua)f3slCutoLX20PK^&shTETf(yUbMpuNpfx5n&B(~18bXDG!QMfX9s7<uk>{;6FXb)GuD6M8#A`m0s7TcWnyV{lFCJ{G}}JlI+R'
        't6q(_N!+a2B_l)hwOO%60Fs1lf|1<4Dr;9h_c9~3E7LY)q>#!;?>x)m-ssVhMmnQp*YC(S9T^-K9o_Kf68_xxLOVJ_M;RUK=#nDW'
        '@g41`kB%`q(G!<Tx$NXiedsuyV3g|SV07x0)^w7$iB50J#5G*r|62ZZicT{+)3H^#{+RGR``W(LPiGjNdm#p{<+}5`ibZGX9HaDl'
        'r8$=OcI{8+Db47@j+nRw*I#_2xbz-fV05XcUR=xLU4G+ubdfGGdjF+(xfQp$@>V(MGQH2p+^DTU{lQyDq$^}Hy4s0jz6`&}er-?k'
        '(Fb&u(e?G5TlyfXbYstQ&^5Zw=;kXs!#zxH&22y2)7*4}ZZgWOpR?PuTYH{^KBNqzk6!zn+=JVHye~ND7JbBMV6(T^dCbh#{(iD='
        'dFf*sV3gfe9k>_wxxKHL=o88^%5Ba;rZWk5_B|`zrW~WYyRHcL<bL-K1Rvd@yNvE{pO^t2JGVYH4-O0q-J|=A9==h{xHtFx^gyxF'
        '1A53P-#cA7F<+k@I1c)h@{B%z<J$2E-2aPrf}1|0&lx@1c@FRM9C<N|U%oSZ^aVX)^wnF{mq+0-zJ8}?pfBkwMuXdCmUq9&DWlW!'
        '?b;e~Ub8?#MnXkG=bVF*NXkg6Sk;i!DTS1bl!}y2X{2SORit&S8f3zhVX827${-^nqaveI4mlY)6*-;q$jiv9$m=wSK^cQ826Y<3'
        'kc=S}Lpl{ukWo-k&}kUMGKN(Q>okH986zr2baLU!a8<ZE`S4}<Dtw(<Xvt`)Xz4VLaT(((#&w#&gp3Il6FM<48B7J!X%dq%CRI%8'
        'G=(V{Q!1u(n#Qz@X%*8t&0t2xjEWhZW-%*cR>iDNbC{Dcr(#a0dCbe0S23^C0v2Q}s94Zx5sNYwRV?bXge4hEDwcFw#<GlM70WuU'
        'U`57?iWQw!u_|Mg*OOOQLP9}8L&88(LQ+AJ7ui5cLP|kOL&`u}LRvvuL)w5T!Bk*sFb!lRWE5mHWDMja<P_vI<P78`<Q3#K<P8i;'
        '7*sH*VbH*kgdqh(8iouMBoq`BG!zUBOBhx#tYO%|h=dUZBN|2wxDs3it_IhDFTq#fYw!)UB(xN?G_(wiOBh!$u3_B3goFtN6B;HA'
        'FbPZn)4&W&N|;nIsbSK<l!Pe-QyQiWOiP$nFs)(Qz>I_$1v46E49rTHRWPez*1(*EIR$eX<_yeBm{%~bVcx)kgari)8Ws#JN?25|'
        's$fyWqJbp|OA3}WEE!mqu&iKN!?J-D2`dU#G^`j{l~}XraKipArQ8BiN%xQcH+(uNc+?@EJ^((Q>eS(oPwxYt=Kqa%s=KFr+I-b_'
        '^gi%uv$qewSUzoT{s!`^;nU*G*LmbjZ-0N)d|K2bvpxxjeEMg6x_4p@`Sfo2bmvnh!*!`cKK&May7R4c$fpm2Pj7xAcKNjXoQt<o'
        'XwI9FOs;cixyzw-PCNvY79@I&OsnsbMsxbid9)zY>WgW#pwC?<eMqB!sWiI7p*fj;Z5l1!RJ&TFbzX%>s#UI+;wTX}i+0q%W%I%+'
        'wmS<QKg8~T-BXRI&ni29;D|Tz<@l%Qg!Rm8Ic3YQ2chMa<0sK6t5I(TC5J02j^*2-8%Kt?RJ>vw9VyfsUaKIa&*Mxa-R8O7x>y*I'
        'eJ_rVK5qN2UHPq3t&5e7X0hUxtiTy<Rz$wdeU3&P>74}=9&*dh#o4V(CfPgLTvqHK#G%-j=(k+E!2tzgiKF2JV_wOLe{vV2N8i-U'
        '<`zG*RIgN=l6d`Z)}NWhHm}2g>10Q<17=|V%`AE~J7}9;)gE=Su{+@2?koY^?b#$aS+L7xuQs}EgMe!vMoA82O&wFR+53xz`}|3#'
        'KiU5Qak<jCk|O{B'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
