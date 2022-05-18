# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/esc/_.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.920442 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.esc._
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
        reg.udral.service.actuator.esc._.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        """
        pass

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
            'Bad serialization of reg.udral.service.actuator.esc._.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> __0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        self = __0_1(
                )
        _des_.pad_to_alignment(8)
        assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
            'Bad deserialization of reg.udral.service.actuator.esc._.0.1'
        assert isinstance(self, __0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
        ])
        return f'reg.udral.service.actuator.esc._.0.1({_o_0_})'

    _EXTENT_BYTES_ = 0

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8NVSAw0{_ig|8L~Rbw4*w?a)r!z>NbmZ8QA}DYv40L5l)Dq^M4k9pz46D(U>Cg|nC?XT|YxIW&iqv<DezerQnx3p9Y)|F@s_'
        'W`^YMO1g8=AG(LT+a-tZ`@HvgZ}@L-{`b3E5BRhASvgN_n#W_SDlK#UQciLej}tR1jn%bk7eCxnxt`%`dOj~z`)#}V+xF{rWAXcA'
        'T@<Qnvj>YGp4C;8)J>(9mwbO*$Qek8N?pWFTFE>Hn@gRjSYo-XO%*Gf#N&4H_V`j&R-1z8z4eLz{%!m8!P7VXqy25WcxNo@y3&)T'
        'R<`}3UA#B=J)X=Rr>|*Us>(_w5(2m1EdF3T)z>N=m!_)6I&F^@KN?%pREffkT#ZXvXYJxG`Y+d$cJYG~sC|7xSHFb@Z)~@VH#0*@'
        '{9dWsMYKCFGnwzHnQ0e4Et^TMlQFbwa^g2mWi7`wY+&2P_i(vge4o_@2d_9Z4XR@aln2dm{6YLECO5QodrGQh(n7LI74<kg_s!zX'
        'acYwGv(GjjJUGvkP`OI#$`m>gwp1z=i7D_q&s8Nh_Rn@Vg@06ND^g|kMS(?AQ*{e<aUo=piW!JN9{TBsf@E6hOJ(Eeqsq)g4R*H1'
        '($eUn7G{boAj+3ym5xAV<w@fCWn*h0Nw@@&B@$^BJt|o)6N`@^%7sD*A?)h;DB3+fKU)<*zzB#QgyT#VDdew>khwL&HYK^#iAMAU'
        'BvaK?Lf=$PHR-AgzAe))aTRh?h}aU}<0yiGtk`f&Hkpf67w{Olkw_VFQJJQ+vDlYMCa|2yNq1GiKcusUNY~&YYtpwV^jD1%R~p7~'
        'oOy8^?KxEj&l5k=NwQ9MUL+YjX&Rf)#bhoxu58Bs5s=x+3&mcOx^PYdg-XuJoL1HB75EBK0lH3?OEN30H2D(tw811FMv)L(;><te'
        'srXe;6;FY?tZJR;Qepva*#x@`;=?3tY#6a)+C2)g!apA5g+(B;ZD!CAI>|gAQilDK#8fG%<0$LO+jH4?MEE>gXX#b4gSEmLU<Q>Y'
        '${A^*>q<hXqM1#wFUVdE-06H9I2EeCGS!RN8Rt~VlnC4Zg<Y!dS-;0RX|FO3z7!?aMX`53>*x1Zt=!h~`g|yCu2ea4`)o2F32Ycu'
        'T)?<#EDj1NTFiM{u@Nc?Js26Pn*t<qGwCB>xaV(Yi4CGDa^|*Hv&Uo_Lqu<-kD%3@U;|kTmI&2SRa;~krXeQMYU_>q5faoyCNKJk'
        '^fB&&LxnwN6|4-(Ikd$dvzfUnh&D->YI#vf&{es)V!Ge;bN2knulIM)#nH~;{_3^!&rkLv@o;P9^Dq)OShd^dRv~WsyGu*ypE!>D'
        'P#t{kselv-rig7B|J*TK`rLHXH;1e?1G7Hl?qlY8bg_M#rh(y52K<1Xf8+o3U)<*sf5hNN<ep{<-IoEUhf6<hUwyOZ>c=lXxEcI-'
        'bR(eb{{{W!@8QS#+J~Ov`dY8=G=%hb@^aV+s|<%q+`*8xYh#zA<JAn$_^D-f4_6$2E4$KMakSsguFU3ECpHfC8WlV~p(oClc&$ZQ'
        '2(x8g=^V8g<nHGcR>hTpQox7tNiGYy!t&0~s;k#!+gfo#SbN{fZgnJHW2IjmiPu``!Z<oIHNiN>8I%aUJ^EZqCBN1vytSN_C=OBd'
        '3DA<Mwq;r7l&N8>EyiI}LW{%43RC+mOBp`)54wA*NPv{7+)%;t2^(-K)kF}*h2XB(Q1L}P63F;S|B{*j04k*HkjguL5DR*r?Vq0<'
        '9~_;B#2ZDoR(DiN09I3hcT?n)-naw=Y`K5*@y^Hld$HKDA~ytyRu+(6e$hy1(vbiNT_u~$BPyLP!hQYDjZB5QPE=VFCMjSs!wNZ7'
        'EfA!vw6P9AfZa?I;w)s5C`Qp#o(f~(Dm(J!9!88zQ(K*OW!5I3+9PO>&>73HRbz1orOAGMVkhcWPE|ec5z94Hf}QAzD0*J<dX^pE'
        'JjnJI^>}R5fzKh10nsEQY+Bp?iD|(64jwj^L0b47Vav}5PG4mPh~8l~^;H8{&WqfIA&?nzjK!0=xYSkMbS62NQINt%|Dq}*_OD@7'
        'YW~D&ldDmr-J$`itc{_Nt?H3S|6c5XPPh?33rP3`etHS2u+hO3J{6bfHPXQ&xKDON&~Ur3dwg_$di-pBesH*d{QR5%mqcVxm}p4J'
        'davvzP;4M(AAAt4$%!*TUp!9y2et)C?@Kt?0w6PP7c=;O*39~auD4`ngsZek17*UtwaD=_(!mvlkCPDjp<qW+DnQsl=}$BCxF{T^'
        'L|PaPb_ii)r5WI1Uzn?Y3t&4;E2XY7rE=0Aexb#Xn>xvw8!+!sG`$sleL?ZT;{pgfiqL-}iO@9<+?GuTy}xPzHR*z7%r3ZQ<;!@K'
        'h4E0HP^K;#*B@1i8b8VlAugk?d~}F?m@-SYjq1#fu%Z~LOxh$Mqhyt9RXOXdY7->TG!C&aW(56J;jD2_V!|_tY^)0A^EzXr=U7-d'
        '7Ax5&UP*-^<awUpR7v1rNVC#IbUPcS8??=R8yvk3`g|-(iYeE`IHgR|4Bf^v4kxi3bkiKu)28BR(qx;NtIp9GH|BRJL}uYuexgD*'
        '59-uM6nAbmZYh|bDl*EvsoU+GsVAD|2r=#SKJ{qZ&qYGWq<T74G+bFLJG?k)D!NH62+^6SOkQf*33gR3Z(;AasiB=j3_|laGwHG~'
        'MpRcg#Jd7PU0h0@n3H9_AzV%vlA-Lx@x%=$natT_xDN<2X|!II*f}{M62l5(lq-s1aAL1CQh#`Ii4~<NRoCI(%(x^}8Jd_;?x~uB'
        'a?In1JVC)Q>SJfx2etL?cM(U$|ASbZlIdoOXFQiCufu2q-2JSjcS<5D!$1q^(kv7}Y~}i;O1CXR4L_|B|GM>PBpyEcf|3L92lcYP'
        '&t*aWc}revyIp1waa&S&0;PzJwM0dM8S)Qrq|Hu58u%bF$|O`+whYK3X}ckXV0$kaQq6cSXqV%N%QILZyXWF`_vF*VtwD%BdA7If'
        'n6t$mEnCdT<~HJmW=;Q(4d*3&9mDMa&s;#s%R%x>8%~l4uq#=mA|QUT;W9Ip`V|$8x+wDeip`J}t(a7jk~!P)7qK`SPD$@DnIEz_'
        'kJYleP|%>b;7WI?azlO2QiXyIE8sL)Yy*y&B6af)kK&f|K$uIVH1nglsABOcr-Ai+(I>?Fvd%8x1F)q7slG%oyme#Je3|fvk=PRA'
        'XwB3dA-0bIZ&H~*rb-{o-7V)J-%3%<5|WR`o&Bod1s|X>vqVA;Ug{uq!04T#qdo|{Kt0?^a_(zLD~INY>JDRc#?8ypx%^n8j4dNT'
        'IOcSJXYb%>|LknJ`+!Adlh+=AfW+DP&e7hJ&)GkW7P^6Vtw!sO216((pD*z1)qNCErLOPqbsQWDIFdZ5sJsoh3)$3$>MP<Ee)j0N'
        'TAf)&Ub3c4*$R}XSHNut4{yUSE6}>zQWTpg1PNGys>>=6L-Gj&4@B3;?p>d9Fh~&V1!<yPOu2rm3zX4H_}_XYfR2F@Q`aGr!N~;7'
        's-Ti(kwH6<?VOV%CUdc&QyPkHQboSQ7*to0gc$7ky+0V<dmD`+4+ptF9D;^asTrGv4%MK;BzK1dOlaB^LFFMX?)h|uA=CtKMaz>H'
        'Tp#$p3*Tq^`zNoBUbq3f-@uWxn3+1>nZC%jy5g;?q|r6-3qw)vvWqPW5EK(S_o1W2f|c^4f@d%(x<udIjG#(kO@*!*&1k$y2%8;+'
        'YUMCF^LA$mrSEuOEi$AjOhe6iUCF|sd6WcIUny0rZkn2_v;$JINwvAumO7F!<MRmb3R2cve30dA-IL~oUL^C75<24!fL!iR*tmP%'
        '@W)2ZO-(_q6?ZFsE^ea^MTNtfB3<9;c9S@&>(T`S+0LEjxjpC_t7T0ajxHX#cfN7Da~C^Z8P&UkI(03{<RhLekh?h6yVE*gL@eri'
        '%Oo>293Vtn8k27UiBHtj@KC9C{SP&6VT1X^>Ok=or+qU)*mA>H%NK6E^_Y(Y47CWZKzFpMDL}~3al$Y?J4z1eQfC}>y`#4SPda?E'
        'Ct-)#uTqnF7p5#P`HQnP*^^shp8@-9<;u*-^C!;^&VB{Oe3?00?GU<t!)1BYtNuJhBZz@0=nzE6DW!jj+IY28<9M(~%`2rhJzY*)'
        'ULij03&$J7&*}c|@!{eA(H;amIXyT&JvjfIP|J7uM7IyX`4lX8$IBbtK1+6ZNvuS9bo(&)j>UeeGqlV^adRE4$*#0&XmAb+KT=SB'
        'eW;V&U<F?uZ6EG@HfCS$?wlVSAB|7;VXZyaoDJtQJmy?V->K<mjkgr(r9?f<>9-7jm^ck473%Nbe;|JK^7fJ#K*+|VshPPKDBW~s'
        '12n5$fwL;=%z+qB(LR?PlvE?l(!9-=vwrlvDp<%Q-KlIS>rP@PaJ-hU{f40qg3!`#F0Dlx+1)w1EtRK+5s=Tq?p(6dz{Bc({}2c+'
        '?kILnXv(Bzg{sK!9k{GBK%0cB(MD6sO)6uDN6fcZo|Qp)h4PWA;h?+|c4>6cZJ_0sFua;G#9<TSDUnsB-C1ep23EHBQzt*dV5@{Z'
        'krH!ckATtXJUpd2EewzVM52~YDMYwxp~TBeqp5yt$z@PYr#!S@LkFIbtvTILhUdx<4)~D(z!b}Xv;Yta#Yx=7I2u79vwDl##k3#f'
        'K_+a*dhTALcu|<EV&u^edPpRB*K4{?w%7AW9=UW2VEf7b5$(`3fy^g%&d#16p78G|+VOdjQxNr{)S~cf3JKi6J-C~DQi%8S#=_Op'
        'OD$=-rerlS*RX|aFnBYQTvofG6Sl!%0!-i|K}7g*FGmk32rd!bWZcn2%|ix<6f{k(T|?{UY(rc6BM0A!MtvtrErx5fA}5<0JEz@_'
        't&|%BT&X<oHbDopNtmv+4)3w>45#uS%C5EGF-+R^duzRM*G1m)pm?TVs4Hzz>BBug#{kzr@=i_q`o^xL{X^ATioM+)hqyvREd}y!'
        'c&|eY1nyS)`9w4jIE*Z&zDRfHAfAwWFQ^k`<i?jP=308Og4Ti3Hp3&{+MK{j_ii03ZkSPQqs8D?q1Y3+t_Kad+xK02?8T&)n7ZRC'
        'l@b!?S2eiJWL!#0je?2kayOHyRCx0$@5UMK#U3=GPDnX1&f4(8Oja~H3e%n*#!Qj+wy=HEiVl<f3mPB3&Z`*@L&Uu1YaG9M#X4`t'
        '(M<@g(JLMZ=Dg`*;}s7C40GeY-M4!6r4aY|M`-Pwu^oc%evW=<0-b_(uN2W~a?@$|9d&9KZ;mIqZ5MwVUJIS*dYr4`qRz%ZC#%2P'
        '#k)^*{fvK~;irG|bMd{gDcgm(i-?`iCI&d7UA%XwW=6l{us>!@V5;FOrU{zzw9S68_`?$_r^UtEqU;~&?opE?4b4~Yf&y2K_P^SV'
        'rw@K-CyTeor6bfneY=@JU9_6*(+BiLUelMi#xs*5r_s~V7>$+W)5!Lynb=7)$)fC??A`2-vLAiXX77F7W<UNWd;ci=N%kij*-x`S'
        '&HgO=^XzAt$o?Yx%j~bRzs~-K-ssFWzR5PTpM$od)6JUrygyF;d$rX#12V*aR2JL2-pB=BnXz+WwC9C;oAUs<;X+l*FWtT~Fn9Y@'
        'Kndi9nzT}FcC>i^BoLy<;$7T3q+8#%Pv7`=di(T`$Kk!sA))_->JPJ+d1Q~WzZ)3;$GfJWx50{Ay}0;+b0Xrs{Q^(?(vkQl@`!*('
        'mPq~N6a__{s#4YZu8?@)J%tB`wBG(5yJr_S_V9QAYdF|@J^L8WQ<iQD+!X6K>CyOq0It|ObQdiE00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
