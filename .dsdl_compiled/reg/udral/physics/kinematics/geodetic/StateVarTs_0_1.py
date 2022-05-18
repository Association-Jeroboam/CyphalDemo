# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/StateVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:36.134176 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.StateVarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.geodetic
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class StateVarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.geodetic.StateVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.StateVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.geodetic.StateVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.geodetic.StateVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.geodetic.StateVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.geodetic.StateVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.StateVar_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.geodetic.StateVar_0_1:
        """
        reg.udral.physics.kinematics.geodetic.StateVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.geodetic.StateVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.StateVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.geodetic.StateVar_0_1 got {type(x).__name__}')

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
        assert 1240 <= (_ser_.current_bit_length - _base_offset_) <= 1240, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.StateVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> StateVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.geodetic.StateVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = StateVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 1240 <= (_des_.consumed_bit_length - _base_offset_) <= 1240, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.StateVarTs.0.1'
        assert isinstance(self, StateVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.geodetic.StateVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 155

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$gqTB0{`uuTWlLwddEqLq(&4iQy1H^e974H+LR+Pyo*Ykmad(wQ^sCxoMe?`6LLh3HN)_hnV~HO-GYlnvraL<vItuk*aA%p'
        '6v#sh^q~)aRNt~_&~DKeKlZIbU%EhnB3SgH-<kOzQaX|xDH{Z6GXlhOIG1zITz=pD&v(8v><0ey>>v7^Kl`cnR@JQ5<0VrybfvDp'
        'udLVAc&XBAv|FZbseSv{9n0uctd60+y46<uAN3c0-2YKOW(P}6r9tZxhPn~&R1KvbZ);noUNPhE>P@wwSS-7twyG-S;&&{?QeRh$'
        'SIxdHmF}sAskfSa&1a9jj{HacqOa)xp#S5(JyB9D%h1<5mTLCjrpgXz=3uM79ehz&>(ycN!lkNWDJ6@wSsQT|YC-!#N4Zx~nsG~S'
        'sPQ{n&5CBUn)>@{^;KG6T1unc*T%H*qQB^4Ezu%WyB5XnGY7S!ZRic%((h3_W?pNW`bJZ&zSOkT4b|9v(k4plx>c&H%?(TI7xUE0'
        'ieg%&2A!n7cGf<*$_rw<#jn%4TWl4b8vh^lU+LSkC2C`{su<Os1%23Ar$d`)=oO=7s+Cr=+P4FxYOB&;`;QTy?^R8eo1MnGYRIj-'
        '@{X-c+0qnC)|7jy+*V9et;(j}tf;ctYN)beP!)z^Y{?D!+O%Z7N!vSHTJbO|6w9g5mZ5LZ>X;r^<BQH#>;%i}im5Khx+z!HyL3-f'
        '<+f@pDeZP$uh8w$YQ|+&Or>KOten9vtfr2shUr4d>#A(1?{(<f(C&AQR%2MYIk<dIVRC~SrW%W~sjALKl@^t2w&_6i<_0Y_?&)-F'
        'PE&NJ_Ang<HSV5L@2ISmR!eTG_t<HokGu8OeYbss_1WAKof7%JUZr-b6@}XPTsSPtOLFR+Y;O0NrOlP~R>zW4seD%6QWe8ol<#YL'
        'MPsYlbmgqAxO`2{Wt=j1>`U$L(7j{G_gkHMl`5hdWVzF9suk5V6+^FYxlN!OLDnsE&{{fev>UaSU6Cx+YH6*G$+mK;r`6RC6(K8B'
        '8x^c>>U6%E7Tw2k#n4UNjJpSOy-xRnURk<+?Y10iwk-L@8w)bs2~9ee2Gv(l47w>gZFatv<@GIsl-1Z)w(2d#xyE#%$Tq~ChQG=$'
        'mE2&>-=K|6O{v$}6=t{FMqOQUHg~JIs}4_8L!|}oJ!%cE1Kku?EOuM4b6~KwO}a2LokTO<ClDrW>3XZlFtG;QX*1e+<SrER+C}YB'
        '(Z_hwuDIxoy>`2J`+GmQ-PacE%WtYiORU<t-{`urv+-`Tb-x+!+o6)vpuT;M8wGW<O*b4fX1h#+^onzTDs|o-Eo+a{Ay?Q^W)5FO'
        'p4Qv`M4z?HT<@%__RJ1DSX$q5EiOBXm^QDawWSUjl&VUV5>9Hh|Dioux~p%h)e^f<CB53eZBLcVR>!EQw4$z-+6tKqdyFM@eZ6mw'
        'uacGDTxCl?BJ<>bmJEm1VrG4$t@rKl^{qBts~c*g)wj>IJL?2)iR^u+&gvUlSUQN1YglQ2cCPyN`F)LRJQ+{K*~#i#%$&`XG{vMw'
        'G5kvawErPpgnzv40?%rYSq<!NA^uwiSp#;G*?mh;D+H`{zh%6;<Pc%*sMEP-PNj6GSlTYasDM_z<Jthn1Ptq;FPgrg5o2^#TMaUB'
        'RaDIG*Yy^aMAnI0VTZwcv`x!cGTUlJzpL-K&*=g2t{P{yc)d=i=rX@ghNhbi+7iF_?a1%x*2~WKJL=#jwns~?cHfo{D#YAsthea;'
        '&{@4j*9%7RdqksRwT$5-C{(IwgnwWAp?!Q+sWRKRXCqBvYj1bzbu$0rS}psteyo`9nd|f*Z@VS*i&AHuj<caR*<+0|$|lQ<u}2%-'
        'Ev(R@pY7-C6-SVcvUH?Z4B&f^rT$(qgymycE+HMq@-Rz7z2XG6kFZqg6_2qr&?`=2`{OK~=oO<_KgH5uuQ-izW>`AiE6%bs+AE%5'
        '>13~XlBJPe@f1tLz2Y49KaG0lQO_Baa~AcTW9gY*@jOfCd&Q?%db(GXSvuD%USR2|UhyJJPxgvWv-Cu-c!{O6z2bLRI@2p&M!T-C'
        'bgEa3p?wQ1J>Dx`MLVBi>9JmM5$#>V@y5~aXIVPlD<;tXBumG7#T1Ssjq{Pg@i^CYv{%gGxR!B#^Ekd0_qrFKL;71te;euZNPh?E'
        '?;<TAy@_-UsfKhD=>wz>k$!^o5z<eQK1TXE(l6ZfmgGlfj%Q*#ljoV6JhR3#8qaL<%mbcz$TOet%p;!plxH6E%;!Aw1u`8{cl1P{'
        '=Lj?HShmg#J3Vp6t)bpruzl>oHBgy5<ZAqA;@Z`&P|<>R-BIe&;Yy`v!x0L-diX*QS>iK?Es=E36N@}+kH1LL#M-6BNeL8438b_u'
        '59mTQlnoMv9VWw{U(5P^zU1=Ca&9G^OlR`BR63bmPUMrBY-%}^N-w9A%ZW@nn_FJVCzcbGW>eXGCbP1V%dX^ClFOOpTt30}N#zpD'
        '`9y*gU^>5?OJwsa*=#<SPA%th`Q?0aIhoBQGHhu&o6My1sZ5TF&!khybSjt6uh7?Io;J>Bs0#W|q_gSeY%;f!&n2j~WFotq%Vv|Q'
        'd@8Y=OJ%Z|l|*7Ck<PEAQ?zp?u}qcavx$6$HcF>gsBBhSI+f1RR;g5KC6iC)viU?ln_Wp$t*JB}Egd2qdOnp)B{IoOW|<D28k?rp'
        'E+_MemE=llWhI|arm_iYdm@!f<}=AuCQs$&@{V+I?r(_{0?y}xExlzZRb6Smz56!*uRRw+`)}{;e;sFkyxwYVeA($Af+nL=Z0hk2'
        'Q4n`!Mf?XOsqR#iIyV73`o!K<{06RKu%S|aj;^5g&z*HeyY{1gZI;ez?HGNS+Vu~$8@II=w3{*QCGGdMqV}?OOS^54n55eS>@t!j'
        'hkwAH8D7fW3S7JMAuC>cO<Qxd-CNo_0|{6e<TiE)zXAzA?Omq#v^rh#2K_e=RCj(s-36fT0#J8;LEZVG?gCJE<4|`2sJjT%odk6k'
        'fV%TR-5rCv3q#$FLEQzQ?)*@9vru=_P<K(NyGf|K2-IB|>P~{X3qjolpzcPX?tD;pPeI+Chq^llb$1r(?hMr3Jk;H3sJl6+yHiki'
        'C!y|6K;6wk-OWJVO+(#HLES~6?v6v<O+wurgSv}A-AzE<g`w`oq3$H8yD_M{5Y$}|>Mj6vHwtw(0(Iwyy7NKZ6`<}4P<I8Wy8_f*'
        '0qU**bytA8D?r^9pzaD#cLk`s0#|nhuI>t4-4(dHD{ysJ;Oefx)m?$By8>5t1+MN2T-_D8x+`#XSK#Wdz|~!WtGhz4qkV=9mvoX+'
        'A3pM|8#?PFR+yv6y05CP>#W`)1|8pmY^sV}SMRBHId<#L%L`6Nl5KL=*`&=h4RflnMM~3Bn@uGyv(7qmDagDg=3=_%I=iS4=KfHb'
        'nTTn>)_zqRB{QM@PwgknWCZD>v#-gpM@eP%?VzKxm}|gQTGaO+YOTI4akbUACmp>-MkFbi5&Iv$i;ZN*cTB4HIho6VMS1W@T6B(;'
        'AA;*iY#Gd#Lw)axM*6VHJWEt{MRSjTlU6ueur5DN%Iz0!a4!=pz@#p}Q*K?^VqQ0AE85NE&TCe<`d)|5EtSm*xULwMYSLqowN`aH'
        '|MC8p8NzpV^p8(mZ#9|UrMYiM+a7oO*@oI=9_%NVR(nX-$N5tGIpq%8ejhXJ_sp<ohCMUP%<vvORFkpMB{sTGU_*33jS3E^kpmo1'
        '64)3M98eQrV+3qS0vqFk18Nd%NMK_GY)pfVV}b)}6l~0ajaje}1sf5tA%Ts6z{WYSF%LFQ2@a?!urUcXCcuUSHiBSd1Z-Rd8!@nP'
        '8Ejkv8yCTb3^vY#jk9259&F5kjgw$w7Hmv|jVRcd1RD{s5e6F)*a(4*0N5B2*x(MR7}%Ht8xq*)f{iZN=z@(d*yw_dF4*XTjV@=S'
        '%h~91HoBaRE@z|5+30dMx}1$JXQRv6=yEo?oQ*DLqs!UoayGi0jV@=S%h=$8-J`*y;ag8b?L3Jr_vx@rJZwLK2cN*h2zc;;hf#rt'
        'QSdMV9)jS(2Oh%UAq*ZO0uOw6A_5*pz(WK)jDm+Kc#yz@4?IkPhcI{;1rKxJVH!L{z(Yvj;fydmF$EqX;9(3rjDUwr;6VltXTif9'
        'c$ftbQScA}4-$9?fCnFVSOO1M!NV2sa0xtI01xNE!x``}2Ods<hiUL|96Ut8!#H>dfrn9nhXi<tf`>Kma8nqbh=GSW@F0PQZSb%S'
        '9=5^5Hs@iR^RUf%*ycQJa~`%i58IrFZO+3s=V6=ku+4ec<~(e39=16T+nk4O&cin6VSDG(!K1;W;ag7wcjs^?1{|>add{B`Jm(4v'
        'XNiBmqgblZboM>aac-YEAg0YQl&!u!`yvbEaH9aOu|>NB$&QuOy2_%j5aBlT!pl3n@b;B-CXvdg(wST?ozJH7`RqzQ$vp4Ld^(fQ'
        'Fh6)Io5>{LbY@NqrL9zSYpY)j?C%Wup*{VI+Ey)n|L}s5(z|Te-OdWR=bTheetPoLlb_tc1nzHcy}xU8XDs0J)qXa5@aRtMBy;AT'
        'q7OUhn3}#lGc-0|WoW1N7gU|sJM{4M@D%WzXc;;^UzHsaz#UwveZY|Uy!IZW^{1l;4Xo5YV66U>eLP?vAF_`>X6PPcF);fLp#0nk'
        'JvCZxrA|aL8`@yOJ@S1`HB=0Txbe0uzuu~Dxx*l`Vz6-`C-mG6coesF2cHJxCeMY}++ijb)oNJUqWlK`t}3RrD8I?SR-Jg)Ll2D{'
        'ZZM<vC;lCV$Ln}_9glB)$D?*U0Jqewf?sQ}kHbHTeZr$SC=d|@5xxWBW+f020TDrgh)EDJ2_m8(!UrOPLfq^L;ZZybA|w!T3PeOe'
        'gdarAf{3s{1dp4Y1Q9_HA%loH5D^6t5{U4DhzlTM9z@ItakD`Xu?QkA3y<P?5HSlPCP9P*B1S+&3Pdb{h!}`?8bq825vM`KEQmM`'
        'BElddC=ekFakCPLSOpOY5D^6t4?)BO5U~j&G!U@{B5v-9n~iZI<~R`&h@d+XNH{rdklP&O9t?612f0rMxkrQCr-R(%LGJTG?hBrC'
        '>2PubFO>&}2ZslT00%^C(4CSbdaP<6jY5*eYJbMm>(E^k-RUk0=CavD2F{?`pVOAb6Z`7E+FuO|{A+i!-5#GPJU+Kp8LX@RBWOFn'
        'pzVAIXgfXwBqV6N31J3E=z!o9uI-KqGeCTRH3V2E1#LGWbSfjl43H_n8Un2IfHewOLqc%M2|?S90#+HY&IvO>B*5wetWN{hvw-yk'
        'V4Vc4V}iE33Ro`z*7HKAavHEk0BcB?0g?u+alpC&ST6zArvU3bU_Aj?qk^`(DRe5!LU4)<Sbc!?Az*y~ST_Ny23XfPtT*?}0Eux}'
        '=eV|$IIF7zR#ykCt`1mT9k9AOV0CrC>gs^i)d8!k16EfDtga4NUERUzWTkaaF?1FrSn3!SLA&;^)F*na%_hkj`i5r77F)ehS9uq1'
        'xCaZ5GxSYo`stp(x7-<ZZa?qs!BQt4O^&fX;{w(Rdpk2Q>u&E;VF7z?>>c|X^h(`Xt!()|Rj(m^1L>OwEf@BEX6a~uPT$pa&$HeC'
        'ApFMe@57QC@1*4Y{u);er5b)yC}wSVoG5nJclk^IsL*#(RP3(Z2636SkAq}<|E)F^^7(3i89ch{Ac{FT`*;t&Jc|3MJ@l=B(?j=r'
        'qRSIqp6J>~bk+VQ$UE%45yFE$nqPUMtB8jr$Q;pk9un}F5by{C4+(gL1(_2ReCLq^Cc1`zha})JElhL`3NnZL&cncC9(YJX3~m^B'
        '$b!uA33yBhzVmtD5dj`c0v<EMMAt>&Ap?(D;2{Bzw1CGs!G$#@OmvL{k4wN~UXVGG;5(OviLPznkr43Ego&<_;KKTNkMF#^Ck9vM'
        'GRMd1$Peg<4d|E~&>?X;ieGRy*5}-f^_aV{KILw#N8F9|33p>X<XH4Zc6QV~C_E@UC|oG`pl{om|9o&n$+J(K^jzVSR^qST*G=p2'
        'v$GeEQtTni6oX&xsr42M9f`lLR;-qhenRle6C4u1N&JfIvKT#_%VPAPAeFM#p#QJ#un>(_NHAKG;IIe^MoV;9Ou%S`V6^;#(Tc!m'
        'NibRg!C`R%Mr#^I>$qUF#s!DPs33ID!)ToqjMf~C)=3zxSs1Np!DvmwXhmSO!Z2DAj8+InD*&T4A~-Cbh0%(`Xf45LEy8F$1EX~n'
        'Mr%PZT32ASF2iVjM{rm?4Wo4tM(YBMmJFjc2cspyXq5$rMHxn`45L+s(JI4em0`5XFj{38tui-S<vm8L%#Bu=8?7=Qj4JcNs4^dn'
        'D)YgpGB;RdZm`PSV3oPSDszKX<_4?G4OW>CMwN&5D(cKZF16_&Zx-7bu=0yB>X^PUcBp_AiJOPM9fg7TN&zd?u^r>a9;zOy9;z;?'
        'p*lU#nIKrOFTU(#WsV$wb>A>tB!1AlAg=6<XzkP$qvSo@J&WO4jQ?L2W6FIm%t250zm@3O{k(Ljr+ZYi6aCs}^q@Y%bN!~|J=Z--'
        'JxcdbItH}ZgZ;)eH$Qx`yTftLn?u-yk%OW`W9p`5=uPVQFAQH3QcE+!zt2Sc$#MF~N=F%yvd0H*gT6iKI1cs;YJL7z%NYoxHYqZD'
        'O>ot17fF)z4cTlf{GGhi_<dx`*FC89FJAY-Gc%r<*<ogCe=m8np}jC{FAUq84ein3(Xjt)XfLqT3oP{lOaIRXmj2@F2`qg=fau}k'
        'Lw}<n(XSLL8eSXrl?Q(;uydcKZW3!eYcA}K8jU#-qYKZPPJHKnWv<DJ*gJP>+GpvLgGggkk<$jMXrG;j{rB&NsW1K#>%Tu@xtrl5'
        'MU<YVKEFN10|~y7kWzVk7*gu#D^Fi}`l@y(%wtHSEL<)+as(nqzl4a8@csp#K!hX^F)9$@7yMDjh4(LTB77j?q(H=|5Mq5?AcDWg'
        'bs9wY1x4cn5z`=IRPaZILBvH6aYA_i!X<%-2#D~3hzlU%B#4+0h`21ge_>h(u}%yAs0#uS$A$N}@*hh{fQT4~kU_+pplG;1$|r<a'
        'CqTp|h`1>b@v-p!g|hG-SD6#x<3xPHiTIoo@t70wDJS9)C*l)M#6wQR15U&yCqm;ytZ^c4?)kBl7$;(m%b4h{_)!lC4+sy4VISOb'
        'gEM!&i=@DYGalFeeS-AdwXvg5D4OCw9kk!j%?o!_RdzOTegLhiT8dsb*^eT!SCg<`OH(&3)%mqU%YEmF*pH~F=GQ-jb2>B}!tr9v'
        'y%=*Z#vC!`we5kH{5U{Z(8uAi2nbmC516hOH~<U3@S6aW2aIj<>3SjIHvuF8iwOaXabPhiOxNST2`~pNCJ*RcofF13&k57@e83_E'
        'EGC8D1mKTO30RyGu$TlE7lj|*<5)<*;v%q^02VR9JI1H$ofCc&U=di%0gC{zSOgZQh2B+47~7NuEMmYy6UH_-frSJtR)NJMVY=R&'
        '*t_cP`Aq;H$Ks1UkIsku(W&kE;XR3a#@hRM#u5Y1Sd@FliofDm{E}nwcN~k413UGk2ZaX(hhpaqvfmg7en{t^w5i&!BcwNec~oUJ'
        'GyKK#Z^E^vl?LOMd96YJbdzhJ-KK}ae@^g+!ee&-KMo954ZsjruoDvhU!9BuZ6|&J00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
