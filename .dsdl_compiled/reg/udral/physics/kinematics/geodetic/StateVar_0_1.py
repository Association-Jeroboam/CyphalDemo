# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/StateVar.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.299677 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{`uuOKclSddK+?sTM`clq}gA`PKG#ZOS9le6#7zX1zP!iGv<H%z84>crrt_$hN9E6v=HiZE1El;V$y9cN$m%(*X=5'
        '2<8+xIc0N+5#+$+<Q#I!#mF%yV-a9C$;Ai)BvtHxky1&r<(a_($u<G`tA15iH~aUmufF=&?oIsh-+bg7e(cljty-tnNR&IeX=n}O'
        'V{NUWC(6~<M!VH9EZwmW-LlMX)#{r1J6mnt`P5ndf%APQZimWEZG&!4nEHC6TQjvrqD{6sMzxdp$Y|;tn#GFidaI_>QsS1SS^B%0'
        '>DW^Fu5NaWR?{Iqd-7eBKXp`}>i<LM2aY{m)-203*1DG7aXz4@+NY7Dy&OCAmZ3Ll<HkkGHO<n>7HcsHxGPD>zI3p*mRg-*Q^_Qm'
        ';;kZ4+7c2&RY$f}dhy_u9<atY4qBtpv|d!@emAad8XJaX+@&{e>a9jgvvz*7)8#e8DmV1zx<wrID!rLitz(rp=xH6YVjnH>!`Wep'
        'H|e$;Y!mwi|G@dSW6zg6me#CkW^H>#_h~&F+IrKlx;1v<JEm5(=r`Y?PsCd&(>hjjexEN@C>HX?Oe&LA^65+}S4b+UY%X2MrZa_1'
        's*ucPa`{40NfwgS=F&MOn=KaexuQ}`6|#lAl4QrE^T~peOs17wMk(ZzIi;A(Dfvvgkk2axB~?h}vdJu4o5`iJ86};~)9SOCbSjh1'
        'D@u_rrWCrflBK7hf5}WPQ^=+AMJ1o4XG<k>g?uiTN-ODPA)n6Xvc+Vwn9L}}Oqw2?O%~|Mlw4BD(w#DyBCVU9EtAgV>0aq{x|mf`'
        '`J9qea=BuLo;97JS4%IEUb>Rbr<2)KHd~+<PaB(|tu3UKWHD7t7mJFLO6QWa?a6dLrDRj-tU~L}D-OH)-8K6BNDca=xVL$tTx(V7'
        '9e&@`YKGSQfbB4T<Ps>Q)T<;-@}zK|DCDc&SMbHZf~iKUx$b@k<m!I6e@wjG)$UfcW};&xx|EQF%S__8jhcR|sx`P4`Bfjs-1`=P'
        '0pDV1L$`F3eS<!_LbH!->zT@HTW$~deTUp8w>nfdYkJ$%tF)i1IS=fa@*QJSua(;^(<&P^=cYYd?zFmQRi_&odbzDpQM4zSX&7r%'
        '5NQWtY?j#CPpJs|FH?9)i}kQ!i&~B9WRN~ljvaY(t4*}VHGQMy*vH%5wT4kG(;lPSU}qk8eDr{@`&c=4pkvVL*rP>PLXhnv<HswJ'
        'N+c7kt8gr);77_t>(CaOdedTk$6ceUI}gZJ@;()mwFa&EJnvb?3Qu>m#AU~he$%kt9xmUai|AwQV7b+HY<a&*I$IlSEqYnBB{%40'
        '(teBe4!_aXP0ebV<DM#9t`dXx`((>LT+(Vaqq)9oC-S>&>&<S1Ugnm#mDX@qYjkzz$4*?m+V8AU@1*Tk<fu}2jb84C(PW(<Eohsp'
        'Fv&VXdaqgCs-GR_>#G6SAhZ6yI)UX7vlD$a3_FSK61GoaIfCue%ue;yD3%W~8||wz%u0RrFxJO#{4BGF`sy6Bk-mC_*~z{-kNp-<'
        '|50Y=`|2@f=lbd*v$4MV8nZKfbqVJ=j(Seud?%R=_tjIV?=-W4zAEGVXP7<RSI;tgs;|Dz?8&}*j@c7^^()LC@2lsTUFxeBn0>9U'
        '#+hC0tINzD>#G-;J=#~_V0NLeuAse_m_5>06KMBkW@r0q675ehd$_NraUB`lk1Vby$Lw@p&EvWXxW5XnuZa6~1=smiW<!1TS8%;w'
        'V>Z}Ve-+pLb==RZxc=+zbEB@p64*`H`>+pTAHhC`eFFOw_8IJR*WQr)C@k_qoEH>cxXuf!yg+zilNavu!b4to#0!sk;R!E1<%MUw'
        '@EnCM_2Kl*w$>cF>{z$fS#!M(tznINJnNdloWQCsuj$r3U2n=3(d9;qs*Sv%YfZVMYjQ)st2gBMjazRo%hX{U?s8|iOPjg2a_i1;'
        'mDaTMW>ZVZOd*-yDf2VQ+FFY)vYlup398XL`5ngm*U3fl>*Sl{--y~JA3h-Eo1{XjaZ)2XxkJ_oA%-2Knn_0vLqD4dvFmA5eI5JS'
        ')N$h8wqwr>{cWm~sj*U$?@(2=|NhsolRO+W(R*`6<}TQZJn{rqh8M}(o`}3do82;Nx+xnSxk~8xfZnB+Oix`U?uBpC4Z}UC9`U<z'
        '^IO+s>N{_sf{yXAKCHK)ZMC|%XY{ZRAGNW{_3w1)O{I0S3f|OA+I>-PgteC5Jm$nZ#3bFJB9cw=-H~wiMy2m=6Vrt^TTRx>HTP6y'
        'd&(7M+IO(Q+ly<f`>B&MT&Pdb(ti8@zT31v;wnuZsDAp){fIg|pU^+slVVSbf7zs%{FLkOE<E%OW1~me=)HiAfWSr&Yy`kYKwu*P'
        'HYBhy2{t6KF%32XU_%nvm;xICurUKRB(M<x8*^ae5ZI8wMi6W)f{l5w5d#}hupxns34x81U}Fhv90MEkU}F|+%z%w)upxns5ZDNS'
        'jf-F-4mQq%jdNh*EZC62#woCI0&FaSjYY6=6l~0cjXAIp0~<47BMLSmU_$~MVX!d)HUa`03fPE)jYY5_fsG#6=z)zM*yw?c9@yxC'
        'jUL$OaW;CKjUH#C$Jyv{HhP?m9%rM++30aLdYp|OXQRj2=y5iBoQ)o5qsQ6kaW;C4jR(w)_h|5F@MxeMe9!F~1{8+D3t;dGFa!XD'
        '4=@A;7=nNy02o4m!3P*3fFS}Hq5=#dzz_ut0l*Li3_-vU0}K*i@BxNdzz_ipLBOyG80G*&6flGZ7>)ymqkv%+Fhl{vBwz>thI4>H'
        '1`H<v!y;gq2MjU55CsepV3+_5KEQAZFkA!-7XZUKz;FgIoB|BT0mC9-SO5%jfZ;G;hysQwzz_xuK>>y&V2A;RRlsl^Ferc_4j2{z'
        'g9I1`fMEa_27qC}VHj{21{{U~hhe~B7;qQ{9EJghVZdP+a2N(0h5?6Rz+o707zP}M0f%A0VHj-h8ax_28h+_%;6WT7!Eji#cc0mc'
        ')52_p)?9DsiQnvMmToqO$L>2>VISXTF4r`*EytdJi^a^{c=0#bs+}{Fhst_G-(W#$cV>4y^C54W`LHi!vdOfP&SdlXjFL+$O0KA+'
        '*lb5i$z+u*n|ny-ve_g8{VZakwY92YZ8_@1-jR?kd+ytMTepn81JQx<N9@p@kqWs#ys4h=>G__X@5u#b;@;-g#}F5d1#9c=pwCx-'
        '9`N}(`$TF<oqR+Zc4#Owj(ub-G&`rQhQV0!{!2ocb%~zO8y0$KdT0u0PPa^h_O05s?%$nGssD`9NzT^)g^~JmTHbF?h5U^Cocufa'
        '5AvV(A(rp7*JR0`+}6#OY_{C<u-OSVDbZo+Ve&nqn>waG^bVi#SZmd`+$j%PGuh;ivEI~c@;$>MyY_Wwm_~CXS0bzKTvA7FwoHqx'
        '$nWuGUF%pY@@>9YYu#(U!ZgSMCocZW8)SHc3~!LZ2O0HEsvyG<)Qzit@(KIr;9ajz=z2o}5g`!a0}+0q>y<!66hwpsB4$9u42Xz<'
        '2p@<Dfru!GSP;72c@QCih+`lk3L^X<Vje_91R{=sh#3$O0ueHZSOgI<5FvpGABZ>uB9=hJ5fBjt5g`z<0wT@}UGEZzm<JIvAVLBW'
        '0T7V}5tl$j97MbhB2Iyb*FeNPh&T))A|N6p5FvvI1w=?7q68w6AR-1L9)gJbAYv0l5D>8nBCc~H6i!5(6S2sNkU#`|B7wxPL`J2}'
        'QR)7u^l(&qG%7tFm7a`BPe-L^qtbI;a_JbBMiD6w4i63w4gn50sUbICPmE60|2qJGEMET~=B<uHL$U3lp-?`TOJ))HsfTEHq%Q2~'
        '^wp<>qY7u--F8NIVu<eCC^1+|{#Wqr{DN=i+sC&H1J<zM+wno953q*!$wJ}2-66ml1FSy48V0O0f^Ro13?id|)dyH-0c#krE&<jU'
        'U=0gdC<}sb7X+*_U|j^PF~BMTRv%z}9k8ANtP6m32Cz;FzTHK@dJeFj5(bfTfHewO!+_NXSTle%0a%v->p8%B8n7+_)&;;C6MVbt'
        '!XUCDWTD7_)dyG~0@nM0brY}>z`Dv|z0P4(IIM9F>mv8<B+hDS#A<28YH7r3X~b%2#A<28YH7r3X~b%2#A<28YH7r3X&b9E)z)3j'
        'G*}v7xocV!+SPxigQeeUw{`Q9X{-}Vw%F$NhR(-t<0DueoM~)ciA3bxpZDF|WOtDF!D#I;@l1}h0pl{Z2}fI|*6cLgp{K?&^V}pm'
        '_8ARHwKbMV$JXz0>Q&hHU~liYUO4uRORx4B4qV+(JUje*k@t2kk89reFfH%(*|=zGwa9Iun$_`jqS_tH@=HIo(ht+L+8u|DGB4{>'
        'Au7I0^^d8kM?wb*6~yp+t39FxFOBBC>WIAluWt0u@A+AtpXK>kd-z%Pg%BU3_X89U`p?1f@V^8PN$_mM@OW6jV_Lu?0z4$(5fMC_'
        'kPse^3V4KpM;LfW0v<eSwFEpuf@j0S;}PJo1Uw`mzcvCqWWlrX33yBk;qfKl5d|KX1U!xak1+690Uk2&m<Jvb@W=>woD`x~lfXj('
        '9tq%a4tOjHo{c1g$7SH50FO5CND6om;GqByNr+l~wkted*_B@_bI-=d=}<;=#7A^2j_8m$9qMx)xq8MUS5JB5>IsirJ?4?CM?7-%'
        'kYmvgY#*C@P<T*yP`FU=Io<Z~x9$5Uj9h-<58A8z2Puhn?in5H;J>_Id6jApSf`lVa#wG(SY}A#UA=0x%*+dNTV4=@_#){kZj>T;'
        'uqZ`vzZ{eb`Go#`{uqTQT46!7Bq2r-5=2XkQA|U$!VoRLAX-s~mITq75MmSy5Un|g)?q=kri2(pP;hilL9|W?qO}OoIttO6hiJ_S'
        'qBR52ibAv^5G@I!6^3X{K(qovjN&pxD*@5E1kqZ7XuSc^x(Lx)7DVd;MC&|6>nlQx;&q7DS%}sdh?We|T7+mx5Uq+3qo_c%DiEy-'
        'M5_YPsz9_V5UmPCtHMRAvP-loT(l}&v?_f5slw-<Dt!K_!snkVT(Bx!uqs@zDqOHCT(Bx!uqs@zDt!K_GS;iu@MqoSHvQ}9)mF2%'
        'BOfI_Nr$fg5PoSsio~VCv11U2&y|nzPvLF(C?2LBrXHp)rr`$d%(da`7tX#tEXo`?*=P!>A&LE7t#M&@vTC=XnPsnI_Y}iZjQ?MX'
        'G3&l&XTP5Ps6>1AKc9SQ&mI#s!l~!zQLoUa|76nZ(>+2xLU$253A9+Je(f7>dEBeJGjGG!fUw_z?3V=^*EcQGXwm`y^7x$}^*?2P'
        '``=P$y8e5N^FNz>`Q(#5H3||q_RKI$uvg0J*KV|iGhMVLnrs^DM$K&vbwV=N<W5_w>T*rLW3a5$JsguSdkX7{CoZ12c;d26T<Rw!'
        '%vpJP)?S{qmuKz$>cFGHqe1v-vzIyQWsZ88qyJ|!NB{B5$sBz_2I#>OK)+BH=;z7>jjWDG$fFO-+}vZWYvLQ1JIlM%LgT}f(B;dW'
        'VFKq~b*{>qI3^#SX^*up&JvB&6AjxyPqfFu<5BxxP0_LXU$asBnF#&oCsQvUwby@0y?uL@Cky;S(ncRh<FrxFtMa@m&#S8c-4xFg'
        'jj@!tSl|_i2)=}fu<#lMpFo5p5D^rJ@C#9>!@_G6I1xS&aa158D5Oyz7Kq^QVVwgJe!-9NfrvQ}5fq|O5fE_}L@WreQ8*_M5d{%G'
        '5OD@X90d{60ukqh*C@;hY1A1Z3Ux*x;;`@@Rs}>PK|~xx$RJ`-@MCxs$|s~zCqcv}h`25g@tN=%g^KVVR+$sw<3v2?L_Fg}Jmo|@'
        ';Y2*<L_Fd|Jmf^&=R|CBA_ym9l@oED6QOV-;+%*@?!3fy<cNAectChSj7Q#<n}E6fl_Gz^vYuw^rD^K){bl$-zZ06}|A*9Gb2Q(&'
        'rR(x=2l-CRlxw=B8I4XteuupboxLqg);BG^S?kD#<-R&Z957V%&X+$|^TW`1u4a4cIQi*K+J!Dhco+KF1l>gc;hRRsh#S}~P5dwN'
        'u=KUUYXAT'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
