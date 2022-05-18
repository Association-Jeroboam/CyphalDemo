# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/node/434.GetTransportStatistics.0.1.dsdl
#
# Generated at:  2022-05-18 08:59:57.147311 UTC
# Is deprecated: no
# Fixed port ID: 434
# Full name:     uavcan.node.GetTransportStatistics
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class GetTransportStatistics_0_1:
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
        def __init__(self) -> None:
            """
            uavcan.node.GetTransportStatistics.Request.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.node.GetTransportStatistics.Request.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetTransportStatistics_0_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = GetTransportStatistics_0_1.Request(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.node.GetTransportStatistics.Request.0.1'
            assert isinstance(self, GetTransportStatistics_0_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.node.GetTransportStatistics.Request.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 434
        _EXTENT_BYTES_ = 0

        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8jkSbg0{?ZAU27FF5Qa}}ZEO8Py!66=AhqCDvA;ltUK~A^p5mQ^?C$hzAe+Qway%;(?2T9mD0KY4PWpjT>E7&2CYj0m<o&kt'
            'dv|$s_T|TZXk%+C86jw8^jB3IsAS`M@1jPae0Pc=HJAb%3?Ar|o*mN>ZRVTOs-EjxNzEH&E9+XQb^#B9veCPMQ&gxU>LynE@Hs(5'
            '%Ik6tA!=u-8|Af+7x5{LN8_dMbWHiSRER;>2_e!a$`Aj^Wj&nFJSzKI@Btcy(9%i1ClB=kT3O~w-O?mKkkO^k02d5Mudt)MR(?j;'
            'lyB{^y2V~uJ!LIR+mu&2SLEFAn)1e*!FS5Mh2Bwq<Wp^QBLmEmDf48jP)TGOk@D)fd_G?QP=2!WYUer(FRGVSp-o8pMOvpK-z<Q|'
            'f`6_XpdWcfwyvRkvJcGMMxjIm6z)*Wz(P<)829D5fjJm~mor4X9K!X+C5ue9+L&@v4g`-7V0k^L8MK073hPh=eia>f0iB4d_XY%Z'
            'Ac{Jn(DkL887h`0Yr|5XUV5e0C=J*dc6@KVnp3{>TI0L3e9GyCWAd_ep0c>ENgVpxF=qzzp1HFVk-hQ3vu1SRukTi6(`nOEx0Ubj'
            'skYU2_TQ#%yHqF17!`)ARqilXCIS7V&GG10tl5?Ryb+DpQ_XUFZP}6~P>T|*$=<d6_~rD5goS7B#kiAH$2!&3AJ7REVNwGC00'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

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
        MAX_NETWORK_INTERFACES: int = 3

        def __init__(self,
                     transfer_statistics:          None | uavcan.node.IOStatistics_0_1 = None,
                     network_interface_statistics: None | _NDArray_[_np_.object_] | list[uavcan.node.IOStatistics_0_1] = None) -> None:
            """
            uavcan.node.GetTransportStatistics.Response.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param transfer_statistics:          uavcan.node.IOStatistics.0.1 transfer_statistics
            :param network_interface_statistics: uavcan.node.IOStatistics.0.1[<=3] network_interface_statistics
            """
            self._transfer_statistics:          uavcan.node.IOStatistics_0_1
            self._network_interface_statistics: _NDArray_[_np_.object_]

            if transfer_statistics is None:
                self.transfer_statistics = uavcan.node.IOStatistics_0_1()
            elif isinstance(transfer_statistics, uavcan.node.IOStatistics_0_1):
                self.transfer_statistics = transfer_statistics
            else:
                raise ValueError(f'transfer_statistics: expected uavcan.node.IOStatistics_0_1 '
                                 f'got {type(transfer_statistics).__name__}')

            if network_interface_statistics is None:
                self.network_interface_statistics = _np_.array([], _np_.object_)
            else:
                if isinstance(network_interface_statistics, _np_.ndarray) and network_interface_statistics.dtype == _np_.object_ and network_interface_statistics.ndim == 1 and network_interface_statistics.size <= 3:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._network_interface_statistics = network_interface_statistics
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    network_interface_statistics = _np_.array(network_interface_statistics, _np_.object_).flatten()
                    if not network_interface_statistics.size <= 3:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'network_interface_statistics: invalid array length: not {network_interface_statistics.size} <= 3')
                    self._network_interface_statistics = network_interface_statistics
                assert isinstance(self._network_interface_statistics, _np_.ndarray)
                assert self._network_interface_statistics.dtype == _np_.object_  # type: ignore
                assert self._network_interface_statistics.ndim == 1
                assert len(self._network_interface_statistics) <= 3

        @property
        def transfer_statistics(self) -> uavcan.node.IOStatistics_0_1:
            """
            uavcan.node.IOStatistics.0.1 transfer_statistics
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._transfer_statistics

        @transfer_statistics.setter
        def transfer_statistics(self, x: uavcan.node.IOStatistics_0_1) -> None:
            if isinstance(x, uavcan.node.IOStatistics_0_1):
                self._transfer_statistics = x
            else:
                raise ValueError(f'transfer_statistics: expected uavcan.node.IOStatistics_0_1 got {type(x).__name__}')

        @property
        def network_interface_statistics(self) -> _NDArray_[_np_.object_]:
            """
            uavcan.node.IOStatistics.0.1[<=3] network_interface_statistics
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._network_interface_statistics

        @network_interface_statistics.setter
        def network_interface_statistics(self, x: _NDArray_[_np_.object_] | list[uavcan.node.IOStatistics_0_1]) -> None:
            if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size <= 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._network_interface_statistics = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.object_).flatten()
                if not x.size <= 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'network_interface_statistics: invalid array length: not {x.size} <= 3')
                self._network_interface_statistics = x
            assert isinstance(self._network_interface_statistics, _np_.ndarray)
            assert self._network_interface_statistics.dtype == _np_.object_  # type: ignore
            assert self._network_interface_statistics.ndim == 1
            assert len(self._network_interface_statistics) <= 3

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.transfer_statistics._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.network_interface_statistics) <= 3, 'self.network_interface_statistics: uavcan.node.IOStatistics.0.1[<=3]'
            _ser_.add_aligned_u8(len(self.network_interface_statistics))
            for _elem0_ in self.network_interface_statistics:
                _ser_.pad_to_alignment(8)
                _elem0_._serialize_(_ser_)
                assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            _ser_.pad_to_alignment(8)
            assert 128 <= (_ser_.current_bit_length - _base_offset_) <= 488, \
                'Bad serialization of uavcan.node.GetTransportStatistics.Response.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetTransportStatistics_0_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "transfer_statistics"
            _des_.pad_to_alignment(8)
            _f0_ = uavcan.node.IOStatistics_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f1_ holds the value of "network_interface_statistics"
            _des_.pad_to_alignment(8)
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 3:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 3')
            _f1_ = _np_.empty(_len0_, _np_.object_)  # type: ignore
            for _i0_ in range(_len0_):
                _des_.pad_to_alignment(8)
                _e0_ = uavcan.node.IOStatistics_0_1._deserialize_(_des_)
                assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
                _f1_[_i0_] = _e0_
            assert len(_f1_) <= 3, 'uavcan.node.IOStatistics.0.1[<=3]'
            _des_.pad_to_alignment(8)
            self = GetTransportStatistics_0_1.Response(
                transfer_statistics=_f0_,
                network_interface_statistics=_f1_)
            _des_.pad_to_alignment(8)
            assert 128 <= (_des_.consumed_bit_length - _base_offset_) <= 488, \
                'Bad deserialization of uavcan.node.GetTransportStatistics.Response.0.1'
            assert isinstance(self, GetTransportStatistics_0_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'transfer_statistics=%s' % self.transfer_statistics,
                'network_interface_statistics=%s' % _np_.array2string(self.network_interface_statistics, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            ])
            return f'uavcan.node.GetTransportStatistics.Response.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 434
        _EXTENT_BYTES_ = 192

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jkSbg0{`ur&2t>Z6~ITk(t5P|u)ZZr!Wv6Pma()J{s3DhfMaazbS$Q12OKJ7YIe6*Jz{reYd)+I2?P#F*;P}OtzuF|<uBkb'
            'NO8=OKY<H(jyZD7d(*E++QlM-<Y-sPuY0=t_3PLDd(+dspZ5Q4X+_KaB}?stdQfjxtbqHD-E=;(t4&_9YF?}D1y0D*WaKU0bXt(C'
            'KRjsj^z-!mXX(f3T2itc*X4dHv}EK#=ts3M@_Bca0n4>ppyEPgKd#ws#r5jE@-`12`nDUiJwJR9+MyGKPA#bHaCqVdP+PYib3brA'
            '7ge8lm(ri7Ok;h2Nk2=IA<GU!->F6+57G~ypJN7**GiLtI}UHw4=pQObvv}J5X}`Q<U>(T=8hVA@0~;QQZXz>l>uTLIu+B@YVNr1'
            '+djI@c?{i8{>BZQU6<GIxgp=>ez%*3tf~`QP44c7B4ub?%??7V1xBReOfq9CMcAxz3(D?e5qPBU&*@H@Oj$u_yLH>IA64`;s=|nd'
            '+^A)7Xb$t2CjD03tEI{ML%|IwsB+)%8b%P+YCH%UQL}kqP+fz&A@s?EN(y@Nv5FN+t+F+7PFxV{vYTP-#^*H-R@PHdNj83@3svvG'
            '>_ZO4_dQ>B@%OvlzR|K>uo)i)hOi%V!>iRIA8J&}XaSGyT4>aH!*QV}&qZ67v+BzRxXcisA{6|<uzhaSyvW6&W7=u8o4f@E+SqI('
            ')4=QN<;ZQqIE<jpYfi(d**G35G(6Dc?>hm<@$h8w$TGF62a*LG*M?XUSHz~+60bxs`E}j~kJvatPm@ur;l#XdAsv=ePq&kCEAS$}'
            '#-X6et+owQo18$=bgF4GXac6OiBCU=rPOy3CRun0U7_uyN%_`6TiDIFc*{$Zg?3bJIyIQ5-KdHE9YPSKNlC7KXpgHuO{R~o|H@|N'
            '<q9tHG{hA*X$d<3TYPX3uKLGLji*mV<<VN7rrk8uax?-SqQ`eR1PZ5SIBq)%FM3f30xL=7c9T30Qy2<6l+`oO2EvP)b;I>Q4FrWo'
            ')7!6<?==kDxU#tcYh5)ooB)*9{A|W>VL{~sqvbT4FdH?`t*;wUc^~q*9;k18a`~!pz->Q}O5MZ4Y!wCTxHgQ(b~EC#@xE`jvr0zj'
            '86R=qtCX{4mQ@Lknp@?t%yIbp0;Vm~gKkAb{m6A4cejE#R-54YRTV!D=>?~Tz4<g5{-qQCI?F$REX9wcXnE~4F^*Fb9JHz)Ogqfl'
            'eOLw%op43J(*_rZo_{o+*T7UD>%HWpY1ivu;twi`--+MmsrQoUTb_#x*L|kSWKe2^MS@ZKNXy?pLt8ydiQVIBf>qlPJ#7Er2mO?+'
            '%>U_M(>1o%399f0Y0CjXgp8`-=9c4PV1<MoW8wq`S6~2jGacJ$9o9#(K(dIkufzH&KR~jCvcJPlpd9G1LCTk@d<f-<4jZQDBcx{('
            '<#30cL|N{zF_e0TjiW4e*aX#|L|N#tDbhEMa<ao_P)>B%EXwf?n?pI)VW&`@?67&1qaC(@a-_o+slOLc4t3aR>URm{V22sh{~5A('
            'ne14hah)Z5UPM{!uvN0_9F1p<>^m?0&R!yUf#f>L4U!d-7fEiCe3|4Wl9x$dA$gVLD<oefd5z?Cl3OHikbI5gFG#*l@(q%2lDtdu'
            '5lKNZCi#Tq7bL$V`4!2pNq$4}JCff^d0+3N#GFd3sl+vvxT_M6R6?jktP)RD;tQ4dQYF4piLX`S8<qG@CBCOb1p5mfw_yi{+bVii'
            '75kFEj}$~asEUu7DL#R}KmA8c3ddklAWVvciQa=rkucE-lLBE<CQJqh6OAw#CQNj~q`wD~al&MjFc~6Dbi!nSFewlw^MuJ9VKPIQ'
            'Oc5p%gvl6TGD?^X6DDQCL?=v2gh@YPQs}|t9AUCbn7l}soFz<F2$N;P<P2eA5GG56$!Wsm1;S*JFj*i><_VKigvlIXGE11u5GK=v'
            '$rNESNtjF!CgX(37-6ClCMIEG5+){LViG1MVPX;{CShU{CMIEG5+<g?#8jA=3KLUdVk%5bg^8&!F%>4J!o*aVm<kh9VPYywOofT5'
            'FfkP-W+xKgQlcvUh_8|7G(4x_ISt3YDPmwF{t0Yo$FQLh8-2t^v4@Q^v7r$gMPfrIHng4%RUff2Ol*{T*f>dSl!=W2VnZV~rihI('
            'Vq=)t(20$HVnZV~7Kn{GVq==vm>@Pz5*x$B#vrj#A~uRWY^)L+XNiqvV#6RdP7@o8#Kt_aF-L675F1m(#ssl3Mr@1{8^gp#nb^>Y'
            'jS{iZPiz#34UO2iL2PUh8`p`AYsAJTv0)G!W5k9=Y{bMyOl-u&MoetP#70bP#KcCd*oYMyv0@`uY{ZI<Sg{c+He$s_tk{SZ8?j;|'
            'R&2zIjaab}D>h=qMy%L~<(oo}p40H0hUYW@4M8<Kx0?*{xVOQ5D>!nVT1oyP&!!AjY`}MY!}D9VTjPhPL%~)#>^e&9X%%#zEe6~T'
            '*PngdxSpN(HEgG;P6t~&6ka_*t=XBNJWg`l-5)su>^`eZ7LGZ3_I>*xO=jP<;VC?kr#3h7Y4_Rhh{a_mbQXOIPfhH$U30>NlogW+'
            'b(Yh>18k~vctEPl1JWm8lPMm^7xTNvoT?msZ|m^h?mEhu-Lc(WzQfx*bdEb8`cNL96rsWUS(MYnC$NzI4`EJYeXNjgi#1k6;JN~y'
            '#s*m#aqJ3v_%y3KDswt$DffgxEf0cuFB391j4dZ+dP3&9f}+%}LL+J~V*r_zxiTBTvaT?RPp9&;7>$jw5{8}ynVW+?1}Si&wy}Jp'
            'jk$gdK3zdnW0PzFH>rkdKbD`@pl#C__Li0X1+;BNS#dfKv01+qX0g=-2ItkTQJ?GbWmn+Un88-^@Qb?6Vy_ou?i5?bP`0kdV4w{f'
            'GM8CUQT8mNj*Buk51w110IlUAT4UpEJrC3xTa(_ttSl{J@V}z`YG6pcDswM^b``*-m(Nldm-BI&f_d)q>s_PY>Y9NYGFO0HsVB&5'
            '>^i%_UZqg4u`PCqy+Q#W%PzAG3j1jNHL#F^p~n8jVju-#qTDR&08YE_XM9N(d%h&I1&wbd`8^4_0Rl%SaCC5XDL;->UzR$w9Kv>^'
            's$Cg#C#jCyJLKP)dIsN+`r3rrqXZ7>8Aa_=)N)!r9fvwY1P(fV0-ZTaS|K;m^ChZh6Ff`c=rD=>`B5fno5FD|DsBBaIG7v8WpbLd'
            'EvY^ha6E?6rsdzPsBHkh6qjXg9v3HplUpIbV&!svQMH=K@6lD&Y6|T;r^<#fw?;OcmrvK^Y`mm&74q*~ot=S2J4fK)7_yzqhRm&^'
            '1(iczoh5K|fNcc7nKwxzfujS4MO@^UWNs7MED|_q=@45daL^Ok9_FgdT>_YA2%K!RSo2loi456m%0eRtCm;P**9_c{xiaKN2^^ik'
            '(G^awt5I#C6>q4r8|*59gJnm+(b@OF3H$VLGqLFMaNqMkv>d$mY1lR1y{mY1s!!9lWgR20b7VUKn*-jq;oZh@zj0WlQodc;t*jfc'
            '12Jr)?nTvX>rju}y6uK?yMdQ-cqilpM)ra?_Ott*ng@FX$2Fi+gWl%BdbVrvTyEH5cKhSFbslGTM%2n~x1op7%Ss!LAB2a-$cv}!'
            'K2g<>_gF{m?b*Tn)V<4OqTljdyrK&a?{(&S_7vxthF8mSXHiaO?%#Z5ZQp+Q-a9+Yy0`uC_RgJ~w{AbcUECJ!$AYMh?g@;jotf-A'
            'I6QgH;vaEjK7gPCdy(V?wSVGq+lMV1Sle}TuJ2?cu$#(OXfxRG?HWD}p!^P{p*-okoTAmZRJeEzMzi-pLDR&{o>tVfJqyx%WlZ(M'
            'f020osd!^syeV$2iMPaUaYwu@?uvWjSINqi%U6#3nL^h+sMvl29?;Tf@4bG`E!X=${DKtUZb#L<78ozz9iPIx<Ga4RByZ63T=F7@'
            '#IP8XKUkQN9>Br>58m0EgW`Pfdkc_DPQdJiu-MZ3S}B>a>hyyV-xA!egXrD08b5Q_YIN;d_hK+vX7>I7N%l`@+Pld`*KC7lv=Vwo'
            'y=;TbMVUXb(0E26Hm&>{Z(S4QDkA^@'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.node.GetTransportStatistics.0.1()'


    _FIXED_PORT_ID_ = 434
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8jkSbg0{`ur&2QW`7Qi+Bl*f+aZ#%Y=C{E(Ii9PvlQ)jnrnxvb68%OJ;-2jV1(2QtP?u<0mhb<Rq(H>ePfPkGvwLr0dLC<?w'
        '^ti|V3H=j#++&aXp7<!wOye{ydQ5=$ks|r{9?9PmMb77a|72&i{9k&qx$lHdy<&wtaP7MLiCwMpidFL)O+R!ao~6T&c(Ci%_~ZR1'
        '&%VxH`y%@^TS<>t0slDWVPr-4TxjW$M^O;hqB!WP*>8Dv1N5Aa?cJK~RXpF}l|S+5abSC4(+{FYksY~V<krH<rqr3Gy0y!L(Dgmk'
        'Joo{nzs{J(N?&DPfK`?qMS)w5BOYcSX6a;G-m31)K0n2J4sQm$W=Gt~o~5JKmYZ<L!hS8+$u`n)EA-=_#-X6jt)?A`EFDBqcdJ=C'
        'WWp#UCO-Wdd?{Vb(mvs%J3UP|OUt+So5HT&;SE1a7n*Uk?$%&nw&ObXXE}Cc=i?J*>40<}+T#FZ>FH}%uN^iFmnxSlI4fC{ZK7+!'
        '4#Bd3dl60(PDb`L?Xw)emZi@&IgGg%8nzMg$ndv}ZSL{Ft{ZiKZ>`REdEJOqA4aG;f%2Lkdl8ImrHnHS2?M$?xChSzdz(8345s1v'
        'k%2Sq2Jj&AjnHm1>)eP0H_$u7j{F8{tM6C9HLF?&SC`eAs=AR?=iYWC!0xC!pQR)3y3wEW{3FQHib;DdznP`RVM@aNM%9OLhJkqi'
        ';|?n}g0=Cm2|h=DaIo$MteSA^P9`p<M@`#tTyOhlmBckH-H7XTJJ|0o1r57)J?7cpvlXVb!YZuFrc{(MJ+6Yg4cCJui3vNw#Guvi'
        '9hiJ<UAB1AgmK4(yAfBzDzq4d#Q_uHh5P`UJG|~TfHbEQn*q!9U>-9uNT!z43ok{G)SrnFF($@81Wkt^UhtBo{qMOPMylw$e6Vuc'
        '`=4v?|Ng^+Ua_-Lg=XHV_zSgqd|3C*0KIm1q5H}AVU)H#?%ap<xXpvkff#OE0U1N%YBq$O22vzGOlM4`2%A-IL)il?f>=@d67iX`'
        'V9|Sy9XRcZp2b!0XxNJz7Ki2-9mI0F`WV(VJgf2mNebgyjfdeDtdD(zssSJobjQO=1}X|Sg+-|<TM;#}Erjf01bcw^!@<D3i?tVY'
        'q3Zq0KBN~x;0Lmcf8F!<jE3!j&G;}hguTlRzgCL_s8K1S1w659k>T(y*K?5{v}Gx;zGT2?83I%Q<okI{kdea4(=PJg00VRE)^ZKp'
        'SuMw29sDrDCa<|$G9nmMX!xKh*mFaU{%|pgKDgp<!WSQjSbQ9d>1SeQL(Gc#6|o=|#c^>$oD_yQl}@)Wv(C6E&OQ^%PgY8rcFRyR'
        '+z|rZn&EoQIJ)S^5s2r;KJd|wRKx^}L*d7DCy#nQgv2d~p_TIeEeNjHF0H}xQ4I|@1m(3L9|@c=sJw49+<G0ntofd^YCz>Z$QOE`'
        'zVX@B>&8B}G3KID@1QWBop3b|ta;RtjrRh(nODNt`w0*HN;#jtyh_+^Zk5CGLHG9{>d63&oT8yY?0FEhDw$Xj7xE<}D&lex0begt'
        'm)oM^^ljh6x2E^p@R|<E=nC(o3~_(4wl8I;PY<iPF3bOjfp!G~t$3T2U}e7p%lsDne-~;oT}EM6BH2T-7iFo%`Y7K|asXvtiw&ae'
        'Z?PfDm#KUh<zS1A(DNgtXB6c~iycK-Zm}_xdW(&t9B8o#sy~Ucr^Tj7-!#g}7Mnpi(PFbG$6IU;<yeayLwU5t=24Ee*aFHUEw)Jg'
        '9Y;CbVkfBIlPHH;%%J{Hk-bY~$7%BG4B2xQWp9fulU?V?pB1w2H95HKJjn|rS4pmstdP7&@)F6*B(IRXO7a@X>m*+%`3A`wB;O>t'
        'PVy$nKaix!XK#^wo8&tr?~!~$QjknYJ|+1L$!|%1NAi1;Kal*9<WEvQ&`Xq<Q;8LoxS<mFRN{$B2$e`w;;Bk}qY~e$#CIz3y-NI`'
        '5<jZMPn3wo9ZFPxh6fLk4HMWfUxJOEL)hpcHhPH-y^D=rVnZi3dWelOvC&U#XvD?{v7r+ieO+vf6C0z%#xSv=6C3@+Mh~$uPi)K)'
        '8#Bbl6tOWuY>W{bqr}Dtu~8;AbYf$G*ytlRdb-#+M{Fz;8)u1)GsMPeVq=NeI7Mt2#KuWt;{>sBoY+_-HWrADd1B)ju`x$%%n}<j'
        '#KttSF-2@l5*ri5#yGJtMr`QBhDmIg#D+<1n8b!jY?#D`No<(JhDmIg#D=NZFcll7V#8Eyn2HTkv0*AUOvQ$&*f13vreecXY?z7-'
        'Q?X$xHcZ8asn{@)4fUpYMZ+r^UeWOUH$?($Brm~+b_g39u~8y6db`*t6B`<_(MxRT#D><jiz*QtBgDo)7aK>3jWV&(Pi$z!#uTwJ'
        'Mr@1_8#=MkM{H=s#saZ1M{G<J8xzFFQDS3+*cc)<28fN`E;g2ljWfi?60u<r8z+d3MPg%~*q9?WW{8a`Vq=2X7$Y`DiH#9rqfBh*'
        '#Kr)z(MN3b5E~k?ag*3sCpO+BHf|6bmxv96*cc-=G-4wmHWFeZAvO|XBOx{tVk03o62(TM*hmx`iDDyBY$S?}M6r=5HWI}~qS#0j'
        '8;N2gQEViNjYP4LC^izsMk3!7di;upS2Vn$p(RfvMLC_!PlmU6V1;dmdCTd4<hiz?iVgVu-|~Zo?bZ0fIZC)*jyevrx>|*ur&}TS'
        'qSfagc&+AVPFuEHSLag=9tqzGQEPrGB@bR)Z~Fy@P@Sh`>B1rBo<U&mXX)$*HavwV@&Ni4KJC8Z;Ib1s2z?(9J?y4kbEEx?^`;Z*'
        'Sb7UjPpQ(u5uGlN=$?X2&pmc&KNM+yZ|isf(tZ*%yJ>sde3LhM<Q{g^{gFI@?u7=Q<xx%(w_qXt4q;AXCDv1Hi#67Zz;y&XjSaCf'
        ';@A=P@M&ImROWQhQtk?YS`h?`UM6I21Y1tZ^n}cH1VyP`g+|m~#sD%ab7j_#WgTG>pH3AAFd7?U0~mT1WNr@n7^1+5+Qy2FHs<;;'
        '_;dtOjZLxz+@u<+{aA5GgSJg$*jrNe_n>X3l@%w75S#Z)VHR6WU~pdU@cLZGSat+njT!885q?qE8SM3f%pGG(7|K?a4+h$>CUdz3'
        '6=lyN>bNL#^DuHJDL`vQh}PIRTP*^$##ZELUsaa&V(`DF#?`=(dR^wugLW0b<tU$_FfQlg1O@YA%-`(re!XJ`ZpvH_<OaHeyvE*S'
        'H`yB$>NU2`uCUiB;A7cUwnkwet-k>lQZUrm|5yT~KunaIWgWn2mVU#RWN+7(WWJ#Btt7uEA=gjf=md@qgFR53L8>oH9a;`!yHVAy'
        'jJcy!NA4Yp?@T?1Z&-b8LhVrk2lb4i_9<#PEuW4<onZn82YmtubC$G1?nu{{sGd*oEP<oLB=!~Om#A$D{aRGo`U-F`H-gLL1Zg{|'
        '`dC1J45dvgzFARQKYl4L$=p0HP6DT}LVm@{<$PAPn#b?aWz}j5?K`K+hB3E7HoPXEuE^OquXObk-?=(F1&el$z(F7Koy(fcEu#gM'
        'gRwe8;OGF`5&UMpL>dVk9Wd<0MSex*E<u|`0tYP}W~&4ajzqqPxh`{80OlD2C-)X>zM)1UNA`xY&?vwuykGB_ftxZ{hTJHDqZ2r~'
        '!s#vL)jC@7wko^Ht`j&|)&`EwegaO|=LegKMUO{&e(;gy;tk1`UE`g*iYLcPnzkY97)717?F4KNc+-Y=8^`^|L6u7RZe_c&YQPS}'
        'unotLtNGT!i9N^mqJ!IQyghO878_pW#$J9iQuASt;CcphYS7y}T+MeazQ+wa%I`^B&*4dayF#t(W)pgd{JeC_4Z`Ta7<omL-)N~C'
        '^2Vp#-mV?Y%kEtsruuE)!^^Db;EMWj*Peni4evGO&Z3;oJh=75+PM4puManwb${dW-OcxI-M;$>cX8{q9}D9q4o_&r&D`X`Mfc=Q'
        'b<j4Dg#%#)_9E$VwSVGCGk`4{Sle-Jt8eBW*mY$qv>Dn8>>54|q5M5cLwQ=dnxWOWROAKV&TfyUiOrp3y_&X@KzipirjEm(!|wyd'
        'lDzqQ3f^hI;yUY>E}%a9`PZSivk_N!z5>JKd*O3<FZ@_4N{R+u&m{}uL2>;KF6Q2$W518*J6EA*ItbGe!79ogXanht<<PGP0!wh)'
        '0nxo3HGboE)aclb?)(Gnm6@FklI*`-*LS#k#c|nyVbKO~SkzlI%*Q7mOe{2>Q%Hei>6d@!aPaenw(D^n+78msk}?{nj{Ea_P(crh'
        'Ur4ALG%edW3mpIK;2%-U$Af>DUN9ri#IiUSS1bPqpUg+1RwV!c'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
