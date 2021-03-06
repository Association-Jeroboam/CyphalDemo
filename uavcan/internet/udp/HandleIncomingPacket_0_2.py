# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.2.dsdl
#
# Generated at:  2022-05-06 20:35:06.013280 UTC
# Is deprecated: no
# Fixed port ID: 500
# Full name:     uavcan.internet.udp.HandleIncomingPacket
# Version:       0.2
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


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class HandleIncomingPacket_0_2:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
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
                     session_id: None | int | _np_.uint16 = None,
                     payload:    None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.internet.udp.HandleIncomingPacket.Request.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param session_id: saturated uint16 session_id
            :param payload:    saturated uint8[<=508] payload
            """
            self._session_id: int
            self._payload:    _NDArray_[_np_.uint8]

            self.session_id = session_id if session_id is not None else 0  # type: ignore

            if payload is None:
                self.payload = _np_.array([], _np_.uint8)
            else:
                payload = payload.encode() if isinstance(payload, str) else payload  # Implicit string encoding
                if isinstance(payload, (bytes, bytearray)) and len(payload) <= 508:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._payload = _np_.frombuffer(payload, _np_.uint8)  # type: ignore
                elif isinstance(payload, _np_.ndarray) and payload.dtype == _np_.uint8 and payload.ndim == 1 and payload.size <= 508:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._payload = payload
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    payload = _np_.array(payload, _np_.uint8).flatten()
                    if not payload.size <= 508:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'payload: invalid array length: not {payload.size} <= 508')
                    self._payload = payload
                assert isinstance(self._payload, _np_.ndarray)
                assert self._payload.dtype == _np_.uint8  # type: ignore
                assert self._payload.ndim == 1
                assert len(self._payload) <= 508

        @property
        def session_id(self) -> int:
            """
            saturated uint16 session_id
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._session_id

        @session_id.setter
        def session_id(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._session_id = x
            else:
                raise ValueError(f'session_id: value {x} is not in [0, 65535]')

        @property
        def payload(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=508] payload
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .payload.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._payload

        @payload.setter
        def payload(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 508:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._payload = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 508:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._payload = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 508:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'payload: invalid array length: not {x.size} <= 508')
                self._payload = x
            assert isinstance(self._payload, _np_.ndarray)
            assert self._payload.dtype == _np_.uint8  # type: ignore
            assert self._payload.ndim == 1
            assert len(self._payload) <= 508

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.session_id, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.payload) <= 508, 'self.payload: saturated uint8[<=508]'
            _ser_.add_aligned_u16(len(self.payload))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.payload)
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 4096, \
                'Bad serialization of uavcan.internet.udp.HandleIncomingPacket.Request.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> HandleIncomingPacket_0_2.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "session_id"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "payload"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u16()
            assert _len0_ >= 0
            if _len0_ > 508:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 508')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 508, 'saturated uint8[<=508]'
            self = HandleIncomingPacket_0_2.Request(
                session_id=_f0_,
                payload=_f1_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 4096, \
                'Bad deserialization of uavcan.internet.udp.HandleIncomingPacket.Request.0.2'
            assert isinstance(self, HandleIncomingPacket_0_2.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'session_id=%s' % self.session_id,
                'payload=%s' % repr(bytes(self.payload))[1:],
            ])
            return f'uavcan.internet.udp.HandleIncomingPacket.Request.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 500
        _EXTENT_BYTES_ = 600

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8dWLmk0{?|rU5^|`72P$C?X+X;*u()vA{7OqjkF9)L`VP$<an{XTJL(b-h4<QYSnbtOcm~~>Qq(F>;xg<2T&rlAd;K^lb@0o'
            '-g)7T2hOePo{!yGu;ksD?)td*+<VTwcmI6(AOF0)5&ku=SF_yZ#UORUDqg5B_^=RzG&5yoobsY=ZtRLemH3#S%qr17Z{L2_{;Az+'
            'uB1w9VOzP;+<4+`o%z~|)g>>anwL0Yr{<H4>w(f<SS|dZ&a1&guJc0dX<ViB_=smu@#0u~UJK{j=2|)t)+wXu{Hq^zpP#q;8~d03'
            '+CFQW>nZo%s$uPgYd^zf7kDyX)iy6YP@>2e<|S#)Jx@K^e9`vGlJ9DQ6?Z<=PK~w5_u$4@*i~Pzr$gn_Lg=xV?fxwso^j{X(&VC*'
            'KWOeA^#{?m!F{|tpjYJ4U)tlg`CjTg5aBjoKIqGOD3c~}!jb=}%G>60nwzX`{(T~qV<Ym2ImwHHWk!3hH1kq02i)0&7q!4w?%9+('
            'Ry&ci;Vir_OvVeQVF8;;p_vmpM-;-l%vdX2W#SW4`?0}?qzVzjDgC+<M)5H&fJ5wYx2%gJ3)V#grV7Rl#YOjf!%FTm8J@?Bok*t2'
            'OQyW*R+4Yx)DK$V@k&Hoe!qF`f{<IwXKnN9M;uS_<Wa!#9z9)+*^N{bq7>T49FVVdC;xE&ntWZpDSrg`n->vC_^$k{J^0UNbGr*o'
            '8lXS7@fJ3|vA;<njoUA$!@{-ATfM1^;KFKu_IumB^nvox;3xRnnc93OHC5ZNiw<$Ka%c*Lw77F1N&_G~(&cd_EceDPb2gI-6p+7d'
            'Ub$~{#=X#Mmy*}C(h5!F!up$sby09TJGb&m8p7QEz1`Zs^|c$ydmR|N*!Ai$*JE)kD&f^dCOu6{eoEM4$D{C6KBmL2;jjQ8^Z_iP'
            '547&vo6S|CRb6m8V1JX=ZhXCeE&i^-JaJla9R%aB9txQBDdO_`gMZzWpRL;=IhN5~pxV`n&kDl<(OaK9+}zms-Do5-qAlxQbg50s'
            'G0*Igu~QHi={>Th>=L;&UNC8#XHc>sP%a0_hr35C^2kMA_M9z^4NTSS-JSPA5{MczqyA11WJdSo)>Ks_kuzmv9<58Dp=GUA7GlYu'
            'p{k;^9<XCE5|$`-{NO%&@0UMgkQnyP&wsH)HscFZ`X{-lz%?r-N=ygIE*u+MUUmkG(@fyTpbH%h$S}VwKBmSmGEccI!qBmt#IFo2'
            'C*q3c&XQ)Q!&$5jlqx@#ccqY9HB=PVSV4)Iw_i2i1<OuFo>s<s62HUd<<yzlW&$q?kyacUNip-XP(x(x5sKF75j}m5+}ivp<Wd?c'
            'L6<7kHp%^21*zOcY+8s%Jp^S^E5=AA+_$I(;OmuGvQUWnq6HG7Y_-iB@9ylZFJ3!?cLv1I){~&$NhNo%(2~ADpe8C4?UzWazrDDz'
            '5pt*(P=IC?0=b+W5M&>-iLd06iTb|R8O11y?9shLiZPFZ+AWE~89iph+6|JULU2c^+2sVS%Ed_OK+PD||0(M+Y1mkx?&DB1A+N-='
            '-&xHU5gVvx6lSclL6R&e6HWy%$QP8IlEYrkI&|Vo=z}Ethzxwy8W6=Gzig}-PemvY-h%7!$T6Nnudp1Fzn!2Wnkkhk!o<-IQC5YS'
            ';c}b9KHQsS$b7DGF_OvC3FKe=+?Bp1YUiuOpcAz5{iPyLBBJGh-OKZUC`_1b18&gK_C*u6coj8wVHq!`eCE31m$Mo_@rA5gipzOR'
            '5>pB7SV+)tEKIJ5Dm6t^bnevDmx0HSdXhwU<~-U}S>sJ+iUHe;@A`l!Ju#iAK)-}b0Lk_lYBPius*dKylTetDt`o7Ql|V|{*+L=@'
            '@0~DD!D6Z`MXta>!izwiaz*YW<N(F^<m6F^;Ay3-KtApHCE3A-pil^kU(K_n<R*}G9~1^6Oh`FvAKeX-(ucBBcsj{w!XTL^om0pm'
            'HHzv+pF{T$0HQ$Wbr$^w-6$_dBb5b~NWt^%puIzA8ycao3TZ&0iSan2;gB?9xTDyh6Yn)ukurGN(h-A<#18@uD<>-O2?bf@0C7e('
            '&&>=`g&(9Nh~xz-!GJAp;m*}%59^{^a}X;{pc@SsvqIrq7d<1^3It4q1ewi?V~DUfNiIBPiH^Q^Sog_D{U=Nd_|C}Hl2=vFnXb;v'
            'd*DvHl#Qt$Lt3JYQYnSaXrxhK2FZikl2K)_Nd>oRu-%4=J0-`I3l|s=t%Qe!7!0yhf=GaS16K2cn3F`;BPPG<4qw4+waax8juOzr'
            'R!V@~!zYaDpIZ^Uy`#CH09J?SjUuoKb@2S0C4|iO5*cw%poQd<&{>0+u(qV?4t*1ISmz{MTo|K9vV(31YDQw!2~D@$tl@O;#{VBP'
            'sG$#FcO|9I;7GRwhFQZg24q%H_^6uI<q*J7idaL%8k=xCiVw2T(GsK`tf#djj&$IqsdZq7RC$j2LSt+pPNNz|`;%4L1}ZJ!i`t?{'
            'i;0hvmH9G`=Y<iM`^CuB7bB2S8B5Jl0pts$#sV7>wIO`XX+R{E3rLaAK2AbQ-~{K_%~uc2ltPNw3(@82venVIm<zE0iG^$@{oJ*X'
            '20kxYEY$36@IxUOUE^5;2d8WpuMn;|(dP$*@{2o0R)mvtbd&HXBu=u<GzuNk2*oOPE}_pmi<;8T3u?Ldbk~8pfXMpg9mf-%Pn3&c'
            '>y;L*0HJ$9bOx<_U;a8y9=}-`Uv3@|FnWA$Y{A>bx(9LV9t}#1r_bh}mWLXekeX{~3&XkX{$|}xC-{%yB#a{RgE+G=%q$yAk1?^-'
            'Yo5o+MP8RL$y@SeGUBe>5^}uUSWESl{KKJqD)p8$vXY-mE1mSRmJ>Opc2$0X)>QrxqgCh>e0%WC?dC4J@%XnNn^FnGue0+m!@T=m'
            'm~_`;xQxv*4s3N&Jn24teDKMowPT?C^blTubDO;G2R9eo4_ML5Z`Zt}t%Lsp9em!X@Dcz3'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
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
        def __init__(self) -> None:
            """
            uavcan.internet.udp.HandleIncomingPacket.Response.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.internet.udp.HandleIncomingPacket.Response.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> HandleIncomingPacket_0_2.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = HandleIncomingPacket_0_2.Response(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.internet.udp.HandleIncomingPacket.Response.0.2'
            assert isinstance(self, HandleIncomingPacket_0_2.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.internet.udp.HandleIncomingPacket.Response.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 500
        _EXTENT_BYTES_ = 63

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8dWLmk0{?YWTWb?R6i#bxYiqqwTg6+eLQO%oQSeDnY!sB(80zJ%46{4OoS~c9Wp*|sLO~yt3Ii5;{7wEPA3c+#kZPNkoyob)'
            'cR63Ce*K=R41Rtk@2f(kkto1wnd;9nP9YLW*2%L%J0QRC0#e=Kqk7-ZfevZ?EA3I$PYZ1fSi*{5c;{@HxYEM$l(WLf4!3w%%5EY}'
            'q>Te>z(u9XqgT?X6kZ!1rA@mflU)vMLy>2u;F?*{1zYIMgaI=jN9RLoR2q}t=_~npA)T{2E*%uKLw<4WF5>=h^j^qQkXuM3BcLDt'
            'g7~C+phTWoC$yrbzbuNZv<Yw^1(8dK<Y&Ss)iL>VE#{%u3jZE5q=^mkQ<w!*les28SMTR2(-+Xm$lu7zIMs=;&@R(3Pblf6a7;=;'
            'etO6PLp$Pu{269~{GG?O+R1#>qDN8Cha7DOh$stwp#|fDU|pR6?fWUAvV?qvUnb&|C#@Zc8fzy~Fl~pN?*6@#KfkHno5B4ZUq`z6'
            'Ga}<ht)AAT=y&3bVe)&n7&cqRu{3XUu+n9A+#m_+R1wzv#g<fxQT>;Mk3+Osrm3|3f1})?E7KC_CsiAjgCb^A<ikePm@Q+5%T%!='
            '!a?@JVMcT^#oUMLIRU*~nt^YcWn9E%jB_}T=kXF=-XUDvBV77{%T2tB*Q<B~Z{jVyjVri{cknLW3zXy9KHkSF_l2Hg)@kd{gkNSy'
            '4OhYn1gZEFB&O4rDYqe6cR6G61HY$jK)q%Qw80+Vm-#WSsj<ok5?Qza2?*c#<<?Q7P!`oWwiQCW6cgWqKdy+vv5TZt<Bj$i_c}fp'
            '%)kwNG{*c=Ju_i3%!v~Eb3+B$ZoFVsd@^kDG{~{aavW=Qbz7P?Y(oxCpXP_%p-j)XV7%At!9bhmP26O9vA)OZjwHvItQ-`h;I+yB'
            'gP}C~3vCH+@6rSS00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.internet.udp.HandleIncomingPacket.0.2()'


    _FIXED_PORT_ID_ = 500
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8dWLmk0{^vGTaO$^6`nPYz3E)mv9W`&fI^_i0ejd)gquKMycn;>yIIzoC`h1AO?S;!;qI=cs(NN8fN&m&VyOj@(s>Mjg9l#x'
        'Q}T#FNIZbV0}p(ss(UWGvnF}Kl6QK#Zs&aGeBU`W56*t@;BwFZtG`fAQ=4Y}*b1X~rrzSiO!VVK=cTsFiKc$)o-kvTh=XY<n)jO*'
        '-)?@>T&tgnjre6HtcxAJm%aL#Es?1lOVZ_;=VDb9!uToooT(C5nPZzh5f?niQJWPXC%ovZ!U<Cd*RRsDe}@-oCbkQhq>95mp4`X4'
        'emK0T*W<A;R_TKFKmU6B{C+d&4bHsNybbeX?wnD>$_d;29EY9a@oZL8KXF@$ES;Md#VL0@IC|Rh(va_Jj2V|+E37&!M7j+(4ux6v'
        '^{IHMT%3vG(8*?S0h=crDCRl^il48q>~$N_vi>cM?a&Z;^t)!isXrZC2Sm6@7dLvh8p@42vci)8u}YizY@F((ssD8#m1QIHh*`<A'
        'j3v5oToueo!7OlRW1dw4U%6uwZdqkT%7#-vp6P^Vtbhe<B1OThC{jehk0sg|VM`s}=*k^xJVd3B5O(S2<uHmL;s7|rUTvqfab(`Q'
        'V8BGdxS=@he5YB?T_XMaaIh88L^;Wnv+YdsO&qy?13W$(5SO2;ubvWeWB9bGpMRa>E#BPqSl*<!$CF)TA{RxM?5y4SOM`X!WqD1$'
        '2>9zK5lHy1+_c&G&su%44NdH!Ke6xv7QQf8qmYK>XX9aJoBD;$)Om1WwLAX3sh|F#a>3wx_}ZFUe=62xQ?t`HvD190GljIcv?Fp2'
        'ARN-=)lwMlv{~eAA{8hgx9ZEcbdhi;ij`BzYno|9LFB^xjom8CxS5`qc`o*0ZvN0*8(etL4(06@jBTuXexDbIVqcWPsnbllALsmt'
        'u*Hg>__y+aHe1JL9zf^=SV9jp@1u?SJkhGkIBhUkqq)8J2J7Lo0`tUC$qO$SyVX#@q&E>4zVnX_Ib5|ujxdeR0@co!e41$vh`##9'
        'owZ)?N28HQh_<X9Xj7Y%W0u(?Z6+Wt(tBid-X?OconTU1$Dm|Gpq%%k*S7Xp;E@fy>^Pfi<C$8pS2n)|l0ej$9(8AeAX7RgHM%SV'
        'iLA~8^JrcK4b7`UB|er68mdZ4>pt5TBVmYQ`?qhgZ+`nF28m%WfBhSqWHY`nRoqBL39cD2R$|hRw&2*I;dyJII7$Rg^t#Z}fDChs'
        ';-f2kka@}`0fv_4B!0PPIT2UXmliZT9!^7bpj7#ayefYoZ&XlGSYrewX4*Wgp9RZ~L>iacI1<0z`nlNZ$|M2<nTSgcjii`4nW-VN'
        'b`QnvXpi2$kK9`O8st)HDnVyT)zs0gX$h&^LTnm{M>PaxQ11?rN;q#`4ZzoPp=6;Dbwvv#MA>TUFTS$5xw?35_FwK3KO0AaekqpR'
        '!a_s(VneNM-bGsd{>fg?=TIl00L>@_axps~$S!0PU&<vN^nJTEicu8V-J81<V;%&xof3pIc+7^C?MHi=;FeOe%?X;7ijgWjHA7e*'
        'E9)U?*r7n($EJErUWrM!vYbsKHc-vT^r1@nQ8cHF-xa_hUr=^(4tqIk(Fudl2TAr38Thg_Ac{tQnNTzC3tu3d0oUP?WjuvmVLBxL'
        'dW4FoCse8k6H6;ZUS@iV!%YhNaBh+y^Lc@TkxY(uApgR1TlyBLoh}oDb||##4i#w>5Y7ASW}13LVZ!t}qkc-6u4uv*r-J6rE#ujQ'
        'Pi<TLQdZ$FzL0ebaXD#8q)Sm)<`dL!3zJKtN<|SBtveO<W#BQSo+Qy8+mBY2MmwG8tk1T?SQijgjCCt2&@W*lKyv*UwHZPSRY!B<'
        'NGP;V*Rfd9N+6}pbS{y*HxHPjU@?{FB30lZ;YFZMxFUBVa)4rdaB$a0@TgQqAfL9~g6v>{S11I<E$7)nauY~J7Ze5}j7d2w7u@xd'
        '(uJ~Bc-l!9gh4b*I;)UFY82Fso_+V=0ir;sRTBIL-6$_dBb9iTNWs(VUVDeoHZ($h7Se!16XJ19!y#$Ja7(d4$KGkGB4u#2q$LI!'
        'i9ZAyW{#ET6AH3Q0pgTwo|);R3O`6k5Xn<if&p8c!mX|H4%T_MW+7GufvyX{m}Cn3+Ta<nRv=))C&+YG9DRhHj#A+$ON!uoi*=Wb'
        ')PKS>kMERR&3RdNoN4RKtOstjOPP@RA*4CVD3wy!j7Ay-rXSs|3>lSso0NB}0^5zRxD#?rS$}{A(Q<f5h`}I3C5QyLGhjJCh&fSk'
        'Jz(;kcJn37mb+XV;K%_zY^4O)+P%l9{@EqL+uoZA3ShN}-Y5VYQ3uaYSVG8LUmzpS@wAY9>^o}^6V~Qb-Jx${2J4K3^8-WFNOsWe'
        'K+Q<3TA^vD>lK{t-1y(u3~J~-*lkJaGC0sJf?-B;Tmup#D121Ss(c7wC`F8>VvR*O9mNM(XlV-44%XA$5l1@kTvvr>hg4~b`a;*;'
        'OdJI@4E9IMwDnY)!xywgkroplDJ#=O98U@(4tMh_S67TcMx_lkOBs;QkQ#GrNYsY#HKhw8shmfOe0Jd`v;dBGe%1Zzj-F6R5qlxp'
        'JYBRp_!e>@6d*B|?WntV&830QN*41q`#Sic5RA6*tbl`6#$T@xt{Ks18~E~zGe$=Eol|s^@W>}lw8}IJ9nuKJDs(Qs&pVEqDy$RK'
        'a&H%H2WmYctEaadk9ay(HiWHHTC@U$?kUmfH}ZS(2jS*%Yw7y3u}8oZhbOKr7@f}>gr&Q5QJTMfXZEyssi7NEy^glf@7oO4s`hq*'
        '|G1p^tBCw@xU+!8JH3V19}L#374O5%MP884$;<Kz8F5wK5HeeAtYz^~>Rnk%drdl7$+4WsBRQ3C$zRD|Q@bjEi`G;=z}3ok3a;6C'
        'bg{mIZan<<V`3^{_&9#wWw`Ht*WYwkW4MUTA`Wc%ruftL>1R7{oLPAdlyC0B>qi&K>+a%az55<38vJO*pua&r8+Sh|wC100PmAQ!'
        '?bAm6(kJ+hDs0wtfD_ao58%3YN~*0+mL7rBMZJd{=^YRHpFg<`@{#;-=ih7ckN?Lg4!-}GAmZ%PgZP;<tAmILUHiBZYUWIs{Z=H`'
        '>2lxxw%HI0i@zkvKVfv;%mV9&TMGSE{zd*>{w+{w=bvkj#rGkRs2cYF3w~hL&x;iR00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
