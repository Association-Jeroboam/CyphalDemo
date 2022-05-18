# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/common/Heartbeat.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.841361 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.common.Heartbeat
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.service.common
import uavcan.node


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Heartbeat_0_1:
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
    MAX_PUBLICATION_PERIOD: int = 1

    def __init__(self,
                 readiness: None | reg.udral.service.common.Readiness_0_1 = None,
                 health:    None | uavcan.node.Health_1_0 = None) -> None:
        """
        reg.udral.service.common.Heartbeat.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param readiness: reg.udral.service.common.Readiness.0.1 readiness
        :param health:    uavcan.node.Health.1.0 health
        """
        self._readiness: reg.udral.service.common.Readiness_0_1
        self._health:    uavcan.node.Health_1_0

        if readiness is None:
            self.readiness = reg.udral.service.common.Readiness_0_1()
        elif isinstance(readiness, reg.udral.service.common.Readiness_0_1):
            self.readiness = readiness
        else:
            raise ValueError(f'readiness: expected reg.udral.service.common.Readiness_0_1 '
                             f'got {type(readiness).__name__}')

        if health is None:
            self.health = uavcan.node.Health_1_0()
        elif isinstance(health, uavcan.node.Health_1_0):
            self.health = health
        else:
            raise ValueError(f'health: expected uavcan.node.Health_1_0 '
                             f'got {type(health).__name__}')

    @property
    def readiness(self) -> reg.udral.service.common.Readiness_0_1:
        """
        reg.udral.service.common.Readiness.0.1 readiness
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._readiness

    @readiness.setter
    def readiness(self, x: reg.udral.service.common.Readiness_0_1) -> None:
        if isinstance(x, reg.udral.service.common.Readiness_0_1):
            self._readiness = x
        else:
            raise ValueError(f'readiness: expected reg.udral.service.common.Readiness_0_1 got {type(x).__name__}')

    @property
    def health(self) -> uavcan.node.Health_1_0:
        """
        uavcan.node.Health.1.0 health
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._health

    @health.setter
    def health(self, x: uavcan.node.Health_1_0) -> None:
        if isinstance(x, uavcan.node.Health_1_0):
            self._health = x
        else:
            raise ValueError(f'health: expected uavcan.node.Health_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.readiness._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.health._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of reg.udral.service.common.Heartbeat.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Heartbeat_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "readiness"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.service.common.Readiness_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "health"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.node.Health_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Heartbeat_0_1(
            readiness=_f0_,
            health=_f1_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of reg.udral.service.common.Heartbeat.0.1'
        assert isinstance(self, Heartbeat_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'readiness=%s' % self.readiness,
            'health=%s' % self.health,
        ])
        return f'reg.udral.service.common.Heartbeat.0.1({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8NVSAw0{`t9O>-Q@RkE=yFJO!fgm0RUfP|%yKQIsoNfy~))!MSkGT4v`lb)Ggb=$KulkT2fEpaNL0u-*As<?_t75^Yya_1-T'
        '6S(9?B^*+fLvrAjyw~$)KP7<=IVDr2eXXAE_g=q#-}AdW{`eA`aZm9?){jgSd%h7`@mRgjgIIWen0B(%C@ae1?hUK+(B@iP?q{O>'
        'v|RY0{7pGu?DG@ef%i{ovFYWJ=CKDjx+)YN?CzwAcTR9^1Ho-s%=ulRjY^YJ&J+jUrtzm`Yo;~(arr@6-05>`wF+`8O!*5yzXM}~'
        'Rb{d74JG1e$WX(NxaGb@F6EwTQtsP@ze|EgDiOw%@_;;8vm);T^71h4Ke`hmnN}TTRTmgJ`c`7pW+I~1#EMO!$K`aVA1Ld`BH6UE'
        'Z0!LyLvF0!Nh4tM(c*#i8WC>uR^Z(Qd<C+Z{iwWD7Weta@+9Iq8bx$758!P3x;)N-gFE~v4a;JtgxN#I+)A3@9y?${9+i*N=*iX|'
        '`ILO7HG|0IbA)H({MobXrChlB=RGqsm!)8Fnrtpvp*svPS;5ja>!?I^c+9f2Co~IzM&8LR+@se3)>X*kxWC9csj<xDf$1A7I)-sA'
        'nCU4SN)a)Y*pyj7@8~g<0qaSTxVf&7DvSkFhGkq|hvjhWiW-d5cH3)g4DnjYEsIi?q)0ByQf)^tS4<n3=5fTV1|4L|G7jt{O#CWW'
        'AUBa%Jk`eK=GvLp-|-ra=8$dH;eDoYA#l&#JjxTUpYcwbS39lh2nOd7TdE>$Vj;5XQ1k6n!wcTYVzF4QM3jMGi4YMS$EJ-SO{;xr'
        'CN#Gy*<?f=&#m)HDn`UWN`O!^orWR;J2VTx?G>p|R>_1o7pqN!gMcvMUO<LOl7)gBMCr@`5q1?Cq9bT*n&DdD(DqV&o$(N~QrUh3'
        '3<$I@21CJPr$9j0!s&n%%_5vM6q&8=1cYHE;(^1WsUTgr07Qm&qO3cSYJ*${2FN<_!#DBnfm$fQ8X|^P3XGv#c+#)+&`}3MNp)zi'
        'EcW|k1&`I1Dz-9^5}s_#PUkLhR97C?b|Fs}2iqE117(KyZ_pUt7qiDpv=9@3fh_J|MJH?fIY3&37WDLNWkCbG2?QPiL=g3zx`30='
        '?v|2Nqdg6;->D8<DM!r(eNJ^Gv^S=hm52?lBAVm6J|c85BCA4`IjJY36en*O3|Jyg;}%7t&GXn2UPo|Tr-&4YSP{Q%Jd(52CD10Y'
        '4;6z>WHFGpalgJvv|_xzo-)D%;meol7UXNi?8(~^_t~{Kn{S>ygW^5_4(kfK5SrV@06@NAjvbURXdf6Nune9^IF8zR;_jT$F_RP)'
        'qL-^S@dOMdlpHk!{J#N-8gDmO;Vy36Ni2eBKpO*)L=H4HENhD%m?8Mk2&@P0s`8L<d$uRY9nyKwHXCDCZP+}@984ktnvQvJ2peff'
        'jQU+<3w>jx+HG*4=)B-IYXUVwH2j*-yzn-?MRc@53ij@9El<F&JMn-Bq8>Q&1ymL>asCKyG}&|pT$wk|Z3>c1a|4Ga<r7_Uxo~_4'
        ')G_RgYw0iIq8|8v$sjt42CmlvojP1m?XRTZv6W5;xfxOTE6q!5t7~sgsnn@~N{Qm=NPgi5{VI1s)tZ+N%Tsbmo|R3xF3;x>uOk8O'
        '1CA}C@@8?!Z>ud4`N)f}qH?Xc*EeadLjf;h;e&a}vN(VsRzX=DT!*}AYaM4lh3G%K4AEJpm?-VZR9Q4u`Wbk~Goq80#UoiBfQ|Uz'
        'VDlL14Ko;UM|)u!vK*JX00oi)_`527DT^Zm|LGm~PI&11N{cDOQD1TcoZ+?m^}d^6EPvTw`6fMZyp@rIk>rL#L}jbsd*}k(-SIA0'
        'F%MJ>-lDz$ca!8wMs8_-pc)van&`P}w}DYX@~%Kziy;(&HYB6W)U*M^HBjuz_kiIU7rEJHoCbsZqp}#UaTXHG{)jq)O<A4BvCB4K'
        '9yF>48rpNplA9c}l=@`o4aP+Q#|n6O9R<O|&>1mCauh+E6Gu)tt>%#QIm@VRYG7%T;vE`efbP<z5<C%L9F;9iu~4z+{FQ+m2V@lV'
        'Aw&X2=Tf8?HHj+4W~elS=)hx>q8|sWQDuHGi7Ib09*S2RyP&|`z(<wxgS0`iZr%~b2!UB@qrup*rIF_tOx$2Awd^&!G4gI{;@M@w'
        '^E`&njyf?#m<^sAY~q=oXyEUABY(rEJGppzqEREgF^c@yBrm&7Y>(mw+n~$1@%<)1O#d}zZcCQ+&haZfb{o5=lwtb$ZgkryGwF+I'
        'u<u7?d&-T*DyCyD_l5A$#R>pCr3+GMh<cFMLqf_m6lj`*J4*6S07d{d;~dbA+6<vQPQwYG2KjxX_G0J*x?HOi10F?oSR~bW$wZ+W'
        '68bEUjf<y{zhF*|4hmwkNi`%IV-X#)b{nFLMi*2CqAJpBiU_s;z}yJYE!9E}xKV%&VriA^JJ*^(c-JV1*d4`X=qK2@_ZJ&gap20E'
        '3IP>wSQ(DhFV0y`WCBQ`O5q@jx1&|ecBP7krEm~K@O-we1%@><L_$0He_7o1y0Yip{~KaZFc*9MG%E|X6B5(!1Stp%LhS{J<m!DV'
        'xr;85PxY|&-|vS|rbVT+#Xajh!dhl(k?iB!wLFeNb0*))(|;)ETYGMqpqPVz?l6?CxjcY#LY@jk9Plk19KfCe<PnIpHH-UZZngFh'
        '+*{#k-9i8FL%8==Yd_5&KsbA=HAn9cBAmO`Y7o4W;9UgoCU}V8Jp>OEyqDk+f=3D7NAP}v4-otT!3POGMDSsPj}Uy6;9~?IC-?+G'
        'M(|03PZ4~Y;4=h&Nbp&L&k>v_xIplEg2xCh5?mta5nLvCoZtz9CkdV+_yWPx1Yach62X@V{)pf!1YafiV}h>{{0YII68ss#a|Evv'
        'lmxd3enRjwf}a!og5Z|~zasbz!EY;gVQ!WN57vYEdhl{RI9Cs@)&p4&w(7wr_29F5@OeG>q8@x%55B4g-_(O|X^<BUtoku0gUp!b'
        '0#{A$D-P;mqi;bz4|9X=-bkPDNY1+<PrL+*aBN*dsZsR>XInGd^aXdSO{pbEguc6!UAuT;b**_GHWbIv6T8l9f>|WEy}CR?=ZVf;'
        'Xh>e?sYG3vDtK<EWii)0^Y-e-#Y@<;DE`!Bp@wYMg(9eRI|2*(o~ze#SF=I73)LN^!b2WK;*w<7q2t&ggcWTl6>=@=4js6AOnsrG'
        '!uqc<UY)mf+8M3Sv8n}Xl$gg$u5(sP!Au?a#O*W<R+?{JUcI=6=j~qJ?G*gl$SE*dPxKHl9!6qQbL=0uo(-%AIk|QSaUY4QCCp-M'
        'Kk@C^zpb7JRk_IiyW{Me+!Y?tc7=7#f1V85Le)tems4Gk-D+rg1=;$i{D=Hj{_EP_*_j#n?`wwuTx;OZL-=z){N(bToATW?`E&W+'
        'y!7QSC6|E=i~W^-L4-yND~o$78-v32_^@=9*Rf1hfTbBg5rQSx@SIfttHd>C9J_3_O<fxhJ)I27tvt3WgX2<Ops;7+x}A|2d0S@>'
        'by~8p*g&Cd+h)+B9akl(7^#2pKR{vZ(x?toG6IG=P5_dvH&SfInpYqzmDXnFmF4ALujj?Q=Y^?GL>zk}%9q2oUbbS(E}wW|`Q$0@'
        '#Ho`fCw8<s_cqh+a+HQSHet`J05i|!j))XrZbn@NDPP}TQ96W_Krc5}{FA30qNNjF7PYba<n-gkQg&ok-MEq6K~D1P!RWUWnTY&7'
        'CLr>|)|~tZ{yzSHy751sZshXoiI}@zQUu*O4$f8X?Gv~DfeX#6{`y<5pI=>RqL=p9&t6)+h#lU-x*ihM9(9KUL&|jVP+O}jXN+WI'
        '&Quc4r`maL?LIG5R=hCmMY#qrpvL-Vmq<f?@UQaTYZ`sv->&u0^O+qzpNyoCZMj(-8GH~O@7GmM@9*^8VBooTZ1n(-2BHd>HFKZS'
        'xUJVZH#l54)&X*U%Y8>2c7p2SZ1Cl#ZUpXB^I;PTeO&!jU|9cl(kkR9uBS&AfL{gR&!tpVp}9?=KIr4tn<6HZ`^@9GFak3YE9#ng'
        '5u+`i>QVunx=+O$L}kfjB2;Y^4xD*~!ecwtyi*$|irlJ)H&NocqgCHec5a=Ck*{5@hxVO*w>wfF-oKJ2*pW`QEi{XRRh_9tg5S=!'
        '#nzj4+w$u*kjDb(oiO;~FuXWCcrjQ%K8+^e{Rj2>np8p{000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
