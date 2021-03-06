# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/servo/_.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:49.172252 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.servo._
# Version:       0.1
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
class __0_1:
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
        reg.udral.service.actuator.servo._.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        """
        pass

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
            'Bad serialization of reg.udral.service.actuator.servo._.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> __0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        self = __0_1(
                )
        _des_.pad_to_alignment(8)
        assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
            'Bad deserialization of reg.udral.service.actuator.servo._.0.1'
        assert isinstance(self, __0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
        ])
        return f'reg.udral.service.actuator.servo._.0.1({_o_0_})'

    _EXTENT_BYTES_ = 0

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8NwtJx0{^XA{cqdG8BW)9P1$x^(X|EEZM~)2AlEYOtStrv%`nGS8!w4$*vi&oNC|$NM9vhC<&m}(IKcYDh6NC?0^$DC{Q-O4'
        'yCX$Pbm9zUQAZ^2-tUj+J?ZaP|MTAuuc&MOK{^X$5ZjLAS>(piBiD<$?f7Dv3K`|RoWHrt<7kSH!DyE9@@cvDZTYzD&41`bNy4)-'
        'yfT0DD9;K%FEZX<@`{tVQ;@ix@rhjonH$?+a}xR7cCp;eMW!AI+bQSQoD-hONF+q@)jylhPs_Vk?!NTT^4oI$y5r_~7I{U^W%;n2'
        'zumZZyqV_pnAQb6&A9JE<nqb<N6t7p<AIZkEO(-y9M0czq$o0<<3-G!)Xl?k{wn<wM_xI9?Es3O9njOK(BY-ca(*=wq{a`@sGM6n'
        'vov($T|O1%{Qb1>;>dTPUl9{OCvbDu$zcUq&R@pka{h`^92|`5(6mw>FO~YB>eyTM4Vzq1=H($N7rGL%Wjx89YUh*rRVNUB`Q>LH'
        'T)DE%)L!Ph3DX2Q<53>+jJYh&+(bemn9z-x$XF(FH=D6oxB)9<luQ_pxexRCEET8NGtR`6VK)n-Nw{$$;@q8Zw!6c;LfV!!!W&YH'
        'iLoZq>tvzt)>shvxZ#qWhLIoYosk4*9<VXiBEF_>5|A9kQ}R3&QIaz}V;Lt`;gzLcfleWBT8wS5MHr>wOh&%6gBiR|A1dbdLF^`O'
        '_Scbo_`EF*1?+oK!p*MFA>M=|vXKq>tY6s_Pd$-`q(APZwuWSI5O|DvmO-;zFjuncc{Jq^dz#`=#qBx~xSoh)qw}q?aKOiI5$B-j'
        '!Zut=rM@!V(P(?Pd;2S!{Ut=yvM7NVk$K-YMx=1SvqZp<aSXR=k<v7tk=1=px3rWz*tf{oE$hp|`x}CSXhf4lKqZ@vYRVE}A2Y-w'
        'tU=q1L`Fon$i)=K^s#8hB4wqf9-6de#4FN((nZC>&i-(8xPQ+X?cE>jKNuNPm<^I_0ull9W=3P349fB{6sHLjiDEVuq%(ySQsTsw'
        'Hrtz~F`p`lwWoOEBl8j1+Au+2`Gths3vQ?IHob^UTvI;VY$$SKnTKw!SeaN_Y$M_g$3h3Td>uWw{ingshz+;z57<RlwP^I!!NrRj'
        '*WvbPK)lvB8rS;5qs?n+4eMPLjccqYIcFY+IoBGzz~{V4@O-1|`a^ro%BDt8v>vx_Ryzij3}otI*KUTwG5emx8*?6bu7Av4OuV|G'
        '896_1ky*9fXPwe@2)84WJVR(B>&{IzTnYl(bfi-Bvces;$aLB6(&Dw`(5<9Hyl&f7CAn%vsJHe3kr*{qJp7)7tHS%4!u7fn;^GAS'
        'e}!Al#;&Wq#<Gq=QN#g@a^xmUxQ{HLrjAnP>mWhrpJbv)sY|J%EvZq&!atTdPy39ZLgq#2eAt#0Q;!;(D%Ddqb!Sx1qz_2NEz>9@'
        'Fx6^*=;2kAF$I2P2tzH(rxFm-1<@Ey5v7;tQ_+=t4OMY(+-_Ba;TPLq40ihq9#c|kVmfP@2~rXq&{uVRmp65>k20C#F9$oV0Xs%n'
        'P#tJNjC!=Csx}$OjS`T>rUYn~ow#wKI&1D8^Mn`>5d%y}CqqQHz(sSRs+sT!7@hEnmXf1tRSLFD1vL;-fIwy+I0)8Y^*(C7M5rl?'
        'R=H}tmI5OD%%vXIUx9RWFdKVS3RZ|}A+M%Q07@Zxl8UZdY<<iA_)|PSL7k`6GmnSv5D#77M^<KvUHwpF2y@+HA8%Q<Z4+3a4hzVg'
        'FFC4aSYZwZPY_o~t$K3CV{H!;ZV4}-X543L;xLLB-16}jUZ3V7>05zNAY!qoR)Or=6y0Wb$nKEQ#SX%8#-d~oHzCxXE!)Kyz`R_t'
        '&iW@?TaCA!W<sI;rr=Ate2aa$Wob1042z*R5?l`XDt|;dc(V-c&rLQZhr<I61C^0Z-3$dQ!rVi$^sR+)j5sjir<Dmm()RDO6-%~^'
        'r;%7Ylo@6c*SJq*76mQQkVQ(kofOIxH&g+M4M|RTP)D@}aVGzP&&KVXvufG|;fScmtI`%P?e4dsE9J3bSp(Nr`WQPItC`2l^~4G9'
        'TT!zp1%k__KC6x}0xbzp<zb@&N*_K^sZ3^6%uph9fz{Op^@#v8%|*}{e{`8pK~UGoh5<l<raKUg)OcI7w`%APJEk0el-YYC>u3q&'
        'p9axJhcKhzg_R#A{0O748YxHu#D!FiBjeu`5drd9;)j_?L?N4^)cpxUOfld@Wc@{hG9sc2AP&jaaOL1=$F@caq-TWo2>VkRq?3sl'
        '8Iadgi8A=YTRP1}s)88GOhr)HRR>$G_%{W}z@t{LssR1k%Y9vVF#hGfy~fnsK`4c6p4VfJ8w+qyGs9}pXT60rfq5cHalL)8x7M7z'
        'lnPbXl~o;F>A2M5XokN2d~7FE`y<Sgcia<V9_88*XH^R5V1O0I(WJ;)>NLm5G4u{il-APJX9VznCekcI3|cMfi$Oli+?lNcAMPWU'
        'lO;qdVlhDq#RBG}u#tS~#oUw<)5ziaYRbFWF-Sf4x@gjB4p&wiTxo!%kX!?AH)n`87NbAtecgi=y9@*;H(71y*c@8cH`bc$)+&Zs'
        '_xN*(d8td|8uy+zK`_D7ug!mp5BfU6f2?t1>D`J#{h`5Wy>-*Q`dkk$(XFlX#?6g$28F*5`t8rv&Fb29LveMj(YJFnWG^xeE;DT^'
        'askuMk&j(|%4@S+UkZRumYri9yX557<hK%WRmipZbxvmNqG8Nh-rjXBJ9&NM;%mLN_E{_I)fT(NO0(Kxms)9Nym~@1-KOg(@ZMl>'
        'po_J~L)3Y6dBT*{X_xBD8|K`saSCSowLY?>7~yKr$%UmIF2>{46JS5e`~nlB!ParC<`x>t&^rNL)HekQZY1k*dt&$5y}>TE9D@&N'
        'v`eHQu&G)pO_o#4DbwhYZpfN98j>ugsmAQoHT2242G$uVZXm`~u`;+-A8l6ntz{pBx=z74-%!|U*^+9Y(!ih2?h}7j9iCRE(<Bz7'
        'R6XYEqfn1GM&JnM45%RzEEwksrvYrY5UPSrSj$f^a7Ig`usKdu9j~i{9S(N(@82H`cVXUx!@d2(z0p^6#Qh?d)m_6B)^pp<-s&y`'
        '20<_36stRjFIY@5o`{xZJWlqlt=Ttc><xn}lt<t#N(ye)SEtB;4l#FSP9JV;-rxSxIe2jU-rmmkXm5Y$91LKs-R9wg;ky!I{LF`S'
        'B+W^89`%<JN+(WruHN&CT*ZnB%V15bnTb4)xfb85#mC?h05GL0hzLL%q*EVu$U=>M)$#JOU|6na0s{x@Aw^591-7l_OkaRtH8||V'
        'u0+*lJKMvKB0xDsAlpQ}hS9YK1oB()PLp49LCw)ZQ@sF26dA#3Gx{1o>ak7|BqprrXF|#aI<4kTxU{Ge9-~wiEk?kF919cHq~W2B'
        '6sj_ya3mrY=~I0S8UegTviU_$)ox7QQ<;w<=$?p(DqQ61@5jbt(tNdkRuc#Mo<6ydW|~AvXbi`gWdM8Kgku(pXB2+A21wL7GI-_e'
        'x&WwjqwhorWxMp%+tOEbG~=MUBs@n|JGR-jIk|uo^-90U=+w>1=qpgEO{X8Rv8iG;iU$Wni_RlNLz-TFP}QJ=?ytTUBP-BZ-T<+e'
        's_5duM9;5MIb9c4+S50O51aZFhhA3FPym{*+2UE14|?dt2#@?ChnwlCI!yFw+5k8Y3cnEw$~Ks`Wt6IF&^#re`G?2jHTyDi#CkRS'
        'U2^95`Z?>o%sqw*{qyR4rvID`mDSH{$3AC6RiVwv`?FRrPcP=%5NO?W(PkAt&*qzP`mUZsvr5P33aa%vuXTJu&8+RDKDKEW9hFok'
        'ZWPlm7pN?Sd7jFfo0}6Pec=%p-rP@lqQAG_4ER*Ya(>nEV*K;l>gNw$lshp`CVA+fKP=yu^EYls`8{=igj@3qhxyBnNXt39h=`m`'
        'J%LJI&fmTdw$URc@V=_bB5VGX!VjZ3D8t{)e|$h+J|>fuMd9!1?XZYrH=8ZL1qF4?TmHN3-M#Xi^yb%`R1+%iUMoDP3(QsCy+R+{'
        'Gy3qVGesW7F737)ewI?siliJCp7aVYw8GcJH^QHUZ#^u-w;z|`J5R!Qhv9qS&wAne;m^Zggue_w2wC{6@Ot=R`0MaD^s9xi_as~k'
        'KLTxjMwOlTyz2z!_am7T0)gQlI>{(6`sE2a##Dt0jP@X*TEK(7BuDMZ+CMINy<zV1E`t)NKsjl}%Wyb<_n;y~+w2{@yHBs4mUmzJ'
        '2mQk0rw(9X5+E&`g#HE9*F#(J2ycX+G>rewj!5X#E$Q^){59=FWKa1JJ8o$be<Y7Ec%((@y+b#d@I#*RJh~_(j*X|Vp-Jo7cgj6G'
        'c(IHB2an-k<Mr?hIFCzu$?%e`zND@8{{UnLJoW!0000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
