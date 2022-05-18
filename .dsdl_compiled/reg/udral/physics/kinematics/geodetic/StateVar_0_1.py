# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/StateVar.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:36.102983 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.StateVar
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
import reg.udral.physics.kinematics.geodetic


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class StateVar_0_1:
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
                 pose:  None | reg.udral.physics.kinematics.geodetic.PoseVar_0_1 = None,
                 twist: None | reg.udral.physics.kinematics.cartesian.TwistVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.StateVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param pose:  reg.udral.physics.kinematics.geodetic.PoseVar.0.1 pose
        :param twist: reg.udral.physics.kinematics.cartesian.TwistVar.0.1 twist
        """
        self._pose:  reg.udral.physics.kinematics.geodetic.PoseVar_0_1
        self._twist: reg.udral.physics.kinematics.cartesian.TwistVar_0_1

        if pose is None:
            self.pose = reg.udral.physics.kinematics.geodetic.PoseVar_0_1()
        elif isinstance(pose, reg.udral.physics.kinematics.geodetic.PoseVar_0_1):
            self.pose = pose
        else:
            raise ValueError(f'pose: expected reg.udral.physics.kinematics.geodetic.PoseVar_0_1 '
                             f'got {type(pose).__name__}')

        if twist is None:
            self.twist = reg.udral.physics.kinematics.cartesian.TwistVar_0_1()
        elif isinstance(twist, reg.udral.physics.kinematics.cartesian.TwistVar_0_1):
            self.twist = twist
        else:
            raise ValueError(f'twist: expected reg.udral.physics.kinematics.cartesian.TwistVar_0_1 '
                             f'got {type(twist).__name__}')

    @property
    def pose(self) -> reg.udral.physics.kinematics.geodetic.PoseVar_0_1:
        """
        reg.udral.physics.kinematics.geodetic.PoseVar.0.1 pose
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._pose

    @pose.setter
    def pose(self, x: reg.udral.physics.kinematics.geodetic.PoseVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.PoseVar_0_1):
            self._pose = x
        else:
            raise ValueError(f'pose: expected reg.udral.physics.kinematics.geodetic.PoseVar_0_1 got {type(x).__name__}')

    @property
    def twist(self) -> reg.udral.physics.kinematics.cartesian.TwistVar_0_1:
        """
        reg.udral.physics.kinematics.cartesian.TwistVar.0.1 twist
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._twist

    @twist.setter
    def twist(self, x: reg.udral.physics.kinematics.cartesian.TwistVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.TwistVar_0_1):
            self._twist = x
        else:
            raise ValueError(f'twist: expected reg.udral.physics.kinematics.cartesian.TwistVar_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.pose._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.twist._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 1184 <= (_ser_.current_bit_length - _base_offset_) <= 1184, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.StateVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> StateVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "pose"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.geodetic.PoseVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "twist"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.cartesian.TwistVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = StateVar_0_1(
            pose=_f0_,
            twist=_f1_)
        _des_.pad_to_alignment(8)
        assert 1184 <= (_des_.consumed_bit_length - _base_offset_) <= 1184, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.StateVar.0.1'
        assert isinstance(self, StateVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'pose=%s' % self.pose,
            'twist=%s' % self.twist,
        ])
        return f'reg.udral.physics.kinematics.geodetic.StateVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 148

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$gqTB0{`uuUu+vke#a?Nq*fFyQL<z+vSY6upG`Y5&Hr5HdOhF8m%7;4$DY$vahi}Ta;;g0B6+(@TXLJ0LD7Sf5-5Re0RusS'
        'ycBSsdVO=z7v7r-^sO)MW8ZuzaM$*wE(#Q#;eLmdMv^Tj!2#_p0r@xkZ+3RMpYQzUH$SeslYjBWN50{wce=e*vuce*+0sozYZ&*n'
        'wT7N3S6dtHmSxzw(>rp@Hak_jW9sj0wRPun=i(>M$4<N#EH||cx;<g)>xoXy)EbF4*|LnPmH5bL>KmHPitBo-rqfd5maW<PyPE0r'
        'r1D+ew2W5MA->+!yC{F|s6KV#C(b8MZ>Fr-wrQ+&Y~6A`pr<;Zk)yqwUhpkLZ`8((3zut}t(9%oV&ZpKl3?%h;o4eiS;MB1DKgDl'
        'MIy8%B#Nqz?x^(A;VV64jjtcJMx$vzugZgNT-!7@4BNO%Z`|}-jh1Hb{$^*&YldBJ=*@MTIO<h;Gpm|qmpABX9kS9pR^o@V!xC@O'
        'Z8z8^_6`22^CPFXShj4fS<}qg&Wg5aJsaA3)37@=cH%pxR<-FjZ_y{>EtF{;tGNlEFI6ZO^2JOllU4HROe$AMDyeKPUC5?0g-oiD'
        '%w}@=LQzQ;lGNtXIVGDd7W28HQcM-Hg}jnv$E5Sgf|5+8m0U(C<dZq2n9C{oOuCTID+MK0NaeE0EL)q&rLq|%oz2tgvzc@%lg=wj'
        'kuIhby0em{r=WkyOfFN%rSe53pQL9?C3A&*E|*Fx>0}|F&gQbkWU`pdD8)>g9-K`U=*g5^QpwVtGMOT+o1HC_&gAJ{>2$i7RZ{t!'
        'l2mfJVuqeIouOAtFOgollFp}-*;F=LpchXYo1v{Oq?BYaRZJI)ijqp_lC<r~bUvkIQ|YWi>&+_;yZN0p`us=@`lPtGd9qw<Rp}jm'
        '-_&Y`*8G6&Fn;6`D5cb^Bu(<9uuT;5ZSO1i`d`6xqt#q@zXNjhpxZwtUhZgjt6DQ*8Ho-hB;hiX_&uYh->Pa2u0<27k7MqAi@$<z'
        'F}R`Iy2-vlA6=pKj_&B0%4=J05BRY|Zj)OUmCc&oHuWm)=W5QUz1i{|V^gn{+bz>B8#U)<Z@z4`I%ZX;8yb4Ktx-|zO)=9j)~F!T'
        '4#L<hv9+I55uUh0;Uz8B!}{BX(+j`3)h1fwn!eF;dMDbQwT4kG(|)4UVCNfmcT`S8?!!b6wCI78?17>yA;Z0+<A*AdN+c7kgK%u7'
        '+egbpvuL|ay=k)^<E~NFolnVC@;;T3wFa&EJnv7&x=wer#bu`#`MzPlJzTy;7tyoy0_9fQ>B$FGVr^}#wdiHhmfWD1NqZ~SC;YIj'
        'o0{D+$Nf{NTqOqW?a5|uuB6p!Mst17PUK^@^=79*FLO)WN^7{QH9ETU=T2O`+PBuIPttZPa#X3aMlW~6XtJ)47PL)Pm}1=@z1OU6'
        'b%Gt|>#Kg)0J9T)brQ=#W+(e<2zCnFC2XI@av0lZn4Rvc5iB2JHquvTnU(tL9M(s1{5-Qq`sxC+;l6s5*{Qy|i2asO|1oA4`|5FK'
        '7y4?9*=S#Vh1uD@x{ULjKs_gMzE_zI_0?0T?=-XizAEGVXP7<RSI;tgs;|Dr?5lnC9J43;>bICZ(O1tiyWCeVF#AehjWZkTs~4F)'
        '-d8U%d#ta%&g@cOT|s*<GkdhJCeZFH%+B}KB-)>1cCN3caUB`lk1Vby$LvgB&EvWXxW5XnuZa8g2Cnnl%m(}FZ{T{r!)&0h{wA*b'
        'ySSfMasAib=SE$HC9s>Y+prH{AHqI@eGK~q_9^T$*WQpOP>AtDoEH>cxXuf!yg+zilNYvm;Q=o^<b_AP@R%2#@WNAGc!olUdT#n='
        'TWby-b*x*n)?8mhYuKZH&c0?a*RQI}Yr1_;*PF6Ubh*)@Y9nvxT2r=kO>XFS^@be3aqI1iGIbM&yWAP>(q;~=+`2Pdr8RB6+0+s;'
        '(?#ZO%KS{Sw$`GHY$sYtf-194exEV_U2=*1Hu*mJSE6>vho6%2O;RD%IH?hx+#&0P^a4~d>1bi-TQl)>y=$tjWB-~uOWebDdb2|x'
        'o2q1LtdpcoHL>@z-@;DvaG*r*%o{RyyH?~;@4qs<MBeg5_#N8lmRZwH*|6j)p<@Dik6JQ4b(Of6y-7C=_n>OT@5Rj@T$8E4ynzZV'
        '<Gwzux1nvdI=Ex>FpH1WSmpYUJM@;)x>*HpY9{Tns0YGYOK%->+#T{`Vh{C@+#~l#viZlO()}G$y7XqN$$GZtzM9;db|sni9Bjb$'
        '{Mzb1>X-}{>H%6hX#YQPoAwi~(PUelpikVV)XDjb{{5LJ#GVlUx(PA)Ial93c<2^mqf6Q7K8Fpzz(xRU_`!x>V8ahKB(O0BHYBhy'
        '12+6%LlW4S1{;2`F$*>%u;B+A3t;02*pR?R0Bpp-#v<5=f{h5+kif>Iz{aa!V;O852OEoEV;*eGf{hulA%Tq`*zkjmOJE}oHqL{M'
        'b712v*pR`-DX?)8Y%GI~7}z)lHWtCg0@#Rxjaje}0UKekA%Tq$*q8(xet``IY{bDv3~WeXqYE~=V518*x?rOVHo9P=3pTo(jV@=S'
        '%h~91HoBaRE@z|5+30dMx}1$JXQRv6=yEo?oQ*DLqs!UoayGi0jV@zjn>q0w4IT|14U~gFaJz;9g<<d<7<>W@e!$=Z3;_X#0ATO~'
        'h9F?@0fsPO2m^+Q07DQkL;!;yFhl@D05C)Wg9I3SfMFgmgaJbUFvI}E0$_*$hL8Zm3BYg+Fw6sn2w<2341U0H4lu}o;Ur*)0ft4u'
        '5Cseoz#svJNx<L(43`1JCBSe2Fq{JnX8^+~z;FUE!~nw*U|0YQbATZN7^VS32rvW$7?OY?3K&)a!*#%*0EReVhyex(Fbn|005A*y'
        '!+^su;4ln03<D0sfWt80Fbp^h0}jK0!!Y153^)t}4#R-MFyJr@I1B?0!+^su*x5CBG<Y=p+S9;8I6Q*kuvqT_GZd$V849hr-p~`j'
        ')6s0*Yz~h-aDt+D;(+;E)6}+{-r`#<PVPpFzsFYXo{c<G)*Jc;3rV}Px#QUmdB<!=??NV<Oe^V3HlNQZxwN9>ib{&jaHNz>R>`vY'
        'hIB5QO(M9@A{JU(s~Yx}qfYK03EAu|{77%>wy}R0+F$;N9lASGA@_$j)$=_)-_!Fwxxh@`+uXVjanV?)w%!W(eD(kI`+U~Eaav-K'
        'I{By<9Eyz7J35w`-BVV>P%L@>1%b@^6g`_aDD=Sez!booX_*G?S+yOVzdMyu{{>}}oUQ*e<Mfxby#IU(`33nU`8V?K<Ue{xSbo!f'
        '6D42V*3Fh|w%oI@nF%%_VX<^D`5w_t9n&7V#b-O#TD2{Ax<l4XHtl1qH}#r)&#=j!ecidG(fr68;Z=7Q$&#Bb(<UqOdwf~fEPF-1'
        '%@=E}d(D@a0y*TQ#eaDN3~zwp4KVlsqkfO-$1wbK<LU(YjQw-?j@Ku2yg`A8Ac*jRhzX(Nl|V!UL<9vQW<kU(h=_s+ABYHohzN*S'
        '5<1>R5Fvqx;~*jeA|^n@B8UhJL>vbZvmhb}B4iK|0})XWA%O@Vh&TfxmO;c(5D@_pK@hP5BF+mP?=py31QD|!LIM$f5RnEEmqA1v'
        'M7#zfPJxJ5K*S=5m;(`E5D^rJkU@k3A|wz|0uf0N5d{$sK*TnP*aQ&-M67~{>zoLM6A|Y`#5fTWh@ej-kQkQ8sI)mMZI4P1Mx}?N'
        '(xXx7@u>7<RC+opJ>w;pj$vsOjq>2|;PBuO;DC!7bTjqD$W;Bm{qV=)_5WeM>NqSE-5C}N=5x7Z7D1o-B<+sWrG1^gdN?qu@QAzH'
        '?#NCQk)0bQ25V{JC49RH!MF1r;M;`&Ye?|z_z=<uSVIS7pm5*r2w;r@Rv%yu0oGZ;x0?}$kP*P@1FZ9aH3V3f0c#YnhJ*~1CBe4~'
        '09F~W#sF&+uu6c{2UuSNtS15M5@4MLtW$z-cL}hb1FWZnA>;yJjR4jVVD$mk3}8(F){B7k9AG^SSeF6o5@3xAzTI_U2w4#_P-MXB'
        '1FR1K>o#EB1gr$Gu5wtfb66D)Yn;Ox<G!85SuKrNEsa<$jaV&>SS^iMEsa<$jaV&>SS^iMEsa<$jaV)1V0E_Ix~rK6O8_i)Oq)Wx'
        '`cHJQ^t<i0ZeBKxbz;jl+q~Y;`S@*o1j~Uljm<a0VR`T8eK#xF9prs5T02ZSljCf_coEx#qis`bS`ByTsj;j)H^Gj5Mnh6<jU~~s'
        '_4}N974|*Y+Xt-|j(z>|%YB9eS2qmL4*$dOd%Ks%HE(>FmiPN?Tr#y<__k2Z>i9ZQ?XG3{g&$h!hiO{vuERz-mvt#f#do>BMNNG='
        'c!)qj6u++8Csy#nNZ!ki$Ls&%M*b!|FU#|?JTGe>FRQ*7<RkRHpW;FPIXoT{FTg_*{2DPd9un}F5%35D4+(gL1-~XJgvKKR9wFcn'
        '0v?ip2aj1T1COBK*YMDI7<eoL4@t<Z4FeBZ@N0Ym9y3B{d>ME|fX8J4kE6gN1Uy!NhYUOxfrkV<G6Ej23NfoG;GqDI1n@WqJeCE&'
        'MiN5fGVoA<M;mw~1w07wP=JRd#H_yD6B@7V$*h&RU*qF+C?h)JBRXOuIwVeq`i#e|p7OZW6CSsE%;Q#%c--nCk6S(9SoHlnN9G<B'
        '9uyuFE);w=w>|tN`@yLqSDyRx^(y}<O5&Y+hGifAclIkUQ|%$^6ti0H>Wvo52}!)GSM8RWc}`Z#b0QF5Co#p1Q3MVbqX-<7eNrKx'
        '(Z8=Ap%6tYB#4$IL@0uSXo(Su8HiR0qBS9iRs^CYL9`}?2*naaYXPD)Cy3Ux5TOVNj_xUl)=5FMVi2uk5UoXs)`B2fvk<KaL@Nx@'
        'k|0_kh}I-T%P&MIu0XUB5UtA)trdvY>kzF=5Uq=XXkCD4orh?BONdas2GKeT(K-Xsk|A0#h?WG=st6H^3Ph^{(W*eSDiEy-M5_YP'
        'sz9_VT(l~CM61F@tHMRA!e^f<eD<lrXP+v3_Nl@JtHK4V!Ue0s1*^gZtHK4V!Ue0sXP+u#y^0Qh#9eOFKTEH+nzdb-D5)traQ#{6'
        '1(_%k7Y3&ng*1GnOq72N?Z`y&AoU>iAax-PHE36^4PUiz_U&O&=E%uLQ%DO*9P}EE3wx7PI}Ob&d)>OH7@lJM|5A*3_mw&a_3KL#'
        '?brWm>IMCJR8$D3o~6gUM34T{DX&NO`1JVP!{-#xVqN;R@44l1pYG1N4PX7ie*JM!{%2g@v`wQ)2m2St@A;^I!F=|=qpo!Qj~L~D'
        'IrXAxr{44^JmB<ZhXI29QdPfmqcxo2qV3RR(^xlZZd<4WlDQ^ZZLO-yHT{mkvQhVOO1|mItD+|@p0s$<vO`+xCnd~QdHK~|ezlih'
        '?fu%oqrsy=_&KweG3sTEdKshtXER3s;hV`AeNN`*;SxW;R`%yt$^i|pj>pHN56jrxXRT}E8&|B0d(%PV!&K0VSFB;;=6-dq%9=PL'
        'AD(HSwa?EEjnfki+dxmW&%xs{``=8{k^0}VF}ob5|NM0NMPv5*C)C&P&GRIIUrD;?wlq!`^?WMNr}BKN`rl9U{Lm;%g^T)Mf{4Hi'
        'hzJR<PVfmtNCFW7frtqq1~n(VI)M}60};mrA_7AC^qfEhfAi`Bh?o$(7$1mO01*Kp1{DSoXF<f0@alwf0ud1q;R6w8K*TW+F(VLh'
        'UU+rFf{;F)5n@nh1R~~yH?JxnA_*emAVLNaF~N)BF({vqKAi*+n;_!4K*X2As}m~1n^$E{gpU*Pj1%#c6Y+!-@t70wh!gRU6Y+o('
        'vCWCt<U|lo#40D^IwwNmM8r7}G48rVcjbn9KzKlSK#a%Twwrjl^EDz5S-#VJ{f9Hu<@@W<A$}b+&;OsO{pM$Wa7)+a;STbhmMPbC'
        'TQeF~LVkz6{G7cVOx8DTy;-wl!**X6A`TX+y7kS^(|i&f&(rKo7$-l!NjuPZn0KIGPSQ>EAHHdHjJSc_(8T`&9a?6nrfUEI'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
