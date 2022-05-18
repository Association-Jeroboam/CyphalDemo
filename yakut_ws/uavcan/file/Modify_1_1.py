# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/407.Modify.1.1.dsdl
#
# Generated at:  2022-05-18 08:59:56.600963 UTC
# Is deprecated: no
# Fixed port ID: 407
# Full name:     uavcan.file.Modify
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


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Modify_1_1:
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
                     preserve_source:       None | bool = None,
                     overwrite_destination: None | bool = None,
                     source:                None | uavcan.file.Path_2_0 = None,
                     destination:           None | uavcan.file.Path_2_0 = None) -> None:
            """
            uavcan.file.Modify.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param preserve_source:       saturated bool preserve_source
            :param overwrite_destination: saturated bool overwrite_destination
            :param source:                uavcan.file.Path.2.0 source
            :param destination:           uavcan.file.Path.2.0 destination
            """
            self._preserve_source:       bool
            self._overwrite_destination: bool
            self._source:                uavcan.file.Path_2_0
            self._destination:           uavcan.file.Path_2_0

            self.preserve_source = preserve_source if preserve_source is not None else False

            self.overwrite_destination = overwrite_destination if overwrite_destination is not None else False

            if source is None:
                self.source = uavcan.file.Path_2_0()
            elif isinstance(source, uavcan.file.Path_2_0):
                self.source = source
            else:
                raise ValueError(f'source: expected uavcan.file.Path_2_0 '
                                 f'got {type(source).__name__}')

            if destination is None:
                self.destination = uavcan.file.Path_2_0()
            elif isinstance(destination, uavcan.file.Path_2_0):
                self.destination = destination
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_2_0 '
                                 f'got {type(destination).__name__}')

        @property
        def preserve_source(self) -> bool:
            """
            saturated bool preserve_source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._preserve_source

        @preserve_source.setter
        def preserve_source(self, x: bool) -> None:
            self._preserve_source = bool(x)  # Cast to bool implements saturation

        @property
        def overwrite_destination(self) -> bool:
            """
            saturated bool overwrite_destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._overwrite_destination

        @overwrite_destination.setter
        def overwrite_destination(self, x: bool) -> None:
            self._overwrite_destination = bool(x)  # Cast to bool implements saturation

        @property
        def source(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 source
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._source

        @source.setter
        def source(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._source = x
            else:
                raise ValueError(f'source: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        @property
        def destination(self) -> uavcan.file.Path_2_0:
            """
            uavcan.file.Path.2.0 destination
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._destination

        @destination.setter
        def destination(self, x: uavcan.file.Path_2_0) -> None:
            if isinstance(x, uavcan.file.Path_2_0):
                self._destination = x
            else:
                raise ValueError(f'destination: expected uavcan.file.Path_2_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_unaligned_bit(self.preserve_source)
            _ser_.add_unaligned_bit(self.overwrite_destination)
            _ser_.skip_bits(30)
            _ser_.pad_to_alignment(8)
            self.source._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.destination._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 4128, \
                'Bad serialization of uavcan.file.Modify.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Modify_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "preserve_source"
            _f0_ = _des_.fetch_unaligned_bit()
            # Temporary _f1_ holds the value of "overwrite_destination"
            _f1_ = _des_.fetch_unaligned_bit()
            # Temporary _f2_ holds the value of ""
            _des_.skip_bits(30)
            # Temporary _f3_ holds the value of "source"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f4_ holds the value of "destination"
            _des_.pad_to_alignment(8)
            _f4_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_1.Request(
                preserve_source=_f0_,
                overwrite_destination=_f1_,
                source=_f3_,
                destination=_f4_)
            _des_.pad_to_alignment(8)
            assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 4128, \
                'Bad deserialization of uavcan.file.Modify.Request.1.1'
            assert isinstance(self, Modify_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'preserve_source=%s' % self.preserve_source,
                'overwrite_destination=%s' % self.overwrite_destination,
                'source=%s' % self.source,
                'destination=%s' % self.destination,
            ])
            return f'uavcan.file.Modify.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 600

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jJ1Sf0{_ie?Qa}M8NYK=+c_sq8k4lNA{`7wXUSQcs#Quq;U+aimvfEdL_xePbGvglBk%2QcV}&Hq>5JJrIA)5QkE|Wka*_<'
            'ACQm`6++6Ng2Y$;0K^ygJu`cEduO|d4@e}6yq<aHdHp@Vc_#0l`QhJ|8|F{(N}T(tA2@C*62$}ckoN-NxL!1jqf}{87Uyq?Kn?Nf'
            '@8z*5pOmW~l<$@8V%}9@D3Ve(it~4Ml6g8y#I(q>ZpepF@lwVQJRUlI1>N1qSN+`C74K#u)n&2h9*87WQAnB=?pNPW%1*P>{9gG%'
            'SuD9+>qPZ3Ez<HEP<x8cW2v%uc1wxCpE%NTeXhBy$-C2z#|cHL4j{4gRulz-httt4xjm)bK!gJ=;T@EEJk{<n@<k~>SzOr}DWGG{'
            'P3(1P3z0OwTke*{C)`x?(C3L?SM(_B$yRY8P6XUJ5N;Y}i3cCfxPIi7#TRZxEQ~Zu#4tJ#OiRJ6gv0Ko!e=^SUKHm{g{c<YXHlO)'
            'P=y1hgyPHAb@`%vx%#@=Y06jRXXIzC-OEs#944r)>!TVf<l0o?TCs7vZ>-gpnK)9ZPS-}xD9w7JA0<K}EMsrEIJd)nALgeEAYUwA'
            'IyvhHk@A6o`}k4MHvGJrl7kKSB5zEEvQT}sii>qz?QmpMo|DgY<~j`mj(i?qnVc(LJ_R;O!t=6t;XcPIR_>U(Y|`p<{m;815JM4a'
            'izAeL`Cgc+K`8v&p%w#?OvxjJMVsmmvtDr)V2Qb>bY6D;Ra~m7@AfH8mA>0k=RVzO5^C(}Gj1<P%i`K7f(d>QjGq0yEY7{9w2k8~'
            'eyuzzo^hkNEZAvE(tOy90tL`5cTr&Ehl>7AEE2Axq~7?RR4A_eYH|5y6nb2X@I+Axnj{kuQr|-U!gdw}Jjstq&btRZ$VB;rvfWvH'
            'jLLtlO2#*F>V;h%4#cjAg;uAzwC@i25mJi-eTyJ9(q-~DR3ZA1J|Ncp$3n3{jhh7=qMas*HXf&FX>k<u&@j+;))R0fLp2V%jYWA_'
            '6O<3JOPT?~GqC}lMd@;}h?G#D>l*lHN^2p3qi65Fy|cNyx%bYlIWJZ5sZnv@2N;1InPR5JU6W}Zj2lH2XZs2FXcY)q+^W8@U(CIB'
            'qa+L&N5B1_oN0A8AGmkk-u}|wmn(1N_bU^!D4u!s_1DMBM6q1sWVe@Fo+qX6$uG+9$oG+u#~B#Y7YKt8;+Kz#=K%L3;k$8^Xcuk2'
            'T|8gWol70;nnV^0^dnF`z-I?n(2?ouCn$1r9jquLx=`j~RTizAc`SKw3s^1D+*uFUbrUf_QDJYw_(;pVB?_D;L%7pOsq?C{;ZU|q'
            'P4v9%N}j@pggTtKSb>Hg$!ib(*=#hn!GgrL#O$q2Mp{^!V{ORDT_!>gT<?R1*}c83HypMH>Wso5XTY`cSt_8IFw0bGXce@1h?{_='
            '0Z%1cSzjTwDTtF4o3%C;S3$LX+=xW;bSjB(75EA%g{qvjX)TC6%g&(wL#aGTCVbIX;3d|}?Ug}SOS0;;b_J3HBw4-iTBNKkoPonu'
            '90%qQy}52i=Rxe|cXS*eNGWLZK+7l_NGOJ(A<vm7sXr-p6In)s0BoTV4v<R%CTo)t5h7|&_^WTW7`x6kZR+AkK`0zhjNE1xY2qwU'
            ';XbX|T*G8wT@i5UP~jk-WYsxc;UrtoYF0*yCp(q)6E&A|SKhOI@L-CSE>t(&F*d^P*D=+^cDw8>X45QECy)8+x<7Wwy@}1G=_{Ee'
            'g!~che@<SJYqBl>B;SyKmLFyE$B*Psw&hRd&)V|m@)z=#@>lZL@;CCg#qw(#H%24Z=ka%pclo;yf$hJ~HyT|Ys@OCQ0;j7TA9aAE'
            'hDq+Q%{UH}NJk~X7%)npqF)Fpl-ZO4@cZbJYJR8`8YP6xT19Xu2v}%aiv&php~6}ZuJrqm68;(tMoz1>H-_=3T*y1{G&D*gQv?Gw'
            ')MBVSEJA-4!qL$Z?p|_$FqCF7k&tPS7I~S4zDR<cP*V#XW;e}IGh@*vNQ9gd#yRv68e9zHAj)m8Rl$bfg0z~Au*L}o2Go5G_i5b1'
            'g0X9iA)~mS!0`|5fQQLDRXr7u!)R(Sx_|?rZ!W*oX>CE3IO4D?)@H2$-aHvpiu*}4to8qz`S!3AYFHddjl5|yLgKg<EzS@$5`!Ds'
            'PL;5ZA+N8JRGY)0v18R>-&WnnSftG~n8lzWdOBc%ZZ38QNH|ofScB>m0m3(yYE()L@^LOl`9mC|+^m7gKu>I(BGk=zVFWO5prnkq'
            'Cf<%n(0XJ%r4iN4$4b*-+?n-R)-ZGmn8k4taZeJ2WppSgO)Vm|zyw;QrlMCLJQo;d85=gOz?8+hhXz4v`y7kDrI-}O6m%B*!xn7C'
            'gtIja@mN6+iAwiJfJQPj--qkqFA$aIMOmnU!7d_MzlnT<<?hD9Loe4J0+#fuu&2g#+8}1EI<XS>BVn7sO!F2K<My%bM*+}5438F&'
            '(~lF@5BOmG^1wmVilVVOuUS0)b})XP_~sb5rucZDD%F}$u5Iip^n%PcQH9ry9jd|<JK;z^rWT8KTxCR5Y-P9)QFc9EStXi@GEdIr'
            'c{Zmeh#@L<tO|gI&TC%UMH_jWpt3$DzjY$Z)is08A@Q@Su5qn~V(e-b`{e4Z%Gnws^~SVqmYF#J_gQ0X3y4U~^nmve_y|TZYY-eh'
            '2D2w-WIDOWQa{e{7Vt1`yc3dgvR9|v=6@J}P1e3;#XNes{QpVTA305WF#WO9G;>B%9^l_-%s3`zpEPq2nwtoX&dw~?&t4s$We{TZ'
            'vv$6jS^m8hZe!|Ui^rvB*DLW2TE2K(d}iGaPjU&b{fqXMe+9$P28N-J{@Vdb{$)H2$)|V}iX&=+vitN>aRu~b|K}@lC2j-!n0=@-'
            'JfOZ}A5bUas$Ru<HrezOH>|$i?LL@0@c}EdZDio-CG!YftUp3c-e~i$Cv4JD=ie}Mcwp`m000'
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
            uavcan.file.Modify.Response.1.1
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
                'Bad serialization of uavcan.file.Modify.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Modify_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f5_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f5_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Modify_1_1.Response(
                error=_f5_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.file.Modify.Response.1.1'
            assert isinstance(self, Modify_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
            ])
            return f'uavcan.file.Modify.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 407
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jJ1Sf0{@j(?Q0xG7|+F~xg<?YiH!x3t_Zcox_PN-#4jaYF6Fpn_q-%6B4wDpo!m2YZ+DrUjk$u*eyFrK&_bpk{Nx+>?gtSB'
            'iz0sTgRP+W{|G*Fd%0ZN3wjC3&F#$mp5OEKd-leW`~Qp#w0_j7xalW;V3ULiP6K|OdI7UZEo#J3!X?vce3=EjflGg*88f}B&)(GU'
            '>NDyn;bF*xh5<FcE=5|CsbB|>43UsF5aPL%Zr5mNZ*jz4i+sM-w5u$MqcFkUJlSR<;ZbOyhA+3*ySkh!=ibvdwHhN-O2NHUvP56i'
            'hjH#4(rRdhv%udcGD>_ZDUpU93}+8vR2}c;RTLsZZ;rtP8Xho);rLZNcA|a!<Y9JWVZy_=(eBh{nDBbY{8A`cor#0t7$Y8+Bw%4('
            'f-X-Ys~SxtX+%D<dO=NB_JGVayMTLZW(y-Ra7$OUdWIyDhCUU3H_+|WLsy2jX^<j=BgBttS`BD?I;HXj3^Cr39TIR7UTm*UmnY#R'
            'cp1)R2!n1}gAFs7*f!Sld;YSWSg^#T<$$;ODwX(*27BnRs7AH~t(m6@?yt1hxUX`v+BlJTXl(AkxQuT)WyihZkYcs!R$H`S5ngW_'
            'fs1PB!otG&g+35R9Cw4PxSP&$547BTA4vI<dnm13Ka|Fo3WehOI$16{rD88ygLCKmfIC(~s8Y39*l??FA)2~avYCC(!nR<I7~9tp'
            'jQTV02yA653N32IRDvaeN-K_dC=*LY_|)fu)np`^`Y|^1bNx71axO2emX-<r-z*wBi$%MRbWE>VMiwldSYaeBEH>_2TaiF2%#u{p'
            'naoZl%>=1GL8G5!O{|nwi)6!f$?8(|Qn6Q%=NJ14vb(uK+!eB3St|5Kd##@!nW9|ZtW@0UM(+wZzYoXMRF@7CubGLffqex|!3CIy'
            'OHhC}VGZ7fE5Lw41lQm?Y{M<M33uUr_yF#ws6sx&cCJw@34KRRkS)H$d=f`O67Fk99VbbYiW(y(3B(kMR>S5a;GR|^6`Tt@74vi#'
            'H7z%Tngfwh`N5cLHCkxKK!au0h*0<A)C+ix2v$!6V{c!EQ67$F>WlY{A+07_3T)5Wv$l~PEsf?)5ugc@5G<5Ncei<s={s0XGY(5k'
            'Q5!IO6sJiVNGsaH0`96ED~g$DiIi=m(F@S*={;53*H8qOkAK(d*c)7~w!W{kj)1DCNEB;j9R`v#8(xGyBl9(k0nP|x-EGmp@zOOt'
            'Yrt_t!2|Vlh59}Z>rWhlU(BwP1_2e#$9G}zu0B(qyq9=5K;sNSm-DHIel~b$<_j+9j#&(w8G{+XYvsJTHgGS&>4UOP!`85MQm<99'
            'I7e7E2C)=VkHUv&=r5Q~;Nv^+i36X)XJ_DZ_yWF!ui$I=2EJ8Oug)&+&Gb3^?W7LAyWJ}2@8O4x@Q?6Q$FE;ItDoU_!x|o9Ydpfg'
            'Kk($A9X>FI19{R6VwnCPY~b%M%jh=Skytl+?M6;bW7%i#F@gXJA%0}91N*&cVQ-!-=S;(89om!n19bwYs%f9FXKvL<mRhV>ZQdV#'
            '>q?h}={f-QY?X#}R%J1h{IEi~mZfnPFLYz&@3lho(1AzjpNU&1x2*uOq`mo3k4<yc{ukdQn3V_$000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Modify.1.1()'


    _FIXED_PORT_ID_ = 407
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8jJ1Sf0{_if>u(%a75BPH>}>OJ6OvYq8m>ZB+0<F*(U5{#Ra<9Wtc`cg+D;3o46`$LeXl(`Gt9&Grl7W{MYS|iTV*Q5CkjYF'
        'd3@jl5)z`SkoW@-h|l~1`~iqB@H_X;?#@1(V5CYU%Julpx#yne@0>Gv<H!g1E=;ID$!GnJ9okOG2zek)N8UA?4lfy&*Y>?oMm$X('
        'UgN=zwD@|*=jpw4?#=W&>1=Y+2>7>R9!5q)`(h$Fd5b%;jU)CT<uOCLE)NvRS`@@q6bD1hjvB7n##N8U=8k2$rIv&YE1oS|ol-+z'
        'lP1%~4i7@<xx{JePWF5+trn_<@1<`-P{WL(KsMuuhv}<edw^~|sx&#eB)Mbv1t}V~8JSw8gO2+FX(@NeG%tFd!%cTkn}?02j0}gn'
        'n~{KYU}~ALQ`@s)r;Ew?)h+`%R$9cn6?z3tCf-gPY4RB(j7--y13S-XKW>WC$!R~}5NC%Qp%(`hWH@5jo|PtFyyY?1i&((h-VSGx'
        ';7n7L*ha{07J1C_{0@_D7;)2PUW<WHx|^jGj33vcizfujo<3JCh$qFYnA7*31JhtPfOicW-jJ>tDNj6|Tv=|Z+j85C@5wL<=exql'
        'h&6f33%Gz<>b}R46RW0e<N84dh$oWA$6I~JlQv@D4u0gV4LL7{B;W*O5zh^%aw2;=oy_FpYSn}_#UtWub+S4^fg{c%So-IZ3kQTv'
        '5SX1bdGwBnUF_Ueeks%LaB6Uex4GL*jf=_I4L6jVF1MH6h;Q;>fF3GLYg4}yH<RNC7T>gF)Jd!VPR?ZBH(F$-j9+cw+*8#8MU6gv'
        '#ArHUnmpCjpdUX_CK~=dO-{ThBdy08e$6CG9x^;XP1r$9!cM#CITAs4b_EWGeaPu`p9f~-1^L9cgoJa&H<ELUo@<#AcgK>F(nJ|>'
        'm+}_$r)#m}m_cWR@|dw>Ix$b*O=qjq@4@rm%#2~-)T0g4-Q*4K^GF^f(zeky_h4Ea*wzu`c6llLwWW(Zqz90#{BtUqqQs3I6QtDw'
        'kxsl9BBlABZ@LPBYH^c8kh}24Ybz7e;@dew@jBiTX9VF9Uj?3y(#Mi%n1u2?$_4+BYjsHA=<&76YPnHfuQ$|r;U-UXodY?52qee='
        'GEFy>rA?=oC~k7R6_^(7B0{E@vS++cCZD;PQVc0U-+GWR#g+0a#_dY&rS&go(ugFxLcE_mbnV8C9y6Yt&0(_9>}Z@Prr#A6u`k{h'
        'KM)_pKunuM4T=yu-A_&--1oR`_+AhhNc&pyNCtNXWw4<PnM~0SM>Y{Yt0+}_DzERs$%O@=qVTAoO!_iSii;gzn9eQ4YKr8Jn}}Uh'
        'uT3}=_w^AUW;v#T0_W+XG&xC3OV>(QN@VRcB6vP)2s4BX0cCioYh$`Eo_^(Dg^7t8P>|4;kiA%D#D#?&?6nz*%eZR+>uta=+gM+E'
        'w#3!}ou2D-7~)#mEaYHJG0SAAU=^^ri%P&k#|#C#v~Y>oh5$}ttoCNHIR~h1p&}B@)2YBiDX=9>3RWF9OM8xIX><nk?+R%Ny29oy'
        '30z{$jxHHgT7tP!vB6;+M3UwUsd>m|d1<r6E|p5S4%(}7(>)JhSHC0U5Q1caS<{Jx7jFtM#zk$j!z@AhNxCb|Vrm3%7ZPCywxqyh'
        'v&4kE(Awhm+?R@sU1nu%I^UBZayLmwQ(G2hGMOXYZQ9ee#+8m1g+ruWiGya}s-=S&_N@i3YNyM%|0d%;mUAjz7GKkO@ah06oz5!V'
        '2pZw7iLS=iuhZ&uJcuHB@Hm#0`;j8|0$x5mSdxi?iyzYa&x;G<s<<rvAf6YWh>v6OqkZw?n)r$M>8$vf___E<{6hRv{7U>fIs43&'
        'o86Y{D*pE3UHs-9#P&aqO-!tquJl#XKyfPVc*qAhd>C{}tnB-a<YCt(Xal+il=KTl3RyN}2>5MeN!CAP3>6cK%$!GX$Z?pfQ;P_Q'
        '{jS7b6QZ<QpyKvCF7!&p;(9NPyY7PB5l?N!#8XaCp$1>HrG-uKk6j4b-9qgp0VsyT*e4KD2~s2}W7p<^)1j!zsg7&Q>Zt0m=p{ge'
        'gyTv$<Pj2_w|&R!=v>Q`b%6z8)*E5Zq&QGP-HISSwOiOw_o~ZaQIscO{9WDPp+gU4Q#vFtk{XE4A%JVE;un^ROJK$KOx(-ohi^f6'
        'o55zrxD|NqT>j6iXA5uK2sdtu2zHB93yI?qFPaQW!!W4Ox~s(PX!2Sz2qSgaRrhE%c(1)~qb-V5HyHbXAsR8TL6wW$MkMUYkk5m4'
        '2n8V<3nO@nZ+3dN?Ai}{bZs*aBm+FLo{8W$C50kDzX6vrv)Grm3xZlAB`LM2sy~(y9Y)Q}_p%D1Lxh>{2cBsO3Sr^xaxznqK+RE#'
        'W~RyD)dtQv3R!v=t5jf8$GU|CfoWSNHf;?tA)LwSEZ(<^xXY(Fn@1Cm9VijVaJw7OFh*o<Lv-L5fXcGG*o_c_E6`+N5%vbkt@+$S'
        'F6RaT4SJc{1MND!AY{xkF(bD<u9HA@^ExJa>7&z+6rh7>9(6zt4kxVTn47)H0|((N(ni}ncjM^npyV7obM#V^-(RMTbwp7fY2Br3'
        'IkBy@axbfU$O{ALgd?3EwCHF@DI=g_m)hGPWtaU+a|AP9Y>6Q|58G5J(T1l+ynwKXIyouzrq+CxLS>-`ehUPabMq=X+l0?DE8~%D'
        '^PZ@&Z<DCQEQfsv)2pj>vJC0@>06DlB}7E1x(Ccdz$09WUW3BnJ~2DiB7?>qF@4X%ONfVF;*BxNc&QGk=D+Jb_4l|Y6EwN}|54_L'
        'oB|C@zpoZlpHUF6;a|7S7@^Z6%_N8>`$XNdL)-bY7kg(Jh*<ut?r(;+f2)aS(e<$DQR?CSjQk31&y11}?d#@A%wXC-r>Fc2XohZ}'
        '8T$CJ4U+g{uNe}5!cfTfC=Jq;PtGLg0Z;nNS6~QK1N;~s)ENe-J9>Z`8&`QR=B>#FN8B)b+F5yJa_j&r?$%&|PtK?zbUHtTD!b9k'
        'zmIvTX5UkoiBN^ykZ0mgWw#Y`Us5iN{X(aYrCl?R{RZ<${$wQx&<LxKFom%nVRE*c$q%1L_4uE)!EZf?e6n60Gou!++<)91U~zJz'
        'R;|@vt{Ig^qc?x&xgGt&jT_f*9D?KVT7BJEs&CY8jg#%#AvjGh*AEn{a2SzJmKPT*Yiq`>N^Q9^POQnR*AKz&#4=bdH!6$k^~P7}'
        'BjF3nC0;`LiKro>;y~@;f~xJ9e$k97U{;Nen##hVnJgWW=GxW6D7Rd@Q@*`?%fPx(A#rY2Fv-sAB1m5(x;=%S!KuH@6~SDeKO)9q'
        'oONnx`F6!vuh)&+<;F{uaYnv&^DsuPZ>$^jC1Y*1yf~iQvxhMf1?Aet>T12QK0X4j_t|Oi+`3knnAj@Oa+8+pw3KOio|Y;tFVV6='
        '%U5VIX!$xVk`_)&M2k<$>$JQ^%RVh{({hiNcd^`Oc0Hxw1VihU{Mfn=M=uO~j{#7{PDD+%IWV~PI>-l?{XFE(=yIwn&kV}i%y?ua'
        '*y0-S6l|Gfy{(T(v8S+v|5eR-?g5f*eF#>g(&U8LdXgwIh*mfMZ-Q(c1MSKig{>*#_vzI*6!U{i+#7}al(-KI2Rh=+X#Gn2-9f+n'
        'OoMhR`yZ~6k1kt`Gza_!y~>yS=(6<}GU%Ua`5P^N?FH}3_Y3zi?ml%EakKOvt{s{<o*MuF'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
