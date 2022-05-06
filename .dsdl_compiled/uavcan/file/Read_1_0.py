# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/file/408.Read.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.629713 UTC
# Is deprecated: yes
# Fixed port ID: 408
# Full name:     uavcan.file.Read
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_
import uavcan.file


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Read_1_0:
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
                     path:   None | uavcan.file.Path_1_0 = None) -> None:
            """
            uavcan.file.Read.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param offset: truncated uint40 offset
            :param path:   uavcan.file.Path.1.0 path
            """
            _warnings_.warn('Data type uavcan.file.Read.Request.1.0 is deprecated', DeprecationWarning)

            self._offset: int
            self._path:   uavcan.file.Path_1_0

            self.offset = offset if offset is not None else 0  # type: ignore

            if path is None:
                self.path = uavcan.file.Path_1_0()
            elif isinstance(path, uavcan.file.Path_1_0):
                self.path = path
            else:
                raise ValueError(f'path: expected uavcan.file.Path_1_0 '
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
        def path(self) -> uavcan.file.Path_1_0:
            """
            uavcan.file.Path.1.0 path
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._path

        @path.setter
        def path(self, x: uavcan.file.Path_1_0) -> None:
            if isinstance(x, uavcan.file.Path_1_0):
                self._path = x
            else:
                raise ValueError(f'path: expected uavcan.file.Path_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_unsigned(self.offset, 40)
            _ser_.pad_to_alignment(8)
            self.path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 48 <= (_ser_.current_bit_length - _base_offset_) <= 944, \
                'Bad serialization of uavcan.file.Read.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Read_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "offset"
            _f0_ = _des_.fetch_aligned_unsigned(40)
            # Temporary _f1_ holds the value of "path"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.file.Path_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = Read_1_0.Request(
                offset=_f0_,
                path=_f1_)
            _des_.pad_to_alignment(8)
            assert 48 <= (_des_.consumed_bit_length - _base_offset_) <= 944, \
                'Bad deserialization of uavcan.file.Read.Request.1.0'
            assert isinstance(self, Read_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'offset=%s' % self.offset,
                'path=%s' % self.path,
            ])
            return f'uavcan.file.Read.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 408
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{@Lz>u()L6?br&IGdzxNShW_(5ZpsTDsmmRG=bXFizbD$4;=_#|O}Mc6aWbX?Ay(omtyA5-3Fixv)|L*_ID{Kte(Y'
            'i4T0@@8fr7_CEX)jpW>W=W!mtbI$La-KS^2j9-~^|C%?;QEJjGjEtxh&(sqhXCjOeotN4uE86DrJ&~y#U(=mYDca}l(r4|j+g@`n'
            'Qbi%ER?an-w{2A?wywnCBQHb+&mrRVn(rpO2nPzXw**h|->+(6Y}+hEyP`5m7bNHWhu!z*?fRMZx!<>+wavwdTU)8Pw!*Z(gwRtg'
            'o}6l%7uJ->(y19ilyb`>OSYYMy{yPbwTly1KPZeE79zc0STPjUVV^EWv9eJnilLS5Itfp>u~Dv5(aLW%*B*@p(Y0_DdmFSx9{sM}'
            'YMWOgV|kJCDxDSdc^%83Ij08$BY?`;DAh^Z%(Ym4)hm{-%k$m0pm})~&_^5s<R$sy7&CbVI8E<0Z=8ZyRq;{Vy!Ii-DpnpiQ&wp8'
            'u*;Vtk%?Rs)<Y=Y=p=t<eL=n{-&&s|$K>}8>bSW8G)kT*J8IX<=9`^+(SQPS;_dJHduO9KGi`HyZ0Qsl7;TUKZktO#Ro2_Pjh~&R'
            '&3vTGwqd6UF{3=znF6p^H$<+1gGI7EEJekwu4XekkqQYU-)ml7)kVUsC{8>|?$XIh6qK4c|I%iiWxN_4J9#eJ<ykG-FWTPv!ZQ=g'
            '`yC7qaO<@#UJS*SD1}w0ne;fy`946!g&nsjKN`z&_~oi-*XQU9j%_@hZ_ZOr))~jq^)qyI?wLWhiv5xouE;j)Siq13aY#1~=B1c9'
            'C?$4DGLr3V=@RU^yn&xrn*~5ZDLjFlQuA<7@4BGk>V@rhAFXVy>^$6Z_vJ^;x5vSO9hER-$f4p}*m6koY%CpjE(|K3&?+)yVXga)'
            '{pK5Q|EQ(hbB5;s&zN9i<>TnVyPNOryx&<P>rRDy(#+q!eP<#}G*@S6CyGa&$Vlj8c}rHZkiV6`sX+#*fE$z{X?xJTh(zBPX;kXU'
            'Mk;MLn=6sgb(M&SDm8LIHs|RhQ!&!#5jb|=)$elz`OHmJzSP8+=PW)s{GA^vq<gSBDkabEA!}Qda~&g#qe=`BUTB`u8!nvl)Bs7O'
            '67)^t!`tDlkZ^A;anRLBasz8Bs%enIu1ZAvxxD`ITk~^so8V=UG7=XCD~zNtGs0TV$Z#f#1ca6{Rj?0s*4_!(jucE6*@z*-RmzNj'
            'V9H*m471o9=xPsi$4thJWQ#W!Nvu)DkOaH69u}8aB?h2>X0^LjX>D1m04_w0SdZ2+ow)2^dcgLiN+hXB#Xy0qSv+$0$Q@BFg~65p'
            'ILIk47gh_ydLkT#Y%vU>4&JkZbaeMY%I-I656MUn^mv9a)I$luP?Yl#OC(h)`R+Wcspml#N@5pSQi`%32@wUnPDHx&<AAYcw&I~H'
            'wZfrdNIr6pEMVd+Q^jLi^H@V==1mbWX;0xIpQ0L`E^vw#q`H-{;OR~${bb1jg%bRs^12JQr%&bv00KLa+K7U2gNwG}saQtKVzID$'
            '0?RZt0P|R7XaHV*DnvP}emp1`!aE=k_jG0KGMcC$iG@M1I<-EvCc06e2r}xi-vys%ncg$>F}Vo~bz!+G2oyffGUW&>5dreXx#eTc'
            'H1tCmuMkqIA-Go;kBtunbQYA0dz!7TY_hd`3^bGr6Sndva@7;Z+94W$=@Cy;Xgo&W*!>wMozic&>kIW^+C7bJg*>3!-<Q|qKV`3$'
            'e>jkT+?0*{q9>opKgmDK=Q#PL{7U|%x$^d{cl>B|sMO_O4^Y<sU6`ArJ)dBMO6S0)0-0DUfmHa&qaLUx$YIQWM#Yq#wM9@7Eg%Ot'
            '>jYI~26e^~ppM+W9kP1_oSP*8_Y=V|+40OUWf6;R7N9^<0SN>Ng~P3@9?C(8b%jKB;RGdpC3qrHeIvB&fZaK+0OvATL4t}yYWicl'
            'N9>8H^w-wfX>=&m$S&o#lT4weSs_H~Q$pB8b}}q7+TF)#J1(jU4V?HG`V*Iwq`sq9N?DhQ3A7nkvXb(V=Dj|vAut2Lg)WwXZsxPm'
            '`|J!v$rR4Q``$Jke~OCo_3ydw2Ib8SC@u)Zm}n0H_k`!`=LkVyG1bCjF7}nNOMTP@<7HWCG-No!L{;f3Ai75}!zw4$o6>hRM5fG`'
            'IzA-w5<!QtPA~i&5q?I9aTu@)EmkKwWBz*~=m>hdpbAcv=h7IhwI*VqhT!wn1r1)39t=1Nqh%V53CQ`ZUHQ5Do+olOl$2Md&g_`F'
            'yWr}0N){>4`B3;GLGEaxv$!+29{?9LUEh9E;T{mcHdHXcROc9vsVNfcrmmE_Ha5^iQluc6^oWo>5WpO5YUJJ7BUUB45yJ|394J?B'
            '^czN7CONto#|K)a>ldlQRKPPvR&Zj|{<Iw$#MgIc3TFB#5QU#kO$`$(-y}g~j7FNk)B`uOc($g!LkX~t(U)d4#*;)>Y1eA#7|jP{'
            '<=CoYHZcSa8M}r(vCs38Y9$k{2(cM=kz7;+dKjx>u|Gv%+Te}kT}~CIuBL6ii(g$*IP_kTX-?LK!FFAi+K6evkE@&v#r@h9-}d_}'
            '%Xfb8!#*?mnA7gU)boM%m^nxHT%pGzSPWqqBrJw(Z4zRa*wZ-or}yB`jHeSZGtruEPb3E`17yIgdlQHHvmoqs?8DQk!d@)syvYII'
            'j2&I!xU-ZZU55-R|2)3rsv2aNJSKkNLr$%e1_@1!HgX-lCdP43Ga=hXbLd7cKOpJSQicpgK}9I2Wk|1@%r*h9Ee2bwyg1Aeg`k##'
            'N2a?D=}D@9gx%dKNjnQE18RGmy!tc4p9du9Y;_wGEi?HEZ62zl>3nl~ro#)RT_;2h)H*#GjjbX3f=RY`06j@M1kJdcbXle7Qpg_0'
            'yGqw48})tCOcFxnrF*~uJ`N8@5`IE)0NxE8fg!hPV(K5Yx9da@gvXNQNwmnQ8DgOLXC2SEhC<zeDu8<q@uUTk4-^H19{tB;$J1S9'
            'Jkb#`yScwBCTB0%gOs9L2EdMQK<f@ZABZ}Su?VEyI{|PvT4FagX3l-D&lC7*v)11y-==Gu{@BmyLHwkXvro-EdIJAPH;46Piofv~'
            'CjaIiif>^$`_FVbo18wf?x!|+QC^ZS`}Z!_Wbf<GZSr4}DNX(xkL)gyY`gKvh2|QbE&YqPDw3#Id>nm&!X__JPKId~l3DlJ;TI6U'
            '=)Of8{WB-NUXaNqy#C~ZdquD?`-;F}MVn7g*rcoB{{Y08H)w4X000'
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
                     data:  None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
            """
            uavcan.file.Read.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error: uavcan.file.Error.1.0 error
            :param data:  saturated uint8[<=256] data
            """
            _warnings_.warn('Data type uavcan.file.Read.Response.1.0 is deprecated', DeprecationWarning)

            self._error: uavcan.file.Error_1_0
            self._data:  _NDArray_[_np_.uint8]

            if error is None:
                self.error = uavcan.file.Error_1_0()
            elif isinstance(error, uavcan.file.Error_1_0):
                self.error = error
            else:
                raise ValueError(f'error: expected uavcan.file.Error_1_0 '
                                 f'got {type(error).__name__}')

            if data is None:
                self.data = _np_.array([], _np_.uint8)
            else:
                data = data.encode() if isinstance(data, str) else data  # Implicit string encoding
                if isinstance(data, (bytes, bytearray)) and len(data) <= 256:
                    # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                    # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                    self._data = _np_.frombuffer(data, _np_.uint8)  # type: ignore
                elif isinstance(data, _np_.ndarray) and data.dtype == _np_.uint8 and data.ndim == 1 and data.size <= 256:  # type: ignore
                    # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                    self._data = data
                else:
                    # Last resort, slow construction of a new array. New memory may be allocated.
                    data = _np_.array(data, _np_.uint8).flatten()
                    if not data.size <= 256:  # Length cannot be checked before casting and flattening
                        raise ValueError(f'data: invalid array length: not {data.size} <= 256')
                    self._data = data
                assert isinstance(self._data, _np_.ndarray)
                assert self._data.dtype == _np_.uint8  # type: ignore
                assert self._data.ndim == 1
                assert len(self._data) <= 256

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
        def data(self) -> _NDArray_[_np_.uint8]:
            """
            saturated uint8[<=256] data
            DSDL does not support strings natively yet. To interpret this array as a string,
            use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
            .data.tobytes().decode()
            When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._data

        @data.setter
        def data(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
            x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
            if isinstance(x, (bytes, bytearray)) and len(x) <= 256:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._data = _np_.frombuffer(x, _np_.uint8)  # type: ignore
            elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 256:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._data = x
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                x = _np_.array(x, _np_.uint8).flatten()
                if not x.size <= 256:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'data: invalid array length: not {x.size} <= 256')
                self._data = x
            assert isinstance(self._data, _np_.ndarray)
            assert self._data.dtype == _np_.uint8  # type: ignore
            assert self._data.ndim == 1
            assert len(self._data) <= 256

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.error._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
            assert len(self.data) <= 256, 'self.data: saturated uint8[<=256]'
            _ser_.add_aligned_u16(len(self.data))
            _ser_.add_aligned_array_of_standard_bit_length_primitives(self.data)
            _ser_.pad_to_alignment(8)
            assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 2080, \
                'Bad serialization of uavcan.file.Read.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> Read_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f2_ holds the value of "error"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.file.Error_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f3_ holds the value of "data"
            # Length field byte-aligned: True; all elements byte-aligned: True.
            _len0_ = _des_.fetch_aligned_u16()
            assert _len0_ >= 0
            if _len0_ > 256:
                raise _des_.FormatError(f'Variable array length prefix {_len0_} > 256')
            _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
            assert len(_f3_) <= 256, 'saturated uint8[<=256]'
            self = Read_1_0.Response(
                error=_f2_,
                data=_f3_)
            _des_.pad_to_alignment(8)
            assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 2080, \
                'Bad deserialization of uavcan.file.Read.Response.1.0'
            assert isinstance(self, Read_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'error=%s' % self.error,
                'data=%s' % repr(bytes(self.data))[1:],
            ])
            return f'uavcan.file.Read.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 408
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
            'ABzY8QiOG40{@j(UuauZ7*Do!P207$)^(F1yCTdEXS#N79lng3rX!?HV%lzq$k|EmX};rb?!BCQZfyp__AuG-zy>>e@JUqgzdnc{'
            'D2n*t!&J~c_$~;7kAlzoo!q2J+GLtSbI<+GcYf#h{l8cD-TieWR{v8+{hA%vPLc#naO&_YwB)cPDSK7l3%F!jjV>~WS8-{t)qJM!'
            '=;PP)t9n}PC){<J&=6Cjt5Sqz84A{^GC*8fMTkd3x>=@fa)Tpwkx?6e0^f53+)I#6CIarc259g?V|_<w<Js72`kGcFgi0xRDU>YG'
            'FCl6V%G+964J>iy*exEz#HNxGX~@A~B!po#(M~HZgonl)fU)MyFoCzh!G`+bUibRKc!zJ|y_4&1z$-4ZGp=M6COW+_LP}f`hq)CA'
            'Iy;W6$~2Iq>e<NZaWz$F0-0mU6z;8<Ep$cfx-M$<2ni&0Z7S?`pc`QcO&QpvPKXTl5!)+k71Jo4REZS&7|+OU5^xxvXsnK9$KgqM'
            '3Qj}_d-7QgNtnU7Hn1LR+RL_l!2%PP4r>!dDp5wACOXWkp$$RHMjGJ$Qe%z#Dt=NMBZ3lMHv3;(M%Q!MT>fH?q>IITu}%x-;n~I|'
            'a83=JIeq%n={^vLa``o~lwZ#+c0r5J^?{Vg<a^SJ_d{uPA(cw6u9C%cE|cy?YtQVdKHv^y5Gqqlr`Gbt7Z6RI%OqLygoS0nsy<e)'
            'C9v>jUJ+Qymgid3@~H$%0+p8UaaRVG^iXPZ!OGGTHNAt)+-yI_WpWo5mNSb4f7jE7&U`vqK{}?^EYlS%9$2m?Elf6UTN|E0D$J5p'
            'RG5skf?9yochTr4SYu0><uqB#=gIOy@qD_Qljr99adLirjpUceYGEPO9qnvCPBKZkx?U*ci)-C8;8Y8asmZoRNJ_P+w;I@|;V7Je'
            'IXDj~cpg^ZMYsqID0pxguD~W-hih;PUWYf}ZirpTW?0T;iYcLQsxh*`x0p?QPe{UTol_Ge@Ip~$!~}tuB++WnJRDxqYN&u?VXI)I'
            'cd)0$XRzmhXPW$eiBF1kzqi7rR>P^957b#?RZpuUepqsNnFv-19dmQ5A>)DlQ6EMmbEQ^e^<JEuO`c4e2Bf9wev<@ffOG_NrRl(%'
            'yv+1XOstt43ru<&u;effme7%ww}GkLmPMB5Gf{6>Nz)`t4qkh#+22~-6oKW=cdZUQ$K`VUeU)vuQni<OzE)N*kf2sAd1x~-UqK(>'
            'v@o~l>ojoCw2jd+a2!_fm3pW^ZJWE5T}tq++0BKHLq%=pF3jK3)7kOcK?!H6A0g;$A}pbuRqmQegA2N47K3KmU<B}3Hers%ZU;Dr'
            'u)$NeK6i6rsh+zyQCKt(F)8uAH3g6Kn7%^LnpTG{P?Vx1^4Efqc22=j!W>pLL5#+6t2PqbwV{S^H2Sp6WlgWd;_Bh1XE)4T-*wOw'
            ')$wfHR7zA@pTifCYrcf9+dOy>$Dzr4w`(ZOr6v-XVCFLezTe^94yZ##>Q-2h`AqU&alKskI`YR8?O=)9br=7TjlqvAu>|~t>e+Y{'
            'jb>Cr_!&dN0;4vLYU2-5Yea0Hsi{W57`$ny{sL3*58MyotsC%m4&H%xr{O(#A3lH&;UoAMK7miw#4{()MjvGz1qYwqs5hjpzWi=`'
            ')sp=Ysr_ku*G=;qxR;HG4TJC>?Wwbe-y<_EG}B77#P>`N@0Lf#!U%q;jYnT-Q*i(PoBMJ+9*ecvhb6(bFeRj3xiqAvusKE_yMh3^'
            '1Rpz-&BA2+?Ez`l?uPcLTb(KNS7Y_}%86e2kwe2T4H?6?YqgaXX7g&7O>;E)FEa-KN8t+q00'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.Read.1.0()'


    _FIXED_PORT_ID_ = 408
    _MODEL_: _pydsdl_.ServiceType = _restore_constant(
        'ABzY8QiOG40{_)nTW=&s6&~-^JK2kuC7X~aP?#vOlX34Q*<1(`nfQ{Jv1iQKUJ@y&Q{7!N)!v@&p)a;)B}5_w>`EOHln#W;0}n_@'
        '5km07I|A_ne}e~<M;_pT2fkC)Gt)C3Z(`tum0UB^U3Kc5@0|0UQ?+lNc)$BdN&QPd*X=ox;~8coLYI5)ZEktOFzukz4I(!dS$f~5'
        '2zOmuZ1uV#doP=REBj_Pm!302@r^`8u^H2ISxV0>3D50di8DI$l<E4u2-TF$I85v~3CDz;G=1K|Ru3k8*XF*_a-l<0a0i3hBul5w'
        'T@glZ;FFxwH}miBWwohV>ATrmP}Agb9J*E#izxd#gdSqqU{;o%Tycfx4Am%`4v)Du=&<G8kZg2!G2_y<AGvK`IIDgv+9Dja=|0nP'
        'W789UJC<3Egxefwbpi)yeKx(k(HBI^j77X#r&narcd}-de%g#;?mIkmih}MYmb{Rj3R<m50F@J_6WCc=%JBFhy|H{mp3T2qNN0+G'
        'Zg2>Y7v-fsX7Vy{8m>zpJ_NBa<h?9?;3mgYJXuq!RO#t>ObAbOgx`+|mP`IZZCXAmAFGwfFgbrGvC=a@qswhK?q#)Z`l;MJvqcV>'
        'xOz^nJ7HR0l%<dLH620&rQ`A6S$g&*H`e-Y;%BaDdfW`US;`I*67@P(;JE<y(z@sbz#&GkHM%0?aS#?G+m<c@NUo*#F9yENW8qJn'
        'O6JncQ1}#@n17+3cpeXX2WFl!ce$5{?44|`HvMj7$$AdMSF!4WCimN-DY_zd4^!!u+2Q*D6$@Td59RB9Sqi_7>u0qReZjQ#H;<>M'
        'DJBz-V`^=Rrk37~5Upar%YBt(^~4fTM8Xg5`kmu)r!Y}=@RlSa*iLj+fITTI`1xQu4M-@22e4CUjym;4<y0&^v$?!cZC1A$O|@RW'
        'o<7od4)h2`M2d_g-*i(U&Aq;KtU1#PxlK<IA=4}Qcf3!JJ^gG(v8NObKTetQdi7OvZMpvP)+@O-@^-$3{8oDW+O_KgVIsX$pdHid'
        'X(A(`U3o+9$w+=rememfI09x+ggDuq^gIH6UpQtr2xHTAvU+;ajDjSzg-MxeDj?I-^x?S{!e;|qysz^2Jve#l3Nl{?#F(dId~(=('
        'yzL^~%Zt6P<lYjZHbXim7NQtL-G+Oy^N`-K;FP8YNTMyX^c;ydt{GPi!aa+LgD#npN6;puoQ`xE$nMG~U;X^?QmGDJ77inEM!CvJ'
        '3X6Jp)?uVL6TS^XbC~P1?X8vP47Mc&3w*D~5aF)FA_2h^z08eRjCZXd+ymXQ$m5Y@vsY$GY~=cF60Dxh;o&?BMGN%L;y|qmgCJ&('
        '3veN-$L8pn7uYH~SkPj7(zPXR;fR(CvSwCKts`?pIB%4j0^lH~v|MN{A~q+Cw!vl%1KYuR=F=YedXTdEjod>p5(IPHgBy~zgkWsc'
        ';XP(c%2cvlS(Z@E!(K><U0_Ke%H~Lj@L{zrocS-78Czgg4P7^IG0AU}ja(xOm^kxX{}w&dSYu01t0JJ%o{NQih^le8z#&?Ys-E-('
        '58vd{Crd7qE5RRbC&`_y>657jfWWq85DB002n*woJ7NJPi&-Mx6L?JB1u(Z<4+TKWcZBE`x9>L!5#e1X5ch&GiWg8s1xfTHI4j>)'
        'ht^<kBq*GWe5~Zo=bjhrMf5RP2@L~3=B`hm@P3rJim+@^M%*Z~w69r!{jnJj;Zn*Wn3wpsBJB$7=~FE31#GceXDdq#G}IB1k;!HG'
        'iYAWQ2#sIZ;EsbG570N>HqhyG_3NxQos81%VQeep+qC)#`LO(zTu9_QcjUWu`2&e(@5>*`AIT5okL6F~Pvy_ji%(yDPPbMgsV;wh'
        '2WkDg=~9W_=>ThmK?m4`Ad{F<z!BQ>$Op;^G8jE#<XRM-NerjLTR;wQCN{DtY9$`CfjVOQn!%O`IMqu4?%RT)v*TXG+!(&ddjWDJ'
        'C6IuVkT^V6*+Vf1u_}>BFU+8z4+Xa+vag4dU1rx0Zh(0nv>-wL$TpR}-aU3(guy4?HQ!O8kRZBT{o3|i<TUezaCAtB*p|7B7!j@3'
        'V|Lt6st^U7_!#@!Dky3DoL(tpRV3QjEmA2fDITfctFQzDJpk+n{sPeTbTn$4m4ZkaUun3ibqlN=WR%W-&3%tk+&qqreFD)U+JnP2'
        ';pzMtBM3Zn0--S%`)(A^SCAKsce`PLf(%2L2*V&O6Wt@3p_P)VRjH^PB2@~i_9ux>7fy$=YG2sfBm5#E`fk8e>=Fld;4%H(7c>R6'
        'T~G!)uI5q;r8Oa9pn{;|RXGh-(mrT#T(p)>xlcgK=0K&NTCaJc<F+NmRg`#fpSpAB2G)=)9Nyt=p_2r$6A+zQxw@4ya6!@4<;M}~'
        'fB?3kgaM{O2kkKxMPgk?rBYtTS^<$1ZD0>-gu&JXFh`l{X><07Rf%pyJ476pU6pV28%oDaa#S&n50pw(FB}(L0rwbb!HG>P!*UqG'
        'zq&e;Go2kE3Om&{2~-Sqkpz)3YH7+*(o#K(W@~yk5&-*XeW^!d+_r<z$x97QqyB)j>}z#ECkDqMVps4^?DI~Sa>WxW3Gvd(Jvr+V'
        '=!WI`vy~wN!vY^kp2w6QCE>8l=l)B&<c?s^_X1AZ8RgBS+YKTyO!$75lcHFksN~yxrMhta#xoTb1qX~)3x<}r0*#q6bWbI^CCak~'
        'G=qd$gRKl)tO9%J=gM#$>?v3}5L58h@by4)x!OVm6wMnLR4Ib6m$MIdh8xaVg62mZz*o>CPaHLuLL{${<^0e;ud*6sXx}1!;B8K&'
        'lNyPD7_Fx&d_s()PBRAEL~+PlF5Msn-IyYzEqqEsK_x@#tx4^u%##?6ZR~1s=p%eVB?U*O7ZlQiPyq?6wL_9t8d3x#@j>#c6q-K`'
        'NIBP4y%_9Lh)?XMp&Ae8E5kWCUP$f4CTgJ4smZ9X4e3`NM2iMclcYj0>Q|FIs$5!Ru!gnk21(@gDmrKe0pWJK>VN}$6dsBsbcdn<'
        'e4(re46#ieQ)OJ=yb?hWjwK5NZ;?_3Vj%x}InSwrLe+sXfNKuXqy>^MyW|Wy`uE9>JG*YAiH?X__5FD=DSb&FgcRj609JehT37IC'
        'M<g8!4}rA0699LkB<5|Sr_9&;X#zj2*ZSq)+wj?@o_3QC;*(|;Pt9|50{<}Y!{(%mzkVAgf1wY>SJ9pQX4st#W{*ABU7MVd7v=r>'
        '-sNGr@X7l&`RhTKCVz_~y9%T@TYuwBdKqU+eeo8W68Vac@e33-xImc<QxTG)`E2w8g6H3y^~%)5>jf$6u=<TN>WW~xctxPFqL*(@'
        'c&TnC&f}aKfu$pntA9G*tz5Xz`pkq2LcJ&(0z2s<>|$}@GPNuBx(O>lH&eVBIH~Vu@+*$;<E9^L)FxaYOkKVAUBrlpbKCV=z45iW'
        'x!i0HE=P*ePCj$v##1+rAn{DSv1P6_w(Coibh~~8Nz<#1L)Dr(ic06Ii;K&fo95DTeRX+~TF0(Ebp&x|S0QS(xxBd5Xubw%>6cdx'
        'VW1JkVI2*p&?WH79vTQDCeWNZ>nXBSjdC=0OwPu%xqj^^#;w+GR@YXSOpM#hq|UR;=(Q`F=&85rA87QoNWYDUiOb{SwaNiCj^eEI'
        'E30eE=2oL&u2q{aFHZvb`m;v?xv{-vHdf5djq2iLY0n)6BnryS?Tw8_b8B)0JT(-Tv*thK-{rsLKX*<|l}bCuXqchlEDaCQaG8cj'
        'X<#%MG(17W^EBL`VTpzpX{gii6&hZpVG9HJ`0k<S=<|w1#t+eV;od7F7h_F*no!5$;uYE8@bU4btH`r6#ey`0f;2OkPKm69ra4Vk'
        'LvDLM|MsQH_n+1E(v*B@%u)YI@t8TRc$5w+9<>q*L}{8Vn(N;%_f1QNWrXZrpSjnx{uK!wIY+KYc6|6%ezfy_@^PSj{E2FA<$u;+'
        '><Cif!`jrS3zgnGJ-pL4GT6wb54II!&-1q8Z^P>Mk+SQ*Huuj|#{csF)kBQ`hZi*n6Z?W`%sid9<_8nxuT<N@L0?e}pFa?gzo+3('
        'H2iS@>G}s#_XPDW^=*k|{2L4KbP;<U000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)