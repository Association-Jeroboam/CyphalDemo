# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/405.GetInfo.0.1.dsdl
#
# Generated at:  2022-05-18 08:59:56.464590 UTC
# Is deprecated: yes
# Fixed port ID: 405
# Full name:     uavcan.file.GetInfo
# Version:       0.1
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


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class GetInfo_0_1:
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
                     path: None | uavcan.file.Path_1_0 = None) -> None:
            """
            uavcan.file.GetInfo.Request.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param path: uavcan.file.Path.1.0 path
            """
            _warnings_.warn('Data type uavcan.file.GetInfo.Request.0.1 is deprecated', DeprecationWarning)

            self._path: uavcan.file.Path_1_0

            if path is None:
                self.path = uavcan.file.Path_1_0()
            elif isinstance(path, uavcan.file.Path_1_0):
                self.path = path
            else:
                raise ValueError(f'path: expected uavcan.file.Path_1_0 '
                                 f'got {type(path).__name__}')

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
            _ser_.pad_to_alignment(8)
            self.path._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 904, \
                'Bad serialization of uavcan.file.GetInfo.Request.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetInfo_0_1.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "path"
            _des_.pad_to_alignment(8)
            _f0_ = uavcan.file.Path_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = GetInfo_0_1.Request(
                path=_f0_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 904, \
                'Bad deserialization of uavcan.file.GetInfo.Request.0.1'
            assert isinstance(self, GetInfo_0_1.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'path=%s' % self.path,
            ])
            return f'uavcan.file.GetInfo.Request.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 405
        _EXTENT_BYTES_ = 300

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jJ1Sf0{@Lx;cpa06mKce>lFkn6cb_?`JmUNT`0kb#zaaBh{qjGDTEK;GQ0ckX2Ra?Iy2k$Oh_OGtU3yY;e&~ZF(&?<zPEdK'
            'y`!yqUvBr!%<sMTdvAVkpB{X3WqPdm*|S+U(oyXB8kFR*{FVnXcz&36vQ$e0&K_NXSa$F+TJL7yUc0$x?uo0}!@f)sP)>~5qj!wT'
            'Lz62Q-EzoJcn2ZQ<a{IKiPw^deFMzRq?LMW@J$ZdI9u^IKxvsK1T}fD_x#$`$LixR+%spVeQu1BL2f|1hi<=^2b-KdbX`Im?F3Tw'
            'BW}2FC^|7&8b#F}AC7C48{xze@lJibK1P1UiHErBRB!it_RKzRmEv7zPv7HcMawNn+D0sqb(D>xKE%+0#FTODmqw<DZMlIvX6`0h'
            'wiAeMCI;G|M)9WoKpH<T+_`!MlMJ~wekYAE$&c*pY9EM>dCR!gpd}*qxm$Dgq^}K6BCeugpzS=cQ;3xDP@1l*XZGFRlHVdydnC^F'
            'Xqm59#DX|qA16q0kxn1<gIGKJVL!bcaLm-a{qF3MtJ0LD-NDyhdUnE3GiTX;AiCQL(pZK_QUf|El4r1MZfBslN!4(dhC*U1h%5Hg'
            'a+-wPK(gmnN}6^mNF3GuiaplM<Cv@NuAPVd4Iby<Ub<Sn@=6EdYLAR-c<S^TPuj2s85p@=NRRyv-$H8fK%+2<)jn3iUq>cbBznMY'
            'ji(cKlB$}=9JkiTY3tZ4jrE4Dj3>oyY32c7AP=w_4;$MP;_IP}g5xS7W5*xNsLK&KN|CxThsGIOL1L&C2IOP6zg6JHqO=Gwb?4gZ'
            '(%RDcZLBtkmRPm#_e+G)D9{wnNE27q3ch*VN5?Z$EyY8!VxLs5_nvXx9=P<0qfRQq75^1XwXt;Hzjdv7WBtosG$QM{5V@ULT)a2{'
            '13NRMB7V><rHMczaaMGM6i-Aq$4eCfra^rYxo!InHvJYvewHfZ%g8nD316qV3c)AQ@Jl);=`WT6Hqk1o=2jskud&qQ=aFlXk_H~g'
            'q_frKZYFrVf*p&hnB@U>u&<zvrA2=`B89XZF0~2IlOvR20`(TX3m&oU4Bg-vUvP~vC=wM^kqsGw`$53{4<^ROnkcRiF@p1|ON>yM'
            '?xL;3C|m|fh;k4ynXtR-*Drf)T>wjyxXZA+WyCZfFm*1Ini*VcrD_w!g6WuR!OopON3dEZZ2~TAH8jpK1ufKYX42x6N>jrkiIgH#'
            'm(|D?r(w|(EN!t(AwxkfB4|mJIu>+`bCeFKIj_0~NDg*ViHlK#W;O8I9y{lG=nk`I3Hj)qM@cK*@!nwz5(PCL8<FO1fxzgf!@DdL'
            'bW17sBD0)k7y81Buz_4sW3n2708T0_b~N`{m9Yi3R8p6v5;rAn%8{4MB2ApdGI>n4l52Dsm!SZLv?=i*-(l6;A8>~)L@g|R;GLBo'
            '`rgP@DkW-%?Bu;-m(t0KK~7|cBGr&EuJNEzJc5O^)nWmdO+YhEf8;!nF^+%|KLW^x-S-E+Ccdjg;%2I}S-=qlgqUb7R?ltOS_9vB'
            'EwRXW3+H>q=W(2FYWf?T#0b;GaG4M(yx(QAkf{)=*f&L5Wvy9?{?Qp%SW>z}m|mVd)@3QsXF|QWnX=`jCcD1EP<%R|JtsaDpO<p+'
            '#fXF-Tjf!N9(PGMt}f%}N>(o8%*{t7cem1#D&+we-{In)Vpfai+u}u2d@p{iiJycOKZ{?)OYutlYENFe@bTc==mK8!!8I3ewguP~'
            'T2P(x-tZvJ4f3K;NDPeJZERn<W@MV*DcC#%6VC0I^6!JE-^3sPmX(;s52WMtVI*e%M^fUiLHy!x9AdDA)7QAhqbWO!I$M5LDqjFL'
            'pxX6e!BFZimr}oH)Hh1gS2V4M$0!>e$#;8C_Z#!$dk$RjpozIYnkt57Wq4>7Bb64P?y*Qmy?+2eV&d9M3jhE'
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
            uavcan.file.GetInfo.Response.0.1
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param error:                               uavcan.file.Error.1.0 error
            :param size:                                truncated uint40 size
            :param unix_timestamp_of_last_modification: truncated uint40 unix_timestamp_of_last_modification
            :param is_file_not_directory:               saturated bool is_file_not_directory
            :param is_link:                             saturated bool is_link
            :param is_readable:                         saturated bool is_readable
            :param is_writeable:                        saturated bool is_writeable
            """
            _warnings_.warn('Data type uavcan.file.GetInfo.Response.0.1 is deprecated', DeprecationWarning)

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
                'Bad serialization of uavcan.file.GetInfo.Response.0.1'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> GetInfo_0_1.Response:
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
            self = GetInfo_0_1.Response(
                error=_f1_,
                size=_f2_,
                unix_timestamp_of_last_modification=_f3_,
                is_file_not_directory=_f4_,
                is_link=_f5_,
                is_readable=_f6_,
                is_writeable=_f7_)
            _des_.pad_to_alignment(8)
            assert 104 <= (_des_.consumed_bit_length - _base_offset_) <= 104, \
                'Bad deserialization of uavcan.file.GetInfo.Response.0.1'
            assert isinstance(self, GetInfo_0_1.Response)
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
            return f'uavcan.file.GetInfo.Response.0.1({_o_0_})'

        _FIXED_PORT_ID_ = 405
        _EXTENT_BYTES_ = 48

        _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
            'ABzY8jJ1Sf0{`t-UuYc18P~aTbe3dSMzL%9hl~lNGIdw7T}LK;2#$0z$Juwv>Exs>Wiq=vci-51JIl_jtTPnihZLI*#Nf?CpZX8_'
            'FX=-m1X5B;9`ewn(2|#y6hfd-@(}V+^3aDq^qXDXX>~fKIr>^5X=i7?Kfn3r`+nc-^OG<AZEhm_F^@z&U-^MU6^{iA#BJsV+@YTA'
            'Mp6mQQ*(5c2cnBZztxL)`XD`XC;d*kU>>3(40)WwggLsQ<HXZR%=d~MrXlO1i7zH>%VVL_7HInl*VV8sohDb23>7Yy=@yTbkfF6T'
            'b$w_2AgxW*O5aWIq-KUPtz+RPnyd8NX!ros1F6&;UK2d<ccDyEpJ_(5#RpUQButy*MP!vYmbjl;I94mwCah;Tj^5zJj`*pA{6?`2'
            'kk~@M^P8a(osj$0Q1cFt_XcE!x<b={haC-RZ4Oa+OljJcKB78pPOkS2Sv6+`*RI(m8;TdwW@;X$O0&>sv0pTFH*s+*hqqXeAc9Hi'
            'OD{DODbCKD@(RWnb@TuPoPtMpMvv9z;LGq8IGbBI)TpK4z#<;)j;$~C_sh4Vm@9iOdv;rHGL3UA=v#+nbEF+J&(11bU)veux+yKC'
            'b`#1)XXpMKmZO{XTD|d1omQI7Ml*v2%kadG6L``be*EIa3m3<*c%<HF(Y3~AeRYJj()lqgm8*>dVU@;#boBDdN@Zh%u2$;R$|zWe'
            '&RrP8+-wz1RhyNSR-^e1v}T^HI@~!+uq=2t!U85SXa3@?7>k+6kT4Q44MYReB$6W3ifD<mzKFS}W!y`L(40Rv&gQE1>zA)qS1JDA'
            'tXMe96{mx6Y^@PX3`8grN=-1?giqQsMkt(U7I(PLrBqKL^nEbKIjm!A)vFcSYBcE8%grm5Q9(YxJWh}sn=RT{qZ{j&S4LaAG)|Cg'
            'Qf_RnuQ!^l(HU@I*Bm$V1tO$wFQ->)_N(v+JPzmK3ar4>a1Fi%&j1Go5^ln6*n$_}4!j88gYUyj39^vSv79}IDUseY$7ow@bDu^s'
            ')>Qau-5jS%Cb7q<Jp^i#BsEj^5ePRmN7k`3Y_Hqd2gqrqMdTcimgf&eA~n-1y$D#a%DXZ(Ux*Sn5FU+rCkd>-T^dGucqnII)VGdO'
            'b1Y+E=bW?TSlUUo<-B<cOd*JvhuZS)mhgCb57TL}&XrASYs{I(c9H~|$TlW$A$N$3c$|@xW2w;%(CuS=R@>!JG^~f;Q#1RN&{wnf'
            '4L%@H^BF3m)R2RWs9x8VxMxIu4P$^k!g_CHFtEK8`lkm1TNM1(e0H7rz6d+}gy8pfwVnh4i+jVXu>4}WP@B82T<oAxZXvCe6BqZ{'
            '6`}1fIAGg$FlBoTo&c)V%2sXSzQXQ<w9dk;+tw2|%UJ9qJa2=JIkg*8TbPANqTq=Usl9-yeWq5j`3h(6W!5H@xXrDxC)Tn<!8am8'
            ';`T6u9kKy334G$>0+u|I&ut#dj0yT2Bv9;=-2J8R=+Pt;+f<7#CI#z8RJLib(_2Mbco}euW37c-*{oNeC6!2e$bP6nZUGOoJz|c<'
            'J#vdFVwFj*%zcM^(*hH1l7u%yd22WXr_Ib$QU;ubd-^?MEalanV>}^LUQ)<<w7{~CIo*mAZtdG;q(~O1>~$bC<nZsK9ZaEvK!i7~'
            '$){U@{EEMf*r|-#(J$~g-{se{4Kr76ancT02am<KapEecVcban<a0{?bP#3`f^9SQW;BSmu$73FZco}S;`wKWJr)FrXMsggAb8e('
            'Yyc2*=oeGq%%}4`i@vk&)^~1(o!eE-!}0x3SKCA-m@j#T_>$+ni*F01vBd^K7DPqVAf-LbhnV||cpa4Zbn*+?>`txky`SRU^7Etb'
            'mRk}j*_5y2qnKN`^+|<$#(sf41A7Dfz?%6poP@u^JMbR73;%%k;Y0WU{s|w!zu@BpesmXpT!){)PZ!{4@N@VD{1RS<SKwFX;jb-S'
            '9Nf#7kbej43%|ab^`zgxtGV0P;PnADy)hWQUZATJc;mEb6prLQb0nudWOI9y|72@7=1LP2*~^W29Q|KDAN>ygP%B|Fy@hv)xAE_f'
            'crJfJ0*5yXePIFn0#{b(5(-_~73%8_O^?=n4uziEuRAnd)GZBk849uex<k{WbzKy4_v;Q#kJj~2$lI?wG(B3^M<IW|?$C5mcXFT$'
            'C<H~_a<YFqZ?Z6hUzv0H*X2np*LSg0Kfp5m82<gg6!MKp%$h>kV%z82Scy8l_I$~l#A{#vB_C5j62?dVIlS9ZN#0TI-E>sNkI2tr'
            'C<umP4;6f_$-)kA@`!73&?V?*ennYAg`%zU{VY;%)!}W#Zo@aYw`6h5LT(p-IAYPNI{yJ4{p@Mx5C8x'
        )
        assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

    def __repr__(self) -> str:
        return 'uavcan.file.GetInfo.0.1()'


    _FIXED_PORT_ID_ = 405
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8jJ1Sf0{`t<&2Jn@756w_w&NrY`PxlbQ3)R!OHRkmw}SYXwa3|E>>2Oa4k04yRCm|7YTVP^bXVJ+2v8OQN_Jb?Ksp@ufIwOy'
        'B>n*SH#ne`xNv|2Ck~uAaNxbJo|&F;JBbf)Vx>IKRK2fy@73?UntgKc<)7akN&btz;B~CPvNb(mzM!^vObwf9y6Lt(HxQD=(a}}r'
        'ZwZsFbvzcoh^Ie@e-Ia=W4h127qUR=64&`ibZmjyq75R}Am?FSI1cj@mR0G8rVRZdWruW!w!zeekZzgO(V7B$xXWb4X}VfN*@>eu'
        'eT(^la2-^2<X-yuMO+=J7JeFk0G{epN?#bEWI_Be-s@~VrZ_sZD41>a9huNADrtJ8NwvsNL{nM6R;c7LKgmy33)K;{%g;UpuJbAP'
        'JJE$b%=$j<#L>BX6jotni8&jRmvD7Bw9IC0=A@zB>lmJo(H2|4acbQO#D>GHiX+(u^9S`E)eRwaJ24km$Ka4Ag}k+03l2FGon7fF'
        'LNRR~_LgxA1N)P>5l5%>KvKt|zLiz<G&G`d(Bx55$WC1KqR*vUdJ}`122o4HGFKhrSNZj70afx_D1A^j>>!T5(mh^ZIh<4ue~+Wd'
        'cZF0zTZOOb@uCB|>%|e-OG(ga8?G%(2+}fZyAV7HRa5tvPo?W;tJLHIN`aT7GxM%vQpucLRy;Iv`pk(j@8#%3EwpXwcXn|e*0-n~'
        'viRe;SRH#F82oM;jBkO|xdwGMSc7>?ioIOg)Z26iLJI<oWRb6TbtUm@3kQ;fAAoK7$${tyW;L`auvQDmI`TY#e6t;oI>~LRg$4sh'
        'C}hJ}etLkL8AjfOUDON}f6&7!2hElXp&N-|@vUeK0)wT{3qDl)P=aqJsRae&tL2qaqqJ6sY`6F(Uyt7DrU<<8S%B^g6!BOii8r;o'
        '+CgT#=~EL|p-#pY)6cLUjb6VMV<jc-wqNJW#B%ArzErN=U3)L}hKH#M{x~`?H+QwCj76t1D54u31x=__@Go(nJN!rdhap@li@`Cl'
        'POSK8bR3F)hgrJk`cfBGT#HWXfgAcJ(-Aau70x60#})<@(F&mJP68z_Ak~E{5Nqxt29A0njwa?i9;fyKR4kyP7aCB(0Js~FTCmp#'
        'DG1A9g-sxjhT`ZLD%Iw+Sq-BdOT59SbWQ{C!ADRD6r9J;c<cVf10y3f09R%aRHsdp2x=ig2iDpI-6hO10S+u89J0Q)cv~ZDoDtWt'
        'I|Qm*SR`Pe7%P{EfJoSDy8bqR1qo~#aB}I&B~%*-X9E={YeiU`CO&Hdh7;)~Qoid-VhIQ-sOpd+uGy}c)C6&xWSa|<qX~;O1wb7!'
        'I*A+}hxyamM1w(appukc@R|jr$g~ZOT+%c!2d5_v+DPRA(vt6R@1O)R1Vw5~?uHv26oa8Q?GTgWEyc4ZCkwH6fi1WQTM$buOj1N8'
        '3_2Ag+nT;JLC9rNQlax)0Zh&Yo{_4^LYOGAg|mrkD%N1qR<1B`X<L9G?MGGHTVX$1pfy?PD(>&3+VeF}U@8GSL_18At)P=6jU0n*'
        'ayMWOp#ca=pIYp)+iVhp$!!M9I3+;L4PiqIQ2H&#ysY_d!w)dt6Bxv8*AL`nXh94$IsqgrHLFUiXB)01BpGhuOqzUZ+wOLNe|nPO'
        'q3cL091IHWR+&g(%48EzH_5S7u89lw!5H-+rFe(nc%icys8oPW2WxTLCG({kSzI6hK5Z6gG5<O*DY#e|fbbJ5)Uv?hF6f5c_h4M{'
        ')Hd|oa1e5LBQ2s*Xi)wXHh;q}1pLFN{G%F=_{T;5od1mfoWB63m;4ve>FcvMdb80iT=d>G=bt>~t!M!^{I<F`)Nn%yaq$62BpbNf'
        'P`-H0aA~HWuo=RnIlb4Bf8G1^OaAGrPQ|BSKstki5x?*ThvL8O`Okj`O^oe8_m%PTqw(l0;H(-eeVsEXK!4X@K>+H%rl3C8>m{{R'
        '$8Mc%qhzopKS)14T%IZ9He60?aMnlTNz)w5HqE4^;^vc_&7@Z!2lNg+fD4woe<Zawkr^{TpFjR8xwsqA%&3`>J(-m)`#x0TD`wP8'
        '^ro_n@{k%>R5j-I)dBX=dNrq?7G_`Fng>)ITd!4X^>5eoa--3k6|&k6-Mn$*+Kqi^9Iw^a^u_vmZ6VLMtNYM2R;lmlR$)Ib9V^Yx'
        'mseNyg>tP@&U0&Y?%F=oO;$ivrBR-T>FPV6E&4`9W7-UXxrMbo>|{RNlq=gl+!}%?pg>S^DpdywhWbZ5<jvK&{T!}RyH{GOEa*Vj'
        '%jnLnGIZS;g*G@nA(&%(Q}aR-n-$=^L>QJ?Oxoqfev);3v9eUw*XnhBsnobz&I|I@Tl)!eeSJ-@FY2o+rTKhqxAzkyEXvjOm6dv9'
        'Ex!V;_0=&%%p(6Q{|o;+{~P}&{|Em!|5xj9VPvE=iew7OB$D$;&La6Tl8Z=Yk<1{ugXAWX1ti}D67mn9?a^6|C$KR%I`U6oOpLA!'
        '%!q(Up)GMHqXQkqP1+!i^{;IoS#X^~818nHDQ>{OTnt5cVhY$=(OZ2du$D5WfiVx}imFLGQ$05jj}hgfJBx|`@C`@2WZ2Nisv4OL'
        'oGm5Zl*i0>ld|nz7=cs4n;80H=!hL%3K%0KZF{=g)a~@`Et*0Nx9G<r4nFI(%6(GyT$prF0)`%@#!l6$w_ylFVWNbYrI82dm}n9h'
        'VjOpS`0z8)(RW?fX4Dz@Jpg<xsM1tEo)Lk1qrer_Gmy}VF0T0@L;Y$<Xi_^!zV?^~4YoF+zVdAx0UJ1*qSp7<aJUvhW?ZF?n#_`e'
        'el<BWOfE3WH*LBBnXxcbOua6!2D@oj5c0-e90e~B8S(d%UepDaE_6=JH*R*{6()?C;8Kx#o-J6=9oLgNHd_eOZ)|=N%qN)KwI2=J'
        '$6c6w_V2<(rAdO&<Y}o`E>nohc0?d&l8G5Z8FZfmV9SKU@R@Z*Y&b6b)zlMzG976Le;4ELMCbE=gxYf9u^WxugFo3KgQFh|a1Pv5'
        'ql7}V)&qzQ|E%>0!RWh4nn(;J4ib(;BJq$sMzV$E36k$C_<DmGa`ScglRq5(pL2k-^**NS(`sQ5nG--BK=2|UxcXJ;HZa}pGj(N$'
        'mh)vF0n?-1vO~*R*+Ng20u$XWJG7iHYXFn6TXtwUU)BUBbGPi!a=xquOxAAMq2;XX!JaG!CZ3g5-E(j`eTx05|8V$B-8!Rp*Sy{h'
        '!^_qBF_8cHRsH?)lLG(4fAKw6oqfe~4s7rJocmQ_&r#%5&RZ?_i8hAqFa3Wd-G^0w_mB9@@Ow|ZELff$g+QK0@-~ulqur1$zbw2W'
        'sL${X9U9ty04EQ)+~pYn00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)