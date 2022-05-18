# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/405.GetInfo.0.2.dsdl
#
# Generated at:  2022-05-06 20:35:06.222678 UTC
# Is deprecated: no
# Fixed port ID: 405
# Full name:     uavcan.file.GetInfo
# Version:       0.2
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
class GetInfo_0_2:
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
                     path: None | uavcan.file.Path_2_0 = None) -> None:
            """
            uavcan.file.GetInfo.Request.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param path: uavcan.file.Path.2.0 path
            """
            self._path: uavcan.file.Path_2_0

            if path is None:
                self.path = uavcan.file.Path_2_0()
            elif isinstance(path, uavcan.file.Path_2_0):
                self.path = path
            else:
                raise ValueError(f'path: expected uavcan.file.Path_2_0 '
                                 f'got {type(path).__name__}')

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
            _ser_.pad_to_alignment(8)
            self.path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2048, \
                'Bad serialization of uavcan.file.GetInfo.Request.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetInfo_0_2.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "path"
            _des_.pad_to_alignment(8)
            _f0_ = uavcan.file.Path_2_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = GetInfo_0_2.Request(
                path=_f0_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2048, \
                'Bad deserialization of uavcan.file.GetInfo.Request.0.2'
            assert isinstance(self, GetInfo_0_2.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'path=%s' % self.path,
            ])
            return f'uavcan.file.GetInfo.Request.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 405
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8dWLmk0{@Lx-H#MS5Z^mKZg2Va;Ls35hX>tDjsXcoG$wK!AL6phW;qBCVAC_xyVYTKW}N9cZcIoZ1_W&dL-Sx_Vho9Yqwz(n'
            'X7=_2Zq<9)o~r6!RsE{E>K<-?^<J$~{F$S1?x%j>@Kh#B1nL{%2GZeP)Q_W7X=%-#3o=lBJo;;SEbU9X^vFK2b+ePJFqDafirI5r'
            'Cz+?SL{6IQ;GyUv#F0#_dm?nY3b8LseI@KhPDg&7$y8fY<?Av@RTL7`+|9xHrEOFivrp_JYj$y=b)wu%%hcYn(_$VPS+nDkl7T-8'
            'q{e-r1=kcE%#}i@nf>E&wS@)?yJ2r*woxI!aNrJF9U54_YmQ8Dn<OH)=I~8{Qj}bkVNb&fNhjIZ!(|}*GSp=p)6$3&Vq2}F#lnp+'
            'RlQL9S3)g&GMU8N#a*R&P`I;=DkkZPRP%o1W0D`5#r7r;U2|4Z*CZ7Y``C7@ImlBjLSH2QIMCC~HS>rR3s33XHvTs63{<>Jqz*`2'
            '8ql)bsKRkL(U>7fI7PR&b2mt>`Cv1>5jbY5-~6^__j#pD(yrs@AU(5<N3k_*8c3S=-6&8VlGK#_2+7mfHP>R92puKkUFw0tR)BNn'
            '&}tNVLd$SVQ%agF6B$~n`#H0(l?8!F^0zE^@^ukp(muEKM)gJN!ubIi7xC8NjtG0QBV(!6w2<!czSux&@j|l@LVFXd;IFSjED{~i'
            'toi4hnWL&^fk4y744GD5q*!mc5sR>REv?Lz7|3m`#+_!R3SW&Gf<P@HW5;igsml@BkC3{GMd5;}A~DnoL-MiP-ze}$MQIUW{`$rC'
            'N@r#58dh6E7ux3i%@ScWiA*V+i6*Xg3cf|KiH>*XyNU2fihWYOG&rN)%%1+(QYRJR!hZ!*Yp&elS1-0MuYECy2I7GW$jr7=XU+`4'
            'q*)l7BHYc((L|s=9ECn8cmR2ZkII*r2K9+=pP9Yb^c&LWag=DTeA_Yycp7DiCpirbUeY;7KY?<wiP|_dH;Pg65=%XE0=b5WX5ehB'
            'tf{T$F^J#-b}UZCICHUsc_MpQTJ$#>Qb^0rayH?8a)e`;K%G<0Nr%|BnqKe%2a#e72@MsTBJ0YN_8G`qf6Y`XEgY`WX9VZeRv4kM'
            'G)GyVQMgQo9*zT_sgT`RyL8rJYam$^206p-Rz6E50#oNQl`@UGZj{`|VZqWsq`;1yI7YCk3VQ@x$m%FuVu|eH3}-qjZY5EqnXiyi'
            'gvwc+WI^N=J;9<byAR3(a^cIa!coWEytqf{$YjZ>btIC5omApt)G}pt>GT|S%yG~iX3s+MF}RN-t@y@whb>4H)J32n%6fpn=%_Dp'
            '<^jD@%Du=equqtR@FA=tm(-Z7P9PFD6&BlH`n1N_akf%Y7e@+>!XD))N@kHJ!2%WDBU#Bcx(v!tB!+Zf;YBfG)tL@BVhd3V$tLhf'
            'GeF-G*}^CAS@{k=pO{Vi+QRqI&08}GwX3*?<5G>wB%7QiZ;udqZka3KTU7oIizz&Q22Wb>9eiJhAHcwm@Dn_T7x1$=c>3g-;nF{e'
            '9X#w`c=Z&dxj>4fUp9nrqfBEm3BC|5Cz=-PLj6Oc<q;9fOlogwTFSo;Prtx#|CSZ(!p*;*Ha;x=kEG!BFn;(0r?cF^wW4kF?z~yV'
            '0aE_IlyH#3$DcPhCc_zawwz&GMt!*yeMxI*d_S<sU2|h_y475s*>aP>?H1;GcfQyL)$wgm><Uso+(JoLoqqs|@8H@b3IG5'
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
                     error:                               None | uavcan.file.Error_1_0 = None,
                     size:                                None | int | _np_.uint64 = None,
                     unix_timestamp_of_last_modification: None | int | _np_.uint64 = None,
                     is_file_not_directory:               None | bool = None,
                     is_link:                             None | bool = None,
                     is_readable:                         None | bool = None,
                     is_writeable:                        None | bool = None) -> None:
            """
            uavcan.file.GetInfo.Response.0.2
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error:                               uavcan.file.Error.1.0 error
            :param size:                                truncated uint40 size
            :param unix_timestamp_of_last_modification: truncated uint40 unix_timestamp_of_last_modification
            :param is_file_not_directory:               saturated bool is_file_not_directory
            :param is_link:                             saturated bool is_link
            :param is_readable:                         saturated bool is_readable
            :param is_writeable:                        saturated bool is_writeable
            """
            self._error:                               uavcan.file.Error_1_0
            self._size:                                int
            self._unix_timestamp_of_last_modification: int
            self._is_file_not_directory:               bool
            self._is_link:                             bool
            self._is_readable:                         bool
            self._is_writeable:                        bool

            if error is None:
                self.error = uavcan.file.Error_1_0()
            elif isinstance(error, uavcan.file.Error_1_0):
                self.error = error
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 '
                                 f'got {type(error).__name__}')

            self.size = size if size is not None else 0  # type: ignore

            self.unix_timestamp_of_last_modification = unix_timestamp_of_last_modification if unix_timestamp_of_last_modification is not None else 0  # type: ignore

            self.is_file_not_directory = is_file_not_directory if is_file_not_directory is not None else False

            self.is_link = is_link if is_link is not None else False

            self.is_readable = is_readable if is_readable is not None else False

            self.is_writeable = is_writeable if is_writeable is not None else False

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
        def size(self) -> int:
            """
            truncated uint40 size
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._size

        @size.setter
        def size(self, x: int | _np_.uint64) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 1099511627775:
                self._size = x
            else:
                raise ValueError(f'size: value {x} is not in [0, 1099511627775]')

        @property
        def unix_timestamp_of_last_modification(self) -> int:
            """
            truncated uint40 unix_timestamp_of_last_modification
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._unix_timestamp_of_last_modification

        @unix_timestamp_of_last_modification.setter
        def unix_timestamp_of_last_modification(self, x: int | _np_.uint64) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 1099511627775:
                self._unix_timestamp_of_last_modification = x
            else:
                raise ValueError(f'unix_timestamp_of_last_modification: value {x} is not in [0, 1099511627775]')

        @property
        def is_file_not_directory(self) -> bool:
            """
            saturated bool is_file_not_directory
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._is_file_not_directory

        @is_file_not_directory.setter
        def is_file_not_directory(self, x: bool) -> None:
            self._is_file_not_directory = bool(x)  # Cast to bool implements saturation

        @property
        def is_link(self) -> bool:
            """
            saturated bool is_link
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._is_link

        @is_link.setter
        def is_link(self, x: bool) -> None:
            self._is_link = bool(x)  # Cast to bool implements saturation

        @property
        def is_readable(self) -> bool:
            """
            saturated bool is_readable
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._is_readable

        @is_readable.setter
        def is_readable(self, x: bool) -> None:
            self._is_readable = bool(x)  # Cast to bool implements saturation

        @property
        def is_writeable(self) -> bool:
            """
            saturated bool is_writeable
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._is_writeable

        @is_writeable.setter
        def is_writeable(self, x: bool) -> None:
            self._is_writeable = bool(x)  # Cast to bool implements saturation

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.add_aligned_unsigned(self.size, 40)
            _ser_.add_aligned_unsigned(self.unix_timestamp_of_last_modification, 40)
            _ser_.add_unaligned_bit(self.is_file_not_directory)
            _ser_.add_unaligned_bit(self.is_link)
            _ser_.add_unaligned_bit(self.is_readable)
            _ser_.add_unaligned_bit(self.is_writeable)
            _ser_.skip_bits(4)
            _ser_.pad_to_alignment(8)
            assert 104 <= (_ser_.current_bit_length - _base_offset_) <= 104, \
                'Bad serialization of uavcan.file.GetInfo.Response.0.2'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetInfo_0_2.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f1_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "size"
            _f2_ = _des_.fetch_aligned_unsigned(40)
            # Temporary _f3_ holds the value of "unix_timestamp_of_last_modification"
            _f3_ = _des_.fetch_aligned_unsigned(40)
            # Temporary _f4_ holds the value of "is_file_not_directory"
            _f4_ = _des_.fetch_unaligned_bit()
            # Temporary _f5_ holds the value of "is_link"
            _f5_ = _des_.fetch_unaligned_bit()
            # Temporary _f6_ holds the value of "is_readable"
            _f6_ = _des_.fetch_unaligned_bit()
            # Temporary _f7_ holds the value of "is_writeable"
            _f7_ = _des_.fetch_unaligned_bit()
            # Temporary _f8_ holds the value of ""
            _des_.skip_bits(4)
            self = GetInfo_0_2.Response(
                error=_f1_,
                size=_f2_,
                unix_timestamp_of_last_modification=_f3_,
                is_file_not_directory=_f4_,
                is_link=_f5_,
                is_readable=_f6_,
                is_writeable=_f7_)
            _des_.pad_to_alignment(8)
            assert 104 <= (_des_.consumed_bit_length - _base_offset_) <= 104, \
                'Bad deserialization of uavcan.file.GetInfo.Response.0.2'
            assert isinstance(self, GetInfo_0_2.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
                'size=%s' % self.size,
                'unix_timestamp_of_last_modification=%s' % self.unix_timestamp_of_last_modification,
                'is_file_not_directory=%s' % self.is_file_not_directory,
                'is_link=%s' % self.is_link,
                'is_readable=%s' % self.is_readable,
                'is_writeable=%s' % self.is_writeable,
            ])
            return f'uavcan.file.GetInfo.Response.0.2({_o_0_})'

        _FIXED_PORT_ID_ = 405
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8dWLmk0{`t-UuYc18P~aTbe3dSMzL%9hl~j%GIdw7Tt_B-2#$0z$Juwv>E!eeWiq=vci-51JIl_jtTPnihm@EO#Nf?CpZX8_'
            'KM$c$Xh<o2=tGl2OJ7=22!TS$L&!tPLm&FkZ+3O3)#;Sv$ZLh9ot^pq{N|hQ`+c*|Prm$*xryw@JQDSM<p&N`JQgevcbFS+hkCLb'
            'NhLH-&G9uJh%OHORxje|gY?|p^jqnId5DTI<Z%iU=J=+L6Hg~G-!F2MhOCPwKA*5{kA+TKpzW(%SHre+np{OPRJdHG+dNi6hSt{9'
            'jotBsv^G&Y^6m6)YGx?YIu>rCxk|r@h7UnKkV?(bb-@FF56U$4nPya5d@z+y!n8SAL{^DoiTjy_6SY!p!g_|2=nYQoik~^mZxq`A'
            'iEZ>dzZELc3AtYlHSh3ve?VraD>Myw*wK*I<`9*~l%`$jBdW9J^hV#1RdZHx?YdpEp?D!}rsiR)Gz)ze`$a=9CN6H}=r#)yL@-Hx'
            '>7`~O#o2jNUd0%rjvj!3Gw|r{=&{-yJPu!k^SOm1jamv0EaK7b+WJC&zkDZ(xw7Z7Z@1+p(>TY1zI9kJ$J#OT?5x7|_1!V9o6=Hh'
            'H=$f~cHyJ29N((f>WydXw9;%gni(uufhTvJz*FYv6PGSsyflWzWA#Rht~a*oYa^_cmdCJEt~L&ZRT>A<@hhvVmCa4MR;gDjqhKAm'
            'aB&QCvsE-zZB|xWjpo<Tnt7_~aOXV1vf$ka3z)>5`HQz>EM_7@!brq45DiR|NQzJ^q9xAyBIcf!aW5T0vwUHk%~k6+u3W3GQT)GE'
            'v2a!@P6y%GS|gSih)^VynqaaCpR{F+P&m;n?r@z;sh&dU2VjhISSQx2*DAEtXwYj{npZ2Mg1o#kPLLa0E!tS8n;TbFM_ao*PLOO;'
            'Zf<RCG@7l^8E|pW95?d?BBX9Fr&nwCOYjIh0n2a|R^b`A4&Q)hfdc~xx8M$J!wYa1UV`tycj4s(S;*&D&K|>*Nbi{wv@LeHPa_#?'
            'D*Uu=PEsY4*yGe50<}q!nkoATgqxaU8`v3kHtg&J<h0Tvat=t#^G70)n(5VE1T0wNU74ECMTr{-kH)-{1lHdk4I@1~l(R4DTSuum'
            'kuk7y!C7)F?WEdr-aG}S5Jb#FZFzTFcs#v_>9knq$|kin=1gNdNdiq|8xy#YJ48l2&Pd9!)aVB2_OU*z?Qtj?*2C|qnSEO5YuWoI'
            '9}uYd6qQkG$YDlQuj@+OGa|o^F~A;Sy*Dx#*j@_#(*uDm3SKjx-eA5j!p;F9_?=y?CqcmC-ta1{yp%4~=I$#OJ7|<!NNeT9#eH@~'
            'X!{Ee*p3}c*&c%@fNHg}Rhzi4u=^mbvoPzn^~B9G7W)X#+n{64?8Vd;W+9R&cxpsyFJNk)tCeiN!ufldwMixJaBJ+z_3TjajfjxA'
            'J<MQ-Y=TSzpSZYyC6DBDhsQEwf<6Zc6#FoDf9pGXGzrBH)uM|@!MYKZZ5r(MR?!w-2HfIUZ{b$9>ea83N+dmGKhz+%frr^1F~{N_'
            'xy=-@$|P6jzC*rlfr&Or!ds!dJsg6wX69)r1J1&I{T?xv@@mg9o)RiADP%obU|GkUZN&+<_U$rKBnwpbIuIIi_|MS}rqDqk!duql'
            'Gc7=V#a~A3R7UOS7kHfS@+;YfnJc$BX$P!>$Ku;Kah20BZlr(mIVFEQ2r~%5wi$af8pK=JO2kUHCv6w;{4>KI3j)Nmz@jJ+JZnET'
            '0EjvCiz#sK<N2ON-&uF-J2%75?W*SC`2MG>ZK4v)mpns!$@AXDcZAZ|VuK(Hq9SUL(jMkR%>6~Y4oZAF`GstDx7PRHPw{T~+0l2)'
            'ZHbg@$~W*)%q`sdq{2O8zrdb>y#c;w&HM#U!{6br@HV^!|AKemJ$M)X4e!H$;DZEya1VZ1habU@7vLxGQ}`MD9DV`6gjdYNUtYR2'
            'xR)<E%X{n#ufCY|q+h|WbGN^N*9X+}`@!h-0$rWL8>da9a3t@UV>#_1o7<cGhg-WjSDKi}UT)6g=>PKh=(q64S_zZs4ZKUdiGP2>'
            'bNMq8IQ*f|7Z$KDaAk!qqtN9&p}y|W^l07ZQ0TdXx<k`N-O@mpp%6Q$J2X97*F_=spzhH0Xk8D5yo0(!)1!5L6!H)14ow$zCkMKK'
            'LQvE#CkLnVCJQt8l{uGxU7p5reG5zVT`bcN;J=@wkZ(?6))dMX+dkjHO4RA~=S$`^Ui<Pd`IrKdFh26n;k}MZ@{VfnrlTr;M1B@S'
            'K`<2isNgeA7It`(M_h};E<v~QE6Nfo6m6C7XOViN4sRlM8@|E4C5vMga=ZBb5sOyU`5$C!lUe2v000'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.GetInfo.0.2()'


    _FIXED_PORT_ID_ = 405
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8dWLmk0{`t<&2Jn@758|Pc<eZdLq17}s0|+)OQz#EaS{db;kC!v*|BH5<8cTPQK!1QW~#<L-A#Yko(NDD0ZQ1GHjoa7J)lKe'
        'Ata6*;NReY_Q(MaoH%e=AtZROt7oQX+>^uyI1we!Gga@qUj5!H=kcKzzdJt`{|P_ubPUfh71d*|pr&|4HIpf-ZnquV6F!T=qnpg#'
        '5jv}P92Px~X5Wjx9~Hu5s>{9`Fwa+gT<2rqu@z>DHi#I5oJUk)S<H=DHhnkH{lFbkc38D&8%$jc=#EY;r6ItFJIpUx4O^*6J5iWd'
        'cbMx5+d@?ncazW0qw-jJ{3p?S;HgS|-xXTmGcS4&jf$<u6orRZ1v8DlBU7qDeVT+cEf@KTa3<~72K9NwPx4dc@$wkj<!2uN*M)@p'
        'Qh0HMS=XhVC_HzU!YZt+F{|nGC0rd&Ei+l0SxIU~h2glEZLtF!r?xClG%aS7ET1)*JE-rdstI2;V{=hC4?*e_&aG`55ae8VcB88Z'
        '#gt{(TgNR-?2n^b6rNT+pIQcWjkKaCffi1JCWq?6??mN)ho4Ed)CMLsNurXZ<!U+47x?vZ4ps7-D1AuPOfL$*+zqd<93u6HzenNp'
        'Tf&z~+k~%4c;OqW?L;9NrNryBHQN+ABx#+sZAhLERa14COMTl-SE<eglmah?XO?YCr#`bXSutqjbeR?5xfjC|mB2Kq+u6r?MBSlg'
        'z@iVLLOK7;)A*ev8SjA9xf->ati~MXi%~9Zt8KamsRe;ryvVn@y5jt`g$0L%AAoKB(}{2bPc<+pu$FVkI`+(i^JaSvwc^`S2{Z<d'
        'P&f^3eJs!Q6eDlIE^3B~KjdJQgJ#2q)Qv^3cs|TSVz3l?$%kqmI^Y}e(Sm}>&Em#VZK+;`({Ax?z7<~T9uausG7sGuDB^rA&Nnr?'
        '+CgTr;Zhw}p-%Fv$!FLP$FJXvu##eT+pltFYJKURx>l^*slT0g!-K>Ge-ys4u(;S$#==u66j8N~geFuf_!qg$E&fCPg8(j-!5|E*'
        '6C-*W9*3geV}|P3uCEFss)Q$1&kkIjsR$aXOy>mtFogz1v;pY47emQ&IO^OL$ThbS1IHZ^g;UENhf{L}Di%=D2{fo+0Nf@VE!gXW'
        '6r|;d#3qnOLs57Pl`0F$yn@+|e7wP@R8Bqc!9`H<B%DW2dF$Rkb7Nx_09R%ZRHsZW5!6Dw4y?5ax=Wa)0~{DcSY)fddP^a7&WLT9'
        '9Rk%Y4B|0RjFn4-M|{|8*zPWX1@TPkadP>}WmM}4tBH!^wE`^85|=dq!-;RlQm$?L#1N2DP}Ly?Tr+Jwt_fl{$SxN;M-v8X2!J}G'
        'bz(UThq<%LRE<G$ppv9s@S1s~z?7y!E-MO{gXoEcHWGP&wD>#RJ19X+L4le+w}U1J#bBsSJ4EMrOELC1vH*J**n*3&1G&V)Bn4E$'
        'pi{wN8?(2k2>A+GlBsiS0ZdjCW27>(kS0n@VQu4@%r%%ar7H|v+7%#3`&m^+E9_?rw8kr4#r>T`d#2`yf1NMMd$2NqO(!;}VSt%^'
        'm;}3TLmzhJHZ+r95KHz$2wt~9qx=bM{+eI(_)nkm_bWW)9~AgA{xkk_{v4QI@Lz<dug@>`n*KagaIb#(hfjDbT)_>uEenEbcHl!W'
        'F5D2G4HPY$3)T-V&Gi#8N0_hAjtco#y-&a7AHOUrJ_DWq40e2e@il_tzv=nUe+%f$_Mol!(fY&5@GJm`oR?gcGitz(;f_fF!@edl'
        'EYs^Xxm3kAl<p5?u-DvAK0R2U%Vl;FPAd@W!^yZC<kQ_C?iINCIAb$zLdOA?JO}OpOWdDGtWBlnr_W{2by6<sW;8WJrDRX0Ws9y0'
        ')ff+7xy<1!mA#pC2RJM{v8=|-hB3fCUM*)diroCmd(ME0V_TJSrTVRkTCCN2O)#zP@QuaAYl{caI9aLI)z#`&WhKkEg#&2Hm#QP('
        '${oa|V@u1+#m!B1rC2Eyv)mfLdhGz}rc0ozR4XpS*zj%87Jj3oFlCNFLuPFUA=-tTa%I<rTSE{9Br5ux`VtzwAz+M#yji$<kl;#{'
        'yGv`O6&2`K5#702gmy9~(FVr?Y)6ROvJo~Ag`rFM)NL|9jY<35ILKigUoEW_)q1t6t}WH>6tj}NaPuHZu5Q)U>Z-cAv9z46?bbn('
        'ghjczwXspH)w3($T3;PQ#4PZ?@IUjv@xSta@W1na@lRVvU<zrCBbh-mjpPE7vq-*#<V_^=Nam2-Msfqm3X*RE2}XC8<1uU~SJN{Q'
        '{}AS%@XEmO1BeuuJ`NjnprhDv8^n3_mF*)9t}_V3-EK0&HTai_p$Jb*0$VFQ-**CQDP<ZMvtX_uo5WMub3O40Q7*i_8v765aCXr;'
        'Fv}`rQ_cb!4oyDZlt;|9<Ff5u7y)drW#|imCH7Qbv>|`A?WlG`HIqlBXb3sAp&zR_EN)dw_ejyPVSYmi80DCpr(~<%r5-_HB88cu'
        'ko)MEXpq3#w(Q;E;OD}lZ`roVs5S7=1s`*=G^LMcgeQk@xT0zb5?bM#bvIzBUk(WkYI^b49@C(~);82vwv7p}fkPK+eYcKNBmC{p'
        'VH8Yr=E^|78pjNi3(TkulQ!XG3``Z1V>8xZ_t+(bytWrd!3#u2{KY^o>jFy`IwzhtZgvM|oth@NRG^My3g&g^P%j>cQ-v`5+UBRh'
        'e2mFm`{A&C+=a>K;4Vy+8pI29o|KAVGl{rtPk25w2GfjF>2>E^u%$y`xXidBnwAYe75R3ZPDa|nU-<A#;f3tquI$+GiVO31;YYg2'
        'AoN2X&Vk!<l#qzlx(~VGpR^t#7<~sx1Br&jLc)>wNE{@OknA9NjO2SSg|GAsx&12q$sP{>&pE)^dKZuD<8p2gnPWg6K=1+}xcqg='
        'EnvFUXX?rhEoaL<1g3}kWrvp2vbmlt1tz**c4#?URs$w&zwFR*wyX|J`hMA=<!o64n2i0hL(6H|Lp@mzOgt?syXW9?@)Y}1|Kae7'
        'ymeadt~tFMhL@}LBOw3ttNQ!($2tCo|KfYDJpYpC9M~THocky@auhk0@m9-xqUEvuCI1P~eOUE(|A@~FxA(+LgXP(ANaSfGpG9(R'
        'yqnVX7rB=t^(nrg15No4TmlDDz8C-i'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)