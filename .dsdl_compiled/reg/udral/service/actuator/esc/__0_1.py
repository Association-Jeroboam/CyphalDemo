# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/esc/_.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.404143 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
        'ABzY8Q-pP50{_ig|8L~Rbw49c?9fTuz>QNhZ8QBANVyf|OA(;(p#gM~94mMFQc348Eu6(HIV+Bj%b_`>q&>($^FxaoSfByS{=faa'
        'H!~!6SJIt}{?I+x+9ikY`@HvgZ}@L-{`a44J>bvcXXQM#X&#TQs<h1YOF79^JWkB4G*;KDUHouQ<$8v%>G`}=?Kkb_@7u51jm7uI'
        'x+qlDW)BuWJgciFshdhIFZu4ckTZ}FmAZ(Vw32xYHkUe4vBYv&n<`c|iO22Y?eV3mtTqMFd+THW{hRjbgQsu&NBjGB@y=M*b)_dw'
        't!(>wyLfl-dpwytPG8ZwRF#!VBm{21Ui{H`s;^Z#E=^UBb=n>+el)hGsS<@7xf++U&f3LW^e5MocJciasC|7xSHFP<Z)~@VH#0*@'
        'e6Pk|Y1_qjE_B^4qTP9!$$U@EOuP7L*-UbsjG<?f6X$U%YdNlA4SE2V+r@X;0N~|K0G)#oumolR&2jvG{3s@ev~_z*N@mhR#!40S'
        'I6U|D;>~etlJ?V2Hy%7V&y-NPO6tlKIuW*1Diw(-@H@{{B{ufYb~lB8RA?(wW%WgYMN?CC3w3cJWRZ#)h(I3t>4<`4TIow=<LJZ6'
        '%tQ@#w#L%Z=%N;8iYp+>mt>WWKxO4g;`v2mYavOv1TiKOX%#&xSuPWc4<X8hLNFl!>-i|!Jw88M6+plUh$95%Ocg2QuZ@toHNrL}'
        'IoF9s^aLbR)l@>?R82MMstdj?(=Tupa#OI_65rz}f`P2qa7;Fti&Yo!7`c&18F5jWrnIrxmq{kDoXAOcRlq-_vxZ35;2~?$w<+|O'
        'jS^QH#&Mi^aUAVARR+%!KhjCEPIg`-89Zqko6p5$E;z1i#{LnI*~$yWUX!|TP6LHX&dHos)$A4c3Q+;NPM1qEE37p60`|1QBp*bP'
        '5L@ERKjW$RRZtaAfxE0~o#;|x0dCm@`wim5By4OLv18gj3bMjK9^{2ZAhK;{&=5MwJReeq{gT8~DXHTq>&n}6*?2_wJX>e!RkDM%'
        '!Wm!&l_ts=X`<^&La3sdO|UP>UJcyod>c3ws=hMSi`W_GRLPVG+y8}Ks_t38$2w`RG7Y{ICDui;cR%ar_gAgl*7Ev%AZ)HwIdc1K'
        'G9L+S7*$-rxM?g73Mg94d0Vj&DhfRq8LFECByuz9BVf4aZ)b@OqA7CbwpO#pWEw+6Z>5i*)tqVrSqqj3)lyYkWErL*Cemu_jrt)H'
        ')I=sP`iS%~?t(*wJ!TcG49YpQ#U8VnxhjY@NtkMRQAyBMxw&Gx-}ZC%{K;?kchAMq&f)&*we!zT_9O9dYvuDW5;s`2+vipxZu+}R'
        'OX+`c9QUC*_}o(qDH2Q(+cN%zW483U>8NiGS#1VpeaPL%%=74C`!-Dj!=ViL0XzTB|LecF&n5ne!H>v2%@n#X15OW@e%!wLX3y1+'
        'e|rCB@Z-^qfU^G=^q0SfAM0x$dW!37y}r{B(%;I<VI!<E94c`KL)xy5U5<`dGd$y`mf1aAar~|9N^`~0emlD|n_HdOIMi!Y@c4wD'
        'IA7wm7G)vKmU*Rf)Mk*opI2BFR|ZM}DaI$cEaVEyJ3p(gUYBia#R*~UeJi`wk$8=jesv^XYo!b0=*ZLr;}~a9BJ}p?b19YlTBGpR'
        'a#o@^MA64UOQzbEWtmf^hOM?3hfN7B4j(H_?XxUp_}D+_?x`XHW~OpO1<NOFz^POdK@=B)yJADd7x73S<0Jh`Y6k$Qkg`K6@AyG1'
        '=zX?-esX+pbRH6K6x~|gQ7HjfO$FXfkyCo(5)iQE{?TuCezU(9iybR+Ly%}?0qNxzjf5s034qX5vdKK6(&-}H*YDiORH*Ajl{I0K'
        '0v0o@kW<wHLCQ)S>i`7U%_JetLKcZ)6iwx+Fcz+|BVX=e#K<(Y)oE8|Z33!2g7yfVu?$-^7Kc!p?AIrDqHg6>)$<;)Ttg+;iJpj}'
        '=OwRa+40STY;RGI$3`9a9O4)dO)|o!we6pn2F&l^VPhGjh2Igj{EXoARc3(b9cEKsHh|^4$Xyr$nIXqmJeiA2UDZuzl7krqDSY%V'
        'sxo5#8b+lyP@Fco8b#VI8lcMB7z){{9(nZd#SZ9%8v!(fgiqk7m!Jw89Zca<afx0d9Xx{jWH$s2w+p++N9U)<&&KBmhx^CR&k1lz'
        'L<WV4hLo)L%5DP124eQX2hp0GI1}{6<HUbpTafg=go7;rGUIkJga2pEtY7GQOJ+v6N}DuLCTv@a98V)1Tv7Nq36UQPb|j?&gdLRr'
        'Bty50!eL6Jh0$P#5Jpy-0Uq{+x$3t7w!^ei>MBzzC;j0US`4|VldQP`^A1JRThZ4S6dyb|fUu(ooj8&RUGu<g*>uqR%LY)BE?CCw'
        'f@@a3j7M1*59JAE>Y{P|QKhKyqr4E}GV01lhuDWHvt-+-&g=*)ijm5sO#(7XR=HM{v(BnEK>|&K5es8R&|ekK8uuh7Jd?=As$f2^'
        'Gd6mTg_UEml6~TpR2V{@=Lt@g1RjPoD?LQFvthbH+uXOo(d(ek$D*W|a!rg=$|TLuZ9L;}63an1%`rV~Dvl;iwwbx=9G!7veuqM2'
        '7H;JyDs=OpPJKji=Vs%Ug88W;qs*JS-OibMqG^s0(@yVGkGB0>B!o<=r&C44m9?_Ni<73Jo7933or%iirKX)=SLN~+_Kuqx+DXJ9'
        'G=DRbF8g9cb%jH`D-hJhrR0e@S=JlE<%A&_%1#_l+;Eb~oK1%NfFP4b>s5)JlLI0#tT0Boq8J7z_DUo5hbNa<QHoM^9q!GHOG1^Q'
        '*%{@YswpVPJdVf{6bz$2cBXw$Tkn1saa8=@kHsmOZl-v~b7}HAj5fgC&sut?B$6@=w2&^%LIK29u3xHj+Y;39(;D%wTaQNK;iJzf'
        'IRJl9FYEhU7UZ9|<h8cjWd;$qC50zYir837R1}yY|L{iI>_nu24-%tHLWO0^fGm=>8&U|i_mUyijOT)OIgYqIgB7xSE>3q(J~`YP'
        'gy@rJd%KP~TkO%Y#e8gTBVK6M^#9m!Ueebw+z#-}1(duTB)_!bB#8jKl2s}K;ujk(Gh?Y=QPHT2BG0eb3|Y~NNhK+nvmJjKi?iXB'
        '^bV8xA)E79EvpL!4T=k{beAeO)aNW!DA=$9PLstp;Fu{=H}CK$ZaEKxxl~FsKZ=Vg7N2k$SkD)ILcA~Q>;gUjTRM>HO9aDPHzv)O'
        '34aiYEg_E9OwAEu`v~wRmHA_;^ugTSat`vX6xA#t`DonPuL@r90U9$)B;??w4pIk<-YGijgTM>a!<{7OzJ|1NXpX4vFh*zGyeyr|'
        'k2T8JG6IBSPWN~A4vzNE&X&6mSX4H7?Ewf#oSp9+?LGO7{ljRX8+g}hwBBeigmUuv0>56}M-f%(`u<+W!J&X7$%Bf@+km@}O>L;Y'
        'B3|KVkB+O=nPuc9Ys!?ZK#6(<+;;HrHvF;zt-CEnv57*EfEB2^tO7A4pD^%1bbajJ^(hB~1hHO_Cfdc6>$kc<8Lfo>tw#dr7$`Ay'
        '9Woi5Ou(!PDp?j8v;*1BIXPl77aKaIq39-6<U5Q(brng7!JgmygW<im(J1n8ko&_SXh@Zsv03PN4LVG6cSyj5rcDu49^&GjPgfX1'
        'P4HH<JbA(Of$zKUeYU@U^4jQy8?gHg965`bspFmLi)^ba-nvQ}T?4-`6y+|v*rEVIF`;uGI#euJDL*QB29u&o^xe$}sub2#=$g@t'
        '#+!t&*-@xg4wEx)ca~84j`!6fLz==g)STCqEF79gNl^8bQpM_~skur!ASIhrn@eq}BMCD;kMOP_Wxd4*S<coyX-?=xG7l-CGwuM$'
        '<^F_?yXOsmY~<Y36x3RAx8mpGHtJARIIJns^^I;fiKDtMT`-XC+-aWMgRZe!*0ka1;*opj8>c&WvD1}Ny*sE=*OE*=;>iNJi(|bz'
        'tpi5HqQ19GGDE`wLbRnZ`4*7)L`@A3m1@`jP~#Rhm`|(@6kl=LHxq;{H+;2x;l^8!`AEP}i{J`$N1K`ggbW=g4AZlt<d80P#!=Th'
        'dOPr>!zX(Zc9{JtHJNu|%JP!GI9roFxh3`)u+LVm%$z)b^6cR3BPiy}%-L#((DfTG%cEZP=OG$F3`9YPAVN+l{Y%uwtEC#pgFR|q'
        'DZT0Ga@z6=@nK&$-WYyP_jivE5BHDuAmGXA!SU(A`DcV$zRf4PeE`m<V8J_H-stvOvcpSaCCa1QhrxF&_EVjqWhRQ7>tIcGrBy?N'
        'b5Qt^g7WJ_o$LlH`0{A`aOcx8`*L^Z{NVU#e6kN~?YZV`IG^D$=TiDkO+RbArARL&>S0d5W%$FyX)vi!e}DD9_~_;BB{6`IjY(58'
        'b1zW3>C6UbR=WacRn(aSF`lA*E;%TvMw+F0n=fbm=y_GJkV(2z*-+M<#7^LNEnoW$LmdR6rQKXwi!`#kb97rOPYoj=pM~AIWT%0L'
        ')&2e<5M10*?3~b)Ny`dVk>5LTS!aMY300$wrj(mh#tx5|Z?8NngYpXHBUQsec_-}B=%U*|%P(PgHD`#!Cd5-Bt4h1G(#{R6Z11N|'
        'euTkR340<X=ExoaqtkhKN^@EmAOVO(EuT_|aMePImzPFU{nnDppqfs3XupOIJR@6kx}glul_4DPBLRRZmH}x2AQXy|xQlT#f<R{V'
        '7PX6MKgfej*o^huy+rY%FjvLMqaXB;Nb;`Nbe(Lk=aD>e=@!8D<NYJrp=Sb_PwbqXJwH6*-%+&V^CG7p>P4wV;nx%rxPg0cH}|9v'
        '@8^w$tEZP*(sWJ9YGSTo3)f)qW+u6;c0(s@gTVxtz(<0J@Z(;N9#9ZmBD%@Aqlub_3=S!1np(St*3H?5w)961z7vi5PLx^<*Jwpf'
        'HaB)oyB%98HwL&;dERY;4rr4wU27fQW8oQ2<w2BPYr$ifwCnfQdgHE(yyZdhOutZ9+M?2jdwz}qu7Tv8n)LOJT}k_gs<#w-yFCtZ'
        'g@#%R<lXRIhZqRlt@QJWXdrMHSxkMA?#@9xA@^QTC(6i;FIUX9^kN0A1Ep<-N4&K;ftBtpJ5<~-qu54^!LLHGCvaU48gjSqyY|?N'
        'NiQ*V$5kpNB+jpDaGS}vl$06;6Vv5xCR3^K=2hN}Gu(?kXhfZma$=md;f0y3Xmk{&Jw1$>BJFKq`=%8gCixdMK6ss1GaiPBdCk{2'
        'e)o!X-j1W25L%;GJP^!z)5XRs9tarb#(leQ_3BF@?(=JC?VPb4g71EgerN)nf_ASI(P?tiY4<I4Y8P*gC%J7GKMya6PINuaRdG>g'
        'W1y4O-|gZDPjvl^f1lx}e+P8&ov|s~g}94|ozEr)IHFy=d#GkczvQq#W=vqJ;mf88n)0;G{$cUQCsa<0i?v1BKhoW!CPx~Yuiga('
        't{UxswHr?#{J~BZZ;wkysD1i&Gl9BjHQT2T=!?9jFK>-!CPhx8r=u|%E6Jyk?NKwalV*}d**n<}vOmdw^m&`T`&FC$`0MPwqwFWy'
        'pKoM8&Hf_$%j~bRpJgKZ>+El`zs>$G`}^$Y^iF5C`E~Y->>;QtI^V2`(|hC8zhhgCGhjpfp~BeS^>!{0%Z%L%vpp}|`<w^J4i~Cg'
        'egXHLfx+9S0%{;L)TEbcv*X2kCxH+>7VqNTA>I0>efq|~)BC4?Iu37k4hj7ylpkf=%p?0{_N#&Uf4pl7dLOK~)sKtsJ2xWY+t2aD'
        'uN{dU@`->?mPq~N6eUHSs#4YZuAq3~eT4^xwBG&$J7^C#_VM3`U%|!R@7YIipR#mQ;HFr=Nsq?=1HQC}#Um{M00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)