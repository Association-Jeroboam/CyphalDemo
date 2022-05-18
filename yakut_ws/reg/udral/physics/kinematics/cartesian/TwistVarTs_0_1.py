# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/TwistVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.345709 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.TwistVarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.cartesian
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class TwistVarTs_0_1:
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 value:     None | reg.udral.physics.kinematics.cartesian.TwistVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.TwistVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.cartesian.TwistVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.cartesian.TwistVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.TwistVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.TwistVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.TwistVar_0_1 '
                             f'got {type(value).__name__}')

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def value(self) -> reg.udral.physics.kinematics.cartesian.TwistVar_0_1:
        """
        reg.udral.physics.kinematics.cartesian.TwistVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.TwistVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.TwistVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.TwistVar_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 584 <= (_ser_.current_bit_length - _base_offset_) <= 584, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.TwistVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TwistVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.cartesian.TwistVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = TwistVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 584 <= (_des_.consumed_bit_length - _base_offset_) <= 584, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.TwistVarTs.0.1'
        assert isinstance(self, TwistVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.cartesian.TwistVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 73

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8NVSAw0{`usO>7&-6~`%3q9}@%^<g=T?bvI_u_(u)^=&0>+PHQNxf>})Y^O@ndbuP=nx)BIc0Xh(Xn^F<!Y&plfouUEd-S<L'
        'TldCW-8N|2n|te_2O}*|6etP<1&Y2|{)dv*Qf>FpODVv7kNYw6c4mJ6c{59Y-2J1==VIZXf2_V)cFNVf<}lmPtHy_VvC8sV$*R>Y'
        '$8cHT@4M>SUdi=rc5SoHf=`3-PlAtvoZq9FdX3Ic*=#NEm2JJ6uk%gEC^`9?hRJHWE8LQ9yUa0kGk@)t;kfVW_BAK)Q`$PS9m6sM'
        '9`k$Oh5u=w#?-Fw2cHCfzoxscZ4^DaIrui!wnv=ps{+60lEJFwt@zSfS$B2K6+!cO>mcv(k9+!hiNbM>8p~hZG)vsJOyfgVzD5Te'
        'SFhCr-pl*cE;S}1;Tfu(590Qbz2d0bM$K@Ib&6x;y6G5eCM#byUAD&Tovqfd6%ALbGIP!4fx19ZmUPF}YF3$|JmMd`A`23?<uA~='
        'C2@+Hrt5pbJAr>dqZrMyZkM+gbjK^wqxIK}l5IJxWSQl_@7BszDOmX;9*bS$OfkJ$k=cs1s%*Q;QCzOO3fI?}Qr8`al@-S@OH6UB'
        '8dG$es<3r?Q>oEc(^U+Ut`Dzt^J!5ij#HtQZLHDhoRMewGvQUDft8}}uyMt3lrmeTK~Yxf%%0He^{P>#@nM;HMHEx=Y+IDmzD3mJ'
        'IV?>br4*TBv+sD+H+1`|ZPm6)ciP<-7N*oFFlL`o9LB<nN*0yt)agMDbB&JL>jphr7>W_ro~Eau;MVo3$3&E_rI>78G!uQSR;^pD'
        '_}b^^<|n90lv_rb;$$VAVthTFR+I^4`o`S+&X%Ri^`hmu%JlTYoU+Mu+c~4$;zo&!Q+4V&cQdb?SLSEKGPm7JaeFj&Y~_~aRm)Tn'
        ')u1SzX|fV?9Njjmo2?LNASj0Gw4<eFquVH2(IazItII9V5m$xP)9JEDMJPJeMg_ACB9g+OajcYV!!ewE>tQZbX)G9}i3{hKm7Hn0'
        '%B73r3XKGl+R~=_2x=M>UR|`;Ii<Kskct}X`exPA!#<{tB5}xvfnSqdrPM_DYjm;0^=ei0uo!M@RW=b`-l}4iZ8cPl(Sg<&b=&<w'
        'gJR4T!$P!yEzX+MF$y)JlMe`l0Y7!YG6g1Xn>#+jkHR~yF7Ollq#6@E@v#;<z1Nr3<+s1N9Pn}f)cee~qE(0EjrvWr#!b_@W#$7v'
        'sf7Ur{!3C6*hZZOoDj1el8|~Q9G`ks#>40QK6>PmI4b1u5_~%EcTEN&GN<SjnLn~k2esm6OLE0i<oF>z!zVlvlrp1A2`5$#?)U@R'
        's<FY!n&>FaC<n{_kmgvPU1D^i%Cx#pa^d$1Q#Fc#-*<&%e&dQb`YFj%*I5z{ZV6qF*NwnWU)ZcuUtMH1EAS83y&{3Dk>Gn(QQwxr'
        '(nBO$!b<mxwhH{CyNYXmDnFSQjTN{;&PFt@I~0__Ujv}Q9qNSNEVqCcH7KG6F<OX!%O*7tjV#73L9G+8?k&r{IS~@!Y^yWuv#?Sc'
        'DK6hZ7!_buy_N=q60lVdec{F$C&s8%tr`hj85N81TC}JnQYWdxA%p95jb%?bbyhM~jcwzcCWxCXFSNK=r6xKh$H|s-(?h$_?}4BB'
        'n&G|`e!t4vgV;}KRz2{Qy$W$QYekFthgx-s`U|4?HqofNmc2CvCAAVK`~&_ifBzM|EVS{7i?}Y%E_>A~$$#`LpZj5uQx_UektXtb'
        'tAs#Jc}058nqi7*jU0VLIK5(OqtPM?RlCG}v4$FlO$ZxrsNMM9BWzbgP2zYjj;CPza6Bz+vZ40l`i!uthPqGK?uI&m>-P)W-%tl}'
        'en{A!hB}OLMuZ)1s0V}{Y^bBc4m8w*!e$!k3&N%wY8Lmuh<Xp9p2H~T2<m%D*uxF=sIZ3`>M>zoY^aK`*@k*t*cTe=31JU5)R%=F'
        'ZKx-OJ<w2J5q6}Zo<dw>!VWdm9O4@nc7H=XjW}Nwc3(q1gLo(Kym`cZR@lCVI*ItFgzasp(|C><w8t!-C+ycmL!HNSokROB;Q3x_'
        '^}G5y?3ZA_4EqM`S75&i`zGun><TQ0-GIFfdl&W|?0wh=un%D$!9H%;rBoN3taNhHS&+`6bXKIprL!TO+tRr!oqN)`FP#U{c_^Jn'
        '(s>NWqwJ1m1e!;LwBuM&2s_O<eePDiIqt{A#MRC+x23CRpEJ8|C9g=MBgyNwV$VEJvCmlMF=W<`k@qOS%CEDkRWc~ad6$()J!YQB'
        'tGA`qhxbVDZCl@@r1z4T(^`UfUL4w)Q}5GQm5D?Y$^H?)?-C^<?vATy-dAYepXOt?satCL8inYIr27qjY-V<HdSQBIc7A?lVQzY1'
        'VeYkssi||5vr`K*vkS9xQ}eG)&&|%Z=4Dd3KFZnax_GoeP4Me{rKO4=@EhC2bNC%rXRfik1jn_T;#QrnZ4*?b5e|*2THrPMXYQ$('
        'u{{(s2F2`&C}uLEm?<b`42szU#mqo4lTgeU6tf?SnS^3?MHDjw#Y{mlyP=pdDCQ^>a~O)bABvfQV)j8XlTgeA6f*|JJPO4;0>wN8'
        '#mqu64?-~yKrx3Sia7wq%s?^IP|Oq*GYQ4)hGNE{m@z2kStw>6ia7zrJOjmi6^eNpia8F&%t0~7pqQtin6E%FPeL(YhGL$8VjhQL'
        'Dp1TU6f*_IEI=^}P|N}pvjD{`KrstY%mNg%0L3goF$+>L3sNx)QZWlsF$+>L3sNx)QZWlsF$+>L3sNx)QZWlsF$+>L3sNx)QZWls'
        'F$)cke+Ea&<Y0}_l13wfG%RfSIRD%$>iqmiL8a6ci}6Pezi@|NT;^Zri#dLoe}k+1ExyE;{kTIZY_||2%CV&!1^yreX=g6Vuig<w'
        '@6L0n?fsMA6sb-J(+;K`Oxu_ytCT&6>|@+N@mA<6k~g_)RJ6*Q*cR9;*%^yu5V|QAnzr^FnFRj}yub3lJu&g~zd!$M&mZqK$N#J4'
        'Rk}!oI+J-vB|0kcG?f^#^)jt0_L|Kv$78X|ABd*CCiDuUla*Ea@CT#X5L7rFfA)#I@+XlybmsC7r5#FlQrZi&#AJT)e9PaO&0Fs@'
        '#DpGhG%NZ>Yx95S6tCpihHD$9W0c0lbk79fxyt8)xj$BZB0&E=`QEOe`w5$^1%6MsKOr`&TRRkipWfP|2>ibGE=AxEg!>ef%}+)0'
        'dH;<iD||IX5$cL~M^$b`NlD4fMa7|IJZrz3+9gqW+G=3?ihuNiWr}ThbJu-Wv1=f<U2SHH7n-|DQmrFN9ZBj)(l$w|Tp_7oj^Lq5'
        'JT#w!hj@gCM1+R~c!-0Co(K<V@Q?-%nFtT^JwgUN#KA)bJS4!wAb3bcco+f?Y4DH$4_WXq3?4GzAsOM}aO6G05O~OdhhFdy2M;H~'
        'g909ofQKx2H~=07!9xZ-q`*UWgog?6a2h;}frpde;W&6W3LXxFhb(v)1rNjEVLy1tfQLTtkOU72@DKwJli*<xJgk6+#mIYv9C*lr'
        'hZJ~df`=w}Xo82P<e@2fXi6TMl82_`p(%N2N*<b$ho<DADS2p09-5MersSb1d1y)=nv#d6<bj-Gdv@s1(4pb~o(3eWJ*}T%w3d=j'
        '*$Numz7^CnKQ}iyyS33X`V1RAqmhlCL2UFaUFqUA@$uhhY_UC<lo?wx!eoEsO?Nb7+ZSPSUnFCTfypG89EdR44<@r<G81{zJrv2<'
        '4uQ!*Fqs6CM<Z{#C6fs-ses9BBx6f~$rzY?8B87llcQjA08I8qm^=+8PlCy#U@{9Phrwh9OeQ05x@W*-9!!o$GPYx2@(`FD1(Smj'
        'CKthEHj=Tu2__XV83U7d!Q^c)xdA3Qm|T%eE<W+5J13dUN+wfal7=Rr484uEcf0M~ZF~3H-u<@spzS?udym@QW9hZ<3_Z!`K*?Iy'
        'ZCa?6nC96ofx7Z5Lg{*4{1}kdWSrKM;`CaT$(7{R9SW`YY-1z*ncb6r;V;IjtzZA?RZILJXv1*C8QXGkI9#xb!@HJ1e=D%>!M?xO'
        '@m&jeb>g}H(kokQ>Gt1u)9>wev}JO&v(EU9>1e&V+G$%akDqmJOsC)9wagVokFMUsnszy={Kvl>RTRcR7435K*82X71TA16RzB#a'
        '_5Gg{d#&#)KNai$pNWs3i;w%_;}`Vd56Pb~?6Q=9`m4G2vC1#0u<%Re*W~TB+-}Ch<#tymq3R@5orFpxRF!`uu-sl6j8i&8AJ0xi'
        ';wePP4X6}|h((A<MTkg5i0F!JK<x(+sR$7<5OFX<L;^&lA{$VWh$M&@1`%D6bS4HOhCxIkvH_I_5hp;zD2Pabh?5Z_G9V%bB94QI'
        'gCL?mLc}Q$aRfvRgNPJ}n2Bsa9gh&PA4DW0Kir!H5jhZ{fQW1)osk<*F%Xdg5tATd14JxFi1;yx_&Blw^(Kf=BoQ%5#A8XsBT2+V'
        'NyGz5#C=J`JxRn}NyKeQ#D*k-OCnYz5sOd!a4#o`$jTgMFurZY-2tKlL<fjH7TvA%kN=hrResPzN!9P3H}M<U`rl#yi`0*6?Txer'
        '%KH`s)cmt$ngC1Paspfwyf4Pvr`kdgJs}z-|8J>mHsVw_000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
