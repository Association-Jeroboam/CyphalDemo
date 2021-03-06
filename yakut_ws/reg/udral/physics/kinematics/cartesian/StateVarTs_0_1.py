# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/StateVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.269991 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.StateVarTs
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
                 value:     None | reg.udral.physics.kinematics.cartesian.StateVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.StateVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.cartesian.StateVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.cartesian.StateVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.StateVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.StateVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.StateVar_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.cartesian.StateVar_0_1:
        """
        reg.udral.physics.kinematics.cartesian.StateVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.StateVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.StateVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.StateVar_0_1 got {type(x).__name__}')

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
            'Bad serialization of reg.udral.physics.kinematics.cartesian.StateVarTs.0.1'

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
        _f1_ = reg.udral.physics.kinematics.cartesian.StateVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = StateVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 1240 <= (_des_.consumed_bit_length - _base_offset_) <= 1240, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.StateVarTs.0.1'
        assert isinstance(self, StateVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.cartesian.StateVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 155

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8NVSAw0{`uuTWlLwddDe}qDGV~Qx`joe974H+LU9_yp!5CU1yyQyk)GYv6E=C-H=0atQnf*uroth3L1cUXyKqlOCT)Z$2|IR'
        'AN{Ders$%(z&_MKAKL8&Fp56x%c6cLu>H>Pe@N<xilro7pv4dn&*5CoIdl2_zwey$&8Y4F>)$jz&ZqNAbGKquYSDtFnz~ZcKUPXL'
        'HCiYe^`>Fzw%Y5QxMQ2GvfVP(ySq)b_jzyS)7~e&NN2LpQ0lZkZmL_+R>f3m(WbU*>18W=UvH>&#b(*EV%n;uD~;$KTd~#m74xpu'
        '>qv!d)wFb@(bGJgsrQlpyqEXnC;q(mX|FR=P;A@OOD)>D_Y<n^kaiBX>UAdH($!jJ*uG$)qS#8oW{uXo{e{|O=R!-_E>m-Cy{<;@'
        '>^91pX*BeY)yiF3VA)E&+0&-9>HI|A!&;)vQtes@yDuKrj;5*Cbz9%2b}YWvu=K5lTKQqaR<~4h|5=+UlytjLQyW{h*30Lpm1V`U'
        '3w5JHtvuT~y}=7&yG3u(y4!3OotlY1>%H6SEETAYjf!GcMhp6^RiZ<isq1Cau+*~AsPsDiLd7WeHvhxx@!Zu^xzVbZR8uzY$s=1?'
        'vaKn$tSQ^7+*B+}t;m+%D66t%)KytAsR~mucjY?$Y}m5ipzWP4?P!n{ise+OVd`77I-*C_=rw06c7o-SVyP>#Zpjt(9^Dibxv83~'
        'O0!wh%XEJjji}6uDYs0Ml{46d)zq@oAYCZAq{^oHCoQ@*wEI2Ns1HlG2A9t%Os-SIRP&l_sj9P4*`RW*CLO5W*rKK8wob?9G(~r6'
        '57JRk<F=JrOJ%LJ4Y{Fiv(rRh_iDz2e)|UN)0tH|CGrEkLhV$`3bpaO!JsU!%88HCnf+&$HdjhU%a#*~Tw2~$71O#VKhX5D##S}y'
        '%GtY7`3*Ufa>^Xpm)hN;d&iU?7_C}`Dxw->xz%W>W!172Q?Kpzn?N^$tlQS0wRGBOH)<`rB5A7C){K_LwsNYc)s+?%AuCiH6|C;)'
        'biNuk-N$m-)GghL_7CP}jqU}#yn6GEbve>7Z27G>S7f>q8gwpAs*j+io1)cZ=PN6hb_r5eV^i6!8H#g_=|Yh>M4g7;<(EpXv*vHn'
        '#+IhkYU~QL+ik0+t~#6dtGK5QPgGr{1^s)}9$W{yDX!S;wqWPLWNRCAVPraqR<uVT%yp!jMuTBu54h77we!eb$mg_++NHdQ@uXep'
        'qcip1dVc+#57v9yO6T&2s%eN-JNFx1H+DAeH;f03Xs;6}I1TD`&T&ytcbas=F)`aG3DUdH{i)P=d$e?Cnhv?lmNGef3wc`KnTYjR'
        '%dAqXq;?iZbg)p`?Mp5@iiozXCAHNS2}(t!N(m>m()+A4SGcF|sFeb{PzAlxTkp&lETd(XRa#L~3r&UOqBF&knqKO4rZ-6DcQ)A4'
        '&q<ypu9I+R2GezKQ}1<xH+P$Kt=?4YMz3?G*(wpZ1rq#Ljny|)SUQM6Us!2>cCLDz^JB#|8jr@J>}2(9CTEKUO|hs^4F3WE?R`cU'
        ';qTV_z_S`;Rs*|Rh=0Q*HDD*1-M0j_LcrP&4D<e~LxeR_r*qAmO6g9qwS9z90Y<IW*8oQXhV{@7P2bXpF*>V8odm9eirM{IGN>d{'
        'C$7Q{gWI%?VXj(DwXEOMNA7bn5ckz6)8bN%PSIt4pA4m&4%!xf_d2uR*X_5R-*?o(P2BMnjApMRA6AI9TQ3=Oedw&-rt1Y!e1~XM'
        'Y{MLypg^Il5&k{xk2@zflnT?v0~=`yTf5$>)kyxuwOabGdXaptYn8~5H~S^@@=~ir$641K%&bvH*<qO}X4>d(VTI-=*nXaF-iy@7'
        'Qg1i!$L~p&PIU7DET6)13F$PJ2U!~E=4Y_|EK8+s{sc??-TWN3KgrUWZa#$d^DLe0<`+=TB1;##`6ZTyy7^Nqo$KaLvvjtbe~G2R'
        'Za$3tUq-#lsOJpIIg9$vvGhzgf1ahw-TW&oeYu;LSsL!<FR=8bZvG-mPj~aLvh-9pe~G0_-TZf0y4cNMM!T-CbiSL9pnWSWJ=x7)'
        'MLS<(>4|Rs8rr*x<Bg)-*I7E<&BxIGI7_Fx`2>z5iSv=d@i^Dj*Ue{eTv?po9FA|Tf8F!nMf!V4e;?`VNdExo_mJK|dJE|$QVr=2'
        '(uYVNA$^SW3DPf-K1KQr>GOViTbe*7%rg<5$??oBp4sFXjc0av<{{5K;+e-h^Mq%<<e8^D^NeSnBhw=9jw}M%5hm?eR${_V7H8TX'
        '`kN~q4>Mc?FLT6Qy?#vZy6?QgjTW5Okz%7qES9XpF-m>y7^NPu$ZJO~l6;>7WsWV9_W&$C+9E$N+SkzN2V_6qSIeYx$pbxrkq*F_'
        'Lpma+sqB(_{uZ;oed&IKE!yw>pD3s`mATC5mYnTOzeO&Sy>Bb>P;QWilF+U^q#LNNY*8aytb6eKW_rToiD%ccnYCm*naX7n$#^;&'
        '%f(aaL^hR3W|Q%3ER{@WvTM0mHb!YWk<O)3YipVGT5c_#O=UB=7~3b2iDh%K7<s12Ts9L+=ho8cTqc>wW-_^KE}o62Q?V3VnoP%2'
        '$y_3pq2g1?L_C?u<Z^5DGoGW3b1ABV{$j~=GMkQP)^eE`)fSJXvzc@{p2#I)*-RppPOZgaYq4Z*Et#O5Q?V>nmP^NSDcUHRT%)pC'
        'ZOKG3Lt7;hiM3QNo=N9oxpaChNwp@DbhLDcbm+N6CJ{@;Q>iQ+JT*2+t<A=Bv9<VGVr?y#izm`CYI`h^iRV)BL@Gz+W^#^8MFwh`'
        'x?4@9tlPW2yia>i+w2>(A8Q|t*u8~!)uw9e<E^K+aG&j}Xj>z;@J836x|ZM5>h#w*)Yy3hW9Nmj^T62o1Y_revGc;%O~TlDVC;f0'
        'c0m}sSr|KyVC-gL?7T2`voLl(7`qURodjd&fw7y1u?xc3`C#nAFm?+tcC#>c0T??EjNKW**v-S(&BEAC!Pt3W>@LCB$uM?jVeG;%'
        'c1tjJAsD+^7&{5Z&JSbffw5bKvAYUmcLm1o5{%si7`yW@c4uJh!Z3EHVC)uP>`ubi&BEAC!`KC2?0hhG9vHhAj9m!EZWG4tmSF56'
        'Fm_=WI|;^a55{f}#%>SBZjT$gJ#OswxUt*g#%_-ryFG5~_PDXz<Hl}}8@oMj?Dn{^+vCP=j~lx^ZtV8BvD@RuZm-+YeufOUaFcbF'
        'dZT3Bw4b+1iuT4Qy{bj}r9HQ_o1bZKu4_NgZbh^oYJaHZwYRm~+Iq)pQJ2HdM47r17~1G8jR^Dp-h+1MGgkO`jLSS%one*UXa1=R'
        's0*kI=n&BU@Wm*g|HN4N^>{!#KJvwSok_<VV`B(?f2`LD4n4A7XL{h1^*VEoS4POj1!y~0Z}P3=vSFCigH$kxq{vOSlhem0OHIA!'
        '7xDdx%eTw7%lARPC1(o9nPqVhAKM#xMd%GFY&<slM=j#fY&iQK+85IP8@b<BCy2p8??p!MrRry7zTUZ#BzHVV{fA5@nM)^fIqHnW'
        'Sx+UNBey=q`VEOR^$OsmS0&ml?;neOb#72mb-usZeotKHo_L#tp#2p>APzhEgkdM|A;V4*gkVY-cA9|@cp(ImAOzFGu+tobK!Ol>'
        'Ap{E$f)m29lMg}=h7c@42tp8oSqOmyA@B=Aa1KJS3?X<)7<QV65X?acW*`I-gkTav;Dr!eg%Cs_1eYNMmmmZeAp|mn;5>xjEQDYg'
        'LJ)=!oQ4oAK?oKg1R)5)9E4yNLJ))yNDzVmguo9W@Crh}hn*r2f-r<Yf)KPJ1Z@aG8$!^A5VRo#Z3sadLeS<y(B?wW=0ecsLeS<y'
        '(B?wW=0ecsLeS<y(B?wW=0ecsLeS<y(B?wW=0ecsLeS<y&>jkb|H01g$NTL3-*`Qq>Id|7m@i&!5na`7`sz$NlF;ic4n^T>`Qat+'
        'h@E!vbn$fY?Bh9On7Z1ql@U{|GD;)Wb%xBdYTQRGzC-!eSX!&UVyylP`}$Y*^>6I!-x<0m*huRb|NDio?i&v~b<=3D`NhWA2_-hB'
        '#^#euwZS4a#-jh9u8Z!v=&p-C;-Xi7PB^O;@o@XbgjQ!?M>mEZ!5B^oL`;GR&mmK!5{Q@u5t9NDb0A_4M1(+u2SiK?Q>3Q^W4Ht&'
        'BoOfuh?oTt6Ch#<L<9vQ_!Q|Jh?oQsGKdI+h!BX7K!gWGTmTWvAYxINBAo;g*FeN&!5A)sh$Rp)2O=a8;RO*15U~m(A|T>b5OE$v'
        'ybL0iK*UK95d;yF0uiz>MJj=a4G<9n5g`!q2t+&t5j!A40}-1b;?{vF(g-Ia%!!ad1l^H9!pUia+|D5PaFBa6$UPq9o(ytd4suTi'
        'xo3mibDrzd;p9r(Sh#SwaJX;?aEu$ieetMFNEnrw%%sz?)V?v7Q%4(fIVFs_gfQlEdxOEcF>wsvZbI<wJcsypJlH27_;xcwuunjM'
        '^@QNtoe+Y3Jb*O-Smy-aZbs<V%?iOj^MEw~SeF572(ShK>v<vAhx>Luz$ydQun_Dc0ag!SeHE~t1+1q4>l|R65`4R>fb|k!Juh_Y'
        '769ukU=0YtK1skD1*|K8^%7ux1+Xpy)>D8rB=~l>gl=6Cu-*WyGGO%p)<=N#Az<ABtQuh5<gng45bP7-u!gyBCvjFc2CQxjSlt+~'
        'x-npNW5DXhfYprws~ZDWHwLV33|QS5u(~nA>Rj2_R!m)Kl+{AZv<ceHUlL01HCa5gsc&hvY_ru{HI+?*^n;iA9&%lwl{-$P@qy2e'
        '`@xg_fZLx8mO5QBIZ`qzyDL~H?(Ia|*7}jtO3h%wlsme`)|iHk#ZCY-TRf)fO{70U`r%>Ag?(RJJ>Dm{Df5ABw)>w3f3*Miu;ltj'
        '33=S7e$`Ye!4HLEHiyTFV)y-)U-+RyKT1%s`*!OMI`1Vv>FhsOe@RKT>_2|zJ%r$^Z`OaWe$NN>u700#hxO2NKBtF1;W}Ne)8#r{'
        'W1OyP!_PbHT`%E5UyZLF(=6g432u%!dL0n(m=W*@0uKpz1O+!|QW(9SJtU?%06ZiCj|Cy7c~Wq5_~>;Icq{`C33!|V9zozC3vP}_'
        'z+*-jy<P?$v%q6jz++K}X}$(LWZ<y`JS5<e6!17F3}H<PG0jonaS3=V3vP}ij9$w^Omh=>!~{GvA*NXphOoXkFnV3&c--K4$lT5G'
        'a5{1WIwAu)!UH-aPDlPZAI5sdhq0dWVXQCtFxC@3jP;lgV?E+nbiJb;br%X33Kxn#6nxsX>BPAo9(!@r;QqT0bjv<^82+{66nn%n'
        '#W0a=wPvs|>gbC@=Koj2M0`gZvhW=iCQ{Vu^!N1#EJV=?2%;qk0~V8lXo&+BGZ3u+L~BA2tyzec1kv&f0~V(sS_=@ZlY(eX3j-ED'
        '!O=Yr(K;)LRv4mn8ltrX(OM8hYYw6{3(*Qfv?PdD0HWoGXnBPJi|Y`rC`4-&qIC_T^%_L$Dnx5V5Unc^t;-Ot?+61HuR^pgLbNVG'
        'v}A}@7@{RXw2H!jMG>M^glH8ZT1ALf5u#OuXcZw^MJ`&!1EN*rqE+OgRpgUVMLro-<dacFJ{eWyf>q>#Rpf$I<bqY?f>q>#Rpf$I'
        '<dadwp<acYfbBw){_qg_XvoN41gK+rCUB&X5sAw~uM_$vq1%@OBlE^CsxGQ7s(n-gH8SYTAz0~LeA~&&96A1$1~&AE$M6q(xbVus'
        '*w0o?F$=D7cNN1`jQ?MXF>fjra{3Rm?#2|^?%y8Gx`#xa=vDuc_B@7N4^Fvu-KEr}^Z=z(K#LjnH{a;zhnBrR9mkBj^O6@?+37zs'
        'wcp&!5p~Bl^#*nPSE9q|sNXREeUW`VWvu^K;P^9AbIyptxaYZEzil`(V9o<v>{U>eeuKytNxs>CkZbS?s4@P@w>_Knx!Z4W^~Kef'
        '5q+s{PhtAXjlXu|uif}-_h|%|2A77fdLe)tQR+sNx)G)Smm*64_S=al{l<Zz-zYltYsH8LH;0|%!G}e3j#=7IBK7Om%E55ah!ZNh'
        'a@}$QJI9r|DJx>P+^K2I(yxvljZj5S8>pf&I}bbV(lqtIXIRI5m*u9XkKb{h=Me<IlUUMUO$}p7UH{7UuU!ACx-`v$M?)-5F62E1'
        '5xy4?5fEN|;1P(B1R{I_5fj3A)Jfsh2b>5Gh&U|};S*x3PYOf?K*R!wm=HV~4~SR*5k6r&DhMJjf{0VXs}C*-M9hK+4~Vz`B2I&d'
        '8G(q)!mAG!gxKn&FdlV5AmSv52na94je&>=h>$@<Snz20c$7zot&V|+9T0I#AmR(*)dze$>IR6AIT0RC#B)x>Gfu=)PQ;g-h$ozg'
        '$DD{qoQQ{<h#gLZ#);VEMBF;?Lfi-^BFx>G(7wP?7YG*!7l>gW-0nwZj=l!O%ce7)Rv!n+pYwf<d7F9ucIa_aH$S+es<N|z^OF0D'
        'YAbrpV*mJp{X-1)MtpV0R-ON7VfSC8FZLtKs`c$p;rye2IECW|m%G8`Zg4q*%d4Lbe915Tgav&a9SgsJ#l#`c>G==AVggu5z+&!@'
        'xlR6@UI1A5frTVsF(Y6x4J_t_=kz3C5e61>hxD$_33Hq0gy-};z#;%F=72?5Fr5;xcuBxw4p>|i{<#9jLIM^SfyE54hzO%&{5idI'
        'z(N8R*MLPBSond(HDK|w(7Q?qbDOe&MFd!A!rbN#u#kYo2C#S{Jf{~HdshQ2Zg4C-9E;}%Oy?tRI<*7;TtVU^W6d!mW3j==Scs2|'
        '<$ukw_yxz}ryPqf{G<M)3xx}X3q>D_aq~KTpHlmKZNB;sGvs6a;<(=A;_yHD{Vs+RwZdSoHmB9;kHFS`woZodr$KHApEBm3`Uk59'
        'Vj!+yCnWkmI(|x!0C4~S'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
