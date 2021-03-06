# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/time/510.GetSynchronizationMasterInfo.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:28.996275 UTC
# Is deprecated: no
# Fixed port ID: 510
# Full name:     uavcan.time.GetSynchronizationMasterInfo
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class GetSynchronizationMasterInfo_0_1:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
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
            uavcan.time.GetSynchronizationMasterInfo.Request.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            """
            pass

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
                'Bad serialization of uavcan.time.GetSynchronizationMasterInfo.Request.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetSynchronizationMasterInfo_0_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            self = GetSynchronizationMasterInfo_0_1.Request(
                    )
            _des_.pad_to_alignment(8)
            assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
                'Bad deserialization of uavcan.time.GetSynchronizationMasterInfo.Request.0.1'
            assert isinstance(self, GetSynchronizationMasterInfo_0_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
            ])
            return f'uavcan.time.GetSynchronizationMasterInfo.Request.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 510
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8!LWp40{?wf-)|f>5WbX<q?Z<`N>fCE8YD_8qHQ9<3lb7-gHUuNjS@h-RF-#la%1YX7u$QuAw_B*K&fPjN-^*JWBf0ScQ0_4'
            'Ha*>G*EgPT=KJQy)A_&tS?IN&aJwFtu2dO!V5Ly<H<2sIcwwsAIO!pVtDB%?MX%)#;~L^=y!$L3$JMaFrPg30_QKVDZ=1q57G|%!'
            '$+f5mV!aWgLg>uP3bOCO?~iqX)@X|6rP15Md9Yjhz+`*yYXi>5u*64T9T^k;;!l(J(>Ul2=KhG!Vp!(Fdn@zCgNu)2xIT5}`M8UG'
            'obHuSTPOq(h|j}Y{6HQ-$!lXhmu1`u*SIr{Er1LPcr84}u$Uf7<}qB}B^i!()4!+0XzpGN^Jo&OOSO!l|8QKRP@7Ph7;e=~u4KV2'
            '3>%f=@ltrfJ!#@%Sm;C`|0F{UcfZ_Nf4vy%*+!O%6MfuE1W`E3&w}=;S|eFNJPGr>G)4URy-U5`w<Ot^X;T98C_EE|cTCWirHIVU'
            '24YnkX^k1nq+^AsQ|XyGNPbcelc#G6T<beDjVkF-C)Eg>u1^xk`dbvk<i7y<j35Dd!)j|rlCqG*!d6{0k(<V|LzD%cr9<JXHgsbX'
            'DK%z|gOa=`1TYQ$(AXzgzyC-V@IQ(FywEt%YfO5|U2Ef64)mwcL&BikmFYN;5DJJYGa5Q^%uIlUWgD%DGO^Ljkj*l(ly0rPHy!uo'
            'NW@6Nc|22t6~0BhubHfBYKu+=lDE|_36*Lj(-|!Bqo0Mc(WTJ-bp`9P8Z)63bJTmPPpY*EIBNNsY=t@$W0z6O@mx_0-Z>lgTzalR'
            '4?R*R`Sa%(t~`+b`}Vv~$H_d0H@K-|U>AY7ag`e)O0Bw0^DxQ!Q7eV9(~F}Z&B}=P!rQx|EJ>!9F5wr+y3;5n?D)Ku5Jo~Z5dVy;'
            'gWe05)3&HPpg34+a-v&FO{*fkh@<qf$SYIQP$us_hof5PcA@Mvxyzdz`?!o(@EyGNIO6r=h&P_&$`0Pd_gC>2et;k1M|c|<evF@_'
            'S;S9I@D6@PsBq+|bK~~Yxv)ZurdyPjBZ!h7Y4YPmE4H@jG7Sys^&@37)KG3|4@0oCTXcC!={R7Ne?g6q2tmX_SlK-TN^aRhvTY|5'
            '?aH~|)8crSJ1?lMY&i{dLabNu^EL)%xG|;sjfY03eW_nrz;L;%AB`;S-BtXmgZMfXgHbVNpl<G^DcOS>yu7Fzo^(Z8Cx>aQr59~w'
            'zS+V1BriTVrrJ&lj+<0Ba1-O-uP`Rp>|ezAhWqFS000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
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
                     error_variance: None | int | float | _np_.float32 = None,
                     time_system:    None | uavcan.time.TimeSystem_0_1 = None,
                     tai_info:       None | uavcan.time.TAIInfo_0_1 = None) -> None:
            """
            uavcan.time.GetSynchronizationMasterInfo.Response.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error_variance: saturated float32 error_variance
            :param time_system:    uavcan.time.TimeSystem.0.1 time_system
            :param tai_info:       uavcan.time.TAIInfo.0.1 tai_info
            """
            self._error_variance: float
            self._time_system:    uavcan.time.TimeSystem_0_1
            self._tai_info:       uavcan.time.TAIInfo_0_1

            self.error_variance = error_variance if error_variance is not None else 0.0  # type: ignore

            if time_system is None:
                self.time_system = uavcan.time.TimeSystem_0_1()
            elif isinstance(time_system, uavcan.time.TimeSystem_0_1):
                self.time_system = time_system
            else:
                raise ValueError(f'time_system: expected uavcan.time.TimeSystem_0_1 '
                                 f'got {type(time_system).__name__}')

            if tai_info is None:
                self.tai_info = uavcan.time.TAIInfo_0_1()
            elif isinstance(tai_info, uavcan.time.TAIInfo_0_1):
                self.tai_info = tai_info
            else:
                raise ValueError(f'tai_info: expected uavcan.time.TAIInfo_0_1 '
                                 f'got {type(tai_info).__name__}')

        @property
        def error_variance(self) -> float:
            """
            saturated float32 error_variance
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._error_variance

        @error_variance.setter
        def error_variance(self, x: int | float | _np_.float32) -> None:
            """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
            x = float(x)
            in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
            if in_range or not _np_.isfinite(x):
                self._error_variance = x
            else:
                raise ValueError(f'error_variance: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

        @property
        def time_system(self) -> uavcan.time.TimeSystem_0_1:
            """
            uavcan.time.TimeSystem.0.1 time_system
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._time_system

        @time_system.setter
        def time_system(self, x: uavcan.time.TimeSystem_0_1) -> None:
            if isinstance(x, uavcan.time.TimeSystem_0_1):
                self._time_system = x
            else:
                raise ValueError(f'time_system: expected uavcan.time.TimeSystem_0_1 got {type(x).__name__}')

        @property
        def tai_info(self) -> uavcan.time.TAIInfo_0_1:
            """
            uavcan.time.TAIInfo.0.1 tai_info
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._tai_info

        @tai_info.setter
        def tai_info(self, x: uavcan.time.TAIInfo_0_1) -> None:
            if isinstance(x, uavcan.time.TAIInfo_0_1):
                self._tai_info = x
            else:
                raise ValueError(f'tai_info: expected uavcan.time.TAIInfo_0_1 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            if _np_.isfinite(self.error_variance):
                if self.error_variance > 340282346638528859811704183484516925440.0:
                    _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
                elif self.error_variance < -340282346638528859811704183484516925440.0:
                    _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
                else:
                    _ser_.add_aligned_f32(self.error_variance)
            else:
                _ser_.add_aligned_f32(self.error_variance)
            _ser_.pad_to_alignment(8)
            self.time_system._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.tai_info._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
                'Bad serialization of uavcan.time.GetSynchronizationMasterInfo.Response.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetSynchronizationMasterInfo_0_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "error_variance"
            _f0_ = _des_.fetch_aligned_f32()
            # Temporary _f1_ holds the value of "time_system"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.time.TimeSystem_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "tai_info"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.time.TAIInfo_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = GetSynchronizationMasterInfo_0_1.Response(
                error_variance=_f0_,
                time_system=_f1_,
                tai_info=_f2_)
            _des_.pad_to_alignment(8)
            assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
                'Bad deserialization of uavcan.time.GetSynchronizationMasterInfo.Response.0.1'
            assert isinstance(self, GetSynchronizationMasterInfo_0_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error_variance=%s' % self.error_variance,
                'time_system=%s' % self.time_system,
                'tai_info=%s' % self.tai_info,
            ])
            return f'uavcan.time.GetSynchronizationMasterInfo.Response.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 510
        _EXTENT_BYTES_ = 192

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8!LWp40{^vG-EUk+6?f94aW`#gl{Tb8(4ipes_V_}`fDA;hwH@A;&^S@PFsP()$F}v&(wGC+|JDPW}_e|s8xb4v?8|x^${V&'
            '18+Pa-grPfA@K(w@yfr!IWu>6XB|5s2v$z^?wOf0XU@m({O11X%%{J(G-W^etLY%pQCtf&Q-a3g4(-OQ7KE~wN-Yd4^5?FySoGjA'
            '+8v~<cu>6YLGgoPCVx5*Ny1dYr}F1^jLJfjDK<IfY>?0%sAy#LFr-P%h#sq5XJ%)Rgj~r4b~8dI8&n&n+R2`*Z8M$9M8lft;E*W|'
            'qqxDjx69`T#ro9xsgH^eiu`;)jZvbT8K#R{u-geo8O<v4vulFI(b&F95K%(|gGQgUJXLsjaR@V>S&Jn#lSe!sbcG3Gmh2l|tP@Zf'
            '!fAq@j99^6$uDjVm*cY9DvWL55T4`1V!Oy+3bdg~L{;P~x(9lCbUzU$i*VyTMMLzI2EVM8&!8iJeQv(qY&GZR7Z>MR3(Zz*VY$_4'
            'EY;^5t-1Nu{6b@Kxw$YuUoUX4tjjC;^GqqJf<p>tOhV9oCWvHMygPq-YU+EMg))i0-@H}1hO@|UR+Wf^3<s-3?h(To!DzyiIAcVy'
            'R4T|2(jCB%(4=QWTC42h4>t!MXdKHv%rcUMoF@B>>?y|L0qJuQGpp1s#K|g45|QlJDr;Z~yG?s(jE3xa(_Ys^_7f7uGCaT~dX!hN'
            'NnaRFD7oI**{Rw!Y~oBfpWRMbXq-VJ2^FK7RVe5Y`w5NVR3S^z)g)rDn~;h^uGL7}*-*{`J+aiL>JC0StFL=s$vy#tX(Zx-GX_<G'
            'BP%!rcJ^f!gZCKhl(HmZi6O8pPJBOuTr`6Trynquf@=tewCPjD2tA}C#(V`+Lh$l{%yelq9v@)d>&l*UuG{mC8reiYOddtCeJT<b'
            'O&rHr7b%&NE(KS^krLSxu%w1r^|Gr4eu<wepDOu9zvOq}znuZ>-7EOB{P|%C^B19Pz16Se7j7nK3X9r_Vf#!?)EfWN`WgNz|ML1N'
            '%x3=8`!=D^S`!OCn@^!F7xL*<s1v9uGhTR!Uzt$xmEq!-Ha0t(yPKW%YOvGptX>P=+T7elU2H=p(m*DK&f{93tGZH}TII+P=CylL'
            'Y>z4Cd`b<8B-6?3W|-<O;tEpt0K&v*s%r&+s53wR;t+ixZxquAb`#h$y=|eA#=}$bHlN8)xysgEIL%v+JM2@tD{VO2yMH}3HHH3F'
            'NvV>o7>H&_Fic-3+?Z5fxqO)=wZ1qIDT@THNwt3&e_ftf7`TN2F2q`Q=?Tv7rDf&-WEjXNZL=)NdR<6A$YfZgqyrSFlo)&gh2nhN'
            'SYE2n)*JA*Td!ZSf8QlwIp|+$I}qv90s4GT+=f-cWs0YKsF!jmI22sp+OdY!DlQ4Ni%+K6XoyhMI1ZrZHswJPbRpyBL)N1S0C6;m'
            'u>9~$&WK3tl`CtNkxH-?5{2k2Ex~aQqK_B@`H5zMaxK7~Bm|A<4?WUji0!`MWZXxWRzsg4G)-d>TK_}-KoZ>WvZ3(=+3?cJ*4B;o'
            '>dJ0=vlHxWU0ZFhwO29qmsZAG%xVBJu{Wv$YY5t&B?k#YZwi<I4ifAkV@@{~M%J+Wg4e8r?!fT^wCY=YiC^cd{B6F?DZiCLLj?!~'
            '<b`U9iu?KVf%R~JE(}Cebn+JiEi)A|7>HSrQfQa?IsA%67h2^OIPUfqN*_RbK6M#79G6H!PN$;CE31Q))A%au$s+$knswo%0bpJh'
            '<9=g00FCx(hhVTC&tBvg#wb>+*BUh}*TP^AzYuV$!4eD{vWG(fjrBgb@@KoA*BE3dQ`W8HS{V*%Fe*m;w`dH`vB`om*XcBNU|U1X'
            '^rbqeRoVb7G{FReRSsezuaB1V{6>nsz8k~IzBa^~G2;NU&C%aQ{_I=A+_1lQ*a%MZrvjN4IXOv*9`w2r+zNi#05_K$Z!^WSOXc&&'
            '5Uh;~{*(N3TdtxWn#AwnXeWzfss=|#dHdsHX8p`3x(j46bsCEG>8uOqgysZ~_&{&t!#QMR5M;E!f*4B^%O^Wo*Op5qKab%EblIh5'
            '^ILxG!c1Xsp|3(15H~E(VI!Ke`kzHY+7sAVoX|EeOtj6FHj?5;_RMj0SN!U}G)ANV02uv|=^!&9Hh_PfnVP}`EKlX37o5QK8A~kC'
            'A>7>DUA3IcR=Z_BW#v}^W-TP%VM^92KGEyZ!La8+D}aI@X?2)^dWZP&2;x_*I4*<;2wX@Q0Kl%WTnM(6UF<7F$!?~N+gJmelu&24'
            'ZHJ19g9&}2ai$M-3aCF|R8<jhwdhW8(K7gBlOER`Z$MWMT>F7uBZllsNn>jOf%6(wK=(jp1mrR<(_w;ap@lL5Lm-=67dT`!a#h-9'
            'g1IL%qeaA=DmdMmZ7XF2tAxV?ZeY6;R1S%u$>7!is!~Oen-JVt2&^A>=fEm{3urQC%r#+QUkSAGN~J>Ja}{|Ee(oNpsJuhm!l|>P'
            '&)wNaeXQE=&;)yb6Vx{9PLjnVNyDErhmxi*nMcW-FIhmzyf0Zq$$~FgLdl{pX`y7vmn@^C<w;s~lq`D|wi+O5`Zl-F=4Qi}pv}#u'
            'FF^~NzRfM%z3JP$jC(bGo0sigi=LikyVsI0v3s?A3HqnG?CU{q%=tDiqc`S!KQH6i=f-|+*6ViFoG-C+=0|#(^#<BAx8O_gq;rej'
            's)pTbsZv?7M5tMB)~jW{;!A|#T?a{W$>uC**jfU%XlrSRDVTpah=`?F&yvjyGEpHuSe!kM3Qaq(yyw93YI|+%+V(ZP0Dzicqusf='
            '69A9HKJceeM(-X&_q>}iRL@cL91%|_U*_0gi9PHP+s6NzjtcEF(T51x@}ueDL<1qm`UIRE-0ZA(Hs9%hZ}_*5@XzsWgmI2af6IT('
            'f6sr%|H%K4@%QfYgAR|moZ%^dpDV7p;Tb>7Unm>hB(36ifI_{SoW@>-2LozGEHwk@+=DBswgeh4dX5<bMvvb}Xp*`Nu#S;7bxyqV'
            'RDoz|IqXi_-8Oa@`|qzpHdltJs<}u<sbO)ID~34#9ssvT0yO|8?p?(+s1DmN3h~wh-A&@_6K!D_BmWJXE^k7m4l{5xfa~5QH|%JA'
            'G+KGb_J-GP?7TK?5JL(uzCC$Gr>{IozbmQr#0_PbxVE1ueA6Rcb@Vw)um&K@_hZ?GWj-6mn-gQuswQt!+9;XqgOW(-5SlyP|NmU7'
            '?(!eHr2aAgaKuA@I(quK$382-KKU<@bn*x5FYp5XeF|g09P`R)q+i0)xY;~e2~CDCTHv?pIUu85Xz11{aG5$3(L-<1ECCzcB5NfM'
            ';R_viDe#Mf;M*RVx|~GxD+{s8FY;gU%lvQrvqu!-8w-v4qu<XSsnB~C1RmqB4?Qmb@~TYmYL^^)DafC3cLE3&zR`V*wtu)y|9R3('
            'KTgDt6TvsNqd4)8m`3RgNN2{<;p8LYzqrXQkhUJ4JSlb=z|RAJf5Gwgix7g(o+Kpv@1CRK7K7wAF~!Ez)A>cXD7zQ)D!?}#@MT|Q'
            'dx%Z|(ZA`s+_5q8J@}Bf{IGp~8@tvv@Npwfy3HN9yVjqNcz*g5>xKs%j#i^@)~8WE^@+Alvi`(Da?Btut^FHX84aMX7ytk'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.time.GetSynchronizationMasterInfo.0.1()'


    _FIXED_PORT_ID_ = 510
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8!LWp40{^vHO^h5z6<#}zy`KCza$+Jvl*T~3iO1ua*&ok3LTJ6-wTAW1F5Y!wB{Hp^>DsNbd%8N^)w?@Uj1nP`Ep<eYn-d2j'
        'IB?*^fddkUoH%ksIdVWCapS-h@x7|<o}T@SO<-lOXI@pkdhgYH-}|ck;jy3bSH|>D@@g<}BiF0h5etRmiT9nZ$7*&@_5&FS#nR-d'
        'H5P7(9$Oy-EPa^1{!w}_ok*UsL-t<GB4sO*^ReWatIQL9EOAF?9=C<>vrtc2Q(@dwakxv_leX{lu~j{Gwt9|VQ=-pm*O*!x_&pv<'
        'A66+L{beUoENuH5vUbC4o+jh=77HT`lKvBKWuG6WOJhq%ew=;;^KD0|P;_I(qV#r}oGyL0y92ZHJ(}mTAY?rU4x|r~XYCEK!(2O%'
        'p|XXWc9Q4qNXB80VZdW{;3%FZC+HtfbkpSID#Eq1O45h$=*Y!1ImRV9bu<uZQkfqF-0`lmzD$#sgShL79wN9Id$gbJI?B<3jMC(|'
        '2?Ewr7}DhR=|=tVVAN}k8XaP)(i`L;cOuvqGGEcD(%Gf=lVi3kd+Dv0j*g8jAY=o}moBpuca-JyRAf2$W6_RQG`f-1*E>}$8CoK;'
        'dQLzoV#y6!C;UxX8O1$btwdbLo{KL5MGd+!Ju{$IX=4xBy~D6(i;*HFtss<J0#*ok5%$e)PFKdt+UBCib91nLUvC|U<diqC;)uCe'
        'g)NxnGqo+lyR}MX#qY796U8bnBj#5vp<ui3OJ#K#gpR)n9kAV##s>t#V{p}yJ~P3QBO8#eF!p`83~zi(Vl1>U;zm_Hue|Txo#2tj'
        'cI%S?3mv63&iR(;2S^JO2836~j{-$!B<MQ};UE5n%#D55@zr4mW~>@mj^|ksa?h(EYTAGZDL-PZ<83>GsD_lYyB<>TwHy?>LfIbk'
        'Hx)-Fsomex<moFyUDw~&@HMOF<Oy2_X<{9uBpUR)5{@EOmr)Oy)hjv_GAsi}4>5C7K9xMT>bNe#v}Y2ZrO{68c}_UkJqit5ju*4^'
        'C+Wn}*e6jJXb~7i>C$-Ig}Z&>11ji)vqK+F*nR1uC~0-YW;=o7Ye4D5-KZOP`E&dff1ba{&)iP=OZQU#)d&3L4*wc|b%I;`>-;SL'
        '2LC4i7JrSOqgv!|+~?<c6<XPjLguE+A0A200B8(QhBjx8i+?nP9t6cfNRv@Ch}TV6v*|Op?JKs)!ci1`subyT$%6eoBmy}Ed|pk?'
        'tmcYnS#2I;%QOV6Jn|y~ju-4mIY_I}Ei1YYuP^Yr-h)r_nNr+eoR>b~rN8e1CMV7Lp=5!(6Z|_y#T7aX3x_eH>MJ*>N^Y=#DREFX'
        '+%<<($AYr1@lW*0EOhuH!ppDS!`WsB&f7RQ7G;B<?lVYBf%PGa0_jIAYi1`h%PRco?9+2e<1u=ZQI_VJGI7w+7M&<fo?H|Rxn8(i'
        '8TJG^ypxNbbkxXs^P5W+e~aH*8l%(W@7~9nzO(5I72{NslN%x7GYmnKT+BXWadK{Qs@`lhC#Pm+CR@|ZR%?2;)o5I*Pc>STQ?04#'
        '#>{MUdTOekl3Ggn<XIMmGDI!Gc0g>(&)=Ft8+kWkJ?XpOZ{Dsf&;%==P$g*22df6kGQiRG2>hZ30Z{A?49XeAs#VtMi<yHDz%03q'
        'S?Cl7MXimHF~I*2OU=R&XkLURY{vnXk|7(VY3BgA+rHKFWKW~-5H|^*h2m%)*E(x!2F}@tPc$EJfc9k!5`Hg4w_p|OeyB;ugI7Hk'
        'XaIH@b`ugA%%YmrHa29l1a+K9RgL3?uVvkvq1?7$u;U7EV2mME2xNtZVCS}OwCFD2EX;QSEqSwgFGhN)!AQ{WG8Ryy<|yrL>L1RQ'
        'BRt*35eh_kU`=!#cQ`(vT#PCkCb(wL*K3yUucNMj!Z-qeG~$l2&JAT?bsdBnF8LBj>v%Ovs1LLJ{b8xP&XlWb9lzFeXQC21ol`ko'
        'N~P5|iaI!kI(Ub_`#@*wlLqto`DBcC`#~}em?C6T!_wKk_(8t-h2@pb%KA#DJ#VkIJM#<nm6ers(#4h~8ai^Nmvv4-!RSh<YL#6>'
        'qF_=X+d#`UQ9}=RC5!xXDo<u}rXiB^E+gs@pab(O$tyWlASHlH)P6>q!1xUfIF6UQ!>{m<lOv{HH5C5xi@bbdeXdPa{Kq3>W7JAQ'
        'KT~PVDI8SKq7!)2;z|Y4<%<`YU)vUUMZjF))MU7Mk-l9VS!kPuHZ7zwHkpU0_k%1cfCdVw5*Z2<_q)g}Bq<h!(qILOz(WvF117kQ'
        '*-P~c^#=Z|*Xx({pLZ-+4*hd&gAYVo5Nu7=QIfhTmXzmu9qO|rxVE~c4Xag5er4o}h*3Udi16^_GExggV9m<RM?#YcKrh24v`@we'
        'S8QY}Yn4JJY$Z0B5o62(-L(ilkeFl^lt%*g_&sQ(ctnLBW$Akuf=v5Fnbm01mJ<|gQ6~=nO(`21kC6>8%&o3oZ_m%Iw^us$+Uml5'
        'd$B!FIe%$xxW$DC_#`%p^f$y2w#WWmpHLNC9z9zLw#S&Gjp@P~MyzRq|APOV|C;}b|BnBbf5!h1AIPJU(?c*Az31>Z9>Bzp*Gtwg'
        'oV@1KsF)%L^Fd942{H=?Oou?Sj4toFPqfve()hghr28|aH;YeY-g1mM&{g80d|_#vFXAugNx@2RFi(;Fc9bFE`Q&!l+2Lgfc2ffD'
        'UdoDAI{&ygkb|K4^awQ1wTa_AA}&|TY4*~vG;AONQSUgiW7Q)h`unl5F*>o#t5O-k1GUYVuPcu7{^t6;?&~`3ba%~Cu!?%uwfQ~^'
        'C9Z=dGSPPiIqCwF(3K0VCV5G3p2&xgi)zL6TPj8LTS3?6uF(A!+sZBhoE6G$j9aAMI09plNX#7#mAHrL7li0Q<J7j$SJ(k_aN$Pf'
        'N1{8zcZS#6%%m?u>Fek#w!uMwp2$0RC{=OKTyR2A3aE5JV7x3HMjAR<D18`$Y%*}P#cI}7sZot`4_EexF7jFxyj#@xmYrbL(ic}@'
        'pnn5*HOmup&)y))g!?mc6Nh^N2U|XO6Tm9{D_pvr7kmZ_w?jczUanLu{9L6@N<Sa$rzqp8w`uBy;^%`4hy7@^-*tRyLQSY`)Qu$e'
        '3Q40pXObk%vSf-RlV!;?Nv6t@8InwwC6`DtQ<k(ya;YqtB}uC!Y1K(GTe7g#fTUTrxkWZN8)XUE+-#O5WMQ*xbBlIwmTjJ;y_#j4'
        'XZ2n)B|WoxuS;c#-m6uXP<)!RWjz#)$+FF}6phJpoM*}R$zhzE^}1d)S(fNIQ-z*py+QU&PM0O*>EujlRYUJ}sZyEK9l2R=)~i{*'
        '(tBmjr-`Ozv_gZ1t|ibGT}wHpQ2x;%Ay&xxn)SrU#E|eo<LrJtdE9{IeFK(P+lz|}Hx`J3LXExL?%Z6nK`5vX{JzNO^?i6p>Gp-{'
        '*^QnB148*SLrXI3VO!KT{@1)nL}f~}hZ)Qs&QnGjh_!D_5N!KqXQ{LDb_cQHpY9?;_1)Ctulz6kAN+6pU;Lkk(2i4CquYmb-13i7'
        'uOi2AL$~y+EueD)*Puu<Il5{XiUy1x-g+Y|Fd3i&BX#N=NWQCJCXvj$Q)FoG8e{)GC)c@>r)tDSP^5;&RgRlAaQ+T}yTqCz04D8S'
        'r8KDK?U#f?zZh>wx}rxKhUw(Lt<&W^DmBl*Vu042x325adNEpgTla>u*VoSG4I-xiLmFQyy6E!b^t<fUeS|9KiL3irNUsUfRL3@F'
        'KGguSeAAO%EZg;v>@$W|HA?Fv6-s{-N?Z~3(A=HP{|~!=3|?6&^U71;m8W*|%5kD!LeseOi9gp<F<s{OyunjYvKRW@FEyHg71x<s'
        'hC}pdU|4jyIP{CP3`|ZE`elXqQ~nYEGk<uef=ej>Jbt97)K9-C5JQ<`rn$sTzue3{50`mxEd<vpg3JG;UmBMtAe|UW^U0&)J4fNQ'
        'ncu=dYw!F~arXH9LGh%B;63D@f2mM*mdB3sl@i)o<{9O{7vFNA4tdS>vQKj9vqPS0vG>7Gwbt?dpK6i36OZ~1JA8gE-A%@!;Y9X7'
        'm%3eyTzYn>IKtxjRu7vH-{~N<cdpZ~@6oRn{4#M~{`ZkXBK?5g|Ko1$KMhO7RC65w00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
