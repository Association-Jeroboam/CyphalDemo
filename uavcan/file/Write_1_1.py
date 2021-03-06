# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/409.Write.1.1.dsdl
#
# Generated at:  2022-05-06 20:35:06.645121 UTC
# Is deprecated: no
# Fixed port ID: 409
# Full name:     uavcan.file.Write
# Version:       1.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.file
import uavcan.primitive


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Write_1_1:
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
        def __init__(self,
                     offset: None | int | _np_.uint64 = None,
                     path:   None | uavcan.file.Path_2_0 = None,
                     data:   None | uavcan.primitive.Unstructured_1_0 = None) -> None:
            """
            uavcan.file.Write.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param offset: truncated uint40 offset
            :param path:   uavcan.file.Path.2.0 path
            :param data:   uavcan.primitive.Unstructured.1.0 data
            """
            self._offset: int
            self._path:   uavcan.file.Path_2_0
            self._data:   uavcan.primitive.Unstructured_1_0

            self.offset = offset if offset is not None else 0  # type: ignore

            if path is None:
                self.path = uavcan.file.Path_2_0()
            elif isinstance(path, uavcan.file.Path_2_0):
                self.path = path
            else:
                raise ValueError(f'path: expected uavcan.file.Path_2_0 '
                                 f'got {type(path).__name__}')

            if data is None:
                self.data = uavcan.primitive.Unstructured_1_0()
            elif isinstance(data, uavcan.primitive.Unstructured_1_0):
                self.data = data
            else:
                raise ValueError(f'data: expected uavcan.primitive.Unstructured_1_0 '
                                 f'got {type(data).__name__}')

        @property
        def offset(self) -> int:
            """
            truncated uint40 offset
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._offset

        @offset.setter
        def offset(self, x: int | _np_.uint64) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 1099511627775:
                self._offset = x
            else:
                raise ValueError(f'offset: value {x} is not in [0, 1099511627775]')

        @property
        def path(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 path
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._path

        @path.setter
        def path(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._path = x
            else:
                raise ValueError(f'path: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        @property
        def data(self) -> uavcan.primitive.Unstructured_1_0:
            """
            uavcan.primitive.Unstructured.1.0 data
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._data

        @data.setter
        def data(self, x: uavcan.primitive.Unstructured_1_0) -> None:
            if isinstance(x, uavcan.primitive.Unstructured_1_0):
                self._data = x
            else:
                raise ValueError(f'data: expected uavcan.primitive.Unstructured_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_unsigned(self.offset, 40)
            _ser_.pad_to_alignment(8)
            self.path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.data._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 4152, \
                'Bad serialization of uavcan.file.Write.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Write_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "offset"
            _f0_ = _des_.fetch_aligned_unsigned(40)
            # Temporary _f1_ holds the value of "path"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "data"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.primitive.Unstructured_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Write_1_1.Request(
                offset=_f0_,
                path=_f1_,
                data=_f2_)
            _des_.pad_to_alignment(8)
            assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 4152, \
                'Bad deserialization of uavcan.file.Write.Request.1.1'
            assert isinstance(self, Write_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'offset=%s' % self.offset,
                'path=%s' % self.path,
                'data=%s' % self.data,
            ])
            return f'uavcan.file.Write.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 409
        _EXTENT_BYTES_ = 600

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8dWLmk0{`t?U2q%Mbq4kqq9hxZESZjDdo9Zn<j^qf$T9twP<7%ky*>&nD={D1ftJ7}@5;*sid{&AXWU^rZHH>NlWo1paPrVm'
            'XF3hvsz>IHk9^cjCNq5GBOmq1$xD0A{ty5O@J}RFC$OyH;@)$<^WC#&FQofv&z$nB*T*x_fBwt0X2q@8#gfbGmT6mGnv*s!mde$c'
            'TGh2Y9{Q($$Zcx|FDo~jH6DH)Uin4%Rao$~lI1wO9*T^A`ZKTID0_`M?=(?MjyZ!6&o|6FWz#86S&0349kGfx_}@0T>xF)<bcfen'
            'tLhMt{`2Je>yTwx_MgIEg#O8r>3MZ)vf*(z{2N5=L3z_E^wm!+ZdY1721*svGfN(k>*Zdn(;}@qXmR#uj%!Ujyz&#r<I}v}xu}z+'
            'Ny{tQ+?n=7$Oyb_x?X9fTH&F1-akK{0+CzsW1It;q80sPcq8<mExDfQRLpv%9q3+TQVjT7b!y7xm=&c|sg^@O6XNi>IItKLdU7@3'
            '=i4(nZX$p<C7xmu%TUh5Gnl8ApZ`LSjMeLAGxVSPxrw7V@@Yin8jW@?`E-ffe1<z-oI>$Jg8UN8iI>GIEJF(u7v~$3{t3)R%`979'
            'Gi3kkpGlTinxY%h)%(@hPbp2>Zs=c1nYL1cq`j@5L;uuYSYFKcGyIq^_2p8v7Wzgn5VtuqS+y-p>{;M5Rm_8j#rD%0ubW=A-d@^e'
            'VPOG@AN%J%t~zDY<4#voS}s}ExkIIi_D^4L*tS`3ZnM-%cTBs%!(WC4mJ8fT@slJCpQ6`uH%w=m-{3XwS-mKIQJOJlF{$WqGa3}1'
            'r&v+`W-KRU8M;6-*wB5QYO-OQXv(r=nh9L2Rz6!Zo#-LE-k9V_q>T5W0-2oPZH7YNEFojDDYdA;E{V(d@vNW2lu!w8rkzT&^QL|f'
            '-Bffv@!5~YuidzI^QSi=fAP8hVtR9sN1eMwq~qbs-H0-6+9^8voS3ScWg5i_$$gSs<Ge3jeK(}qi-^wbMrHu6O_V<U(e)qS981`U'
            'MiN4N>C11w^Ufw1_s_O%JEh5Hyps{=7h+h{g(Lo6{9OY#g9^uGP=!>&d;U{c=(D_1s#WV=$*P3c{bx#UwNWqg5<RJ<D3QKSKWu9f'
            '%V!)n+1cp%{Tgp__Dy{9MU}Qpsb+=#z{ky+Fzp{=t%mpzHzu)mOLabtHx=WxHZ@F(7H<gXPl0gPCeY&B#o;1lJM?JhIa?B@iyZ3o'
            'B;!_a$13yip13se$808Z9d~11F$k_WaLphT!)@Z&j6rk_?v!yGs~DDJ{Osl@BSqt;;6~N4n+DdkRWV$Sz*Mt_<r*H&O;zi6ag#G#'
            '+jNC-;mr#K>srn<0Y_s69K2%G`4n#YhF6We>eZ@eR4hy>LN$#7joH<5R1-#Z%D5}6vY-$ZK4sw+ZA>;JKUxm2UnvgU;Fuh&q!<@j'
            'bJr;F;&jotP%L6NT)p8?jKm+e;^;Fzaae+sf`Vy#qS}}i2#kSd%%)Km^nB9Vqm?!2s}5t~gK!6PNrh<?2!uPh>N2lfd4Iq#-Y~Ak'
            'sjF2jG;*eCjb@x#Op|HYmh%OT#kt0ic1(pMrMnh7nysuBdjqzzg{aX;3f!7W(7PgsVpMz_KL?+5>`G6Mo0STN*|r<u>|f#+cP*X{'
            'S+3E!i}c()x_y<sn0%FO?g2&o`c3~lQHj6TvaRp6HjJyu)w|sv_zxkI6(6<D<u|`>y07?pJoHzzlecfN`OfY7uam11;dk4NF&CN5'
            'TolqRl}X7@Ir@ofk^-hAW9sG@lbI4QE&eRgwcatuRHg+im-wC7Hpg^i!3H+{aRfh~>}tnOuz`S`isy0^>vT^$c9NY6*i#+2IErIW'
            '@94u$v!?=<Phte@nO&{f)0lB~W?Lkj!SS<u@@LPmGXZ-xwpDQc6#1UpvoAZ#o(<Uft{iX{=bqaa7CXnz2W&9SG;(=<-~Q}5HW;vP'
            '_2h&WIRC<daM|<hTLJraN4{_t@m@SI9(#d(J76#E$QP~9=H<tV!Cqu91<csYEwO&(u@TwJ%m~<p7{}O&KSh7_P~x#y*oA;yOk=j)'
            '2g=fGhZcjq$}R@%(yn&~Jq)x)+slU<o4v*^1+0*+Gr4D14m}3D%nAW}eb4Je548Wzk?>$w*y{lsYTet5h*@aAzi%8_T=pF{6tLpH'
            '@_=6G^X8FqVsEfwz=m6OP>3txts{@h-eki8dwbs*K~MDi?y>M=Z?U%nc6EEj3?cS#S~c$+8yEInb~Rw%J5bKh8-3qBR<7(F_Pv0O'
            'bXM0e)z^E+&V#+nMgsQ!fpdol=>NeJ;mzJ-?+5I|-gS5tV~kKOe)Ponu@BgX0sH=A<rh&9;|EW44eTTK{eX>bt694HW9jH<=lDeD'
            '_*gVE9?yx^+^wy%Y$9N@+vi1MQA=&++im8$Td~=IEyQ+YF^{wO$6fR(pw$R^j-l-Y`U~_x+r{m+3ut}6m;F+2`$hD4(9LIMcb_Hn'
            'THflnx_7@7^nBRvyS{(lRrFp<{WlKozm5ox5Cd}A1O)$nx^J9~cBH{ANC-_}kk1|rudpK?h9gKYvin0F*#|08AYd5I?hSkFz}QHO'
            ';9)eobA*XQihxup2#jaD#}P*o2kFP5;8wOh+U&7J!$na*sAVbUd|OPIJEE|-vh9%<x<*DqNpJ{`HvZzC<0I9C0^C1r7E6!C0vC}G'
            'fd`MzW#!Ph;PMhWuzV0ktH;6!7oL!UhkN6-{=|4;O4_NxS{HU3|Nq!w#u9??h&VPx{D&;aNRUw=qd_Lea*&fCr@)2^IgRBZFF{^`'
            'yv7D$P=Y}P1~u5wnE{3bh60Ah3Q&-spg=)m!!RttumZyx8-WoCMidy)*eHxjFsi_)#>QYwf-wcgG&T<75{xS_uCWQ2kYGZA360%?'
            'TN2z-;FiV&2nmD&LSr?kNl;Uurm<O=m0(tZSq)P=C&8Qoa~kG$UV?cA<~2-iAVHu&pka0wBv?>jLBsUkm*Bnv_chG#q6CWyENYnG'
            '2NFC`;DLr2UXox*fh7%7yez@80?QiactwI01y(dn@<Rz8D)3OlEU!wis=%to)?iJ7H3il*O!2w|>k6!EnBzwhJW}A1hIe5@f(^{4'
            'Mum`(A)`V@r&7qtki#VFR1A3;@+#zYDu+QC22~i;sUQp)3>6HWN}?b`L4|@&MKLVHunNOEmBok*BPxvOR2ZW&jH)oIQ)!IJFs8zo'
            'PQ@`U!?+6LI+e$S3==9$=u{rJWVofmEuE@E$RJb@I@L!_hMEdBo$6;+hFKM6b*y5TlVMJUIUVa5=4F^yVP3~dhCqfug+Rwzh6NcG'
            'R9Miln&G|-_f@#BV?D#742vo(>R8e6K!yh@JkYVGVM&H16_#|YYFL(GS%qaC>l#*MSW#g`$I6C>GCWk_p^mi;t1@iJu&TnUj<pSI'
            'GOVevrek%(x(w?otm|0c@JNP7Dm>EhNeoiCI4>%Y|0anWIXcwtiyOxvZsg-U^u>)M5I6ET8fEuT#SLS(1Ct{VH;m5v@Fy#77%f5S'
            '&qmy!HD5&JLg)ScvlcffCxx^U`r^hGaig<h`r^iZ#f^BEp@Y+WU)*>MaU=d#>Wdr4A#SvG#CCCmMn^lxC*twZq{g?48?h{r!I{*r'
            'Q`|`BcM>;JX(N-^<a&r3WHBGj?k;Y0+U_oHbhqDG+}PQtx45x4zwYA3{(QHK8*|aUm`CsY!NrZ}Sh>YxA-Wqo<IHv-ZKUExibN;H'
            'IXbAx9u%+86OYb)lcnw^Zfrvx*$3(_;>I@Yu>)b#xoiTzRovJXVd9V?Y!NrM#Supmht5u;Q0?NzMk;Q!YA{k64n11iLFh&*ZluSc'
            '845Xn=!@KbK)jKP8?DIm+4kUc0K01`?sk;FWBkQE#9zpEQaF&fu_KG6$6~Q>abrg=D~HZy58}p-j8>0@QCD$eM_%hsj2FoVo7C32'
            'v)kxo7i}aYZOlJ8cAetJMj~#sOB;~WAeT$E4Jpw!G|1;j;UIA%5;>G7DR00m{x6Zpp>&rwNY+Rcj=sF{rz&s6+Qx>wcX=auWkrqO'
            ')QjI)F~$5>;q8COW-{V`T=CEM#J^k@zW8N91mfSszl*O$D1POiXnTR}T>I-Q#kbnuz!JZ?CocIPUUQ5_n~hPf+BPqzZ#YdhJ?;(}'
            '^vcqZQ8(`zla^!Fn}#)GPV-(b>-^{D)$hcACGX>W<7ArtJ1BjbrZ3a<WtzTBb38H)9d`C*n!Zf4cbTSDF@2flATkZ*t}oN{WtwlQ'
            'Ow)NBkfRfU&EtR^{tZ^`c^vR0&jQka?btsH=${4jIt$pyb{+@lt>XZN`m7|U0h~?)3gR_!Ui`Nx-2Ocs3;edx<5)oa+COu3_`Rg#'
            ')m!+h?Id7cT$=bw%4DKR!*Zg=9d$la#ZOUJr-7TBZA}bUn6_=yY_rUx4kYEO<8jAx>AWE7NJ8zEjLSsya*P#^+C1(R68A~DOszOB'
            '8>Sb{#;v9dx5mpB`jf>#8&*7hxi~QJx!{g*7im(*k+^@!P|U)%kVM*Bq|R%c+S1rfqfBh0<|#>+nYif)(W3?~$jYqTF`aVM!lXr|'
            ';dmDL@qvgrx>HnKs6p+>Z0>QpSu`R#<aIa7oJ)<woN{EInpL*&BRUBuzDcR-aKkoTOolbXhXx{s?Rml9NgiG6OWw*fu}|Bm&`7kZ'
            'IB9&Q<~4_s9yNC@3`l*%OuMZ^4PM6iAMom?<4*CYU(S@}SgzoeG~2D^RioZ3bTrhqzM*!&czIsE5%sBxo9J-2VMn(sE`ey3<gt0L'
            '<3;X%n$*2H%HvtKH%uu|YnAlCsvs)(JMAAM{v-a^#>1ilg;racP3tY=xBnHN#n@vMXGZedJ+_R;kGD7}PKkWnG3~r4h~Mt>5x@Nh'
            'G}wHkZ?EDfUoY`ldOkx~KI5M+RgwmJ^^)Lb1%GVqgJvACF^$oyG0lY3qcP2OOu_P*sMA-jz0+5eIGSARGD)t*{{z1a*Els$000'
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
                     error: None | uavcan.file.Error_1_0 = None) -> None:
            """
            uavcan.file.Write.Response.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error: uavcan.file.Error.1.0 error
            """
            self._error: uavcan.file.Error_1_0

            if error is None:
                self.error = uavcan.file.Error_1_0()
            elif isinstance(error, uavcan.file.Error_1_0):
                self.error = error
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 '
                                 f'got {type(error).__name__}')

        @property
        def error(self) -> uavcan.file.Error_1_0:
            """
            uavcan.file.Error.1.0 error
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._error

        @error.setter
        def error(self, x: uavcan.file.Error_1_0) -> None:
            if isinstance(x, uavcan.file.Error_1_0):
                self._error = x
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
                'Bad serialization of uavcan.file.Write.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Write_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f3_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Write_1_1.Response(
                error=_f3_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.file.Write.Response.1.1'
            assert isinstance(self, Write_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
            ])
            return f'uavcan.file.Write.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 409
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8dWLmk0{@j(-D@0G6wlVC*`!TOjEzN+jtI5II{Bz=)Rz)Bo3d;&vu=_Wk#f1SbF=5t*_q+aotP~M?L(!-3oZ2a!6(1Kuj+#c'
            'f<+M@e6ST1{~cdEcW1NNq#JY-lD#|k-rxD1uiu$#2k-qeJka`4$K$4-_<>ClCO8fFRq6%ICbg&$M+uiqtI<Uk@CGjZwPwupU481h'
            'eovoNhX@ZtCNvDF(N!tZnoI@TePob?w1E)MrgXDLLwkcG_9cN>c9kV@6ehTtC!0(pJPHlc(8c!pt}f@wx%c&Ttqv0^rQlvFS)woN'
            '{U~=1X*IaSS>W&R7$H8Dlt@DkhO&n+q9(d&6@`e<nIkZUh6jvcn7E9`j<$~<+s|$+Omz4r+MQev6J8IQUkW9wGqF1whl$4}30PQ{'
            'pv&XPszwt@8j+8zUQkn&Z6I^aF5upZ*}_N++|X66o+gQ;p-+Y14Rka0(3QbW8l=eJAn~J`Rs$NJPO5wXLyUK1hXfph7u%~7<#Bik'
            'UWU^d!U4Ce!G>wfYa8qNZGYKTELdXFvdi0il}da@gKcz}SHl~E*38oc_m|ph+*i37ZJbCvG&cKRTt?TOvg2NINU>UVt1VhE4{x-M'
            'z<D)z?(Eq!XZt`LcHA|x<gPo5J<xJ<eIVsa?!L5g{ZJZRC=`mTt7Nh0l#0D*9hg1S2i%boLY1n;!kSxs8`0GHlFjVX7PbXz#Mr%-'
            'VAP*}*L0s1g%-79D#4OKr4>g!l!+xHeCl(-YBCZ{y@$=*Y(LJGoQn&~rA31O*NcYEe9^8W9n));Q3Z=9Rv1YOi;er%MkJ65vm_OD'
            'CbLsXGePQ)(dZ{xV@svwB3W}?vb<2eQ0x`tx%qyA?5?j7cZsZ477D%5Uh5}FrYKj}D;2l8*1H1E?7%TK*`<TTYi8PNU|)gba1Q3+'
            '0u<maSb=xo5-^|;!4<d)n{WfJ!)^EgK7@NIs*umHoof_JLf=wjWP@)ppTv=ng!|f26C{aJQDej;ftVuEYRG&9+|z2ff@5K;VxHbb'
            'P0LNA=0Idb{y@yN8Ywhmpur+*L|Q!;r(VEoM6h}q7<)T1jPh_OQ(wGq3~4piQeb=5p0SPWXlXQWk^oJRgkYgGy1U71Oy9zCns!)X'
            'irRqLBREacKw8lT7I0VXSW(PGOQdWgjb4CePi(8&j)o$z-1}XtBX4rK-1@%CIs&SmAW^K9wI4{*Y<Lm+jLcUs1~?;(b+<(W$4l4n'
            'tO3Un1rOAd73%vutUq=LelfdF8U$1{_wK^{ZGEylekbv8fW{euF6UDZ{cP~i%okkHEwdOhGX^t&*UEWwZQxFV(+6dphOJ@iq+Y9H'
            'agMNT3}Pv!9)*w4&|ff>z$drhQwKhS&riY^@Fjc&U&DR)2EJ8Ky*l%Hd!*0eZzpr`-OW}#e-A%oe1C+WI&S^iS^W&Z8`AI)JL3`l'
            '{edU{?9hS3IFHB89EPd?K?eTrvW#A{Es15LSFYvM6jpuq79$9t4&q1lHn7v07PjW8a?bQy)}TG9KTt<;sG9Bxd!|+mXPL!<)#ml#'
            'x2|kin5|t<&s1qxXH^z6$@i<1D_It2@Ip6M{!S}I4;^@f{+YOSQrik3OWK<s_t-R7?SBD#3w_-N3IG5'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Write.1.1()'


    _FIXED_PORT_ID_ = 409
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8dWLmk0{`t?U2Gdyb|#0z8CvlVZO4uh$H}bYjp<mX<-b_YCcDzwa%5Z|Nh`~-7Ttm#kypB-rH1T~w51e56%@ObQ5Kmt+*aEb'
        'sDYw|itd9S`k<#mk9sL;^hqdCKo5P;qaTI7wCBtW$)QL}qAbbHuHyKLy!V{%eD~Zl_fq$mXGZ?je?JU3{}tcQPN#CIbUcycmZ7JO'
        'FZIzhk0+9u$!sQP<aw$1#(i!*Hj;dJI?GGnmd<}&`l=Kw9!gmJ4+=b&Pvogz1d4}l^RzLEDydpYC1IE*w;YlCd8?4j7p!$);e@GA'
        'qN%qF`s1W-#>Wig@X$i6_>gO*RE#7Zb1P?LOafBB@LqpgVnG)CW$A0=nb7lj%NQ->d9L*Ph}vXo6{%7&e8=GFRFy|tBBkebcSg<B'
        'vldO#c#IOqADB5~+~lddW}c68t9DXvBu0&VBF)Y5yeKgOPwMEd$xI5}^<MGhU>S(i;<s=NXozO?i_%c3_+}!P*Ugk}rTjoo3!~yl'
        'QOS&r<v4mpPNXu)QZZ1%?sr_n;<PyEy*g5i`aL?RBY-$6jx&h`$Y<gt`l+f{Jk`WwmZeXZif?_PV=wmHbEx!C@A{zNX+Fu#a!_a<'
        '@&_y;&WaCNfF>r+&lX0D2hbZ?J!#~pOYDD($Gqt!#%MtrYR6nXIWd~fm5LvhnO0qcr1R_Fmx>2}Y~)?O_wlXAv=~ZcvZbQd3?w%_'
        'Ihsiu=-A`HCo|}WJO<l9mRov0WBEfnDGUrCaj$sdR>n-~d2TiorRkES#Z3xLlt0p6NT+pcx=vC_Jl4|%UizjKV-Y(yD*8P)`~<b$'
        '8q&>iKE$&;Z#1Ly^Teb+g-%6<pE{l5XJstMf0Kq;VgY)AVz8zbRf@?%T1Qb9B+-DK!)WDGS>1FVvi`y-M<N2(!GJ(SO!x%FB#sg?'
        '2AiC90_=k5z_;zi2)cwqxZ-vS&Durnb`}*?58Uq^>>27A9vE`;#m|bT%Zr0NES@7GH4k58$nmtEE~BH)fiX)@QZGhG<c{|m$BWXn'
        '8zqW8hp4p~nKtMdN!;u0|9rU5V<W!wOo%@!hOS({UIF99<GyVtF*@z;WCWTO*ToZ&6MrK9xPY5MisLjWLQ<ut#lslrQ#_T(W~_X|'
        'NR|4FM-#bB!AkN3J*f%Dkwuk$q>WJwpF!M=r<~{aTU_MeC4BNlhPF&8Ym|y@x2Cf~Pv6E^E#X647{%Dd{dpW07420wHFS&OZV0GP'
        'hDyal1RB2*?~IeTOL^LPjwghkLk<=_$vJoTFFh3(M*b%l2=wD_%u^b{#oKx`LeX;5*f*&WU5%Sb+{RLxVQLSC?{vkrVZpVGnV!}#'
        'u8owI;|NSKs~I^hk7HvQ>j`dhS}v{Ugm&iA8G_9j<~RX6eKG7juUUKyH+?OiakQ*VCa<LobSXkjYcc9eXOd1#XqhqXi7=9aOr-dj'
        'fm^gTI_>Dubhvds-ZsS1IT%SUF0$r1Eym;HaqUbzj^=Ronn^Z1ecXzj_xQwN2$Bn8dO9yMg>iwvXlPQO){=srPnx?kvjQD;XbT^N'
        '$LLE6Of5zr+{9TYdFuQpZJKsb>v3I|%@`<Tj?)}<*R$v*T}vD0&#BM#HJVJjR5((4VxXd4^=iC1VAWfQ>hzR>t0NwIL*$a^6@Bh='
        'z-o4-BZGP>g=Xq@BOD#TgFEXEmsq4wyNfj4JQ^Kkr@f=BvIoTR_$_~)NV(@)uzIffFm8IUK5hKK_dp;he(W2IR*sv-GrsS3eL*|9'
        'e~XRQZr8f^Dn<B>He>WfpyG>Ic}r!I_cP@D#5qYelfAxhrH_S}Y%|4uFVSnYW{icIVzY>+cc5;JsmOx0RrIk3-@nmNjvZiaHaqB!'
        'Mab5nrgH2JcF<;rYjCj_`;Kg=!w#{-Hj8>TY<6^0X?6rX&W_bt!V&C0z9oHjlpV9#o35;k;|EFi#Flm0arUOoPB!F#qd4|fOIYj#'
        'J884_vZs;D+b!#}w^+N)-f7ASC2;)Iws6_o>>ZoETjMVrMZDA7#$%`0yEc1oL%t}5GVi~V4R)HnXEUwhTVnmaS4L#-GtFjaTpVp9'
        '{$%}w9kIv0$IjU7Y}ux79mq@H-!U8P19sMCA8xubsG*@W%AVU%+wA-7Lz~6Q^Yqs2{EpjT=UB{UA8mP_sDbhqc7+E!&pxtQM|Ew_'
        'B4*6Lz881RF1x@wY!+|H52%GYmv)sCyU5};>#W8>%#DQ0yKa?TVx2a-(y~WT6ZNj{2|sq3U9s7<`iSX3?9Ou3T;DS;>?*rvvyZps'
        'Gt@@i8+*!?U1uNLtgAM<Iw`(x?l}*3gLT>LlWqGB5m5gJuZ1_e$v&~!r_JN=8rtZhSp4j@@nb(=pW5t)ujF4uL5v^0);X}x*bi;i'
        'T^F;o`hDfz?%Mv5+WtOgWY8TG)v-tGN7;zYrs~IqCy_17%=%?!8cVS$o6Wg$Br%Jl_;D9?Vkp&xntdocg8BkAP<Fmvb`GVVHIrXx'
        'E<cYN&l~A1ZLYI`T8r!Tmbb3Agqkn>x~r}0E~EBJS$}Q&`m2cW5-}hW^g!_U)0T18{7CKVkPw={AR62rUTi}=G)Iu21zSVyY5^4~'
        '5HNHGw}#!fZEU1P@X#IH*uuyTSwN~}1O|hR?TB5mgY;cf@F?iFHnk_#a8hItvO%&r>$3?nyJQw;R&RN(p=BiG83%iJ?ay!7K2r54'
        'z_XoZvG7VPa1tI7c>d~KmUf&APS2wQi`!weyeEus;vOk@u{B<+uZ<VF#7_-Y8n9dY|HlqJ<`IOK#IYbI9gYx?ARt3Pfk1>sAR<9T'
        'hP5z66c&Z31W_5H3TuaU3EE|7S71$L8fX$|GH42mK}>>}3^9duLZ<|sGIT1e3%VrelA%js-Ow#Tw+!71>w`WC`ef)+*dPo_Fet;I'
        '!bV_3f)N=;6!r)nN$^O9M+y@lBoHzPg=HZtK~{#W!lqzKf+-oM6m;#31T!+sDCpZ+31(%ORnWP%1hx#eg5I5zU`~cP1>O5hf@d;3'
        'Q_#Qj63ojmub_jUOYmHV=L&jwL4pMt78G>xq6CXFEGp>ZB?*>fSW?i*FC=&&!wUtyyez@849f~zffWf>WLQzq#j6sm%CM@Sk6%jg'
        'QihibuELrGYv@mf0wEBBKo|llg+e3*5p=Rj!4M5WGz?Ld!l69`?O|wFDIl~EXkpM)3W-<<Vqu7>6cn8y=nO-rN@39zg03)hsT3I9'
        'A?OZ6w@RVW7lOVp^r;jagCQ6U!=OsxF%p82FpQ`a9*;usC=8EOiVhJ15eA`Bd}KqA4MSF?_?Zg9R2ZgIjAEDx!AuxtRE%So4Z&;}'
        'W>t)2utQ*n!B#PrVJ-x7VVF}fn&DXpo`vC=it!BdA(#)tyowPG&qMG$49``JX;=usLKqfQjA~d6!D1K|Rg7y`3c*qsmQ;*vcoBjZ'
        'VR)fpY{PO0)<UoxhGi9F8&*QF5{4BOqZ?L3uo{L{72_LThTvrwUaI&c+U0a{R2UHbE+sc2bg8|c+}MNUM%4AgesW_Mk{eO%b-cTy'
        '$qj9@3zJ<)ZfLdZ@LQYQ(5eZk-<jkF&G{@M$7<L2cRIO2K8ckhVL!RCF1b+~G5g7lR+Ag<E<+cm(f#DcD<n7EQ)xfBu@}jW>W=77'
        'ZcuM`ZU2bd-|fYCeR9K1O9XJFtXG@dD35QH+$g6u0-j8yNpgcEW}VT^lN+_Nn<qCK%Ws_A*jT4|a${?HjguR#>DDJVW}LN{MeXSJ'
        'lN-*pa+SxNvl<)YOw}N*m6ID~B)Tb%&_zvfyLhptcy#aUO?9*6MjdKb3#gkUH|ntawuMdivL5{U<VKx^ksY$IF1b->N9>9nx;u4D'
        '`I8%K<>W>+2AwR!j$89xgszp78|7=z0GXWK@k!QS5U-V!8&%7*LBDajfZa3{H@nK;(Ej`u?9T;jDQqjbu_23vS7Om}a$`d-OFPbG'
        '3(1WQ87=P#qlU?i4SB7;HeQrIs8CyJ%x<lgowJcpYGd~Gv8zpPta-@|e`*6F3Pd91+=k@kHWY|PD8oU?4JXMVzs~dqOyU0$B{}5A'
        '=?zM2co~lU^u}*%dc)0atcA9o-tfM%5_Z3-=YD5J7k~CuY2s-x5D@>86W=@)cE9*@QHqIQiN6$oCFaDh#a|Z>_`bk)!vFP^_+|e$'
        'u*Baz6&H%1_Ly41C!-}Z=`>H4zu`1Go#(j@jlQzfp;`J9ZPYMzYg#iV^>N<p%R2v9dG)X2pS<tmeCN_M``<y?Pt)wDY4+1J`)QiJ'
        'Nz>3}=YE=IKTWgsG)*;P_R}=mNz;(;_R}=`X`1h9nx^(TAVN0+mFs{A{stRvdL8gO?*hvI+HwCbVE-<l*<HX|u=YAYtzHMnRA<Gz'
        '4d8Se5ECDXQ{tb+#ffFQ7Whq}$+dv^o8qx+oj1LTSC{dR?<QbYTp0OE3Iv=%%`lz99TuO=;5(<PQ`>N*tcjKrdOEFT(|VFS6-bg9'
        'GtbR@j_wPbiX>ECNjpbG&$(D`Z<@QcLfkqj=cp9NIZe+yqi(4wEtlm<1NBLw&4=X<pNqG(Jrvy3o*+%CIO5hX>2O)34J1*nEn@L3'
        'r?NEZX)Q@?o#H88l^M6_2+^YgF33txJ=V>nQ^KT5rC{a_(&KFob5tj*I8lwtmZf=~r>EnZLx;4UIG)Q<Au%)Qh?m7u>-Z5Jj}xy@'
        '%9vbB>p66WG08jH9EN_s;9t*=Ipa%S^)#_Bmr<b}XI8G$_+&Oe-Qm@!d19bJsw1YSeHCi(rR)E;yrrADG49mM88b{HCwQvt?dtS0'
        'PVE)C8uHDr!w=|AFK-o`I#q5F9iA(so#k>vz?mg!RMy&^<mR_Yjf<nanxwyAN{mXYlrOAe!oa`f`Z40~-G6P|DGZ2J%gR)w*Y!{Q'
        '1wM<eMmLUhMe8-z^}CO^h>D})gj+G~l(;B<)8ZpO@t-JAd88-)3*Qyh1fQbkvjmIBiYF5(uYjJF5L{2;kM(uXv~3oq(V7*e8IhV4'
        'rs+o)EFN<zeMS70z8uHV;7Wr*r@+|Z1V&XhW9GO=U-hiD`D*#R)2Ps&t5qtyxnU8YqkhF+%gR`Fg@1en?bg-wsTBCCxwvgu53EL9'
        '8ek3TfCW1@E-6+6ap*xm>mPX7pXePLs?<31qlG`de*Nn877!2g4-6;n3_R$+-H6+j7LX!$2b$6fwnFJp&#ha%_wOfe_x9iIZA44D'
        'e6<C*gLe_??ojWo;enx_B3kiBcjG+Xf#*`5Hc(DSiJrRT?SCd7IZn|lXXA8Ev)sD6SEY4qu3T<qa(DZ`=(%_Ib^_Z6y+r3muXFY8'
        'Y@Jl~jdort%jMQN8>1pyxR>U2YaEXVU!Al%8m%nW;X8Nl^(KY~1`_vrhCc6Y<m4+iT5<BggW<%$oy7gYo?DI4x>|7(1?Bw*gM$M@'
        '!;K^0Y8B4iKqun(;b!6^YOYdqiJH%-xk=6E)ZC)xC)5BnzemkOYB)7IHCbxX)cheePpJ6?HD6Qn4K;s?%?2OA4m;aPqeRT5nwob*'
        '&Y?-?yk1lNu5tozep=QQ4fCa9ShVrRO4}B9H#}dy=^tofXRyg_@!-J)*_hnK-y&K)As>$kjU>EX+A+RuE)x=p<H!Gr5JB$VL5Cj#'
        'nxAts!41y2XThe+akTCbD^))tRL`IYimG0*+`9U96YtW*aSygC$Di-_hlzhDm;M_y|3S@*N(95NgB!c|srMP9FdF|q=gC=r?^gf-'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
