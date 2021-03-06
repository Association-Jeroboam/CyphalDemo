# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/pnp/cluster/391.RequestVote.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:05.966419 UTC
# Is deprecated: no
# Fixed port ID: 391
# Full name:     uavcan.pnp.cluster.RequestVote
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


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class RequestVote_1_0:
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
                     term:           None | int | _np_.uint32 = None,
                     last_log_term:  None | int | _np_.uint32 = None,
                     last_log_index: None | int | _np_.uint16 = None) -> None:
            """
            uavcan.pnp.cluster.RequestVote.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param term:           saturated uint32 term
            :param last_log_term:  saturated uint32 last_log_term
            :param last_log_index: saturated uint16 last_log_index
            """
            self._term:           int
            self._last_log_term:  int
            self._last_log_index: int

            self.term = term if term is not None else 0  # type: ignore

            self.last_log_term = last_log_term if last_log_term is not None else 0  # type: ignore

            self.last_log_index = last_log_index if last_log_index is not None else 0  # type: ignore

        @property
        def term(self) -> int:
            """
            saturated uint32 term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._term

        @term.setter
        def term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._term = x
            else:
                raise ValueError(f'term: value {x} is not in [0, 4294967295]')

        @property
        def last_log_term(self) -> int:
            """
            saturated uint32 last_log_term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._last_log_term

        @last_log_term.setter
        def last_log_term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._last_log_term = x
            else:
                raise ValueError(f'last_log_term: value {x} is not in [0, 4294967295]')

        @property
        def last_log_index(self) -> int:
            """
            saturated uint16 last_log_index
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._last_log_index

        @last_log_index.setter
        def last_log_index(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._last_log_index = x
            else:
                raise ValueError(f'last_log_index: value {x} is not in [0, 65535]')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
            _ser_.add_aligned_u32(max(min(self.last_log_term, 4294967295), 0))
            _ser_.add_aligned_u16(max(min(self.last_log_index, 65535), 0))
            _ser_.pad_to_alignment(8)
            assert 80 <= (_ser_.current_bit_length - _base_offset_) <= 80, \
                'Bad serialization of uavcan.pnp.cluster.RequestVote.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> RequestVote_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "term"
            _f0_ = _des_.fetch_aligned_u32()
            # Temporary _f1_ holds the value of "last_log_term"
            _f1_ = _des_.fetch_aligned_u32()
            # Temporary _f2_ holds the value of "last_log_index"
            _f2_ = _des_.fetch_aligned_u16()
            self = RequestVote_1_0.Request(
                term=_f0_,
                last_log_term=_f1_,
                last_log_index=_f2_)
            _des_.pad_to_alignment(8)
            assert 80 <= (_des_.consumed_bit_length - _base_offset_) <= 80, \
                'Bad deserialization of uavcan.pnp.cluster.RequestVote.Request.1.0'
            assert isinstance(self, RequestVote_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'term=%s' % self.term,
                'last_log_term=%s' % self.last_log_term,
                'last_log_index=%s' % self.last_log_index,
            ])
            return f'uavcan.pnp.cluster.RequestVote.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 391
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8d4_dj0{?YXZEqYk5WdhfNt33e3Jpb-=prBli7t&QK)kn2DWD^l<680wWO;WdHx@p7vAxF~5>opC)Jm3!6!V>*%6K;~mzO)~'
            'wBwg&JoC&m^KACtYxAx8=Wmze!WJ@R7L4Fh{J}E`Da-Ys)K)kMe)$ndF(9*eIxZm`g!i9^Kf{KfV?rq~0b73gi8EF1Dg&plTxN<7'
            '$i;fahdEbisme5$m33g!9{g5;b-UWZksbU38-lSytLSxp_s~8F?U{D#@9;eMCB~gIBC8zO@C!XLCH~`E!C!tXKo%!KEwX|;&RmRi'
            '8oV?yV=<%~t3N3#`U;Bgm4iN*(-|(YOgJV%^&N(GLe6t;9UJHZ0>0tbx<`&8EZw5B?RZ2Pwf+jd;9q0baaC|rOgef|Ww_{PiKapD'
            'v#ij0@U1|bH=1YhCf+)<-fSm$8{fuv8qBhc&r98BH5k|Ny(zGjN!Ybxm{0|b2<JC?um>h_I&la|kMFsp<R$IwX_LUHlw5H~)k!HX'
            '@T(JbVcEE;dwl3!T*D7=12^$bMQjyN8pt_`DZKR8*q#_c!Afl$6GiCw>&)uP<Uj`!SjmYCKOa9*WWitQk|amnxO+g{&wNPappF82'
            'r4+$0ZjDRi@(~Pl@VCk;lOksZ`jw3DomAZhKi3E{_)8>7dg4%&!QZ_1>E<bEZl-tBsF2`dxmFo+OK}-cE=p!7atJSoEqsc?CeeFB'
            'UrtmRm*~9{?sBaxC|l8?>}w+&4$`D6fm=w-B-6Ez2W1JW_(l<>U~9$;a9l{6Mm=PbQdmDy?ul+FB6oHj{MCoT{ZOx;(DG2Z{u0xa'
            'crwk29S<^1{87r=#3%Jdto07npF3?Phd_>kx(j#wt6g3cLiNvGB5r;>ws!oDEv=#g)P*knmBu469Q%6$xqE@PpKA-*w3`%Fr;?JJ'
            '@ws>A*pSN#!arf7o$T9;W>489K+~qmh~|M%v8Bo2qiD>>wk9z}^dh4c;Hn-^9cm%n1Y(Z7fz7aL-^U^Sf2V_SyyT+e^V^fym1As|'
            'E_Eld3)T5;o5l9UCA^9&cs;VPM!j|i@ZQ<p!;fC##~u6xKik01@eBMCzrwHaK0d&QxD~aHk4eY)EoBKKDvk@=&u07@HEc8d4MX4s'
            'ed@V+X8gR>o{7_}nI_+1yGf`srBG+NI;D=+dtCLQ2PHT$O>)0B6}d}*NnZ>5H62w4hZK9{sJ#&PTl=;qtL8Nx{&&G)gr@%kwuhDa'
            '83zCW'
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
        def __init__(self,
                     term:         None | int | _np_.uint32 = None,
                     vote_granted: None | bool = None) -> None:
            """
            uavcan.pnp.cluster.RequestVote.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param term:         saturated uint32 term
            :param vote_granted: saturated bool vote_granted
            """
            self._term:         int
            self._vote_granted: bool

            self.term = term if term is not None else 0  # type: ignore

            self.vote_granted = vote_granted if vote_granted is not None else False

        @property
        def term(self) -> int:
            """
            saturated uint32 term
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._term

        @term.setter
        def term(self, x: int | _np_.uint32) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 4294967295:
                self._term = x
            else:
                raise ValueError(f'term: value {x} is not in [0, 4294967295]')

        @property
        def vote_granted(self) -> bool:
            """
            saturated bool vote_granted
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._vote_granted

        @vote_granted.setter
        def vote_granted(self, x: bool) -> None:
            self._vote_granted = bool(x)  # Cast to bool implements saturation

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u32(max(min(self.term, 4294967295), 0))
            _ser_.add_unaligned_bit(self.vote_granted)
            _ser_.pad_to_alignment(8)
            assert 40 <= (_ser_.current_bit_length - _base_offset_) <= 40, \
                'Bad serialization of uavcan.pnp.cluster.RequestVote.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> RequestVote_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f3_ holds the value of "term"
            _f3_ = _des_.fetch_aligned_u32()
            # Temporary _f4_ holds the value of "vote_granted"
            _f4_ = _des_.fetch_unaligned_bit()
            self = RequestVote_1_0.Response(
                term=_f3_,
                vote_granted=_f4_)
            _des_.pad_to_alignment(8)
            assert 40 <= (_des_.consumed_bit_length - _base_offset_) <= 40, \
                'Bad deserialization of uavcan.pnp.cluster.RequestVote.Response.1.0'
            assert isinstance(self, RequestVote_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'term=%s' % self.term,
                'vote_granted=%s' % self.vote_granted,
            ])
            return f'uavcan.pnp.cluster.RequestVote.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 391
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8d4_dj0{?YXZEqYk5Wb^nlIDd{g@&R^bSp}Fd|6V81m#^#1cD{k(-o>p6|%g$lN*E2UTp6vhlJFA05y^&BE@{?r!u}xlRes;'
            'blTbR%;TA7p4q1h|Ew=|W<P(UnwGYdDYIY%m*RJxOGsIv$Cb9iLGbIlAjO!>^2ccf;W)hiEc_9Aevt{Kzy$30^@q;Xg{uwBhg@We'
            'j|t*-%_jv{X{D;PkhOJS(joj-gLRLz1F~(Um8HmKHUVRWRuOjT(TRN=vToM-D?AH+m2u~c$ZH2S{7iS8)4*v|@E5-kAj`9=R#?d$'
            'XD*g{UV3F>%VI(i8$T&4MheRBl!FnN`4(4ME*z7fMh-)k5O~3@V`E)Hz_<P8-~~`jOLypOFCI}xoj=1c_&1q#T$S9EZJ_6Mjw^nF'
            'cp3-4z)D>N-wEWr+FXm*2z&Lu))KgyD+u4ox_ATM#ao9njI{|7%tnS&@nyg*-y6a{n8fMCAtXb-?~;mF<k{CIfrCnN#T}8J(skfB'
            'T6D8~+RQUv^B!(uioKc$D4{Y?@Q8otUuXN`07_PA<CrKz-(O)?*QNkEkiaTV?fIqnkRlKM(tu=kFo@n`qO<z}^@}=+=Cw)$zp^u}'
            'kjq^d>)@|fbuLB042)_S?>if$4Sul^S@0J~W^~1g(1O2q_uid3x!p;((>V0t;siDra!Yj?P%f%qA_@r4aSLw~^SLDCtrr?On-B%M'
            '|Gx*nc3-$3X73N_^<*Ue0@GAaavq4Cj&n_IQ6+oSCMht||A0oqoi^=#D^QS*G4q!Pyex$py%dB4+&i^0e|1NzI2iRxNPnq8q{ibW'
            'wK9h-jLZF6N^YhvWiPS`mo<dHLoZ8?Y)-pdHD%GZ);W<k7Amd;8T=p`OK~k|axr^_k=D4Ht#_Z4n$JKHB3hTwz~+eAO%(M1g$`s4'
            '8fD9Mboa>JJ9XPUDjipG4d1{kv6D^g0dBWtiXR^0-9CPVANTMRyoaCSXZSgOfnVZR_;r*4?ldD`qPmDM7xtcZ{U&L<`Suxxz)O0}'
            'z8ZM_blDPGwwqZu?lRtrYrBizHm!W$BJ^?NdJ>CkcN%${o7h`Ju0}9~3Y<7k2ER6ZZc{=VYx!tK1olx-?U9{qIr=+Cc1F{T(Rldp'
            'D-L67`X6>MN`M#!000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.pnp.cluster.RequestVote.1.0()'


    _FIXED_PORT_ID_ = 391
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8d4_dj0{^X6-ESL35VvWXxcO*Og$6`KxC#_pC`VHy#Fs>yqy^+ASWbw95L)f|Hl7vdy<>0B*eRg)0cfNJBC@<!;+2Q0Nc4%n'
        '3xRlG_RjG~Y`0K|6y4tL{APB3^P4%}9Q*N?$z1xUpNU$2><2E1ndCI!d(;b<OR8Z#3S+LA(NkMYHh7h7w<2Z^&G}pA3sclHM6yp4'
        '7AvCcKIHVwItzFmA%4H*IN?GtnVM`VnN(FGk2yO@1g&GJ<%Bk>RJf6d+-i`-ib=PUh1m%eJ6aoEAPpvC9t!JqVyC@6G^Kng_qDl&'
        'mnKvx$-P9e*nEs3M&#MCGWz5-&H}%CsY&8fMYHrq!6Rui<_)x%|3JjNCYb-8P^`vee}+@U<B9}K)D)PKgU+iIxvPgha<`-x%14eY'
        '%w5B?4SR$c<-Rf%qaP=+qQa-r?{#!L@nBYuAx(9o$A}+Rjm{a|d@2hIPlMB5JzH|%IVi&U3^Nnh@IhE3DHvXa3nO52y|B|A7#BWk'
        'B2E`8Y?nz#g^mK|ROqg9A{yb&ZYUkri~=gC!s@tqFQ(^v>O#C$R(Bid1z3a?cnMyGO9`^&vq-WkMKPIueVXj@Ci6)YN=3MDHuV`2'
        'hl#8*JO~(xC~~1E>?7cw(WlBN-DcVD9wPVomysL@t-v0OxY3hqtq5qa&g!Aji&5eQyozeBC4r6Ct$J+qcqT}rPoN|*L|c?bKl#e*'
        'D}B;jaWA@7Ax7D9%@d$8-b*r}tYmEenA^w}Yy*!S>)pX8MXIE7!rd-+)lkGt#0ee-wNP>eb=N5ejK<87y-cS*u0#<N{#AjLvN&bj'
        'XNvM5cC8+~08>~#Qf^l_cq4WE-RS96uCAx=Tlm^mu0BCROxzjeByQEc5c$KDH;_;43tQ{=vHnzrvUdnnfn#^Uww^6h-{+z>U<4n+'
        'PG_~P&#r~SDnJZ%sZV7dkzw24J;;xSc%$hG{85&8tIZ?`sB8_y87B=IB+PtoiY4bD_Hgz@Spqn15)Wyvb75N=7qn>?6Sl2UOcp&!'
        'umz|{$I~XZkjgId*^xIEd$3o!3^(xqb3FLc8nvwB!R=n`TnAf5qjE2{kPL3eo^4;4gEMdz7Ay;k*lU*<ymq|z;EjEFa}(Zzw~KHY'
        'uD~j+!8%-pYw!-dYqbp})G=JgELjtaqs+$5yk5YD&4#}uz^IRp?6c56ewIslJI%6bvH|5Rp{)^xI?h#}I-aOdQDYSrF~vto?vtz{'
        '7ZK3wt8kFgv9}2~@a~qQQo-)$4&s!olvjIrXUL(2;y{utj%=s4)0}AEY!as1t6Ba0LqBGj3)3yiL&x^m@M*oIr&hxdhlJ?+>L5Cw'
        'q4!htbOYm(nxw+c)qgv?Gp+mz_ux0U|4(&tVR)GzrAG(kaMUIaO5GXWCizaAoI|5?gKbj8?c(t^x!bMCJ-Gj<iGORw_1&>b{_x+m'
        'f2Y0r>HiltYGmobsvRoU0^%mxKL-cJ`7@ptWJm1jahuaW;CJ{7{>(Vt_$L2AR`>1LNj&#&4k-Itz6t;U'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
