# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.1.dsdl
#
# Generated at:  2022-05-18 08:39:27.784886 UTC
# Is deprecated: no
# Fixed port ID: 435
# Full name:     uavcan.node.ExecuteCommand
# Version:       1.1
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


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ExecuteCommand_1_1:
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
        COMMAND_RESTART:                 int = 65535
        COMMAND_POWER_OFF:               int = 65534
        COMMAND_BEGIN_SOFTWARE_UPDATE:   int = 65533
        COMMAND_FACTORY_RESET:           int = 65532
        COMMAND_EMERGENCY_STOP:          int = 65531
        COMMAND_STORE_PERSISTENT_STATES: int = 65530

        def __init__(self,
                     command:   None | int | _np_.uint16 = None,
                     parameter: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.node.ExecuteCommand.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param command:   saturated uint16 command
            :param parameter: saturated uint8[<=255] parameter
            """
            self._command:   int
            self._parameter: _NDArray_[_np_.uint8]

            self.command = command if command is not None else 0  # type: ignore

            if parameter is None:
                self.parameter = _np_.array([], _np_.uint8)
            else:
                parameter = parameter.encode() if isinstance(parameter, str) else parameter  # Implicit string encoding
                if isinstance(parameter, (bytes, bytearray)) and len(parameter) <= 255:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._parameter = _np_.frombuffer(parameter, _np_.uint8)  # type: ignore
                elif isinstance(parameter, _np_.ndarray) and parameter.dtype == _np_.uint8 and parameter.ndim == 1 and parameter.size <= 255:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._parameter = parameter
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    parameter = _np_.array(parameter, _np_.uint8).flatten()
                    if not parameter.size <= 255:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'parameter: invalid array length: not {parameter.size} <= 255')
                    self._parameter = parameter
                assert isinstance(self._parameter, _np_.ndarray)
                assert self._parameter.dtype == _np_.uint8  # type: ignore
                assert self._parameter.ndim == 1
                assert len(self._parameter) <= 255

        @property
        def command(self) -> int:
            """
            saturated uint16 command
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._command

        @command.setter
        def command(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._command = x
            else:
                raise ValueError(f'command: value {x} is not in [0, 65535]')

        @property
        def parameter(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=255] parameter
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .parameter.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._parameter

        @parameter.setter
        def parameter(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 255:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._parameter = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 255:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._parameter = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 255:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'parameter: invalid array length: not {x.size} <= 255')
                self._parameter = x
            assert isinstance(self._parameter, _np_.ndarray)
            assert self._parameter.dtype == _np_.uint8  # type: ignore
            assert self._parameter.ndim == 1
            assert len(self._parameter) <= 255

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.command, 65535), 0))
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.parameter) <= 255, 'self.parameter: saturated uint8[<=255]'
            _ser_.add_aligned_u8(len(self.parameter))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.parameter)
            _ser_.pad_to_alignment(8)
            assert 24 <= (_ser_.current_bit_length - _base_offset_) <= 2064, \
                'Bad serialization of uavcan.node.ExecuteCommand.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> ExecuteCommand_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "command"
            _f0_ = _des_.fetch_aligned_u16()
            # Temporary _f1_ holds the value of "parameter"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u8()
            assert _len0_ >= 0
            if _len0_ > 255:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 255')
            _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f1_) <= 255, 'saturated uint8[<=255]'
            self = ExecuteCommand_1_1.Request(
                command=_f0_,
                parameter=_f1_)
            _des_.pad_to_alignment(8)
            assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 2064, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Request.1.1'
            assert isinstance(self, ExecuteCommand_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'command=%s' % self.command,
                'parameter=%s' % repr(bytes(self.parameter))[1:],
            ])
            return f'uavcan.node.ExecuteCommand.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8zp#X20{@j+O>ZQ{8Mev7dV3)(*{~3;2$f9&W67QbmW3!QCGy&1u#7)6_Oc;>nwst!S7m#;n(pecXQf1NAOfkStU~96P;MM@'
            'LrJ83ClWd3m|K2Ha!a1Ks=H^#9tReL+|ykj@5l2z?_0&&XMXYg<vIIL@nkXzvoLD=nMf6n)E(Z7MB5MaAkmpJqAVU-6OkI=G29;|'
            'qWqv-e5d?z*(x6JRUC`7lyk*HdnU~Tlc!>O$o+oI2Uy}t&W8by+p!KsyK^Lh+=x{@81Oi3cg0(|$V^!*_(PFqO2@R~*;lIP56aE?'
            '&H0~}@07)PpBs~^9wuky8(97n+nZ5kasRp!Q8+fp^Fwa9Z^+8irY9+RtA-eH@n)Q<gII(cu@MI%o%Zg$-&4kqM0{Xmxp@JL2Rt+W'
            '08W<jE5)VVdLf$DUd6X9`UH>W-YvUj@nt_VhyYK+$%Wp_d(tb;1};2hamEjIP!|8*tH!b<70aRME11QqQ5oZ@VB9bx1v5Hfx^Ev-'
            '9v=wSsz>)kqz@O{-YX&wb(%4xgt>2+4--<Jj+WTaeqGKI5vaZj#(SvPF51(^=mAT3YL4v#cT%I`1J+M5;EqUjv)PR0GRdQe#oDku'
            '6HJ97HW+}kGv3of!LC00!t*b*ON8T57jXG_aru;trzszm#bd8<yv3WBZ75gh?R3f>@<k*D*vUaaUanUD>gIxcQhr^21JN(eA&&_U'
            'lo^$q|1G{$CC2X)lxEKR+U7hZ)XhHQ_oA#Uo~kV!rxr$=<G;(|!5hjrd-w3Ovb6YuuamN1r!A6=20a}q;Ns$z7-+=7fGj(SNV(DJ'
            'Bu4|OKmhsu;?Y$d2i%Bw=1_8)My4VrYGM4t+j$fL5GO`H;179}i}Gh>Yjfdl){`q$FxD{Zu`WTOD-vPUX(rwF2mA=3#e|pbOSx08'
            'W#czcF(^V07`FAFv&C8BR334fzd281=k9JUxW74QCyo*xTeaBEdjb}{hP1rCHMbz&m^DLk45PikvvYtkB+8JEJyra3g=NqVAh>zW'
            'vOGy51@;(iv0mY~&Gzx5uhRi&hu>faMuVHi#+RwA9@#*@?a`E)^J5}}x?zElm}h~;S`Z!$Rx7i(#Kch`5=$*(ca1<~{Q9oP*fLw)'
            '+1gs!Uh{8sUfkIB_jcCzZ>@AY{>|OBmHiI!=VGyd<kQ9tz(A%65MOA(kB~fEuh;GD?XPtADKKw$MNey|FIL38ZEeV0IG^dkEUyN9'
            '#B^%^kasC$UXe)Q$?62jiB3aAm;%dh3nuz~5t!>tv=7=#tj`1BW<<k*cwnS>qGki~jklEWDYahc+R*c;b`o>W^;4{ax1i+0di9L&'
            '#r@A;yLR<jNxZdCke?NnN9wTb?%e8h{hjr73d|4pWNwhb!?=mfb=J>Q{74xO0+`7TRi$%1!BA8)1%+Zc)Go4f5`BoV$UEw%RcRjF'
            'W^fJW%eN{&<j@)X+&vil#Q(>IeCh`ud2@3&#6hL&neLlIsv~)VA_==vZOzX!!d+Ft`wDv772M)~jB%v-w#Y1mtCDb~VbGNd(6;(G'
            '4vg6q=-6--XD$-l$eL!cI2>D~1|0Q;_NLDWBLzItJfv`qob@6_``{{%r71WY8_yYUCV59ARUl?~w9~VzI9OXMYAavF=j@Ot&dO9r'
            'aJ6#NZ9@X!jjd>V-pvGaQejz(Cp&r^uBAznTQ1&W(E&w}x>EcPrLZVchQQGP#|EIvnRiOg+H9lmyui#*pyENF2K5q4lRD-$MMzWe'
            'Bd|}<3uHmZbtXNLrkWBJij38rL<JeJ5PoLlN-*W89cK#wYdJdKSXuKSC;J_y`VCdAO6Dnwj)_K|j+evSjI5e+=x&IXz{zTwH(^u;'
            '{Q))`Vs#i~V+!quj=-!u&UhdG(F&P{6X-t>3A8!KFpX(EN|E#t=3wq2AGxShxj=KGb6^&oNa|Fto=HpB3T7i!gOzZ!<mGWhqb8Sf'
            'T^76;P@`303p==~0IMyom7A1-7ZuQ}^woCu1R;40{3Q=bIFu@o*nt|TYBWgZij_-F$o6iou6FkJtmQ;E73ae4rQzT)+;|o@f^<5i'
            '6ftcfh-snCW=7p-5anUbs?>GwqF!k_iWXZai4ZnqbixqNqJtY}i1QasWY))Kb)-RT6%Y08&rM+LlnAUDMxzONrOzHkw_2ZY(no7E'
            'Vyz?+6uDINt12W(S%RDzM8|s6cb5n{HZbb_?5lw-%(1KfG!8gH86a%t8KerZ^KMC(#R*}B6)uY|KH*Hrq1xGn=orCT&I6LqEA-+D'
            'F>mrP^^yP(d+>VEg9BSTYn|gl-)6g?%gvdq&h!?}ZCJ1Y3i=>ccL;A3q=C-R4vYYYK~?o6A6ms~SWKI%6v)C_QJu+*hCpd)hgqe_'
            'YgM$et%e;1C1?golva}GghC6mpmeUurwH?`rj}z#>=u#gKrZtkR}t^22(5l?H>GY%1;8Mv0;!MaKw`b4t;TSN#T9p)M}3tJtTndb'
            '5pG0AXE9;VyNx>1;7aqFNuCuft0`ou81zJFYa4nl%XU-=9vJ}SKvtB5yQ$`Z6z=TTln3~GD57W)B_MWoliy3;VFSlmt5Y)bI7R>+'
            'CN20tC#W9=4i$HAkpn8kv!PPqw<o+=FeJkwjRf(mIz=Aa-0m%gB>8<(9v9u^R76CT3C;J&-==Cb`rT&hz^XXnl>Mc;${f@EJ`zrg'
            '#o=)y;1IQF^lJ)&OI{<(HYhWF8`n@5v35le9%cFjOB8A0U>ah?decOo(}^Q+)O0O2bqe96LlqFmEF=0Se5&*`u|uoHt$?+%9Oa_Q'
            '0HtqvW3BFFs&1qXO@rr&-i!LPMc~>y1xD^nWGGcZ)ge)_BjI(8H$%6?pp;avn|%W`Sxw_mpOu`@%xZzJ-a`xgXx##@udMFxbYG<-'
            'O~)Q+KJB`yR0rZ|+eh@(L0<KHwhOPsvObEStKoTM>SSfCMP#o}HdR*u0a?pMJvEO5ky3{Xg{d35i6c-}&xTSRh*+d5a9W8iMb>m7'
            '5%8Un@C6eGsF~4u_8y{hsg6!(tJ8h4v%UH%I<%c#3eV41ZONEyv<7G*sbWXylt^3259+o^w@iJWsZ1jVtXGGiaSQE^f>s6a{^Vh3'
            '9GAK`MSPrkV!>J7K64M=K3RJUAHm$+PIqr(Z@;s>@7mHmIuNbiH#awRtij2|-fWH;Q^|Vjw6qrTY3z)TH}<B)HH}WT6S~$!0l^#_'
            'x6G^0JLrCg8hj<9(FR~$n{C^!+g|RC8#`D=lsvH%<GImPq5}*@mUIuo-CP>jngj@WlLrxMvglD+K+`77N`z~7W>_{517gC|P9!L?'
            'AbsU2WcVf62_;#wh1QF$2bB8AGRj_XfEDhfj>5adru$esV&eLxt}1l6#2M|y&tQpXdqy#J+?u*-5OJ2L6MeXKm6V5)8a5TE$#<wl'
            '7C&vqUB%dWuSr25s;tm}nNa<9165I6oVdvLdn0#APLTbkyd;He$$?bzC-RPbU%o3#c~|~Yekgw>KhBHuekiB|Cs{AwFTUva)sYB&'
            'sye<3%kAP3Khrs6!Y9G@NwCY}Ed7a8uPn~(>P#K&(%TQpRx$srvN$6(-O%5csIu@@M~URo8gg6~my^7QD&(i)Ah%^?e083c#RIMf'
            'z<df4Mn8A;+VPwHXYemw*p!BDyD$2ZXRwI);#ZAd`5v_9lZ`2oRduN5TE%~6kD$;X3iVV+1r@TXp_9q6Yw@<XLV!MTHAQ^Vi9_IZ'
            'rrHAMQ!4%kIba7|Ihp}-bob|4An?T9Rs+q*?|0;Nm*4MA-F`m2%R@REow)VH*YUV@H+6&VS;uex(L7CFie9*z^@;_A&8}N+&gXQy'
            'c|pF8|K7kLy2_L{+@0s+^7X9?3**=S+FZzIymvRB^1OUdUXYKF5tjft1-QKnsC_6u7V?wN14jAl_vLT4<!|NhTJrbu5Au)lPx8<5'
            'FY>SQZ<KKPDUvJyUYzyC5s6f}_2#+a67cK(XHx1*K|RBX3v~w3e!+?M%qUMrZ!%JB`YL+Adb+i>G(YpAS-!T7xV(9e;!<A?XEs1K'
            'n)LDQ86RnC`+wY`V&p*^000'
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
        STATUS_SUCCESS:        int = 0
        STATUS_FAILURE:        int = 1
        STATUS_NOT_AUTHORIZED: int = 2
        STATUS_BAD_COMMAND:    int = 3
        STATUS_BAD_PARAMETER:  int = 4
        STATUS_BAD_STATE:      int = 5
        STATUS_INTERNAL_ERROR: int = 6

        def __init__(self,
                     status: None | int | _np_.uint8 = None) -> None:
            """
            uavcan.node.ExecuteCommand.Response.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param status: saturated uint8 status
            """
            self._status: int

            self.status = status if status is not None else 0  # type: ignore

        @property
        def status(self) -> int:
            """
            saturated uint8 status
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._status

        @status.setter
        def status(self, x: int | _np_.uint8) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 255:
                self._status = x
            else:
                raise ValueError(f'status: value {x} is not in [0, 255]')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u8(max(min(self.status, 255), 0))
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
                'Bad serialization of uavcan.node.ExecuteCommand.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> ExecuteCommand_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "status"
            _f2_ = _des_.fetch_aligned_u8()
            self = ExecuteCommand_1_1.Response(
                status=_f2_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
                'Bad deserialization of uavcan.node.ExecuteCommand.Response.1.1'
            assert isinstance(self, ExecuteCommand_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'status=%s' % self.status,
            ])
            return f'uavcan.node.ExecuteCommand.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 435
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8zp#X20{@*>U2hvj6pf)DPWnMh+VW9B7Zs|u4<;ooLIMd~$0<<~C$gPBAXTH;-J9G|*SpKkY#JjKwMZ>345HAf1geC1=nEkJ'
            'Blqq)iQ_g>gZ<#yotZo5o_pq8-`V%%>G)Xjv1ihLsKclxG-OIf>Ko}tP!mDYOB1aOID2FUBGsc|*zKp_9=i*7-EDW?9uO*yA#*rp'
            'k916y2PV&8=aT&*mOTn_Hka#xjB9ZcLan(0L2jUt^m;N5Yi-bJ5^Gvj73+{`mBbwK;Pt`yv74{VSMIyJ&K?rdm`wS!Te}++e;4pu'
            'tDN0Gs~`%u5lx6t8Yv9J+--ZBak^@qR!pwMTCK$p&cz1SAlsSVA>k_{B8b-vy7?*v52QAtM_D?2%br@^48+@N4VqizDavT<o@+aM'
            'LTE!2$SfQV^dR?f!XBV0lWS-9i7*MAeY=a`WuWuOc*&|~il?u0(5B{S!=$Y?h(!u#w(#MbczQ5;cfN{e@GQPx20z;A*1Ibm(OGFU'
            'nw^frbJpt^nNf|sB=exGQ0VDA2te!AJc{~`3cfC*oLG5hlQ-B%2@;oS2W!=~H1tkJn^17dj<04i;J1`gb#^eOd0UxsOosLe*@c${'
            'K3kt#SZOyI_@|8|k3ug_jHfvTPJr17L92}O$qk7aykKjY&(z5PAtYcpJwS+`*vh3nKsh;p(pu_@`bzi9rS{xc%^5~?b_QZaCx<zB'
            'Ch;N}+~ktU++dQC$coHIPX1^QC%-;8`D%SeG?o?@>#gG0>F%~B==7kxU!KxM(l_JeR?OTKMCECkaJ5HaOz#24i6I!v^>%%+*=@EN'
            '$ma}%kBFFsRA%G>1~QKvU_gJaY2ubLSX4?w1i=vGQBarn0P5HfC>|CPxyFEkJj)<1L}Fm`3b7%1VFD#bDP$z!f&8gR<tid@7hqTZ'
            'hg{}b#8RuiAe!y=QbE@&qf6-QLKvRLLZ~R$p}c<(5;f#zo{YUbrYl#HwJKFahU+Ckk=b+LKHdTcc5=u#h2Jk-nL&Plr?7?>@eBM6'
            '=kXd|$2Lm5fe|9!LY<Svg+O;akSvym_NZ7@8xRUsk5Hj&+2cYdc@_XoL?BX024)ZPPo#Wj$Cs&zY%KHJ$7Gn556RCk;g;}9s+^r@'
            '^i!144D=FbPp7#bsX%0~mPdTvwpEj794K1|?dO`&>dVttMq9}x`m!-O!|pmMP-;TNRcD7^R{^*OMEDq+svl9%bDKuCZNIeAj6OSi'
            '_^L7s#d8O?4A#CXlGIsmw;;OT^ApO5pe#~`gPXrpR65Cq8)<-wniT$SUt5-8sN%Kf7U3T}+ae>DS$}jEr+#+l=c|vjPdzj(BTzre'
            'eaf?^Vs1?|kQ+QW$nA;vW&9It;4&`SY%BK*Ay42TJdDTiIQ3T&$3+sxH4?=Q5`+f)_GLtacOK&17Ji5K&f|Uj9v|RC`~iPNi$8H;'
            '@DUXOe<38WVW>84@lM5_BAu20GBSZ6L;5Lt^w4$k=sLYOUtv|3m+Du1Ql|eKJ{@A|BsD_TYy3jG?Rd#Hse=DP;IknHJz{W2s5ja&'
            'UV}EIVAO84yIC?jMH`-tRD&@7)xy6iKm6x5k<ahP9%=lS$Ob)_{PP8qytVcp$m1f~rU?K5'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.node.ExecuteCommand.1.1()'


    _FIXED_PORT_ID_ = 435
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8zp#X20{_KYU2hy$8MaHBIMcLon<lLil^(gMwW+-{P19DS2poHzTCUe-y=iGxG&wtS)@PF0nPom~ZxJFDP?~B46`fvifz%7`'
        'ii8jn0wg{Q5?mqi1Gt2r0C(`b=bV|HU9Zy^2?1iVo;@G$$MZh#$8z(?`#+kQQ2)su?e*Q*^=o!4B9Hst8@%m{n(c($UKo3c$g_L4'
        'M6}~MqSfz-{Jnhc&HQWmY<905iLaz0PV9u<%ZcpXW#M~WY;lKI9<{w75RqE4l|-qNq|wM>ciRE);;NaH?>IcD1)(cy^*!OFiC7A|'
        'T^_i#roJxErtBRN#a<ZDiN{_xpWn;ZCf6q4%HM>*HcyhsYh!bqe;LOgpkuiz&+cCFgzpXnvTT<pT&s4__FhEVdOKKg>S_>s+ktRb'
        'gG6kLXjr>@?6#NKz6iDxnXgUbaEHTgT_~B$PiAK}i-TxeZ3*A4(^t@F;#+w$&mOen1Qy_tTRrIQv@K6&#~f{*JUe2$p_6C-+%juf'
        'FA@u`=y(u|nN>04kzhPwi4-gedo1jzj}Z^H1)D8aw}l_>&eg1!Mc{@}%-|BHzr%ir5b>x#&vw+e3vo|4UdM9=cX)w1v>hf%*kwH)'
        'B_sDhohb2wZPtmf;0+Ol<z-`zizWAc7K8~)W5GOE1PK<v?Toj>9l<U<{oJ$9)pD5QtTwoOBs+J2$D@e%^X#FQIo{&UOUjgs^mY{8'
        '!WUiKWYEpb$&al~$xq2yIS1=!$Kl5wcf6#Zul+lFz&OV45R}I5dwgw@9IAI8vD<!}XO9<>4qOYNlhMEP?8Id+(eiHLPa|pe2|MiN'
        '89V5ZxZiDuz6V^KS{L0Ac1RE`8$A*6B#f#t>PQa(AeXb#OJU&fL<D1(lG3y?5&?x4)}L&oz7Ig`TY1#p;eIOe@8+{>Q}4!Yxnhj5'
        'id_#i2?|Zo6Nz__NH^>*--Btf;fv~}Y!zoI`*pnlAwnOpZ2e!yvSSoesn2Qu+9a)=cz10||C=K0#9ogFiY*#xTR@^~a0_3bn3C;r'
        'J7fpT=q|+BaljZ9l@O0Tnf-N<#o!JgxO~mxwAb@JL{AbbtQ-8+SPOr2!l;X|!{3MwtVV1m%D&8ti<KqxYZh%OVtx<^ZdgV^BC$^a'
        'jm?61LPWKf%*`{g=ZKyPtwi1GBardeXD!AS*wV)O`eI|*zFfbu+OW4aR$8wtHtY7)&E>^bo#N-=Yzoe&i%WnZm?|KiF2N6zoGi|3'
        '*0)-V%@!HvW>d7oQ1go-ajOv~BrcSX!|ph(y1dWANc}_FQC9JYr0_}c1kp(txv(%9mfsLebUMOGE-_KtuFbO!cYvEdEeGO(k?fHo'
        '8sKldC5I2O^;A=tp8JK8*mJxS;T*h0NKUPo&-gyO``L>ZFI>ziZWR=|A7_^P3$tu)yi#x48!IbhnAf&sn!tm*L1~*ytdmCgBVycf'
        'AST=O49~R%L-LJ1FceF{cD~xv3wN;=en<XPEX|!845~qVxnuN@U)2IXa|nSSxjioAlVAFQH8F8nY#UyW!%nhGc_i&2NkXnDRN|*G'
        ';m&06jt9PN3a;=!z&PA|L&OTgCMC?25j0}}t+J1ffkAXRVUTbyh_xknB8xB!#O^>Mugj5N=x+KNW+a3AA$Q4KeJwqT8Jwpwj|x-7'
        'Y>-%5_@o+lu`YYYXtdE*r)XHKPz)7)Q9Q@Hyr-p%LLaIcHT5+_0M<Z?nq^(>VNWDf)Z&v`JuugNRpeQ1Z!xEVB8Xkd{<~5r6nP1O'
        'qXdpJfbp4ifX`}dwWGDbPFEn~fuFj?5%X0Z)0e`ek+_cN6Z8UJ2!q0tmWZN|9Oa6b6_td645AQv#-xffq^DY^5&)ak;e2^<*#@1o'
        '>dfnup`utajgWK_zi)-Xf}19N#iks*>!Kvkv>K(Q8NCGc0WRCY=@3ZS6x<IUfmmq}^A7Z*6XFm`p#Fd*Q09za8r!%Z!RdYM!QNfo'
        '*H$sUKyebLz$_|}NV8tCla4MJOj)V`E8%F~N&}x(RgcnD7PRP6p=Gdz8+2BH)C$+0-V`G)4A71H3OU<?kURkXyagxhO3#tFfeI+I'
        '8bPL$m3EHHwyrKM)wi~k<P>gRkP3BI2n9!QV=3GS;^~N7#6kr@Y;%=2W2!zKKXr?!GR=Z0P8znN!WL2@hz%aC2x2L8@I(uu^+gdG'
        'cW_x@X#}<x?1VS&IDm0ePvA_~?^o!RzP8A^=6u3Q2c=D)&GvjjmWxEkWFbk+;-pj{>ZnJ4*N&jJfl=+JUUgMs4s`aXb-)SI0AVwY'
        'K~;dA^@`M9tPm@t&|cK`amPXq*-jlqZ3LUu8W4TX(2E(0ylOM`q5u%v(0a~-0_z*g^--d)vCTVDbL^>OwS{u43T%KvxE*+J5Z=g0'
        '-7rQu&<7m4ChJMQqZq4<V!GUmfGnKl7oLo137D2{7?+BySrb;O)KIIy1mz-$)JpW+Bhx}GFr6;)$-+D?LQ6+UpbwGWwp`#l-1B+c'
        '^HJ&-a+B-UJqH*>sDSEyYDkoJbkzXvkl4hI)~Mq}T_uewc!XXNQ!ge|zgw~+EjFB2Zn6|%DNZ3tMYk<nmD^Brsc1)*;C=#tY)cc8'
        'P&W#>BZcn$%JcwzcZKiIAq50lZqj?++AZNY?sRfy8U!$)#-sut!U^n$g*zVCZ{Y(<#N(l2@Y@#FI2e*(eh3Hg*mRL2m#e$Q4pDxG'
        'm`7W8Ard}?N`><+(znbSC4bl03a~2nIC+1*$TB0m-+{yFu)rM^0t!)yMt==KaNa6uSs7)lZi5`EEmkuD!u>eh7bPBXVRsl}6!l4I'
        'eNG*RqeD}d*i<RFRfP-?2T?}h-{V86r?eePEv^V`HcpW)j0ebl3#-dTC1a|Q!ZanGE43HZXLG={bpVWXPn3|W98)1tvLoWvg*QXB'
        '#K4r4ugiNK6j^2AQ1nWgXvUSm7Y<PZpDs$^mBppjM)Or_Y3iz>`KYP0QelWER2|Xrwo_B@sVdx%WzmYDs^O`h6wZp-ECqYf*_f&T'
        '1hSlpVrv>WBBBZx3{w<zl@=&2c7v(5MIa*2(OiiuMO;=PKJXnA@i~<SYOHmhK7@776xOM)*PB=Bjipynp>1rEdA_%#Qbx7V>Y|9G'
        'jP0XRB5ox;sM;dlN{W8Qh(-~xVw#{q39VZ}#R7Q0zZn|XrKn9|AI+XPaGbX1525X&g|^TUk-J%MZmn*$>W!8zOSh;YTDoguVyLY_'
        'XQC#XgNQM-9%(Kuh<q43gZ4&EN_5evX}d>bO(YQPQFe>1qTfOFyAvW_DbVNwL|u(FRMoA9dxOFbl2J(RJBsl%2`NQ8SPU<PZ4h@k'
        'G*CGS5VER`2o+iM(Nln?OPHbvUG9vLtSh<{2}3s#p#*~Xl}DiA7a=E@WL_m&D^MDc>wOhbYQTZ0(49IG?>rl>W7Uev_@&4y)Lf!R'
        'yYewnVyT)@47FQBqXrSgX;i7hm8!%%<W#rJK&8LkP{hF#$)KtjC~uW6aD?#+Ef@>cr%I@b>{MltZMXY+NKTObv^*!T%LN(9Kz>7h'
        'U4BQtBfl@-mp_yr$REoO)9fDG6;y!}t>?G0`|OUlCtRDdj_tX5BfH;@!xS`O6Jgs#*m-u0{_(wbo*mx|V{dPh-oBU5W|N=Evm-L3'
        '3H@C?FVC!{eou0L89vUlbG@{UEM!MwJ5_09FglO(?5M5*u%C>C)z4hGI6B!skN?uZCQoSEeae<RhC~!EwkiDbx4|_(Sse;8lZT2}'
        'Gx5(<3knV*Qx8>CU?Jri>P$w);x%iL0KIQCMe!8&Gy*R%uO`r+Qu5zU0XyJIhZ!J8vp-z|Ax`wP8fb=pKPSJS{kt?Y{XDtJU22W?'
        'O+E4LVBMPD+Mqe>;O$?^Pt~F5^t*98n}XTYx%t{;O4H40$??B77SSkEUePnphb3R1o*KOV+uBq*=DnVL%4vDOJT1?V5a$570C0N;'
        'Q2RiBDCE!X1dQ_Mx8yGx@|W^gv+~#SH}bdgck=i0Bl!pUM{>CQ6PzpmoE@{p9+6bOe(iX62Kd!KCPlUsR5R=ws56lE3!1dYTDfYy'
        's-@WQDEd|N>Gk#b$+3fGd94AvTsuy7DMrJwGLW(+eR*@tmug0RpIuBojQGdQZI(P?KAp@SyX}u&dV4-_!r3tiY^s{TjuOkKF{S6T'
        'Ej@gpVx;&9Mi+$Y_mb|%9d#e2ysKNb>B#9wwxts{Q$@7Sxs(ft)>XSaLTZyw-9Gn@y>Df4^`)y#nmuNhmK14I*y)_FI&ILch^ZW+'
        'D$$`v%_*0u`kFc(cT|+~hY;no5v8%wvKOzmUfgJ|zE)o*i5^=P0gYo^UA?JvMf{SY?~2SXETcC+eTbVMFgMdA%+w-u?S<CR7^PDB'
        'kkU5-8ZC#BHdH}Jqhee*gcuK2#MoSHF0R*G^(G1OdG+f=@oPtAM5{X^lYs|AuUPncU|9TAIU>|EhY)JIB9tn}NT4gNN`<AX%y1+z'
        'E3@=yw3dwa*@N^yD%i#U0xqi!SgEo2l3i~$H<Y<nNV>{=SQjB`;Gx1ssNN_|)bueBdp&I|>OiUf2py%_KH;7n)Cr1)uUnH76W5Q@'
        'W11c(=y8r757Fasdd$${JUtfZ@d7=br^gj~EYYJ$j|LuhMBCZK0V!^Ll2X3{7TIPBxoI@nTt9-FORCe_oG5jeDJ6ftl$S*PKN{fr'
        '>m=~s*KbbBfBX+~)7n$FNlm!>;MDZN<oMJC$euko?~F}1Q}ll~Fa(qv)vG_cU!NdboXn=8GHDfyjECML+kTTCx9IWh(#q>UoxF{m'
        'Z&7`awrl?Zd{nE{w;})l'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
