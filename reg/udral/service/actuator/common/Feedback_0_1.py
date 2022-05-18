# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/Feedback.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:37.361614 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.Feedback
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


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Feedback_0_1:
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
                 heartbeat:         None | reg.udral.service.common.Heartbeat_0_1 = None,
                 demand_factor_pct: None | int | _np_.int8 = None) -> None:
        """
        reg.udral.service.actuator.common.Feedback.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param heartbeat:         reg.udral.service.common.Heartbeat.0.1 heartbeat
        :param demand_factor_pct: saturated int8 demand_factor_pct
        """
        self._heartbeat:         reg.udral.service.common.Heartbeat_0_1
        self._demand_factor_pct: int

        if heartbeat is None:
            self.heartbeat = reg.udral.service.common.Heartbeat_0_1()
        elif isinstance(heartbeat, reg.udral.service.common.Heartbeat_0_1):
            self.heartbeat = heartbeat
        else:
            raise ValueError(f'heartbeat: expected reg.udral.service.common.Heartbeat_0_1 '
                             f'got {type(heartbeat).__name__}')

        self.demand_factor_pct = demand_factor_pct if demand_factor_pct is not None else 0  # type: ignore

    @property
    def heartbeat(self) -> reg.udral.service.common.Heartbeat_0_1:
        """
        reg.udral.service.common.Heartbeat.0.1 heartbeat
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._heartbeat

    @heartbeat.setter
    def heartbeat(self, x: reg.udral.service.common.Heartbeat_0_1) -> None:
        if isinstance(x, reg.udral.service.common.Heartbeat_0_1):
            self._heartbeat = x
        else:
            raise ValueError(f'heartbeat: expected reg.udral.service.common.Heartbeat_0_1 got {type(x).__name__}')

    @property
    def demand_factor_pct(self) -> int:
        """
        saturated int8 demand_factor_pct
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._demand_factor_pct

    @demand_factor_pct.setter
    def demand_factor_pct(self, x: int | _np_.int8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -128 <= x <= 127:
            self._demand_factor_pct = x
        else:
            raise ValueError(f'demand_factor_pct: value {x} is not in [-128, 127]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.heartbeat._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.add_aligned_i8(max(min(self.demand_factor_pct, 127), -128))
        _ser_.pad_to_alignment(8)
        assert 24 <= (_ser_.current_bit_length - _base_offset_) <= 24, \
            'Bad serialization of reg.udral.service.actuator.common.Feedback.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Feedback_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "heartbeat"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.service.common.Heartbeat_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "demand_factor_pct"
        _f1_ = _des_.fetch_aligned_i8()
        self = Feedback_0_1(
            heartbeat=_f0_,
            demand_factor_pct=_f1_)
        _des_.pad_to_alignment(8)
        assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 24, \
            'Bad deserialization of reg.udral.service.actuator.common.Feedback.0.1'
        assert isinstance(self, Feedback_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'heartbeat=%s' % self.heartbeat,
            'demand_factor_pct=%s' % self.demand_factor_pct,
        ])
        return f'reg.udral.service.actuator.common.Feedback.0.1({_o_0_})'

    _EXTENT_BYTES_ = 63

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8U50gH0{`t=&5s<%b>F2#a@nFJQnV;0ileq{%e&@oFPD^PTS_7?mz1<#a!Kq`7VSV8)J)fG)v~9%-BmraE6|7pJB9=_5Ju_%'
        'Hjr~H1PBly0pdTwe}XT*`{0X_9CXMbzgHjgJ^ToeQ!>EJtLd(;diCnP-}|Wk@X5cwy*Ot+)l2zdtl}hUC|*dG$PZXE;ZdWNb@EI}'
        '&Fkvvt2~h%G~?TcIj=vfmp-b0TrXC~8Zu3JQH#0i>0MovEnOCTw9C;($~qY0n+4yC%D7-jglW36#UqC9OlL)enL1e-y~TOlWUae('
        'wb1DDLdh(pk&l1hwLh!3=C<a4R)17iPc@j<g>06ZtNMLRGh+??UUhZ!Ey<I3z*x|TnPv@5+=}D&q6n&&C;4>jy~A0do1E!doD|P^'
        'R>WycFP?YLpL?W{b~uY=%9VQ1NVArd7qk<yizS_TH&t>k<?&{!`5rGuCI3{TDRm>^>7Ew#))6eY#guMzvKR|qs?Of>1JPsA2JYRU'
        'Tafbn-_$#G^`(Z=ER9(a4-fQ7*~Hq8c3Dz_gC`qt)~c(y8duL$3maKV&*(lA5XgDginfl3Rk5};M}v!3-8j3~uU)%Ui_3TZ`N-Vd'
        'ZNbANOZQeZFFGMc(mc%CVMnI2!;&!1db|i*n4|3E8X6G=U|qIYk{m9FolNOal}&Z1H1DX86+Bcusat}_p-goaY7B4Y3rPlHPw>=S'
        '>vADm2@j<Tb5`6%cP!h^hIZC&N5Sr3TrHRm<19=wnl8_?LJy5>nN}hzlQ`4`v?Y`}WMC%^`HxBox$#ufs&;R$Z(qIggD42r2W*EO'
        'b{H1a5!^F#o#ct_4_PNG?UPz|c!>4z18JvL3Fo<8)M7g;aD#R7gfH8kG-Q*9DXa_2(OJ;UGW%SX^MYxa?uBl4T6a-esVJUcDh{FM'
        'Mb_dmEL$ys+xLVdS*2s*T(%GO7Xo2oUm!!8GHh|CXh>rQG+<YfNt+3k&T{Gt4s|ap?uNhx*_HY*fB`}K5*P|CJHrHp7fuIKRLfXt'
        'i|5+z351~pjf2IKsnERG02++;L~64l*@j&E1{ikm!}e(JF<Xnn8sd<w6pWEvSbFI7(9DjBQoHD=2KqTG__DWDevm^-w6YO9UD#oy'
        't}O9(A+A&>+6A!&WybxtTpRbR`3p5!h-$(>zB9v$-t_i!+-VV6&{yZJ1@-Nw$!Q4?L40V`1t3wFT}rcp>}jz5Ms={Ij5HVeoE0%I'
        'q7lWkB39JP%{i*;LqdlUY1xvwk$O5j<M<B4fCY`IOsAN)S(#`zu9<LDr`%K!v2^^lX-URXSD;O>51BwG@&wcC<k0UVSut&2PbwZk'
        '_~M$|1@XOV{^H|^``Y%~>u+DXO5#2az<Q4$#9f<W0FW=tu|pDu_Q4RrGLVQHj@o5v_B?dUOfz&Ol(P@96o%3gj5GuIuOLwsJqRky'
        '#*Ko+GDHJyY(f$x<}A>y&3iCIU}y~M!CqN}#O~=HcW~&|L$(==Y_$p(N#-z#7;_rt0SLQUhY#Z}u|?Pz%XS+8O5lav^b`02$?*L|'
        'i#*zkmI-K^8SLHcTA2dZjd&n}xCby_B4y!Y>yNRc>7FrQYu>EX86=sN3X68i$GZ-4v3$7v1WzVj`peX*2mBWyydw{&f58dVu|*!Q'
        '1ZRmBMhK-EQuz1QceXdT-=0vZOMR8%)tRA4rO`aJ(GaQDYvLQ?yW(}RBeuo+;s+)Cb<6=DST>LAPpW4cZF#`s2JzC6alKugZm6s*'
        'S{yeL-hg?Dx;joIk<Gd~aSOrP!7aM_8NC1eD!jAEDD*m#%eo3S4s)R6Ro=<!>czZl!bTbZ*fOE{2C)#}=m}g#yktTb%;2N|ytCm;'
        'T|L*w&*(z577_N<nnH#%4Z##Rqit{a=RSe4{Pvi|rlJqL*2rNbrE)I9+A6TeZGhQ3)@3qbO_=~K{05kvbWk$1ON)KgAUCy6$n9Z+'
        'yn<j|PPUf76+s))VP^c?7-1iZZLtT2r;O(g_mZsHk3X!%M8P$LsE0%92%FMHmLw+Hz;$R;4;tDt%2KM5q7=U}LW5CJU|AIUk|0>C'
        'WsI0SIf<an97jeub-@ty8O!iC)wi^9@eYi!NpNXG36^pghqa{%7A$)PuM}b&$f$V;7l|1SqzFE25;hnPNoo4tfh8&<9LK1!H9uS='
        'l~*}y@i&483_(wW51T|l+K{ZdZYCxVK~ZWDgyH#>q0f0-xEF4C*%#rxp?fQ1p9frsq9~-#Or4mRIP8D!g=3$|3jzK9)zEkF>5g}v'
        'yb$<7?+p)rew>#FU6?+^y>QoU#=S?o05ScqG4oim^iPg%>G{WadO{f{KMx;niZVNWQ9<}<lT4pE2sSAkGqEq+N0%}HAf<6qWQavS'
        'u17%13M6O+101DgrwJo~%@_chsm*ZZN!A*}G{pCTM=`>HE-Pe44$paZbP{qjWpb_?0exO3%J@^nFBFp#K*2YwtU#bK;?WVc>lQ&Y'
        'L6CJs*3%cxBY6Cv*ocN(@j`AgB{3R&sSWlGw5D+H1qmWCOED4pTKLWf%YjV}OnPGnaLF5Gh9mil0n4#SfM&2E9HMwVoW)E_RU%4-'
        'n+crfD?S$(<jnAddi;M~oxCFTb@P9h_Y>yoiAI*!RXA%9b=YZU5ExwT4R~_-fsx!z6Ub-9aABr}G%c>hN7b{pSWLOhL?`hxy1QK_'
        '2{dQ?uDJ5I_2Sl%`>I(jz@eKF>aB&ciFG1QMUxurfEvfCrhqtt2Hl#c=jQHj9dYytJI>aV?*CDuPu$-+=B^(nI)8s_!QDSWbm9J1'
        ';OJA1o^<qSN1t)@Sw~MfdfL(F96jUcmmGcG(X)=e;OIF=|H#olcJxI@|HRQRJNl=NzT{}==vN$l+0m~$`ZY(t?&vFye#6m4N0%J^'
        'rlaQ_U3PTE(a6zNM=v<K=IBL7FFE?Eqpvx7+0kz~`fW$Q<LK*-zTxPfIr`_0{)MA&I{IBl-*NPgqr%YxM?ZG-=Z=2v=&v08wWGgr'
        '^mmSaVd;&9dDl4S8;id2ZQppuH}3d`@QnlC_}Djo?i-)`#;<(i*S_%^-}s$xeBl~p6;ResF&QFbcdco%$)Gw>3<`ah#kX*6TAlE@'
        'l66}wjZ!4xRAfY|Ve5kPTXWMYj5BgmSCVrRJv^1&zIkJFd;K~ds4fr^n{sbTQ6yl`r$+>y1n#^*@Ve+y)TN1p=W$9F3+q?EzqxyJ'
        'hiVqpFW19XfoRsaBILRqP6>U_<ZGqL*%0m`yK|xNfJdI1AlX#t7*z<-qm5LdEV!@G0q!aEMM_2aUoe`Tw~MSZoS#!xi`iUYo~)S4'
        'nU{i^Sn%586b&}k-@UzgbDP%Nz5Sq7u>GM`khdPIA&@_e`Ch@Oeqd@g=npxWa){$T=C&jpnu0x>&i-T7JY1Gb?Ei3-eN~#oBc7I6'
        'd;ZI`Uly_}F<eemK^~Mtix_O}&&|)xiT~O^3bH>>Kd0#DB>lWdKQGYFEA;a+eoE2)MC@$~A?_}UM07+dGLcuutgXRYleN{=v)0~_'
        '#9kPrvEqPIR*6y8n@C6~{Ti&<)dFN{iZq7xaI@_yIM@caN~B(8qGgVyyBI-I{lrv0V?K1(M-o0nSy~QAKvPQ&1#c%dJ>^5WF#W?2'
        'O0Nv-vkOdMw4)Os@Omqw!mN575vtHSSFf+G_IkZ2VZEr86)8`Wh{xq>t6i*WexO&^UR}L-DO$U9@#5GMZN{R#th*X#t&$3|*JYEU'
        '(A5r)C0kvOyAt8wVPiuUErbWf>iS0G;%jE0m9;33+f<1%x^lS|ABZ2@-TzShq#vJr+;3H5QHi)u!HD>~tp)KZzMuVn=<$C(^eDw2'
        '#{BOw;k@Z=pSWP5?qk#c?2Yw1ja%<txxTrvPKe#Ob!}(!CRKYYZR$xb5AoFwaxasKgtu0c+9(k^b9U+BVpbRwFU(Pcwc@2gUCI=L'
        'F*M~u5AZq`6UBdsm-hdfaPdF)e@e*r;Y{QcKN5vdLRZiAk1<DUcNX-1@6HhVC_c0710EGT49q$-M{7*`z6J&d9Y?A`2Di+a;-D(z'
        '6Se*+jxP$%%KxY!MHuH#2nM-uC$sK9HT6BW0dzuuuL-Yg(m5q*@7HwwLvhHZIr1@FC{EFd=01O3CeO<zDpr`s*Q{9JW?4}=Z^^c7'
        '^}*Z@5rwnz--!pu5?))+8%uZ1((GBv>@pf3I{7m7w1?vEPlj^E=QpyHs?+Jzq_a9<bIyXNbRs`>w4YAGwntwj{;&<fT!sR2MLkZT'
        '$EnF4{Sju|_o25KoYr5y^Gl2hCp~gf<KI3A`##yL1r=ZmbNmO*ChL8qqnVrjglQT5N9)#mCHf-b;r3M8O&CYPcBcDyVoJU44Twjm'
        'h>q7!mqV2qtw(rc;#|blO%r#qpg*jyZ<os2&-frwxNB{i4%8=aKZK)TRJq0s)$>-`0@j!&k}>rt@~B6$q^0Wg?#wqF#^L*P%&ErJ'
        'pn`c;H1d|&`yXQO|I!qtQvH5#%Qoo5$ceGT4rHh780(8En$F4EC_YtG*a>d{S_q(U^Zd%%g$rLNBr_EvI+N}qGs+mYl1^Xfv^O+q'
        '82ZFy*1qIq%WNdRJWr&pCTa7w1B>5447kV4v$LMEC%LLj@7lzLgiVhQ-fI|Wvn}YEgCbkyw=YcCs-W>L{>+;|Gok7k{V{ijqFUk*'
        '(zLg@KivSsSsp4z+i%16etiBp`JuD>|3ZG~pC00ess+z)4VQG<zxXrFBmJZCNZ?J#J+WdSa-hyrP&*^zlpPa-YL2Yco)Hs->pYV-'
        'y>+_~1)FrtVxr-J5l%p|RTONv6P%(qIas1byk38J-zf^r>F~sL0|6GpX;Zl^FD_4?n)ZZV<)G-=TwZbRba~P#1fx#Dov6!xE@-tO'
        'FJx8_D2;2wK$vDZ@XlnD!%GAz7I4{_eKlfyVUOWU_J4s*HGlU10j(L{V*gXpsQX*<qi}D%z;HgWfPBFEjC1I8ZqUiQiqXr~Lx`uu'
        'NpZ^7R?ZrQ{U7M@{=ZUZz5j0@eU;t+cl@i4H;_7E*XkQz%vWa{v3r58XaG_X{kiwf27zb@B)ephY?>ISh-_E{A*DpazWRk7s+;Wa'
        'oNGC&M10p4aNitDuSlFmY;)pMFhA*Ht*k@bJ$Gcf1CIV1YuRrkUnl?o'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)