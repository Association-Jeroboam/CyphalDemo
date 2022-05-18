# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/408.Read.1.1.dsdl
#
# Generated at:  2022-05-18 08:59:56.731227 UTC
# Is deprecated: no
# Fixed port ID: 408
# Full name:     uavcan.file.Read
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
class Read_1_1:
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
                     path:   None | uavcan.file.Path_2_0 = None) -> None:
            """
            uavcan.file.Read.Request.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param offset: truncated uint40 offset
            :param path:   uavcan.file.Path.2.0 path
            """
            self._offset: int
            self._path:   uavcan.file.Path_2_0

            self.offset = offset if offset is not None else 0  # type: ignore

            if path is None:
                self.path = uavcan.file.Path_2_0()
            elif isinstance(path, uavcan.file.Path_2_0):
                self.path = path
            else:
                raise ValueError(f'path: expected uavcan.file.Path_2_0 '
                                 f'got {type(path).__name__}')

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

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_unsigned(self.offset, 40)
            _ser_.pad_to_alignment(8)
            self.path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 2088, \
                'Bad serialization of uavcan.file.Read.Request.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Read_1_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "offset"
            _f0_ = _des_.fetch_aligned_unsigned(40)
            # Temporary _f1_ holds the value of "path"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Read_1_1.Request(
                offset=_f0_,
                path=_f1_)
            _des_.pad_to_alignment(8)
            assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 2088, \
                'Bad deserialization of uavcan.file.Read.Request.1.1'
            assert isinstance(self, Read_1_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'offset=%s' % self.offset,
                'path=%s' % self.path,
            ])
            return f'uavcan.file.Read.Request.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 408
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jJ1Sf0{@LzU2h#n8Mf0jaW+ZYV44<H(7`}*ES+r9sDX;yV3N8GCw7AEeq4aIv%7Q7OtZVQ?9AFekw7gHD1nt4$d(H(kdP2U'
            ';-24zxPj-L+4JEq(L{;QnUDA5d7t;08Gm;A%WKOE?oab(IZjQQg^>}J;+cBP<4lB6qVrN4WkuUuyel%5<72urE=BviUH!cMW!r1c'
            'M5-u6)yjqD;<l~o#MYHKxa7sC;5kgZUi00A7vWIB_Lkr&{`*BOjBT5xXjfE5>4NN>{jmG|yd5kK7Ju7*-ZtkWZf&LF+6vSD97a!w'
            'c)F@>UR+lqOJ`vOQOYfkEX8)x_OhZJ)h<>ne^3}TDnxp(uwo>tgE^g#Vr8RD6eBC!0U1xYu~Dv5(aLW$mmf|H(YEjo<~C@GGWt!s'
            ')iz&`jO9hjt90Jb(>j(xb4Cw`MgW!5QL2-+S!gl*s&_13muI_ALG#Kypbt3=$P4nN!KuLlVJ0sDr`f*djS~>7Dn4$T*FNMJ#mIdZ'
            '${LLxO!;CYGLehIdI;qko#k&0mgJlA+k*v4On&!C9XIEIM#&Rp$L-+1&DXm0q9GOJ*xldp`%Xu3X4>Y;B+?l)2-+V0-ZmG0tgMfB'
            '8(+Ifn-?NowhcSUh#BXx&J=)M-VnJ44i;p4P>PCMUClE)kqQKo?=`R9(M7_oD2`o9>C(zd6huv|e|fXcGG2|3tUMF#@~jr^7j18_'
            '^vuNaUI)W{?0RjB7bCGHN@3MWAw7z6z7J5bVaE;1k0!Ppez_{z!2*52vW<VAZO#%W>x^URV3C$CJTqXc*e`kEnryR<1p-M>hje3M'
            'Ns76JQeu`YgKVcuN3bjMD!wi^OMrwZJcXU8d9bLrT~V?1-1fT<*S6Mn9&EY&@}uUPlj0zbN*D^{K=UnaIiz_uv5r0Gh80g}6bxBf'
            '?>=L`Ira7rTH>AyH2;6W1RHA~NB7^|d~fIdE*e>PF686pg`2l-O^u0Wc}{ksc<hCYj6RY#WF-svYx%1hVvq`?K@3UTr_D<s`o2h`'
            'Qdc%oX}j56ij1zSL`2l7kpr?hOFuFdgFX+TvHPxnpQFf&*U|Y>lVYAKRoeu2#--%hU2wHU6W1}g8&zV2qQc)y)BwvFF9_IAjv(4('
            'G`tz!2np@hlJYD^k{iTOQ71zRc2y$Ur}E0j|5;pE*n}F3l##hGSYu>`nK8z4M&UA1B#^O`se*m5v;I!VcBEjs$i@u3Rw*+AhKaLG'
            '8D=pz)YTqDj+u-b$yTnfkXfUO5gB%4Jq)h0N(>?T%xbr*(%Q0A0aBP6vmT9QI&qv}ddT*qN+h{R#ZW<_Sv+?8C>>F)hQXEqIAD^u'
            'i>QTRJrRyVwi1SLhwNEFKDzyoV)q>#2MQ7dJ)T*q>yd<EILi5$C6fA+a(9{4bke~W8etb$5;0kijEDkRCn8<_VZhimw&tNLwZfue'
            'L^*PgEMVd+Q^g}1^H{@W=0gz(X-{DzpP?F_Y;cAath$kj;n_@Q{aDMb{E@ul`(XWmD!u%WrzzYVQ6tR$1P6ENr`y3&eNaVC5)UDt'
            '(C+Wa%kuBCSIgf$mA~JVjr^h~pUFSSKg#D=`KA0*bLs6H@A!MdTlhO=u>A8Au=QU{3kx*oaT``TM>-XH#8PEb&^G`#QD!Q&-P3>z'
            'G7}T(wZ**#gaDC%K%IabW>{w|;aP@~y%n;%=qct7MsW49V7R96%rIpQn;dLJed2|HjDio`I#Lj{Fzfh1abX43vJyOzAk`S>Prz;-'
            'b%1plq98-X0XO|g+++4wRQfA>?L0aZYSU-RPbZlIRaqfK>Y8mRY$7`w7CdqLvD!|!QsFcrnSp<T$2UW#8q|j5tw`X_I3`LF_{&S5'
            ')i9U=;6fMIfNsXpS<Ws%v`^t8yys)n@u%Rar?qeCtHheCa9j|GF?BNv?)w-a!pb4uV=&diV=nfUv8#QwHsfVkX`C)dgo&!sRX{3+'
            '9zayist={_WPn1M3w5$c<RyxZV4Yv&J0|>$5R)=s6ke=ObjJMWLeLT%RKQ&qsqzvL<D96C@H*%D>WYRe$q!Czg?myO#KP_gQTUv-'
            'Yd*K%YhSKLl6Yn6%uW=kE3S?$R|S;==<uA6gl`gXM<b9t?!xT{zy)WCSJhOw+b%Si8U~o^9Ctm^dJ>b=wNj_fL!D)Mj~paZ=?mF?'
            '0nDMkW1r5R)P}f$yK@B|2g>yueMiuiNe*%5_<<9^$zZBR%JPg+6r7Z`KT~;w`uanMikW^2M3JX+QzOL6Yd?-=M(1;2>Y+P;y~xqr'
            '0Rrsf9!D1r#*;)>X{VsHjE+5uauU^%m>3EN#;#*d?DM>&Ude=OLQKY8C07)I9>%Iz>CX_Dom)ooj#GuHtJ&$*)vqq89D1+FG^gmo'
            'V7o3$ZN#kMCtXf~Vt?(LZ~OhVYd3Fwzt4<5lC;|}%Y3LkW-ie^*XXebRzgGu3o9X8pO)AWdsgTEY#;KO%XDgHu3EF{spVj82nNij'
            'H%+KN55iujK0KW{?8SoCn;h`X#nCm6TT2w_t`|Y&AD64Ht09KTBhm*xLUVwC++8R#(ltDCYf>C{H4oV~4u|e0;m>_tT4KmZ6x4)*'
            'jtuEtQ`jcpwbePg$eZJkA3;Y7?*F$P(o?EHgx%hmNV^D$0ku6UUj4Z{jRz#?Vs#T!FLV5aHxJceI$xiy>F`2p*9l1j9i3i`CecuQ'
            '!IUi?KrfOGK{Gi`I#wy#6tV~LuF|#1#(htkDIru|y4yPNad<e9!1HM2EtuPZ6EJWaZ)m`DDBkWQf+5_ouT85(LCpyR)j#WW&K)Rp'
            'I#362uOVKvAo78tV$eHwB6d98RmKY)3A4M-cFpACrFcLo>SX}z^air-;PZv3^B99b+C6Zg-8d2vCMZGojj2B`;3wU*{yP0M8{72D'
            'eoC*(<5tc;0ekeE{9AVm>&X=VCYLbz7yrV$fxB66b~l@@J~Zy{Z1TLkAYbvnM7S(_U-i}||1rIz$$#SY>1brzjZe-sm+?&UzeB1b'
            'iEhP@!@mn))87Rg57Im!^U1S=Z|R?PpQ4Ta;;}DfnQS8GPtLj5?$Z2g*C9odpB*zvTf_eWgBiB%I1>N>'
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
                     error: None | uavcan.file.Error_1_0 = None,
                     data:  None | uavcan.primitive.Unstructured_1_0 = None) -> None:
            """
            uavcan.file.Read.Response.1.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error: uavcan.file.Error.1.0 error
            :param data:  uavcan.primitive.Unstructured.1.0 data
            """
            self._error: uavcan.file.Error_1_0
            self._data:  uavcan.primitive.Unstructured_1_0

            if error is None:
                self.error = uavcan.file.Error_1_0()
            elif isinstance(error, uavcan.file.Error_1_0):
                self.error = error
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 '
                                 f'got {type(error).__name__}')

            if data is None:
                self.data = uavcan.primitive.Unstructured_1_0()
            elif isinstance(data, uavcan.primitive.Unstructured_1_0):
                self.data = data
            else:
                raise ValueError(f'data: expected uavcan.primitive.Unstructured_1_0 '
                                 f'got {type(data).__name__}')

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
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.data._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 2080, \
                'Bad serialization of uavcan.file.Read.Response.1.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Read_1_1.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f3_ holds the value of "data"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.primitive.Unstructured_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Read_1_1.Response(
                error=_f2_,
                data=_f3_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 2080, \
                'Bad deserialization of uavcan.file.Read.Response.1.1'
            assert isinstance(self, Read_1_1.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
                'data=%s' % self.data,
            ])
            return f'uavcan.file.Read.Response.1.1({_o_0_})'

        _FIXED_PORT_ID_ = 408
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jJ1Sf0{`t?TWlN06(#pc*_K1cv8}{Oy-6IKP8^zkD{r~790}tqv9g`0D2mlmTx;l1Btb46DnJ0`BL#ylkVUfr)UT>7(5f#$'
            'MS(&sQdIp2pf&}f{HcHX6i}d0|5%_Oy~E{Gd`Oh_XcFdOEobgM_spHUGvXZYP6;3X09^Th%oB;pa4H=2t0_Gh(V~%ev`|#{t7Gwr'
            'L_8HSbldE_u16yicp1Junb7Tz>@)A#@7g|7QX{dLp0ugU?7U?p(_=<DsaKnbYD}9zh)2`f{V^@(zZ*g9VO<O3AE`t<mcl-ddS6eb'
            'BJmgllHVv?e`FIkaevQ#&o=j~nqed(p|qi=?C&CK1Ii^U+Z1m^^k}%uW1kw<3{5o{IVwAibf0;sl2%_b8OOmKpa(Isi$$h~Fd98l'
            'Fz;#<H<4u7iQLDyhwsEvk@1)w9*7zGxSp)e#(p&vG1RCY8#ky;yvS-yOBw1!JdCWKG>-<0K+MhGi+#YlFcq%%?P1$|L`@l5EUYEN'
            'l|b2a2!|rx*P>};AgJN^m~FajY&~pxdNIf7W0XkHF8Xxg>J;(P)ATud)<NKgh)w<U9L{S2>xtrc^-LnEr`Wtyjn*@)8Q7*pi|F*K'
            '*>N|ijj`4g_TMO6W54MR*lZA~5C%KH5tq(8gJf{%%|W$qcz9?yPm5lqFBXE(*G%!s<;xc@w}99&ICNXRF?46}dL1<Pg%*%J149jI'
            'xm%&sd9Am%@768#df(tcUp-pf`HL;U9T-5Uf#JU1+e5?OMl|!a0l)4)tKe;+PbBc}Rg!q)oqIcpcd`<XDVmbd45}DZGn7O;5;IbY'
            '5y#eWB&m-X@#Lhvj?IPhtqg8p@QrIX2d=C5=bb)A=W3sS9O<xoO<}8o5=kksxS?RNMZ(J6coM1TilHUPb;GerO{S1~4UJYN>)?%n'
            'n|<o-p&|9=wc*$M>LvNY)mD-`bmz7@bVI!ryw+PEt-F;Zv7)?nCm0+WzFofpE|%eR^KivNsD>t;wUxm>PfyS*^a6dI_R?=rpx>cy'
            'Qk`lvPT!*M(EId#`X2p|exLr3ew@ZtD6He{Jf>ku*dLe&)w_|59##|aq@hN__Mmx4O~up6F<oVopt2&dO_}|OMnbmP5yWjF6J)I)'
            ';hN??hieXvvqhduL~L_k?_`2%(d+s|+%}IV(xGT%Oik+J=_rd=UWRdbket;Q{aGN}JeXgB{pbAwKU;QegROaoRjQ?sL{g6#Y~8&d'
            '8Pn|#u$;~f>M2&#49vd|x07_#P~vy7fGcW8i6``Aev$ICr7;x6u&0WvT6qmcU}ODf+dS~ih;cLj`IcT<KuunaCu~z`1d^JZ2*q*C'
            '$Q&>SxJR()LwOpwy;N+TV>E(W6#b+5P*4kpBeC%sBl>67JD83}wdCabUV8OI+ef@sDug>|!a=Z!Cmq6ZPDEmCf58ha!!BgD$KVX0'
            '8}TqVmzBcZ2bXm%mfvj$)1iFD;y$7~+aQ)AelG2O6`ST0g-x@x5%_V_D{lYcnhmsK|2*Dc-%cjAN!vX3hK8-!;^h1qYpvctJ5@cZ'
            'Pq0F8HuCaa<tg1&W(RJn32iK5Oxoabn-3Rf=Pvt=pvIBij%SFQ-DA#8`8)c1C%u25pH$4k5!^`G9TTfNoh&GuO)OIO3kv;o-3(Ph'
            '9UInS<NC0k(2Yo=+ITBJbI2b(D#1KfewzM9T=X+=dFbEKoVcACC0yYrpZ|$-z*$5nw27rQ!V|$FlJl8k*K$=K5s73KtAupa^br|Z'
            'kbNb8Y{Ad_>)MeHvd<z1oIVeW)!ERF>?a2-a<B>)Te0n-raq*T9JGkH5W^yeHnb)W;iQm<Ya(F}wjbV<KRHAmw#Xxnt$_UpnD3EI'
            '`;x=t5sMtH%K>|_?^sJ%<On%xk*;E<k;|hk`;%j&%Oa08<b)R3e|$^0<WcgNMINup7xp6F6I;e3$I0Us`9@Q|XoWT>9w-KRf_%dw'
            'N-4LD^^*^bNKO#NB2PIuN;Cc}`qSGIk3319vdGC|%!+wnS$byMVvwiFNsFA?aAwd$L2I-<y{)myGvt&-e8q7V=IqS2#~`PP&mzxm'
            'dYtHi_RsAI4|0Y)Ymu|%xjl)PzRLN1e#hdH=g3)$_*=>YdZEv`9pyxxCw_|r%5~s#D&hQ&M<wS-z#<n~&Io#<-^E?wN6wQA7P(Yg'
            'F=r7wP^_BEyT*lFB$q65WlK3jZ}h#ot6a%ta>XLu)zuYX_4UH8^B`AAw?$sua_$fT{a@M>-sA=HqD5YAT!)u1MmMX)SN4n_d5OGi'
            'kyjrmzleeuukGm=$SdSki}cjgESvrQVrx%z`$%<rf4(Q^^wDzP==xqVVv$U3KP^}!iZ<Cwo2mL%Bx8|j$BtQKu@`^cMIRqpb)#oL'
            '+K!+<MGv%{t+ky->zPLO^NsCi(POTj&*H{D^XRp(-fwyHev9b2RO!3gy6-Z2uN3`rTlZf@gf+wfkGlYZ-%ne{$yFkCtwTa+1_oaD'
            '*6@5y@h}{N1jXGNYIh5$NPz)Ez`Z%_{w-r8Ed~!g?&c9jwkZNqWkDe5t{;c)NF1c^go06bWwgw$M8iR`fRJ#rnAwV$FttNrab&fT'
            'r|U*WLWSU9?QHznO~*&71qv{;-7MxGhy@O!Km_I<oXg_2bHU*i=)l5O7%lG#BOG{v6fA9y*Xo|}!jx1}gOxh$a{qtqFk=ORu*Nv1'
            '>F0Tl;Nrj~fJ*|Ghj_rlfk%Lx2p)-e!OMYH0Ix*4po@bp0lFl}$wUE#14RHuB0lhO;1j?nkpKiZ2nZ06NH=tI&@Di>M0%iygB}5T'
            'B+?K49P|s&FOeVwIS2|6l*kB-a4;gkh(tzVl!H+LMkPXlazF*35=lUUgM<JHiDV$dK}LX#gsGk4U`l`~33Hp}AS*yt!sJ>USOQoQ'
            'W_Ox{X#u7sOz#W_GXl&=nBQ3rW(Am)Fu`*i%n2|jVTR{9m=|DP!W1uXupq#KggIX1U{QcY36s3U!IA(=5@vasgJl7hC9(o59IObi'
            'B4LVGIan27Rl*#vaj+)9nuN2E;~<Cmlvp9ScyNi}l36Kuc<^A7WmXJc9=sxWWmXPdJamcBC9{H1cu+)8WL6SB9(*GBWL6Xb9s(i+'
            'WL6g4JamiDEwjSt;h{%_9+{O!KM(yP^vkR`f;<F82+FKHMtB$zVMJ!-G0MZJ2%|Eq4$1=+fy%5t5<DbCNXV>yGCX8N$jDg5FvY`^'
            '2vaiFF=TnjijbADlELD^62X$OmSLKQX%VJntY(<uVMc@*8S5Eld6*SpR>q2kIUeRjn3J)lVV;M15$0vAYFOZ5L4*Yv>lzk$SQKGV'
            '#>$2z9+pH{lCid7nTH$?%OWhxSlh6|!-@ziGFCUN@~|qxs*LpwYdoxpuqNZ3Xr)7XiisOu`Wbk?OyY)z9cs75ja?8oyiOk4;>He$'
            '8(wV9XLno04P~PPlN}H@l<Il-%8DCGS&;hLh#PFoClT3KJ-=UTaf9W=SFD7#xUo*$sIHi{xY4S(;jA+3;MCg|Hy%LTaCW7(xUn1J'
            'MtMc76gOCFPj&l<)8134@mg`iktJN%Q}nAAH;Vnu#Eqh~;VRg88i*UrBAf5sSlp<#-B{eHZ{J+pXztTk+}NC7eQ~2T-&%2FDnA!l'
            '^!9FD+{hm*mw8O*XQMezrV1%n6gP@U?4;Pk4r<(6#q%}9W9Pnwp>8B@)Sz~^fVzRWQG?yTC2V#sTYz6LZq!5=*`^5V#EqIbbVuT_'
            'v(tR2N^v7s6gSE>m{%FLJzB*<Xs#%36puk&EM#`u2U&YSoGXeO<;YogWpH)?yJ0DAbd=vT{_G~=PrIurY)RZ`%3}V3ShOr|H083m'
            '?OZk?ZZu`Iyeo|AiW^ONt?n5wCLffjt<-0it7ey9NSL&d-8**G;zq6@Zd6Je;E}-NDQX*BLEDhP>tPB96F2fAhp?CO24wI*j)@#X'
            'eR+e)8U=-;EpL2P<qb#M$nl$(H;T{LIL}u)&)8`6NAKGAK5@HT^dBku;}7Uh2I)`f&wTXfbe8^t{*wNR{@U!Qc<S;<<>NNhPfO9?'
            'vL~Znz7|u`6*kIPJQ~&W4`Q+hq(YO1o;s`O`KR%c+S^Jf64R2CN@PMC*Zp?=Ct&_ky80*mD|^c5%P7;dpFwHMG;NutEz`7Rn%$9U'
            '*kNZ|rfJJGo0n<I71Ne!wj$H8+_hzzwoLP7m1(Mv13c_RpmZGI!Edl)!{dOxJPRoPZO8UmK>IA9(OE#wU40xNmyZJk_EMC>X@Jg7'
            '1AKIe9=*4pbGhgj=>|sv^f%_AOM!0ZWm@O)--<(kZ2m<u8+?y1xBbg8`!{=YMLo+uRes~g|M3ey{d_PTy7#Hu<#PVUrb0gh#Z&4j'
            'Ijn1U22A(U1JvuhT<a+PqJ<&f>qLW!F`BZfXAC`N*f82*9#zAI7nLPdifO?g>tFYw(9?9a$%{TJQ&IWe4W;@e9{(v^{TI$QdPBz`'
            'j(oI(jlA^6m3#{F`C^?@bvl`=|9{-U_rsk{000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Read.1.1()'


    _FIXED_PORT_ID_ = 408
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8jJ1Sf0{`t?U2Gdyb|#0vX8c3PaiS!fWY)<hbRyHTV<*bbZlty4m2iC|RkE{MU>DSoywV+ooMC5%mK30<7DZbbV6iO1ZPo2V'
        '4HPI`6b1ZL_|cC>i=sxK{OE^12>WF8p%u0d?KyX5$e~E;&$8X@DnBFY-h0mZ?z!JR_veVS68+_GeioAd)ZVHr7wuvxo3pv4YbE__'
        'Enni<T)`|?Oj~z&qxQlyw{GYKer>tJ8{afe|Ge=BjZE!G&f>pc<+hV^s9c0<M=tY{UPh5(d&_uEHw<pcCew~pEjU$cld@RO(8_44'
        'ud3ZBXhwEUM+{S3E8;^MY1ERr8{D#W(;z*GFTKy-G+3C0|D^GAgqhPE$I|mvhue*xq0$~bYqo0CVpnutDz;#xaz)M2+z#~;uUOPa'
        '{RXx;aow=>d4m_n42REitG!Pz<np?cD{*7q5e-Jl3mST>Y!=a5Z`NL(^c9g<_7c_sRZ)-rxG~kJy_B;Z%_wSCF{tQfH7}0U;^y3('
        '&Cx5-T+u8vYM}-ezvdbiZ-~R*r(?Br(4mtWDiFuT38t_R`Aocwern0pUhm;C%hHw`wO78>uoO$KN+`orx|tKa#LL|9IiY%*-)2ei'
        'j(C@asAJ;vYBgUwgx;uV1>IS0u>Y;S=yfkQM+4GTI^)VkbNQ0psJ-hWZMg<PJDY!R)DHhpcU-*F_^XGs7Ri~FMosOd#9l7v&619e'
        'JpsIIq8}V2+eC$1nqyi)W*3Bx1QJ(kCoh>sL36m#wJCL%T3Xy7YGV6i<JD40vz9wr#&b8cQk6G;(a5l5-Oh_~&ketaQm;&D#yp?m'
        '74GQ0Abpi9YfI=<6!?iO6hHNKN&l5~qrpP-0h_@_qLv^|R!bT-WnpR>s@up`zEsf+ImyPWd5%B?j)M-Nq*w?v6lJU>%}BOrMH1`-'
        '(T~6O)spBEqHxpgM9ua=9g>5JqKBqOCWohnuT4xzdGXWQ8~)%R4vX6aq;2vgr=+K~lCK?Q4$WCwfl84f$t&Jxtgk5-K5h{ABv5NR'
        'Few<G$z2^8|IxKk4~_WRGa>%47CC?MVpAEfod|@TTz=UNWTdnrE{a8Ai$4{ARK;LW<k$^jNU?FVb`*)e#EZF#X*oH)*ch)J&)H_x'
        'D)1c5)SPr=EkQp@dLHRBiLrP|&fjlvki%zj<_nV|rc%)xwbZ5MiqJ}zk*f`y#ML}<7sK;B4l3Gf1vPX_+zkjQPlg(`BcwEYK0A;l'
        'Z#Nu@JSTEOvk`+uGud{7f8(b3VCFaBP-q;ZF)ym5E}I%wNsDSPV_8`xxGFaa7{-dKZm8F<T^Y=(*92EhqqM9dul1s8b5u;6Rdri+'
        'ux`$@7BR@Fc1g2^dg|;cQfuqRJSmoC87w@lT6_+JzUr7#$}&wyE$Zk}RJE*TsH|ibBqvmJPF)mwL6C_epVKi!tNCRqN8RDp>1=9>'
        'qjQi+u3kjVZ8gKQ^I7#&HjC!4_o_iQJb4Vo@^_qZNI`NzMk_hOtj-HmjE2hEvRV){KdJAsXH{D1&=yXF8|X_SrkWuo+`wKJc=7b7'
        'DOEkA4!f?am^wBx=BbaG>sfS@rj~T$D=Kq+jV4Pj6poM<brjTEUd{Ga*zy)?l_kF7R*k2<tLBCn5u@%rU~N(9*rZl0qM43pgtZg6'
        'a97;w21{1kqe!pd!Ns4E^!ws<@ekrmRs7<nsE><37g+X7@fYGR#hUml@hkDywc{5C2HkzaIsCWDVDUGr$ku;KhC)>5`fbiK%h(+Y'
        '=ZHfiTSWS%kefKnG}O+biSEKMlP9lN9o+vQA&^MufocKCVb4`dYC$WNaLCSO)yp`iRJkxBSHI>eZd0_9t?G`g`U@LTpLoGBj3OU2'
        'N0NeEi)tl52p6`Xv9!2W5J;+JTz^vP`A!4au7oH^k<n(R-^abIe$6d&$5uUy(hF6)U)9~}LP<xess`spIoam8QxKjG2YDjpv9;rK'
        '#lqEy!VKCc_qdb6iyAZy$(m6>Yqn&f;3;?W(yvxgVF?{<n8q3OZb>b+`YZwB^f4sDF&CSeUqGI^w05WTd&HXe(6B*H%+qYf0e9yy'
        'LPRZ_c#nlele<3WOS<ix?#HREYL$v*;_8AOQMqNAR*Iq+&H+RvwYpIHWf&kR0jPc>UasJvBUot{`@2m3vpM&N0ZY+}V;0Pk>V7sj'
        'HNk}n{cajX-3<|WTqmkFcjKJPS2<|dOR|HjwT}CwVk*y_Ma~Vk&!(JwQr?YyWqn={uk32c@gtHqxMtqbbc2Qiy`z=2dG1aU<c^6z'
        '%6SiNe+vDAYl$0Gi(Kw@F$U9wL7$ps-0M-Sr(jZ)Q^||Yb7rYzE|P&lGxTNEs~mlf(RbPH&Z01F;s)-WE#z@Zm-CH&N6?NcGz`uf'
        '{=gMLhQXpfuRB^vB@`M(*8WzMw{d*kMTZ8nxPTtTeo8Y{glM_3AD3p8*5{O6os$c&8|0|2jQ~rykE0ETsuc>RRrDe#HKS#ZQ2MAk'
        'FsV3j$k;1b$CtEnh2~0$%Snipd2b|7>E!fmUN=tlw>;2Vw``$#oHFdH)mpv0@vBy7ILt+(WNL&io0_gxDyGd_6W*WY1Qg|~a`H`&'
        '4xc%H@uPm#Haj{k1zJ6yGhLs_jxNfHp697kSww~!PG!|A%^{Y=ZjEz)OAh-J=xI|;V6<A*P0gv{Ib=Yvd(95@2c59!MIWu$GMLG8'
        'YHyd(eE}Ta#F1@@BHs2Q<(*(p%UO-Vu<#Yd2W=iF2NF<|8;TOeH9QPgDdNbjc~+gq#lhQ2xa+=Iafl)F+@MLwX~__-X@YI1w5ns4'
        'aTdAiGz>qSmK5Coe<nTMqzVRMDccIt5+O05>U0LL{=lBbbx6v?Dl3{+0{ld4uB$fF`E09==P#Vv)dGbES~}fe<f9>csU}-o2f9I0'
        'deHV)6OUCo31!uZ{0-f#+NI@wmo!a6=;eyst)qXWKV*==<I%jU!Tu~I0~m4}&(P?mO?bVP2o>QT`%H7R2vi_2(D;|UI42hrS{-Nx'
        'Xl@K~gBAw)lum;|=U6}3X~i45?FKpu%yK*HO(uz#@F1mVE~A5Gyuq+8-RBNOwVcO7^t3$SV(i8x5n&=FXur|4=LYazJFUNKerlCX'
        'yUo6&Q)Rc7!6RUXj+1}y?ZPrb$N&9JnD|@wgg1bDvrKDm)@;40+}*Q@v^XwKx|ayAi!(djwTXXh?$N{@Jbg+UISrUSRC^hZN$wqz'
        'l@mBy@yF)70JV7+(A`NvhXgyXwx6Xn?^6-_!(C6xLX2adXAjBKZZde<m7b!?l`fU?kbM*nUpB^Qn|tsRp0!lqYUb50cU`Vfqvh6a'
        'cRI&|f+Mt9aW8ekT`zS4u1g0GxiR;e!8@&6+cj4vSeLVKcwp;eb(@MK*T>oT#E-{wBU4k&bAC`;?4yepKfJgLjfci3uH~*wTpz#O'
        '4cqx$XiAPv^n?}O4WuK(moAM=Pv<U=jE{|UgQcANa2M(hkD;ousgX<9CZ>LZ+G<~nWqB62p?Ctt?Iw2@z_W|EeW0*}K~5h0WT=$e'
        'WP8)uudxZu`E$GJ+}QY+!&k>H=kR%bgy4KUf;;VgH_X${%0JGyXMKMY;ZP)Zf_DWSFm^LoN3V=s9m!prn8;lnp8C;9Hz%L}csEX-'
        'xPC1+aV0lBIee+Rw!z&viAXtpeR6VQ>RNXOeArUw#mxT_|0(`Q{P#jE911Oj>2Zu6FVN#vdYq)k+w^#g9%txrnjVAnxIm9f^!S1v'
        'K#wtc{Folo_}JnMeN=`JJU$Nu570MpaL=~g^-Q@Z33((A-ug5T9@{Tl!6=&!E=FlwjMCkMDTONT201rWbqk4acp<TQKbXCaJ2)@Z'
        'Q0xeg0Ue)spFZz?88{4~u=wGoq29~#lkT<rgnBJMEY!Rw$@tf;O!0n3<WKCAQfE=GEY>Vz5f-hpxcj?8pA&6$EXLw>-_`6;M;%Kb'
        '3YKchV+sELLf3Ze5KGnBVYe<xwvO~{$6jEE>+EQoUM$73V_V9wBkX9Mr9B&Uc6{5`>==5Sz1U$1Yq0#pj^x>K_F|pA<hG4s{b7<l'
        'xno&&g1uB{FL%X&wOIGcu5_`J?BzP^^F57NUfs1kdxiDY*=s#9VGFE(eNTGXtL(Kp`%as`uom^bv1fhkb@rV)dvi;?*b3Xc^+Yz<'
        '8|=+GQ=7ge)Zcw#jqEMlcCu5h9(61HWc}@ZvB$p4PSx2vzRkcmke9x<Z#LN5?43G$ciWLc2^Cvo+xPa>Hv1lXx6U$tKfN(Kz3(>I'
        'dw6bQ@9(&uD1q%icq%y9Y4(1d^|!|M9n_f#j_;YLW|w`y`s*yaD?gwV%A9?wnAjPXt+Rm^4>B$j&OLRj>?|9ov-7+52uh;dhtC8b'
        'JIBt~*@aHV^rP+ppEVbs85Z^-yHIBz?a5~-jj|s<Q>^SF`>4(a+u1ch{QBgX<6s}N!8-eN&%Q$qDF4}W!OcElpVryuy?J;6Z443@'
        'zyI9uvCr7&b@qcN@-J#Z9bY`xKCthzAJo}U2WM&YNBz>F_VStb@=;kc>DGx>-R$OCHdALyo%O<NQSsZX2HUK3Z^f4CY|U*)EmpA>'
        'x4S5l!B&GPIf`v(P+p(}w!Piib`4wK>ec>k@AkJ*;!Zc2``gRhMX7t6<sR-_?mkLB2+FSSUiKkMKl0@__AbAU8Xlt#NQONncs|{='
        'o{gZUzD=4?H7SF1cyIbLTk1n|q!QHd?z9f>LMuWb#V`=wneNd&>qc0l9)`kOTbS7=3ka2rz+||)9r0A`Abi&p%!Y&3mY#_<>=YS<'
        'N|<b}25iF0Q!<M^>$JSq)iMI|j6?nD+P}SH`v}#80JruV#oZ@Dft~Pxz?~<@a(~~kVD~&YaBnY&9zGL9*l`aOJlGko_2-5QT@r)_'
        'kGi1S`2U9vJ>~&~$Aqye$`T`l6bMBj6o*ifB_XLmG71|pNXA(j(h8)bkdCuH=u@CC3Vm_dNH7&t1=J|0ah8FM0+}de;%op06c~uY'
        'K%5Q2paO$Y7>u(a7*b#;3PW)=3Zn{)MqxD0CSg*6$tX<5*$m7mFcXEDIGcr81!ki#8)pK90wM|`&MHt*pb~{joGrnU0!vX?ilb{+'
        '6j+JEN*sN=s=#U#R^#a0x&rkm)Z^&gH3in9uog%6-csOJ6mG@Qzqb{*9fjL*bnqPo?nL2E96fwjfxA(-8%G!4Q{Y|{?#0o^_Z7Gw'
        'h5K=I@&g4PMBzakz5Gythf#PKXOG~K0*|8bD2^^(S71E~>v8n)V+9^Z;c*;CVMBop^k<xi5Q;!32B8E|AsK-rIypgPNJk(YgLH!E'
        '&=-Ne81yBG5NZU}7^n%NL?!~67-SMeih&3W#9$ynv>1%QU<?KmM2w*b48>q5LDU$Hz-SCc6GV>52u#LcGC}m1iNH(@W)eh?*$B+W'
        'U^YSQ5D^eD5DDT(B?6TgR1(CWr3fs=U@3tthLs4c#9$?XJciW>tj1t9flP*a1nM!UCy>jq7J;=GtR;}ma4Q10VsI;ge1_W*xE+Jr'
        '31l?fiNKv0+({s(;cf)(#^7!OSq=9ha4!b;63A<~AA$QZxSv2~!-EJsh{1ydavL5-U?Tz#WAHG6+=fRHcoc(231l~{M_@e$>j~sH'
        'JdVKQ7(7nkOsxBVN}d)vq`ytcjU-)aA0#)PL2@JQ`r#nC@f4C9X)KlA-Ph!Xy4{7zQ%G*8?c?xUo7_-a38~+i<OcQm9n_p@AK%~U'
        '<Oca9<1^tPxv?p^(axBI<i>838*Y@Li_`Q$a^ne-8}6!fklc6{$&FS-3??_Ibf~?2#w{Q6INq7uaMKbYtnuaAlN)~hR>=)NwGr~#'
        'Bzq(`sKu(R-9EX|-gf)sM)&qxCpWg1>7CrznOyhe#_nW0lN&2?ELKrEz4zpXyjE`ESd*i%wVtImO&fl4!`DPN#YwuT3GY>3rl&r-'
        '_w~BEU2>yC>)<Z5Zj;>T&^@{*-E=SOso$L3=&&%ePZl;MH#+Qyr(%chPNk_}a%00!ZnQWkvkd!gEpQRK;U_ozYtRsxT;2Chc3u!~'
        '_{oiy<<)S|I9<SQOU3Q3^0%~qdk6N{!tD_Dl-$@7#oZ@DvFqf<mRRoZJC+?JH?~Cd@R=a$n%vkD*ZOnAMd^bkv`5|1ZM374frL^U'
        'tIrQzdvasLOKt>H8<31cGU?|w6fd_ChjfxM9F*LUNsj3AOmDyv{-;oqBicQ^L1_&y!*P(__-##ZxVepu$j;Ln{&!Y_U$4{XTRsa+'
        '356DJghL^_$Cq(xhXU`nIT`#0OSf<5d_HWb)j%7yV3ta};J*MRzwB_kU*+=qS(dh_=5>R<3G9C1db_XcEUX~T;Ma4$UCEk*Z=xI|'
        'YYvh%2g#a)WX-cl*3gybL9*r`S+nzGO^Y!H$(p?+Yshy8$(n;?&9^mK(|#$Cq<ewpr9cwTv9X?)0?+eC!2g@agByW^8-ZRo0vqA>'
        'OMyh|QXooi4QzYI<wBXx*}q=+72OROTfV3x_}ZlYeS1OFLUGeU-+d2<eEr74HALn9xuz;~P`kVrYE!xQUa0lf3ygj(d-a5!{bza)'
        ')4zPXUIMlG<=gazr>-w{N@B}|_hz-ucbxnOy`0Euz8ES<oqr=Y{wqEHogNPq-=R1Yws7f9dhJ#<pZz~-{kJj&UH||'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)