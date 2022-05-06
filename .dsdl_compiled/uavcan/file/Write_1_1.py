# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/file/409.Write.1.1.dsdl
#
# Generated at:  2022-05-06 20:25:54.635641 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{`t?O>i4mat7uXq9hxZESX-f?XfIN&@K(rUU^ObZK!zH%gu9Z8CkpLAt`VOJo1e^93Ys1M7YW+ZmKp#B~#hSdUnIA'
            '9HL59Dm?1Q%85rFbx5U{8;?Bd$jT+@o*x1r0se`k;$7&c0KC`z_4j&u9;o+edS3b62jiLOm;Y+5S#c|NvE=f)W!lzP=9JBgrE+z)'
            'R&_0phyK|gbK9E5x0Tz?8V|n-ul*|gIxP5F$#NWC4@Jg5`?*(dl)Xlscbcdr$DBoo7aQi?vgs73EyVt!j#$N8{I43^^+G>ay36aX'
            'RdonR|7G(2n~-H$_HV;qh5qT1>3MZ)s^M`r{7XdbL3zt6^wm!-ZdY1721*svGfN(k>*Zdn(;}_AXmS1*j%&?0yz(>0<1@V8xv0~n'
            'Da$L_+?nx2$Oyb_x?X9vTH&F1(Z4vJ0+Czs6PyE@q80r*ycPP-mt4<uDrUXX4s^dUB?f%0Iz8=j%!*Q~RLh~C332#B99RqrJ$X0a'
            '=i4(nZX$p<Bc5Rr%TUh5bC{==pZ`*ijMeLAGxT5hrHP|B@>xXX290(u`D}^Xe3m<2oI>$Zg8T~0iC4vIEJF(umlqmS{wd5x%`979'
            'Gi3kkpG%fknx+fV)%*3>Pbp2=Zs=c0nYL1cq`mE*L;uX5T3*cebNrYv_2p8v7Wzgn5VtuyRkbZl?0Mj`Rm_8j#rE?WubW=A-d@^e'
            'VPOG@pZXU*sXArT<4#voS}s}ExkIIi_RrpI*tS`3?y%HKcTKy&!{3AjmJ8e|@v|fipP|<aw@hb--{LjyS-mKIS(-KHFsbNpI~o*U'
            'q*zh@W-TXV8G3_eu&Mhx)nvmq(UfJ$G!wX3t$eO#I?+vbvoXbyNExp~1u{9o+YE)kSwhBQQ)*FxT@hFD<9R=aDWMYHN;{Qi=SBT6'
            'x~S-S>hqtB-?(+-_Rnuc{^AS&<@Dkpk2-gWNXN~WyA@^Hv{Q8SIW=83%QT7=lKV7ykMq8C{k@QCFCsd-7nuRLF;V*LCpUk3dn{oi'
            '8c7K8l`p^Z?z>xH+&|y8?UbgP@lHmdUy5N-7moNF@z)L93@RL#K^0O7@B7bSq0jM3saCCfC94wN^q(ua)keL{OLV7}qD1;Sz1Y?i'
            'md`kDvUAb>`wd>?>|1!}iz;oInuo6@u2-J1u-peeY1V{k{}`(_#M`+sg;iXt^BKIn7`e5*p@SB04TwY`asMXx;ycCRBIP~wXb(DH'
            '5~ho6>U2-zrf}CP^YFg7GVwpzOy(x;%e-O`TyfxrK`4gX#Iad}h#TA~<Azo-EXVl8?N3LF#%;lks$(||tZ=JhxEz70dJW4pJe-@Z'
            '*6-nVXSlZM3ggmSmk8FioEZX+#tJxi&8YKf-2M%(8hO>LRnMqcm|TQv8U-4&tL3OVjOw&;PgrF^Au4>@!p+*4YDRvv9A3Xx9Js|X'
            'IapIMF0$sXQQ*ayqH(EM#BjKJ!=V_7KW@s=XT0~Y7%2q>)5gotm=Oq!fo9F7Q5JNk(%PeyHRwwZW8p1v7jsD^Y7_{BJGkmHuUz|J'
            'z%br4Zp5jpRV_4fW@wFOoLNkhY1o$YC5^?o#*lVQg(IbV7CM@(tQLC%wz7q&(MSs1nn}>RB8OsBd=lRgpLXm|&yJgw3WnLSFX8N;'
            ';a7Mqo(@^A(Yc@W+(x>6slA+hscr2BMf@U8f3m2=-*DO1H(VRW_2k`q-EaMmAd?jzx6S3ZzIeK?_+~ux=d`D{Z?^f)jr%W>cO}B_'
            'wk=~WGF!PQq?;>~l2<u;#WhI*Q<5=tYmCWE378gtmgv3SF~?M<1uU2No!T+SbY#H>w)}AfKcDVu$4;?<fSrlwaun-qPdj#+oe9`8'
            '9k@7(W6$pD!_Km20+vr=1njvzt=Y4fadvJ;B%HzV^ZW8=&#`j>dp@>RaQ+PWUf8!UJI|gE*u}0Ka2DrYI1m=Qz%B-CFwHb_dGWyh'
            '>;*O$u<!Kbgcdme(xGtKi|jiA`))_Ra2D}iJ~SSCiG4R<uk6Yft<dJxCyK#dX0HUy*vc)je(i}7*{jS5*rgc9*o{9$fBi_}vDet8'
            'fL%^wwp|Cx(i=w>gT2l!2kgq8R|Y){v_{*jM;e>G!L9_XkghYiX4j592D{1%0sG#**NGlz|NUd(!LG6I1#GBwZ7(Bcq5b;4d2Dgn'
            '_t{XuiU-OAdZEu-$I6Ml$%+9RZq-2{u7tObJt}*P4F~L<17`$1(eDQ*!jHYp-U-<CofR{L*u!bnynA9?*bmtCfc@}LIYV#seeXoM'
            'vUk}J12)oGUBgsg@1Hmi_8uDv*awHs9U`Frhfjq!d!Ky}u#bAz;dP8LLbdquQ{%@zWFH0WM^BVrL_v%{d8%t*AG03?Y;;G>($ybJ'
            'M@KuyCpyQ+qM7k{PPFDGx6iVPfX(fk7l}nJwOMGlneT4J<^r}D+mXcr&f<@|=u<$e5%e5G+X?g+=z+FNJ8c)y`av)I<=*y7=<%?d'
            '&+6Vj%jmVT-EVFGeyiyDsNHwt;J$0<y`K7S9^QWg5gsE3<gy6}{`>U6IGgQAgWHf0n!q5RJse(PS3C?ykYHpFhB|TpRHQ(_Fr3{V'
            '_Sm7Zkru(jXm<Aq6Gs#QsZtOa&vuU^jwKG#k3+#^wmsV1iA2LiQ9!6=Dds|3Oqf5Wu(-0Fkr%s0MnXw&2#z=Y(!S#()r0~(IBFKl'
            'Ps9Qjkr080PtIla$hqM15<0MQ7)EO+!Uz|hkb+11<F)bBcwtJ~slj>|cANkI*kQ&Jg7BC)HbneG7GxyID3H-0lVdr^Nsv=uQ-z$y'
            '@{pGxuRva7gD@z;paO#$Z0gJaLjpqqLt_OfNKjCqps`^XmS9+cVU3Nzhy)`FjA(2WMkN?kU{qscFebs60%IB*hj9tU6&Tmp1WZUU'
            'p}>U3CSg*7Nd+b~CO}9a6c8G#K}~|10yT}z!JGth3e0Jk+Ib1)6`0pBw+j+1D6pVmasvqh1p*DTyC}h;0*e}^_kjct6nLOvewQRz'
            'Qea8L1V5DEp#l#z%<!@V%L*)OnBo-)Ruov#FvqJBtSYdoVUiz7@JNA28fJM-f;9!!G`0@w609q*u3?HdB-l`3L&F?Dmf*1hk2Sms'
            'n-XkdJ~b+Yj0_nSGCGw)PKF#NS*K#i%aB(guTwb;$}p(HpiTv0$Y7{o=u{E~844;CbSjEr8HQCD)~PH;WEfFlM5n?Sm0?tcQJqR-'
            'OolNP#&jx<aT&%{7}u#hCS;gUVM3?!n3Q2sg-M;NL&zXh5IWUIO@^8ZHJ$2bPKG%Z=5(xLn3rK*g?Sz87#3t$P+>vGN`^p&K!rfZ'
            'T82d#7FAf(v6|t53=dRzpkqD5k_<~KEa_O$@KA<_Dm>J&reRrzWfhintZG=1VMT=%9qSraWmr{VRmaMPM>0H8;gOED4Qn!N%CM%w'
            'nvS&%>oTmXu&!fu!-fnSDs1Rj-|$$5$0|J5@lFg<;W#fUkpDJ`8#y}E?u#2IAa3O2JoLqlV-Pp;I2vX5NW~3fuLF}~5I2m@>+lCF'
            'ZWt{=>W@a;pfz7c<U;55{i7B)C?|!q68hrCHgTh~V*297LB)-Dm!X5xd|%vn0&ye$R_cozCn0XMcEomZgGNU?$0y?P(WJ(AiW{*k'
            'k-?eNuT$Je=XVn~QfVWT*yMVM8)UH%&F(F3blUDMZgjWbUEJ8+r?<GVKfmtc#=(4diW~FMwOBy!{Ncro=vcYMV==lKyW`AtAZ@1N'
            'Mv6oy#W^~t$sQK3&=Zf&eUqi`C2s6M9XSB%9^%Fh?6E^()46N{zg^te5n<wpB5V^kcEl0K5{J%CqfqVQ#%3yRv}!O?8IC+!+d=4N'
            'DsH65pcx9eaO8{Jc|g3GiW{xS3)%MIbO5_&DeiTYzia%ZeZ*hPc2YQ$xUnmX<tJisU~ywtE~`h*Wgp_ku8h`Bgi%*<V^>}qPmLGJ'
            '2V2zEyR+NuWEX8DByB7_J$9Yq#%3aJv`ZV1(;$~iwGAoJHZ;iRNZ}xHBN923rzvm19R86=<WRcH8zgHa3P)ew_(PR9Vr^qn-oLz&'
            'JhGz3&+Ns|te9fq>+sI6vzd%|=!(C)FaG|f@WpQmA`t&5ek;Baq4=Hny??6hVYUnH53m&9Zhr<#{PTTr#sBDrV>H@qjB?esc{zQ?'
            'X{zaQcgUcJmWGVFdC!=#9JAgutXXr0_j+9CU$@@<hxoVTiJWhpP}6@3r7zU<g_^!l(-&$^MyR3V&c0C77i#t|)U+z5FVq}HsG;2T'
            'g_^!l^KBJsIu8VLbSAKMAdtg<!>T<G1fJ$;K>Gh3`=<f@(|}&50h`&*0|C8tAfQmEmE=5t(|JHaydf@%e;0*2|49b}OO2if1LB|j'
            'bJvI8Px@cIjlbK@0v5!TiLa$hCYm%XCu-hN=d)G(6!mx-xV_cd#Bhaa+eXbc%RK5rQm#54cRZI)45F?i)NIMPN>s1LSn;UM<9;D='
            'uav9Qj^nCfdeLm$c*<~VylkOASq!vc#nV@d0|Q?O?ilxwCUqT&dzcKxENlx&r2R$eyvC_DjomcL#5QW6l60Dh8;=k@YT|;d%*tKU'
            'DMxKgT2va2XOSNth?t{0Ma6|0)SS%b9=DrCBcelI_oB?X)K<(XN9L(nWg9=DlW^i&l&TIlY}3VLShIX+AY#~_7yO&#(Y3zftxOa9'
            'w3P~tM5~IE#%F6@b13OkbI-zn)K$#1+q%@?+c^INUfp!uX&&{=nYJ9u6}*yWyS2P()PIEzhuYRR)D9Rg&#O10u2pd(9qu;l=yJs+'
            '5Ur9twyt%&$i2^#x;IF9GRyX+DFte;k{($VL<Rq*J!Hhc#Q)=XSX7|UYAv&6y>0x?Kj7UMdyL}DNPefsw(<A|7pKJ;k&pYQT@(ee'
            'bl{u(&VQlF)=hoqzwwi=m-rmrp&_iC^DmYvNkhGQNpQ1*FWdW~8Ha37WAtiIGa>b8PjeHKuyQWy{FQ6({1v5+CfB=6l56q*07Yv}'
            'EJaWN00'
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

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{@j(?Q0xG7|*p$b4i<+8XJouT@h-Fb@OH#^-GDDOF1stJugX%NEv2tC-)59+g)a7W3C{yA1W;lw9x4XKlui}>jx18'
            'iz0sTgRP+W5BbdP<#K5+=v}z%+&nYC=l8ttwL|xYM+RCSbuw=Hi67V`VS>|uU!`8aY*LFFag=b$v>IJv0dL^aUvI`t-_>WX>v#2O'
            'b(rulWJ1G$8eNkjt;tldy+;N~NE-<8OiH(EG_*H4VqX%7Wmj1eM`41(JlSF*;ZbOihAy_(cXc^e&b_CvYjuQBDFydZ$r628??<_F'
            'NUOnR&H{gz#|ZJMq(mBWFqCb=h&t9yt0+W-#vFw)R6Jl5!?DYF?0Eb5iT(7(!gz;oq27s&FyZx(`K3^@Ium=nafEnWl7NME3A#Lv'
            'tZFooq!IbZ>UlL;*#R=w>;lSGjR-w4a6?zMdWs~HhCUU3H_*-0LsJH~Xpka<L&T42S`BF2olyA#x)|@s4hc8`FSJ*u%H!}NyaZ=6'
            'gad9_gAG#{*EZI3JNB~eSg^!|WskM_DwViLgB^5OP{W&o*352#^5ym#<tjI=jS-25%4YtH%jkwvcHB!2DORg)wM7dS;Pti=IIjlJ'
            '&Ck!x_klR<xa(xu-EfwApyg)!K+2cgeQD+Tp)|T!C=}P$$WqZM6?@S-Ff-Q&+|d$3m8!+Ux?6n<(bV~p&Fr%lmIZ6XSiP2D)Sr6C'
            'RG$@v7PVq3!ID6w6-PXji6tZ4^|@d*8HuKTgw5<sKgN}ui;F9zC4&DqiiXZY(XJyMQ)`y#3KmbSFp?G~8~3fvNFWtvNh<10W~Y*7'
            'g47?Q(ND0(mP;!|vhKQMWwCmp*vrYY3;j6R-B>5?GFhuE7J8$-+K-b=Qm$=ODsFYXcLvPu!Z9_`)dz{!%zCSVeHl)|IhchDP=GgK'
            '72bwRz<@#oSKuma!40?$x8Z&G0PdyOg?xtPT%(v0`j#3an|z!3B#wk6+}DmeMv^EMHAYMjh)EKyhRh@2o>s#Z91GhOvwIhNT5bw^'
            '4n(HOAC~x}Soa6(TxvB^XvRQ;CDw?vdNxkIfY*p%^)xV=cN;QZIGpuiL^3M18f*1pd&Zu&O#{->biWA#G(kFoh0=83EnZ{#7ADq|'
            '!xEF;2FxD8xsnFbiZ(HoyRyiNVkTPc$~H~X3sCK;o&L7lO%Yf=`dh1`Z*aNN`n|?FtyCQ(QLL4<A4t+{coEu+%vaF|I4z8Jw?zX7'
            'P1hK$0moql_tg^>>iaybKXwRyHBu)H0xFu1N@3x)K3yKalXy5v;|xKU^Qnh+Hh5?z4KC=mSqzzJgAu@M<-EBza3{ezgbkjCt+DH*'
            'UMqKTqOfcrVp66ag%45D-!PfL$G6}U2R?<*PQ&N$1$+r#!PoE&d<);HCtsO<tv%jn@UIg)`2J=qw|{^iGsZu`&mF^l>#Tl(KMZYn'
            'fK~DkzklM%zdD5A2+rnlGm~NRf6;+|x^$!EY+GXL=+$dEHHkHlz0(K+*cI`Sy&LQns)dDmrkpd?mz8Tz^7qwo9I>XB!k*z(!&!7O'
            'X|;Ko_`NG)7Dj9j)YDZO)>)OsO!ED5<w_RGX}r*lmA}(+(gOz`qJ745o$$6?$db13qaH$Y)&3V(CaXsj3IG5'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Write.1.1()'


    _FIXED_PORT_ID_ = 409
    _MODEL_: _pydsdl_.ServiceType = _restore_constant(
        'ABzY8QiOG40{`t?U2Gdyb|z<rGqmC#+KwG1UMCaB8`H5&%YU(w&1R*w<&|-LBvqCZEs%m9kt5yFQbX<xX-h$aYFl(yE?Ddo;kMfT'
        '0D34|VX+JNWdXgd9`#hX=!=R1g&y_jN1-Uto-;EfhaxG7vLrXVisLKt-gCb5-E+^}OWk9h8R-}Q^LfbqulP=GI&G&jiKMMthL$nD'
        ')J8LUBALog=CZbt*Gt9M9_ZF%Bc%^d=k(IorHel)eN~DVk0dSq#|7QaC-c<LL&YO^^o%iyD(PBDIcb=tZn+{4@>U_0FIXGEB1u!5'
        'L{o1Tw8tsUOpF=G;d2YI5<{MqQZbr*tXsB`H3>-h%zyoLiG^ACr=_1D&!m>mTgGT1uiK?RM${%#t4NiKk-LVTNmqHaCDU47^Jdgc'
        'J!jD*jmIc)@}X%P<EEazXXf>B-Kw3`Yspa~pUmjyc%GLSfu}Td*JL)0?s~g;daw*cYKhx81~f!7`is&~srY)*&TD2`v(iDJr-e~|'
        'tSD#4#%vwEA|=z=RH+y$VfR~}VSbh$_Fo+<#)2Ll)DVCl=O>xKLgX`k8vRt&E1qfMG0W1XOT{-n)36tN?z>casCQ#f=ox)dH_Jhx'
        '`pECGC_m5NXCayxzc^bMEgnK|<g}ELpDwZgEuQeFmmH%7X{a6d^rYly#x51#FEg#W21(~PzAqIIf8WS^d>`OjpJ`D{W^<*Y+6=^='
        'o*d0)40P;C&?mF#hdc(`Ku))`eAWtvc8VJqK>U93)a|U9((=05P?V-il9p~#XrlbF{z4|BS<`ira`Lg3Dd?r2m*Ony*rUAPcf%i{'
        ')*C~bIj#@sIX!PQqx7TXq&9_4MTH-_o&1Y3mg~Ps!z{57y+AQoSBeV7WFe!WC<~Kl$gwe6^{Jd@x(``@VN^#V9M{2sP?S#u1o<S6'
        '5;6vxlyd{@67Rsb?Zqg%ghIIDb_&hfMeTMM6;%&C=pF1C>KPswa`pKa#k1wbK^~TF6Oo#SFFNFUTFaEtQRmQ@rKPABBP4p)e~sfs'
        ';l`~J#hy#l+KNmY^o%6$_xAr_xX)+9zw}M;KP`&aZr-eb>BW<QZ6`T8?d@a)n&UV56K?aL@jox%W{}o#8WbVv($nHm4D=~Ioy=ve'
        'e9}ml`isYtcD7)p^dvp0N!O7@g??m=Q4F6!+>EE(=l5$|<nR@I@_ClFOgWD~HJq<FZeX~#-JZ^IEprE>wuFy!VHBencj|FmUbI}@'
        '-cUjIwgyBZlcnMjf=^sabSB8}r9ACHCzD*Wk&Q*qwC$Y(rKkMT$bW}Jp?=(#^|VTGiMAe<P*i&w`zBQ)uIgqAH?*{BnCipfyIl!&'
        'nCoiR%uK5o;YM1ubp)p9RSjFs<Jef%dV<@XYG*W?tLLtqBUsxo#|hZ&i(}_S)zZgs`&aW>SIf#~^J>~a=OWa!8mGQYHswZ#njKT0'
        'a3jUZL|Pv+aI;oNr(Hdoj&5B{v<>O#9E>Rs7g_7J8rKu!3H4kef#z`bs!29{ecY7Y_xS8#Fp>-6S_YS)FwPMe4NYp(YKqg7N^^H-'
        'R-i)<ZQ&#F7=1}0s>TUKH*wY}J$>=xHdVc>_IR$#WepTE$7zn5=UH@<re+NDN7U!}8ck+ADmqenVxXc{^=hIyVAWfQ>h_d@t0O*o'
        'L*x?g<$c~0!D{xWV}n{cjb`fhB^({VBRuB~msqq=yPq`OMj9PzXZ=I1vKu7uATEEhNP8z-xO&0`Fh25MebV^R?}1R5e?Kr5s~kLy'
        'XZ*nH`i%DU;AR`E-MBUXRhsY{ZOiD3P{kMV^5)6}|EK8w#5oBLll;C&rH_eBa+vJB7wEN8GsYrJc39NcJ5)Eu6lB5LD*D)i?_X;u'
        '#}2VJhaL9DqGanxQ#tk;JM6HdHMrP|eaAM{VMo|ehsAsw4m-Z3G&_bKXD8|`;RyDh+?GB&&Q3V&bx&5p@x!EhYTLT(BzxUqryFv>'
        'Q5<`tB`kJ|opxAz+0)47&6f4q8?4=7Z#CtF5;%TlN4V@w_LjrGRpT!lMZB{+#$#vLw;cBNrhHKfW!`xy8|*B5+hJ<Ox5WD0mqujo'
        'Fx6q_JREg1{$%~VU9rdBW#=4rzHBqF4&<e8@0tzv9y{-__qSXb)KF0xWiRZiZT4;UzQf|>dHQR1ao26I3oP!i54Jr|)Ij-5d%}ZV'
        'WFI)Jqq?@|5i=fK-^+VumtA5V4okG;2h>8HD|^a`U1kY~bynjb?nT1YJ-5oPuug|vYuO{HiF()fg&(`ht~u;ReZ+Jic4s+iZtfcw'
        'cAedD*oQmv8ET{Mt$pRnZn6&@)>Ru_ofKam?K=;4i*-5d;~o1B5m5g-uY@=Ih<)s^PnyT!4YbikvH0Cr#*cl6ed4fBU&_CTf*9X>'
        'rE_54WuH2%yDnyF_4~@b-L?HAwf%kW$e=gIt7DHgj<OMlP1TQcUm{nQnGMR!G?rph4x97jNMaU8@#8M)#8IjXHTzI@1ob&;pzK1u'
        '>>NtZH<Mp%F28^p&l>40Z>_V4T1y-CR<^IVjGE7bx@)cLuAug6S$}=!`fG^r0x=*O_CfIX)0T18gGlWgkPw={AQs*kUVKwLG)Iu2'
        'hFe4JY5^4~5HNIxw};)gV{D{F@X#IJ+``B%SwN~}1O~&6?eIOZgY-R9@F*O#HnlI-a8hIta$&ML8?Xs8dt?@8R&RN(p=BiG8wY1^'
        '?JsQGK2r55!2E8rSbQlKI0>H!JbQUA%e&46r{~jwrJXQZ*%wAQai0`C-yW~ESH=rn5~K#J4cM*!|6_+9^9jNW;#lC5E=LFn5RxDy'
        'Lnz9k5EURQ!FmLuGK)b>fS3d^nYBZ^0PPaA%doC66;uIK2~?TIAud2%g1F2&p;LfP2|8ug1ziGkNzf&;Zs-=ETY_$x^+BHieG>G^'
        'Y!C(o7?fa8W+N~nz=#ARGJ6D%1b8IDBbjmF0&oeq%yN(uASXdiW>YXFz?1}2GP-s~fEfv9Wc2N<0J9Rz%II8207n8xM(@rEFekyB'
        'jP9KmU|xcG8U4E;z=8w|GCKH~0M8_NCZmTJ1z40|QAQUp39ux=l8ioH7GPO|Wf`6PT!7~iJeSeSD*~)Yup+ZnSQTJZf>jw^ye7b!'
        '1Zy(-_=Ny3BzPg?Dy$2zj{cM>5JDn^A`nt26rv(T(a8!0LrjEN1Y!z>L%Rs=5olK^AXE|52&f8$L|lY;1mX$>MW+az5$IGXEV@MK'
        'ia?h_fzd5OcLcf>3XMJy`XbP$P;d;2Fc^VBg~DS*gpml0C=?!#M0gZ|M+!v;7lB8BD-<6&5pog8DHK0bB1}bKO2H_G84+e8Fr#1`'
        '!>kCi5tvmllED$diGZVEEW?}#a}k(RFq&arg!u@}D;UqPAi_cf78HzVcqYQL2s~3TreRTp#Rx1a7}c;O!cqj56pU+F7GXI8%L+y|'
        'JQv}41fDAx+pr?Sx(F)~SWz&xVO50H2&^g?-LNLYS_IY<jBj`$!ixyJQ1D4~%8BC`Hz4*+N^V5yQu`peu@A|OnCFLs<i;K(H)7c9'
        'dUsco8|qdUCVP<FP;1xW_cpnqRufWxFv$&?^La#$*RJm$baI1y5-&%>L2_e5a-%k44w4(KCO5oYhAvKH2g!|>NN#wi(m`@#Kav~O'
        '9Wj{Ppx*A<{t>Ug+mG@3<c61)2;oRsuQs_+9^WjvQBG}ye3@vI<OWI1x}#esH)>_KPHr@o-#odoxlZ%s#`g3YCpTKttxs;uxN9+s'
        '+OeG{H{5IGDvvpLH8#hYszF*WCpXGSbW<Fqi<<CG@#0PK=-$_#>Q>2(I@GQfP`5~K)M5AS2%GL@efW*ZjXDb>yJTTQa-+@;-xE7@'
        'cj}r7CO6j0$&G3Zx><%@w-&evT`wm$%GaPFGC8~JldQiWUN0v%s+MQNLF04*yJaYDb(O!V{e^AVp9|Mg*imw0Qx=Oa#iHfp#-?1B'
        'cb&^Nk{g>cTG<yy4U-$2@>+XkyeNH8p|;wX-FhuMcO#+H#_X$OSDV~e_mdmJ)CNRlh(^n~4Z+WC$PkNChJ%tDZjwWKmFW$b!v6(I'
        'a!8HS8<f`YGaLu$jo;VwhL_t|7q_3@@V~MW@xHU?eP>1EfAv*q;xEIY5dW>sfBuv^{rs<aDb9bv|Azl9pX0yef5-p6cqs5?wo}0`'
        'uq3Vqzk|i+pYlt^PkKzX5Rg$**-S=HmA~UOI-S?;4wb&N)S+716Lr)uHEUWmCbe<B+1GXcrSj@`{8#=ra=vkinuBkl93*NE5;X^j'
        'nuA2m{v>MXy7M4WbC9UnexjxtF$am7og`|=cL#}@gG9|YHBnQ0ArPfIfy#wI6n}?}G`$dbmA3)qfA4s38*p$N(Cju~JzRSspj0me'
        'B&xLH-v{V)9}wps@H70^{PM(q(8a)S3QaEt_&*d+-01wsuYYwF{{-#=X8EO&uY^#@9aIg|E#6`2lUaP{)_7_gu9P-WZLVc9YA&Ot'
        'bhipgDr@F-GjG$4fm@Y?iY=)Zi0TCo%j?bPUcC^nR>}n`$8kZ`^6sctcuKW%ddfh3l4uKHdBYbHZEc@(-Bh0-O{zNL)iCMsSY!+&'
        'QLZmy={cQB(`2UA6tQ&+sQ8s;yuu?ykBYb;D=qz4GgEFElPZ;hnKwvJZ*!TWI$6bus#L@*qv!R^bV7CMkk%8|b2gO~GgGd3SuDMQ'
        'AJOqS=@m*@Q&%&Zjm|J8^^P`|VbCx5*Y~4se5qGGP3+61RH(<DmFF~lGMAt3@axn(G0-4Y71J_-DmD1h^M703(oB0ycWdU18Kz-#'
        'Jze&8b$VI1{t8_V1?JZg1oWntw+e36DzA`^ZWl7{a(N-(&XP1LYwb;P>-(g}1yWv4GFUVvPUTg~S5|Ru;NNl$8U9b+zc}vX2E?nS'
        'Wh&Ae`X|1|r_s~s#*waAy~c)q?*ZpAew?53>ZhIIm-%m6e#j^O6GbWy^~8VSyP}fRr|1bS!P1H1>15h3sAna)uBGwE#=2<g4$IT1'
        '&C1h^2u;e<^rI7&PPmo7qQS~vuIp%UwZWiUaO`Lj<0_XmZQZA@_}1D26@A`nRQS)+DwQ4GuoTeopkl9OWv#mMKY;>w8!G!$3VzjG'
        '-!`ldRwFJ9um*L(!kwF!7^{Ie^01%v4}9LA>>V1a)I1BKMLxWF^ZLye5D)ba3@7gnJnX;Ih}*RmkfQenn$illLg`4)?c2Q%9whJd'
        '_TTGmL`%4Oy#=_#_YmsdQ19*GfuSEFTJd}L5_+NoPo_L=p*kHVTKbB=1Dbf~xTUY$t<ycv><!hgN*mZ*yV}a+?)87xbN}9*B(@KG'
        'iO#KF_xj!4JgEvC?Y&f-%d2)aMy0lJH_dC-I35y#YH4*eT3M{4ckkWrO%4wXB=7eO{h+szlds)s#mNH?hm!+$lMe=aZZ}5jYQ;$u'
        'ln)*b4h{?rH;#boRXA@8ow$M@Zze8LbAy^rYCfgrV`}=SxkJqmHT~3lLCpv?W7LdN^J8izsreIXrl|QTHGf8pLroEzO+SVmbvKko'
        '>6j}uweN=9gOkpBt)>cI<rLof#H=eG7D&jjSmUjgHZI-U@&b9Mf2OIuhmF1M!v_~-b9xj1h<Nps0!${}B?*70cFn&8n+XvW@E3sz'
        'i9q-6xWf+v%}=|T@Fu6-e7Nb79IrddO4W}F)srZSqKaQax31RR#95j+?!;E*5Dfe#G4Y(7`mfadJ2n4SiDUR>cq<1#^*?JAMic)B'
        '5L+tD2Uq|A'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)
