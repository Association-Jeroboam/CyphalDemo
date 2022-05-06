# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/file/408.Read.1.1.dsdl
#
# Generated at:  2022-05-06 20:25:54.622919 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{@LzTaO$^6`qZq^}1~*F-x4F2vRIy&r0LAW5p2R7Zy94nDMU7?&k6U>Qr~vOjX>|)pS+w?pOjPNFW<piou=mz(b@+'
            '2qE#zZ$rGmcdB|WdlRu`?@V1zo%5aVe5YzZIsN&q<&OJPzg~<}lV)LLM5%bD9`QI6VU*}mp^dVlsW03SnHu3^x-%|B^Q>9@wE1<@'
            'trsJe=b~(6r@pXl%PO%|DGn}qKFawBCSI-hZo>0$pkRAT@D%_3suIRF^-{DeN~3g6cFw%tety>U7y1joZ$546a}l?;RB>g6X?_W#'
            'CwM$v)zr_gE0Lu$H-aeTmPeL+J864SQjBUBE0*8OjT+`6y_;Jx6y?E~&PB1ZQ6}=Cl}(?FC*0U*q*KwzZ`GF`ObpSs@HXZ)Xo@2G'
            'U9;8H-;9jqdCJRl-q4dOmO;I!2LmI3%IPT8NmF+k48QCTmaob)?WdrAX&%rA90ufh`9lA>euprV7lG4kU;Ww%h?ONDH}xy;bBto-'
            'o^xf5Mh}L3ArhGwiQIY!<!i0w@AQ}C>+-w(4h1H^|G0|lvp}QZiL&FS|KIu>ZFtdu5_0VB@A-YFqc}57eR<;P3>r9X4}Wj!^FLMA'
            '`@4;=t*7;=NEc1bPBLP~qgZDOz%Flykp>PHWV>I8l3QKQGdqzA1d{L6FW=UA!mY@UT}t87%2MP+O{{-$v&u4Fj*qNdjCOfeiRQDW'
            '+h2NWVtKcP;U0Fqvc>bE*b;@X>LiyQMkBrtP_bdh4ayHDwj6#Vl{ftkeZaDff1jz(5GSjQV`+bZmUf;RuvP3AJa<L5S;Yd5B*;U$'
            '(OHsWZlRQzCCeb&>B150vb=(?%k>f<Aqr1nCu$x{>MfU4Y(2aE_Jg&pwVnH0ZomAX{`Mp}@S_xl963;YOIr?Uo=vP{&)GrA6B-3W'
            'me$+Pn6ICE^G6MF&pA5!f6fFOYad4U-rjs?=iSyDS+z&VNA;;2H*ZdjiF$cXcA|Lfg^Y|ol-Fe`bNO5On+jr(3WPxnNt-A23n2Qw'
            'NTWiRHd1M`SznBduF6D2RH=~zvOYsUG8Kb951_I8u6~~($qUy|`BIZ&E?WHLi1*Y`f$qWWaUpqj2dr&S&Q%N+N2M4dy*PO$Z`iQt'
            'r2&@cNXR#t4{wCmL&CkWq(RG(<Obf9RMQZJU6qLDiM;&be-=8OP3W>n8JP=%HAYsL8Dnh3$Z;m}1cH__m9zJD*53-*jucGi*_eUh'
            'DrH8%FtL{@!z|_oy4-`@F_Up4*~+yQGHX;mB*Sj3i@{Y^iUH)GS?zX}T3ePXfD2P&)}^sbCypIV57?emiKHV^F;Ea|7LVON3P+Ty'
            'VX!3t4mjoQ!fRnzSA@fmt%M<tL-Z`CGur(SW%nJm2Qm@_U7jHg)lkAP4jS<>OC(h)#qJ`jsORA<l*BHuB#N>w84)?6PDHx;<AAZN'
            'Y|TSgXoW@jkYeN>S-`|urt*h0=CQ_+nRi9Nr9Fj>e1>XxvcVZzu<Ax8hG#Ra^<ynJ@+b1PuZZ;n`t;%ho~AhFh%RCFXK3MtpKkg~'
            ')j>TuNk)WxOuK&|FUh~lZYBTlME-G8*7CEid@BDW|16(j<>&GX`Iq|Qo7dm+cZN6ccgkV;*T>-Nzm_^3n)ApFN<BhAC91?yZc`9A'
            '06URrO19n801T276YiD89S4*Em4HE&fF5R0Wh~)YhNQg_vOB0M=9(nf`baQbS$JlcvW88X9Fd=xAt0$>1h<YB1TM@vhLB%aLD?(?'
            'Pb6qHMlTB3jiU!(T?Q}6P=4T;-o)=Qdn8KzwNGtNbSPA&$CRH=G6k}-T!_?_+d$Yvwl*x7;`U>;ov@`uXCk4&`2>$IhgLVJ5b3l$'
            '!D+^EQHsD{WO}TE!3+TBI=>2ZGnUR`b`GL|a_8Y)@0*T422(w;eNkT_-dw@KIe{2cJtN`1lHnq(9AZ8OQ!PB^VqY1%+Cy<OUKFK9'
            'r$Hc0l%*~M(lJy4ymD5(D?KL!<jS0@lSN`wAn9<{or`$Kgr5;&k_L?86sr@RG5<Liv;<8Hxa&MsUL<1ljLHbFbe^v+X^4`}LFZPu'
            'Go?W+?4A(0k6F9&bNjvejnq&QuS}KMi6*tl)v@I&r*r@vKH@{+iv--!aAXv>?)C!Uf^On<H5KmW3l*k<0j7F{dmpJi$w}%;snzF!'
            '&N9762P9MR3)wvZ%%Q(yAI_fChPZ)ybO{~@%GDcvhtrlx4teJIfga$5FjZ)GJY(bqCvEM`blxDpzU@#l(~p5D;&jJUaIy62k2cMy'
            'R|lpVxMu8Sj^+*!U>|onx_mI6B)Uvn4W(t&_{htNS4VteNE{fujybW<M+MbNCR`C>GHx@uq6qXbR{2VAhQO?I8Od8t<)$iU{j1Gi'
            'RZu$gUY==A-i5(-RTSEYS;0@LoE*je$`#-CyK7f(-27pW8GR&Zw_z6fKzqzwpnI;+V-c)`@C+7KLbg6lu_N{@&%N0`#4{J^)XZGA'
            'X46y4!P)=}m=A9nP;VZDy;gmAIy<l%3tDeRfN#!^ws729qDXte2ulCZTy<3qF-#tkKJX!m0|eymN|BMS;lW#x;<#&i$hOfO+Pj4B'
            '{JOBjkfF$_2nDqa>5nG2O~5OQ8=F<$9Ebb}YAJXN+;T`ysR9vpduJl;JR}BG_NaLE=593}kf8O|O-xUj<0nq@P#vc8wb_~$FO+tb'
            'kTg*1^kOvehWrbrZ1Dhkk#q=}NjGU(rD#*g?#H`IS0)?xJZYwcP@}@#+<}k7!-)i*N<(kK+zOn4f!lab1Exd%ww(xuaNoW<%@#Q|'
            'Ck&MTtkpT!P^ddl1#qt+UbG<cfudy4n|300Jl$2s3mplwyU@19<oqRnKq;za0POSzvhLvXiKs>~27$DD>_WTI65%E&LHCX6d0xOz'
            'x@&zk{WKff^vixuFU;ds&OZmc^tAk2dk^c%6#pjIF!`l_?On(1tUJ4%O;;Zp_qR5APM()9`ClkplHIR=Z<GI+-qPeh@fLMNvdzXv'
            'XX{INH2L2sm61ff;>Y3N46x~M29Aem9+LU+*}<3fFWOJhMsMNRce6}35%ouB-P?C*{_X3qqRCH=nWU}Z{{S5LQ;$Xy000'
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

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{`t?TWlN06(#pc*|I~&v8}{Oy-6IKP8^zkD{r~790}tqv9g`0D2mlmTx;l1Btb46DnJ0`BL#ylkOi^<)UT>3(5g=e'
            'MS%(}QV9JBgf<1#d<p&1rwSCP&@ZAuf!^WrDLy31dNc|BA~|#Kxo7U&oe}4FcS`v96L95!nI{sH;Z!*4S5ta2qD3R`XrZX?SI6QL'
            'iFhhv=(c&_x*m;8;M?%+$%JlyWS@D@e%JPyk{XG{^rTH)=7C#AGCgLblX|s@sK&Gjgm^Tq-5=9p{<{&x9@e!m{*y|?V=3(OsQ2|`'
            'DiV(|Ao-2L`;TnmChqUq@7d;lRWpoaB$PJvl>J>qZ9utXWt-xSh#n1>dF)fenxUx%BS&SYk?u1ORnqE9CgV7mPI?d{yI5p;2&2&>'
            '1@o>(aT7_FoydKRd-zT)6&a7|;enW;kL$_mZ0uJ<5krmYv2lai#EY!Pw3MMv#KXwyN%Ls12*lj{z1Rn=3sd2G-yXKjN7R&|#ll)L'
            'TnUs-hj1w3eJz?s27(%nkJ+Zn#@558rx$aKK1PWI?V?W?-kl;|dYV2*&pHU)5V5JBp2K-9U_DVBubxRH^%R?zs?mCeH3QqUXc3)W'
            'H9PJmwK3M3!u}hD_t<Z`12!8(Dult#Z^Y%mok21<^yZ-2H#|HvoTo*v(iaOs=xe5U<?`i=ms>#W7#zB--Wa+wc)bpq`$7vyo`Io;'
            'wA`&wI&iJGx9`?1^?KjnKwmvt-1&<wz;zBF)WC3G@9m-CZzG!d+JIm8pH=X(&?gdj^(slc@Xo!R#4A~e#}rLTXa-dbsu@Zm9*G$#'
            '#fW2TIFi)IjCgX=UdQIb`BnxuF!;u`n*-NX{P#{DqjR;-KaO<RwWhFDL5ZZ4Slm#s*dk%&Zaj%pbj8q;<GSHkr6yBIy@p0BlXdXM'
            'z|B7O_Rx@e^V;z1ef5%j;c6>M9=dZ|9lD|33SR52kJjBvl2}pRx)Tfz4d1R`0T;_~x_P)_Ayh+?&f3agpQk726?%cbPJ8LMDA4cF'
            'H>plF8mDj3cj$fkK7EgVNWV{iKtE37Diqf7avsyLB<v5&gX-N#Mh~lrc+yZKVSCU#q^9EO<e09qNl;ml*rv>0qLGkob_8)-$OKvI'
            'N4TcB&*7Rw<7|<a41Cq_y649uhHdWaolH<IdR?E0+vf2^IuwnJsY!i29c7Wr3o<%L&N_@pETnB7%&*1%^ZtOJEkL%xR=>k4)lx_&'
            'smBbq0^g5}>GlU$Smy@y6f18A=HG`KOFC*O@w-^c6;-6f6M8bgT>04|8H!@qQ^obIyqY4gvHr7dc78Kr+{}NzrI(gclUL&j+f*8X'
            'q$VdqaU3%;2h0KP7A*Quo(66-72D_-jo@ZQ|6o28)WYFNY`n&ZF0kIgbTq0ZC)fAVs~_4v;<ZvC+)EP<f=xW>5RP*q5@S0JzR@!5'
            'jm&l%oB?zr9_Hq<Qn(M{0<XpL`|e;ml&@XfQFLcR#G=H{rCqRM`+TCXeU`QaKW=};9|XcRTWQ5kdc467o=j?!wt4Ig4O_9r$@w+b'
            'TD_AVQ1z%j!3x3I(#zMEr*wUp9k{(Fw6TaWX@kpcK3trgyX<F!8b@|vo*`~_wK<pPZ|U!x^!}cHS}_Ypa7$&^POR>9vY>1>u}ImE'
            'D)h5;GgJk2Y*>qp>%)3NHzJK{<E{M6A%FC!1oK$=Y5EIs(a*u<p?^hl;&x_~aD`Vs|B7?KSwtwbiKRBe6Tu>q^O<As<*Gg+63Hr7'
            '3F)ZmBQmle`%3=Uf}i)-wIdy5pG7*IJ`am^prIYvPdY7funHGjvF)LzKI8y7Xc2EAhD8o-XiXl%Ng)r{M8Y0yKfEb_a)>-^kw+X`'
            '0sA|d?~zUWlEdT?iyW=X0ei9USW8&s2svtzu41N<%cCv(lVhaIB9ArXgcjI;d`r0GQSz8Y9<Rz5_9EUBTgD^D$>SFJMpM3Mg*GQ1'
            'C<b|ge8VD2DYuOElMjqYP7uW+PdPYBGyW|4)7uh{JV~Ci$jM^Nig{pJdS=^Vkf+H>i=5hUX3#@HYqUMRt+B~7<dj8x#c>wq?98^u'
            'Ag77XBF}Dmoalk}&+P~ga)vx>k+bEwJ&BmU%K3eM$KsOb$XSc{Tgn4^q0hM;<wTw*ev1Ukb>MR<;rxzACFe-MA{ScD2zsL5#a-b?'
            '&XWrkxl~&*XAwJ4teVTa#)VuYmn?E+OF2Vt^u4;PT*+l}#UkC+)fHg%^}??6AXiDZMPA%;?hpa}U)mGi<OTAgMP6=PhnFx$H><^0'
            '_KY8SiM(u)S05<9h=Lfe?dcfEE96y+^wiWWoBjS`Yfp9iNOgOEz9;DP(Q@DD`d%_(kxXqrEm$OqHrYy>srptVW07gcj#*@}7k}JE'
            'A0JwEqh~+bj-Wq9544@FwVg)mnMU^WjqPXAW3Hah;>JGn=(VukZ+Y{6i|Dyj>ATvx?=pI?6#a8s_g_VXHN*gqy8wdUPg};xRU&n*'
            'Lqcc<2445p@O(}2FdTyf#oZcecMGUUfdNCny*cduEn_1s1`j>%<`G7=DFRYuK_KX^ABXNp9Hj4rf>C#6w9KwV!$GltkZ`k@*@~Dj'
            'wL@WXWVMl}>qbUGh2UWAZ2Z|x$49CK3NW+XEao4G1rDM>1m+%`%i^|k!QmC?z`|A-E$<2=9C(2gENzb0>Ynk!lvGlKl{)Nl|9|W-'
            'V+De+#yF<wQl2BYIB*HzlECF59`JDB5g;dmM<QPEa^MxfE0Hef;-E`_E(vlnQ9$895kQfM4}2W>1n@~D009mH0t6(|4c#1c3(zf*'
            '9_ZnqM}QuQ^g}-f{Q~q$BnUwcf&v63G6EwUj0i9ykx>}sU{runiBO;%Pywh!5|H2^AwWVR8OU&u5g;RBYNt4u5@1Tg+-5n*3XqjB'
            'xfTbO0G5Q=o#tR#fN2TSJHx?@05cNicb0=$0cIsk@Eiwo0?bL6;du_`1(=sG#S0uP2(Tbwju$yt6kt)pBrkEWB*2n{SzhK~S%77U'
            'tiTEfD*~)YnBr9qRs~p<Fvn{gtO>9t;Vk4h$YDMuRtPR0Tq3w+Rtg>-JeXve6@!-tuLxe5l|vT~T_SYJtRNH~6cH4em4uH6p9nsg'
            '6-9uDfCvGZl|?rX-6C|$tT1|b=n<huW~I^3L%#_9GAoWC4?z)vGAoY}9!5kMky&|+@-QmGsLZN^@<2tPGOLdS4+#+xGOM2q4;c|M'
            'GFCB6@h~OAl#F!@Sst<?WM!;muz0XUuw<-dnC4+xglQS88D@Bx5n)EgdWKmZW<{8lv7%v)hdB}EWUOhJ=V4xic^Ru37I;_?VL`^a'
            'hD9D0MOc)vvSEpbB@vcntZi84A;-hA2+K0oHmvZlBEpJ{)eWmWtctKIV|~LK4{IW<$#^AN>5!gc;)a)g4&E=5xZz=k+HG-T7sL&('
            'lZUpru><0U7hCh$-Bxi!+33Jz2gD7fdLF*A;)YTdq`o%d1{?E9MD|tB@7G$~U^(#>E1@lJtP?k?E2b@Ov?^{ms|-6h^|r;02M{-$'
            'U8yZ@?1s2eUJ)zB4c6LI-9F;9_Y`WpR@`u82^aPh{i?-{Vt+GnqbO~-3O1ew;s&$G=6g35H>zzn7B}kKHy1aW`!p6eHs@Dg+-S|W'
            'R@|7%&qWr!y;~PI^2f?$9@F{RXpWPqLdq4zjUo~|DfX~~8uwQ5d=2r~xo=^p8;Kh=sNF4~ZXj;dVE1nco1M!R;Ma>AH4#R(DZ)B&'
            'qb3gBkvQz^G#{!`+{hKhjdBg<RfcVkR&fxTD~cP%V^9|hncen5)*cY&isD8&a@JiLoE^Y!Sc)4R<u{E#yNUSI?rI8K5;vN%n13J^'
            'EsGmXxh!rwmraNpO&Klk3ZuH>MpIs^d&Y~&2PJAN_1WdB+2t1!CT(Q*j$O65kt>KBmC^=yB=C5O+6Gt9HYD(Rn8Lxtjl9Sq?4`T`'
            '8T`XBkwd62Z!lS-pm4P1jjyV_;b<E<e)IB1@g5uJPD|$=8;$<(UHjgrZkLPxJw<=?0sUl<{+Ry6M}JCZ>CfoT=`ZLn>95R=iaRim'
            'RNin?eZLg_4ZAn$<!dn|U16h)#iLO@e^VyAMJhCD=&7@cp1(6MslBa)A~7vFsYE8Uaoum%zX#?|rFZ|Ne`fa?eHn$C_FX7#p{6a='
            'w1t|sP_sKi4Lj~^3pH(_X7fT#xnkNv%~pgOmb<o4(-vyJtU^uofq;jd36u^5Jop_}Y<M8Bm!|>6|L@p74QQVRG&&8)xvLKZ<nn=l'
            'z#fZII1kX-d4P}pjUK(%$+=wgi*&<70s3q6(4|1P^JuN}_`Bj5Ae(=z%m&}&%WeO1%>K=uUQy5TkCor~@h^Vmr%QwB(7n&xE|>Ga'
            'HWm6gD4tSJ$zff)Gi17-c2ckNsI8;)i<Sm`?;x5~jM9`<J!9xG!-mlg^QamwJh&{WQcMiKtbgc-LQm6wG<n=dWil$CzM)h<%HuzU'
            'cmIX6jh@pnh+`k^U}G;mcO{>Me8yPkRGm)d>i-`^4>K{XO#lD'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Read.1.1()'


    _FIXED_PORT_ID_ = 408
    _MODEL_: _pydsdl_.ServiceType = _restore_constant(
        'ABzY8QiOG40{`t?U2Gdyb|#0vX8c3Pv7;oLWY+N}bRyHT9Vg1q?n-OREBE?HswAgcU|VWPUg?fP&ag8>OA1g_LD5zQSS*WhTeaH<'
        'KNP4@6ovaz_|cCBS`;q&;zz#}aIr52`cR=L(4KQ=h8&8d{w&+guJSXY?!D)n@1FbJbAOIFE7707{5v7}Pwnl>a?vi9vN@Yux>nM^'
        '(()yq%@xdY#k6&YH)=0UaqEU&;M2<$-uR|*`s>E;H8QnBIg9^pmD^6vp>h$b9lFd*dKpEE?JeUu-7vT%n@l-Ywcu2(4a#CULo1`H'
        'zN&Vkpc&aY9WhLDt%wh4q)|)eZg9)iO@s6#zVJSO(_mp1{-eg%2s5WSj-}_T4!0Y>jY@m;tl6qji(S!qsn~*%$`v(7b34>aykb!w'
        '^&8mY*mc9!=M7%GYB+qJTkU;%DVNusT!|a=j%YAaUeM56WwVIhdaHI~!dFCM*-KalR7E}d!^UKz_DarnG^40l#h{{_)x0=Ti<@(E'
        'Hb<{Sb49bzsD&C>{JLvcyeSTPpN`bhL5EIgs6ZSQ$C$!G<TG&s{nV1Hz0t#CmZdE>YOj8wVJVhelTe1KbR#EtiI=(Ib3*krzr&K^'
        'lz5kgsAJ;vYBgUwfZnKR1>IS0u>Y;S>~$|UM+4GTI^)VkbNQ0psJ-hWZMg<PI~#v*)DHegcU-(v_^XGs7Ri~FMosOd#9l7v&619e'
        'JqEmNq8}V2+jxarnqyi)W*3Bx1QOS3$1j;iL36m#wJCL%T3Xy7YGV5%W7Segvz9wr#&b8cQk6G;*2u7A-Oh_K&ketcQm;;G#yp?o'
        '74GQ0AbpuDYfI=<6!?iO6hHNKN&l5~qrpP-0h_^kqLv^|R!bT-WnpR>s@up`zEsf+ImyPVd5%B?j)M-Nq*w?v6lJU>%}BOrMH1`-'
        '(T~6O)spBEqHxpgM9ua=9g>5Jq6el%CWa@6r^hFyy!dJDO@D9@hsA9I(l+^$lhV^#$=8lD2j(oTK&8l#<Q4BT*4LB|KW-5BBv5NB'
        'Few<G$z2;6`|<RshemwmnGnBUi=4lBv8jyLjs?O_F2C#sGE!O*7saBm#UG15sA4cEa_j~%q}aGwJB&nM;>BFWw49t?Y>d^8=4`WS'
        '6?l$jYEC+`mY^RcJ&*L6z*xK_=kGT-$l<d%^My$fGw$F|4f`9J*OBh2OUo6Zl`bP|8#tY-d1NsL>UkVqwA>1BC=ho;18O3ZjoKkn'
        'pFN))$dcb14#l8jIicBz#-cfGyURf1rubmyzr&%>7{+B@R7qVnHLQ{r)n3N3vP!^JZWJ(}6;<6(uTNhY%&OCZtEN#}R*~U)QMEZL'
        'CibejtvXmYXIhIG?o_*^*+M;e_9Usbbz`0s%d!j>o>nbBhv8p!OetlVrlS^hbS|n|Rx?yqG7FL&syU}F3cVo6M3K+w7_8O&vXrCl'
        'aO-q7HObLA$SGGZqUN@m;o14DdNP|ubJ%;;ARC@M24(p>&OIa}xgevJa2Trd0u`g7vbL-i1kF_HyX;w&);zR@Q{o2tk|?TXNC`Kv'
        '*9BfY{b@>7&#1$$>nf&>jf{Efqvm=R-K41{-T0EqTwkNfk_&|+q(vPCwU$@2y%n~+g<55aueep?Y457JAx6ZgJ0n<Id^$3r6^m%5'
        'BQ9a>I4<E8x4OZS)%JMOD~xdQCnWv8ctiZ1I8zlryD92p;!g#Z{apN+_;ax){zCkv_=WhZ+R+aO2HicwIsCWDVR35}`TCE^P>AYW'
        '&&^q889QX*EOBUTi%8%UvJ(fI2HROQ(P0>J^5plbgL@&Q1X2loP%R)m?73=5Eoh|@4%)e_dKqVxDi=v)>sMUGEsIvNRo$^we~}~d'
        '6Eir5RAhwaNLr9{QLSVM;ldU)nikgz0%^63Yf(x)-)R8bl@J9fGTO}a`?#0YuefDy+p1?#dZB9ftGZiVDCtO6)!@7+r`sHN3c}Oj'
        'AXB6~wsw5BShzA#ph5fO9(Ou;af2ozSu+Y~&6ZpgJmqd=`qe5bETMx9(>R0PEvdy;pCv$?K!!wk)x~D!7m%qgvE51i9`WWqG;EL)'
        '^E97vz}=aQ5K+qp=3`;e<gU;8l5RVv`*CusTBTx{xYA%pRBl<Om7+L?vj9;^tuB;)83+hU0IJ`Jmn%5v2v*v~{w|aMY|i~*z*4m0'
        'm<6+>x}ObBO>ogdznex;cY{P8*Nm#o-AL#1RSp{VlI-Bht>d1ln96f!k#ocCvni*aly{?FS)UigE4x~9{Fvkou9<f<-Jsz>?`UOh'
        'p1YF-xnm-ba^8d6pF+RjYU0M#B9}W~jKVZw(5Ge@_k9%YDV!ALRPy5UoLMTFi)5hC41QVl8b_aF{9SgtvnWiPxPkj<3wfN<<$R;x'
        '5wxQU4a2jBKX46@fv~9Ka;KG4LZMM??Qg|-8^_mOc4#n*3+Peor!-SVh?X1uahX<Wtxnn1Ik_0SVUFtB2(W~EI@)}wTA^TCMK6X@'
        'Gg|lvrH`rulZpd}jJ<+&d`T-;Xs(pFoP=1J_eS!hPEOC}b>n1z%LA>I%NCl)DZ{Q>t@X<rziNes!(22<rbg(psi|tEV%oel;r&@o'
        'KvBLbC*RcQ@R{=$Kk8R)v!l~epw;s^)AgC`=%SqHd7e6%MP#VqWLCY>9AZiA);RaK<gh=1o;KA4Myplb)SMcgLk0x9*X&S#&<TrP'
        '^wEkfgPA<1_I4TF7r^079NCsA;%zWe-f8x<oYfc%3tv)v(B^S+AOSVGr6^Hc!-H{^B97dqXVocO9K5}RyYibAhZr)?4Vr|UmJH#V'
        'CfIgLt2(%2b97gohT(_Pl7eS}&!nfDRKXxDWm`d7A|wV>ozCFZAK2Bn4oP`fWku6UfS+j1b=5{XpKZ1A{Do7yTA<KCOQ#!*d^ChF'
        ')ntq7KsQKA58D1};;~96p{zQdzoDB|yR_WzlBP)ry<Cwycl3|+hYS*URGN1+*q^0j07Gu$c^cic0k5|bp(5OGpJ|R3feHi$8vl|P'
        '=j4Jys{_pd&5a>$(83^}(rGa0OzQ_bt$0JX-9SfyS#D^($t3X-9;6h_WpuENHyGBX``m%3mh)JMo|cDQjNP~-B21(N?KhhC+yLHd'
        'uk|<0Ppz^kx7inT!tB;EcpS{o(eiJ-eON~5_`kmm6MyZV_6BfwmTB$InyojKySp}#7DvT#_d?+fac2AbHu3k(U7Gj@Jc~*qISrUS'
        'P&<K#Cih0k$_bpW_+#VEfZDtn=<cSVOM=~3+fUY-_o)c|;jZUqA;z%Rvj^naHyJ$pN?%dsN|#D`<UWiCFdL(^%{}-D&sr*QQS(}t'
        'n=e<W(Q<6J8=j*<!4cZ7xK}*ku2(z(*QJ9;-k5vo;GNyAt(q(2tjozbJh1s8yG_NR>tk$e{I|w(Ba@TOQ-4rf?4yepFI?P##sg#H'
        ')440-*T*h*!*+fLnvz$?d%_Cu1k$15OP5BbrgE1@#;%TZgQc9iumg1mucE4}lOva=$0vV++G;<%n&nyCh~g;}H=NvE0?#hu27&?;'
        'hB<lolfhDMl<f`Yzs3eM=g;k=b63Z{7`}G(at@!@M+nZxBe>V@cLP1`t^5Oxd*1iA5e~(2CwO1b0b?hFb@<BFYa_Yo@$uZX;mIG5'
        'baV3gk9Xqa@$1vM@hiEhiQ!A#wGHmXNkq!2>k|{>lhfT9aG|Bni<<u>{!{#qSYL>TL!kwQ9%*_Uq{r*@I6;q7^ib)MrN{g9_=Fx8'
        '>2aAJL-ZJ<$8XSMh91-S*z_EISOyV1LJtHF(Km5;&$iw8OuDBDc`Odz{WK3BTQ6O~IGYYGNNHS<(%r);1uO1`IX75!3yN=gL9uyX'
        'n7xj>I4|{3><Ewn9iMogKJR`xI1Hh%_|b;J-pvA(?zI4gdM!XK)VwXp_}8yY@qR|+PwbOYXHl;#)+}QY7Ok_m`@2G)6K!=Y#^QC~'
        ')$Bk=9ZMhzmTJml3I6_4*LLgxOV!yyw=PMx4)tuuUSbF9>~Nc2EXA@To64|5>~Ni>JsWj)bj#N42zs2o++hi8u>9Dz<k?a7a-F^6'
        'wvA%_L6SYbZCQ4Vy;5f<x?;dutb27wy4Z1cqR#q!Pa~Gsb}Y|cWqoz_dQVK)0_)${m0tE5d%e!S)8;R%MSXAXS|59ZeW%Xe+7vIg'
        '!ZvR|l@0bLd#ldWrf&)Lcb{4#dmA^N?4+wl-3&ije`inZvG1~zb#}_P85jrh()aev278B{s<U^u92t~Qu{E}RZ%=Kr@3D95EaUgn'
        '8?)1UZiBstXD9alw)=?^*#3iOf`grA@7Gy>Yiv)U&P;H8&pb1`>;u+cXW1S30i{sp>@&s0&aiBq4YYWWahY)LnOkLN*+8A0-?2wf'
        '66G#D7kum-J6~rXb~2_Pbr1Ngx%k|$unX+NI{Ro>K0|4g{rI_JWf$2;bvD?}t^wlLC(j)R`<M;Z*{8eq9cn=N&t3>__6hs6&OYzW'
        '!w=EMAaU{gFAN|1jD22bKX@wtq88Ng!x!2I_I>t)IveWXERFuCUpmxYKGR-4Dr+X(I?<||-B`<J>TIdAUU)4kew)=`o0aaZ*ixOX'
        'x$UUMD%Rq57iBWoY7iwyvF!}X3zWdNw>#UeVe4DH+TZQn{x(Y7=_Yf3Yni(!b#J5G!|lu6N6804*~dGVeTdSJeEId=%Rfd9Pf!OW'
        '!=4g6pYB-CdQel}22H4%ltDVYJAIi=^`SXZ32Jy}S_gNa6(Nvf7zl4q_vo&5BP>!6L*dOW%<Pc`gi1zWBHZ1McqVobzH16*!$E6H'
        '&&3*ciVQ*}Og2{oHeux%nZ=%UT3+jF83B35q5f>`-`=);gz7<nTYHV-?o*+_PIy4z&eLPLzvo!6dmbFPw;Mzcp9>=FxCaUzY!BDt'
        '7lsR65`+eix}aPC|A!7e<^hB!gt02h5+j5Z2t^?jhftCwA*nzz3hOaQ##tKD3Z$cuj<Y`KQ=l&jeQ{V%Fcnk<)F`NNmVt}{nJ8r9'
        'Yybun7>L3^oDIUD0)tT)jI$vaQeY?wLvc0=qY8{hVKmMrU_yb3C``oJ49qAn6NQ;Ln}t~gW}`40X99!*A_^kTDo|0N5`{{fEy0ok'
        'OHo*gqia_bSc$?)9DTd0z-km$<LKPF0`(}=<LKQr1=gal7DxBqQs7n;ZpG2Rw-vY@h1+p-@Ery2MBz>xJ$zSzyHU6sM;G5y;9eB&'
        '#nH$26}TUT`*C#g0|g#L;Xxd|{7`|1QFs_<kKmC4kD~A>jxK(zz~d-9j-!vCDDWf-PvSTV>k6!+KjTD%Py|9T2qlOL$p|FT$q6Du'
        'Is)k!q!UDkz6kWipf5p$P$QtmKur)OG7-qcAd?_c3`Afc1_KGA#b5*mV=$N?VhlxKC<a3bqQ+<hMq@CVAaYDZU?K(+38KeL1ZH9|'
        'lOTG`MqoAuvk78{h=7QJNDx0N5vatVk|6#pMPMlgO9^B#tVCcX1}h2VF|0;lH3q8*WHQtvP>(@9fn0{Q2&~0mErD!?TM@VwgIfvY'
        'Gu)2A?HJrnAfw?<1n$J(P69a%cO!5&26q$4YPc7Hdoj3|KwiWB2;7gs{RA=_9z@_l3?3wq+wd>~>k)VugNF&^Hav>JqZm9&AiLpl'
        '1RlrWaRT`bPa^On22T<=6YKt;mZyad>2FhVBT1Lq`^k;xklaYSe%McLJcHy$8cU^j_cXboZgpYu43Zma`#Ai{CO6bpLh9Ehxj}tC'
        'g_<+%<NIr!+#sK1d?xHCH#Q_U+8MK-+}LSy!;La@ahl#wZahVD!(Em3lN-+?xzUP<!Q=*&4z-uhxaC70$2*f7ZdxLQHNISXa>K9R'
        'EV<#QHbP#TWRK(qwOEz4TPHW#+isoQ=-z(w<i_SQy^|Z;lk1+`*qLl+a$`k~#VSgtcc0vl*UBv%YjQL;*R#~7Y28n5_?qaZI7t^Z'
        ';oa)X^wdZ9zFt?iN^W#$9o&J|Es`4@x<_}Vo9<;j^&68L9TsNx$ijx?Mu#2oOzhCzsWcT#Zmj#sjTQ%GmSNAW1ujC@{p5y!4H_bo'
        't9#zb&I{soKe^Geyc!M~rwiCEskqfu{-*YCZ^QmtxE;c-k{g?%xcgKncAVVU6wCcR$Fhy&#-@lKJ{Lq?lN+1jdi=t0QTm_>?NN7h'
        '>+R@dAfeR8>Wf3yp4?dXk{iL)1|;K<O!~PE#mjBPA)TZQ2PHRTk|X*e(;Kja|0$H@h;~nJP+G&waO|fyepS;OZf;{evi<ai|DBcK'
        '7wk0pp3lNHB@|j%42ME?&#&Xu4g}tKb3FJRmTuqA`Fz+=tARFZ!7P<{!G94-e%ax6zsluzv@C5=&FcnzAK3lc^;TcjS@;@}2EU;5'
        '?Mm0|e-~vxU9+FA*-zK(r)!>1x`r-2_tQ1|>6-1QYg&xiPuJ`wT|>UxPuJ|HYrd`Nn)YjfB;5=&uLY8Ll8yDe7I=|&0{&k;?%xUQ'
        '-wE`(6Ic(oUkfB!*8)*`cVOGQE*A_sXa92H7j!#dZt=2?;LDTx_v}Sc3w*;--+dQ{d<DnCb;RZV$)+lFP`kVzYD2mAeyIOwy~gO5'
        'vR_Z#-G8F@G5zzm>t#?IU&&2xdg}UurzEyac<)&2eACIl(@To1<_n^N^m#yz{1<xs8$JG2@m-3uVN<8xq!(~i^V$CcDJjDI9bNzc'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)