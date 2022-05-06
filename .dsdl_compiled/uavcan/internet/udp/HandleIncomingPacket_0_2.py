# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.2.dsdl
#
# Generated at:  2022-05-06 20:25:54.561484 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{?|rZI2vB5xz?t`!bHPV-p7yiF5=+Mmm-wA|!wWy7;hsI^X$pzJy328uiZfZa1Fko^<!@-tr<5Bv2xaAjrf2$xq2o'
            'fDe4*15b6&?91IASh9C_reCU_s^_UH|MAK{{&jmJ{ApgVX1U9YLF$B6yimX8!$J(w%#@XJ%8RzSu_p>u;%k07t3>;({obeTAKH7('
            ')l_LMY%4dK8&ABgGhbV=y5xma^Abnw)O?b0Jy6;UtA!ubc{O;*bzX>ljjNO%AM@-fUYv+eYT<m_Y^4)noiduvzxF}*{aJgkaq!$<'
            '+E3f&ddj`GYFK;W+K+MBC7#Szwap6;lqm9rc}bdc&r?q}U$(un<hz<+#hv%HQ)4aieYi0ecGcJG=}`H!5PIxodvFVfXWaR;G`VQy'
            'H=Dc1{Xw*Ca3Aju=@ohO=k}y+zMeV{M7YhD5BjVg%A`r0aO8ig^0v8><|b>Kf1gU_*oZu0PV%B)nbDpr&Ab%M0e3dxMJ@1?dp6~c'
            ')lTGWI1BF!lktLSSiq)IXy$~@5ryzBGu8@MnfS!ier)h1sX~NsO24jzQGARG;1GM<E$iaQf_2e=se*AsaoPReu#)>shUf8OCz7f1'
            'k}2=HmE@Z^^Me+6yb=+Y-)LUDB;?leS=+q&0moB3c@(hRrKhVgyOD}QltTNM1M;=*<Zm5p$=Bt#<#zyo^CAKX-<6-WhyU4ZZg-(c'
            '1N0X*-onN=4mK&Iar>2YSh%)%vp01STv+YT|8AR?-cvpr`~*KcQ=8{gQ?(7d><~9Aho(?Si#vy+GyuXQT^?7$a&PQ1XEUil0r`vO'
            'mHS3#+zY*SDS1sRt<Xd+tiO3w7X`Po3oEatA<XUH+It7LzHmdi+kvr%U9X;SJr*aT5?)<q($lo$XM`<wJPJ?cV>)aLhXnwk4`2y>'
            'p><!~Y_1Wl>Vne&2b;8Z<BNl>_*sK_;;iC22*y!86fo%{#O2qA|GX(bUbjPXETg+XwQCih6@~+%H$Qy1xv}xf(MV)OTh_hkQk#@x'
            'p4lT~rywrUdt^=7C30!JVA43xpkza!Tn>`=_l{ZQk&C?SIa?YVn5x;^JMV%d5H)5-{hc7ljPA*;sj5gKXUfPtT9-gW%UY`}#F9Zn'
            'RYhq%U?*ZEEK%&_!F~45PkzWCG3>1${dk9L#t)|S_j6H!YgSB@m=2OXI5xJt><koVnZS)f7dje{VSZVBOpOmRPq{3@(6OAvuM8|F'
            ';)>?Zl4hsFS*#9}D&LiNrI7b(s3@$lf)X=tKX1MUmYs<_t&H^~en-vAsWY|B1YQ&(tvEE2V&-L`hRE7u6s@ykdio5xwfO_cr8HE6'
            'u6lfO5b^o30?U&7vkIcQhbXm>k$MR7q*jcPRJeIj7qH=KEM6!{efh#6C}3^##@jnP>&w{A;H?2Mwe=+JcT&k6Y_+5`kgAEwMEe;M'
            '?5{6wY=ms;r4;a4g^(`i38dM_yy7caWunsWcSbRaCwsJeMA7C^TDv7tLZioQSi3=TTnO$cNxSTzRk;``9Y`7j{67UgrVkqnbO1Qi'
            'Ovo!S?RQr5MZ^oL9)%gJY>*@i@`O_X3^E4=sN}Ghvksm35=tS-KB5I*wFZ<i$TS<P$5RnXg|}cmJaUZZP%bQo_-`kujb=(ki!gDt'
            'LzGovX1Ltuun+fU892Z-E=F2;I)VI)-@78XMDl!<B6NZ_zQ0uDNkp_9u-!Zlh{A-~HsA&^ZC^fNi&s&77nbp2%4e=CgE_15FMg19'
            'OL4hqNn$FY9SaE>j)ln;k*21Iiq4&yIy5jEqEF)J&YefQDr>ySOfg{l@m(Jfr6;D77bux<2_V@%M{<VHLf_Hmc#;eg(sd%%G!;l`'
            'J6nk5(e5ep6fCC7QsfF8B)kaJDOco9LJm-jPfs6(2%c5S3gpwiUlJf}2wH`p_|-gHN^Sy4_d#JG!h|%m_R-xSE`2CFt*4WWCJd5!'
            '(m913QlqGI^gZ+u0U!!=UT4v7(2eqPG*Ve$i4;8F4k|o^%Aq9+tB?j1ni!9BY7TKDhC7N4dh%Xf6)A(KEgdn)Nc=;fVdX>xKA|+L'
            '93alf=DC?6s_=t!1d+T%B^a>9E!?@f>|tH>Z4P3k33Q_YV^%1f>!N4GT7iIxkRY>pnG6y3Cdq}TEYZ>T4(mP{sS|~10pA(9TJoyu'
            'Inz~~c{ki?m$EVSV@OLBR4S^l87(zR%^-PDTQaH)HmTrN4Yu1*d#B`>a^V64qLuKF5Q9OMiV+ELZ@_AP5Ob2~dc@?X-Qg>kt@gVv'
            '!chWx*h&eocl3l&C3Gu-w|_hr6u{~by-@@<p<bR}u!NA=ULqsz3AB)W5_)V96V{eg=b>+64(ptRiwk4aNOsWoK+Q<3I-%*7n>C#7'
            '-T40l2etMA?5?Er864@Bz%Xk#27=5A3LjOox*P%+N)c<QSYs1zNAW=xI$DCXgY~p_#E}lXG_?-wkSfnnUud8$#936sXn(Rw+d!oS'
            'd{J8zX)*DUvNB)B@uD!|a=#e9`eFn!Dr2c_Du8@})L39cqBexDIgN^>asesw*~gh^37p{kx=HJynNmm*dm*|!UA8*<7IPsMAhD3`'
            'q@TbR(!l2>i-nrK4SpyDqiaEH;NX-EgBHRyC;I$=P=0a8$ck`sj=mBeg~UnLnMR>Q8lhOl&Lwnw=TTGIc|pzhzV3Qa7Z6#$yyJMn'
            '^NDgXY`xN=6(DpkiO!&v@5-OW8RX|HgUroi0!EK73@~`RSoa`q-KUXh@$^sgZ_DEi%}UJ{+QM*dd$3t|a|-@qObJ7Yd@oKf4AaZT'
            '(&N7$Y}IR?#~DUmmoLd%@?|pOuDmDYc)7)v>T~&<Bl%S7d(y~Cej=@O(#u*-<W!zf!zzD==2ZS3V^-)De0%ui?dC2z^Z5TjHl-ql'
            'kMpxH!|eM`n0nWvxQxy+5^Qy9Jng>y>hQzo){cboqa*nJ<!$o2AL3j9AfQDrzgqK>whsOa`O{%|{1N~F'
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

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{?YW-AhzK6kp5KH2c8P$Ud~9)}Wgf^%MvyQEYCDR&O%Qy>r?#cz5n)?%ZWJ5b~i=7)bE+m-Wx|*qL30wRB(Z%$~3L'
            'eVlK@zkUx_dOv?J@2Wzjkto1wnd+}HP9YLW*2=R&J0L%~2B~iGQGM*@K!>!jOFLBcBSISkmayU{H=QjLS6VokazPl`;ucG#Y$wu0'
            '+BmQVTvVz&dMk}e;ho`8+B6$7+2+6o6nSO}t{D?;u!YV{7%=+z=zK`EO6}Ya+9f|Bq;posrGtXD$WIO2McnO=-U)dMatn!M1hnrj'
            'i!ZtZO5~Y!LMy8KYof?Xn*aw=5V>?nel&bi9h1M<U>-V+@b4i*8hS>47_)$C#PL@a<j*&?BR{^{%~7Un(8|cq=4G7fL|AB+X_zdO'
            'bW%8`hYLpfd@#skMz{%cLVo_`;^OJdEJn|xpcFaU2w+hb{8kIb1?k#40owD!LS+g03cpdrDNlNIEN`rxNWnB6a=QEXPX5x0cJF)l'
            'O}-u}=+BFcA2oMYlcL*-Glt3US!dX69>*em$iYgN*+Hu$s8dC_<gYZOQjF@qBzzU3^)gMR?fx6(4sDs1KtHKks~i+D+avEcqS{y)'
            'GhC*My%7$w6Aq)Il_};vRF4bj<kIvUR4?NqE@K?W3A}_?@!A&Q)DGc|eVnf24Bo2ZEZ)XDco*;C9M0o?e1H!F>G*gLtGK|Oq2ri$'
            'TK_ZTr`cWo^{@g#D*gnK>8!=dZAjK_&Y1edFKQZ4@7M%QuqStCVt{R`%`t{V7A}AS!gW90IBpcmqE(KqhY&Bw(D&ew>!NV%BWcxO'
            'qdi9c1fTY1;3B>l;Qq#HX2Oz~Q$_R_`x>(0c-gA>y5C|s2r|cloM<((Ax#rDAP1+<a>RCDsAVn~>@{}KQ)i`)t4uGh?XbQ_qT?IZ'
            '4vM4T&2#?;LuvFEnI#(Y-UI*u'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.internet.udp.HandleIncomingPacket.0.2()'


    _FIXED_PORT_ID_ = 500
    _MODEL_: _pydsdl_.ServiceType = _restore_constant(
        'ABzY8QiOG40{^vGTaO$^6`pk*d(*kBV`B$l0fj)31M6WE5pDv3u`yn)ceAWFQIJ5Ln(msZ!rfg>RrSnHAX5AQ#8L|)(%}*Q1`j-h'
        'f09=OLOg)P0}p(ss(UWGvq?b0l6QK#Zs&aGeBU`WZ=QYkH<x?<U;XKFn%Xq$$5t4{Gxa(jWTGD@Ixn?VPBiu7_k<a%L>x{_(Y(_<'
        '_n>*BxmG_J8}XA$SQk5bFMIWqw?w9LEJ>GVo{Lpc2;-;RbEZmMWsYt3Xk73dM{QMnobaNr3MWh<T)#@o{vBSVnb<C1k}5{~Jh_j7'
        'gK&6Lug7CytkMPTfBu#B`JHB`w{zwf%>$SpbLWg2R8H9DM>y;hk7u)*`qA4;Wa-?zC{DTK!O_!}mxg>-W6Zepa$(h|5a~AD7zwlN'
        '>*Mi2xi}NW$jN5s0ya-LP|S4-6hBp8+3z-@W&N8N+od7$=;zHrQ-3VB4v27*E^hQzHIN&1WQ8UFW0f}b**MinQ~&c&D$9oC5wntK'
        '8B28GxGI>Ff?43s#yqP8zH-MV+_K7wlnthSJktr!SOE*zM2do0QKX21A4{|`!j?L`(Ulu%JVd3B5O(S2<uHnmZ~z=)FSXO!I5KZt'
        'Fkqr!+(4XmzSAt{E|LCyIM|A4qMT&P*>)!RCXQUc0Un<Sh|5pbS5FDKF?`z8&%DC%7H{r)EN{@;<H;^Ek&B{BcGm9v*`0OyIeAS!'
        '2l(s95J>p0+_c&K_ga0i4NdH!Ke6xv7CyVPMj;K$&&GqyHubZesq^5%YIpp5Q$O(?<$}TY@U=Cyek9gqQ?t`HvD18@GljIcv@3EA'
        'ARN-=rBWE~v{~eAA{8hgZ`GG?>LTGz6f38a*EG|Jg2;vW8+%ojaWg$J^IYu1-2A$^wsYZaJCL_qFt)MknFC&o#DOS<Q>U49KhF6P'
        'VT%>t_iyDPZMKfhJb=&#u!J6H-uoN%d7@R7aoS*Kjpp{=-dPWy6__WEN?v%u*sBHtCcTEZ@ZG;}$ib==a)@bk7N~Z<<kL)ZK=g%I'
        '@2vHD-yIG`LbPS=K%3g69J9<GYBK?Gk={e2^EQ!l?F5tBItC>h0Oh<Ny?kq*1s>VJ%Z{_THlC>kdvWWlAPGc`>0x&!2r{K}QlrZ<'
        'kjUyhFpuU%(9papRN`aFprNXywC=M5F%*U<c5wS9`^wjzXOI~7!k50hMK<FLQ^oaEl;D~XV<jg2=oTCs8J@QWilao}M6U}i4ahLJ'
        'C_cKv2brgA5@2XqPU4q)mJ@MBeQ80n<H0mk2TGOC%d7Io@_Gdog*8S{Vy4Z*`YEvNNThM8jU(~ftDlaou1q2@kcqhD&`64zlbISI'
        'Yxhyyj`r#8JIJlIFG4P*rV@0{;gf@ikBk&p7Tuhd5Y1bNQUe*O1|SbA-v~*Cljn5-3(ke&g_6{jFKmJW*3_SQacgUJ8Qbc=&?lxg'
        'j->rkEV+fPhLpyJs@uGU1pC!vy`ImePD%lvQ3&Z`o<N#i$Sb~-RXQmBc54))c(S`U_9)ssNNYPKNNDhw4JzA@_A|jPC25--G%FQD'
        'Rd|wy0DqvshxB11ferwh>M?mGCf&+%Hi>va)g#j*mGq-%P9DE2fI;S<0OcI^a@L{~2B8#^>?2z6WotkgjZ8D4dfXSjR5%0H!z0Uh'
        '3gyCdi2r7U+NdW~v<MSRD@0yqdWyqM3j1(wl7Iuez`;l>M>~*z;khk>3nWjMDMC9G+I5GDGzy63eRd;FJ)$sSy2+@sQl=}Pu*IpM'
        'zH`fXHsMp-mcf)&_=_)O-9lVWS`z6}6qfk}_1nVal1NigL`CaPMI9O#4bdlYw8!?NRi)8RCpzo1?J(8_L=|J*$_tcC*a(np9wRwJ'
        'Xrb?Da~w&A_USqnE1C+Vw3*Jua_`0=a}+G5@?4|}93;F5)CpJQPDBn+j1Ld*`UoDC$_V7swp$P&Ebv-|pt$8cTS#sKspx{jK!h=A'
        'Xyt;tUR=6Rwpvd+>4GqbW=Uria!3t>&e5~)BRoJ9=(I|L-=G`i<#4DH&k`wky6IJT0F^^a<YyrbC^R7+$J89+Mhv$U8}#m-x++oz'
        'M@w2_kdgR9pkd}%c|M^us}vwk$>y1vKC1A8bOez+MI{)p#VOp{D(_&O_iYwpRS@X90E|hdu&)iC5o-kkCVYZSXJyhy*y$)0j<Tc('
        'zPDI+$w-|jO!N3o$<>^fWyhJe;>^0?R=bo5sUJd`qo7hzh0SQGQEK|p?aGi*xwlDqw<@sR_}V)m$CUL4Xb>%jhlCgmGE|I6fI9=0'
        '^MjZZ1=j;6UvD>G!fd(UwE>PC(8E?rfLnX_7*#^MBzW8VGeH5Y7SS69U?b|~`3Xx1nau?<;v7#4$;ZCO1~Fl6PIVsoCT6hCNH{+*'
        'M2%zzeGk-(#HtmVcDi1{>CTN0zi?1%@4;?MN|(WbZV?PKn&U!{7(wBqYF6a~07EHaG!<(s!s#eJ$U;j~kan=1<_<a1f#<p^JUgUH'
        'Q`8r__-5iLs9~@_TBfb1(j2~^EsC_5_()lqF5-An7;(6pU%t9x1TrdZsBOxCe1_DRV?&}gfUhZC6-nhhQslD>ccKMwyz{GWT6gq>'
        'LW<Z6(dOx*)xo!r3!wmsxok(>4QwtAd{(lUui2a6he9yg7PJBmRvCZMLbzr`pKajFFU}Ym;df5aSHdHoIMFK8D0E086syp=_>S*5'
        'YO1hKQ1iWAw7sbHh^(I8ay;VcSlJM^PHE8!5W1&Cr{BnL%5R4|$jzmT%*H+eQ;berU@$tLw-c7`(Uocb_LsA##p?~-mFji0g?`^='
        'XRT`QDfo|TiocY|?}gh7SiIX?c>UX*^=ifYaEFl><kRx9yh27?mDh#L7F%ptJd}D*meO96PF8X(C-O*6<?HgN@@Mi5YFOo)Xint='
        'T(f+y;F{g{F4kAjnTOwjOiV=#AII;$40qpe_*?I46c^E1M1n2f8h_9}{c!iyGb^uz^0htq{oY0LySv0$4}eFD2H#&X=x>ux#obQ~'
        't@-EM(<1pq`?OI%|6lxG6*g-+$O-I^3US>#CEZphOpjpdBHu%v^o|GqkN=Am@=x-2yZ>5~zyCi*a_3tg5J;STdLTc3W_2JDrE4EG'
        'O3j=Pv)_*7I$ieL-#QyYVeywG`3H=yn^|!Ea7(1W$Un=!$-f37?fzr!LlAyQRH_F3{{Vo0(;=M|000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
