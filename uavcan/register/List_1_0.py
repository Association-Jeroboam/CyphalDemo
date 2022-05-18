# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/register/385.List.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:10.424248 UTC
# Is deprecated: no
# Fixed port ID: 385
# Full name:     uavcan.register.List
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.register


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class List_1_0:
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
                     index: None | int | _np_.uint16 = None) -> None:
            """
            uavcan.register.List.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param index: saturated uint16 index
            """
            self._index: int

            self.index = index if index is not None else 0  # type: ignore

        @property
        def index(self) -> int:
            """
            saturated uint16 index
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._index

        @index.setter
        def index(self, x: int | _np_.uint16) -> None:
            """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
            x = int(x)
            if 0 <= x <= 65535:
                self._index = x
            else:
                raise ValueError(f'index: value {x} is not in [0, 65535]')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.add_aligned_u16(max(min(self.index, 65535), 0))
            _ser_.pad_to_alignment(8)
            assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
                'Bad serialization of uavcan.register.List.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> List_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "index"
            _f0_ = _des_.fetch_aligned_u16()
            self = List_1_0.Request(
                index=_f0_)
            _des_.pad_to_alignment(8)
            assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
                'Bad deserialization of uavcan.register.List.Request.1.0'
            assert isinstance(self, List_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'index=%s' % self.index,
            ])
            return f'uavcan.register.List.Request.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 385
        _EXTENT_BYTES_ = 2

        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8eui~o0{?YXOKVgy6rO5pb$qo{+$b0~qMNHCf-4tR1Q}b4R&gUC_vUmG$W5+!OlJf^7m7kap~pYyFY#n%>Qtq7bCaB$?>xTm'
            '<m2+sU(3Dem#=jb8KkLr0I!A7??r8(;*D!N7jy*7=U+yjnwUK7PCCE?y!8n`;LW_kt!T-9HHlFpY~^97Lj+$vqhIv`-X#bT^JzW;'
            'AGEWmdU^Hre0_j}r9tlte!_f~ix|DGQ-pwT@wklsT*AEaM1zrwO!{1kD0nRC9p~P8-Rh`EbYtU{4SHxnKD7~s;Qub`EU$Is2JA2@'
            '9IO#|BSPe@lYr_{zPxh?RNSgfvTYR;71aBTFEC%?Aqp#nmq&rVrdqA!6>TMqF)wrJ8q7URwa6Ps>gV-j*3}QFm|72%jfBoaBO*xr'
            'mM`!<JqF1;=Ofn=xAQs=F8Kz?V1RdmV&&EHGrGonW`{@|@08O6s%_~u#a6DccB0dm`<s(a3G*0QhxtmEYNH!YJSJ1(ExH;opPI2u'
            'd>-<QdHvpl`!lxhR(Gn>b&RD28(fJ%xp=U#&@j>s;8%71&DK({x2tqu^Ft<#ar=Qq1+1YpcorR#Iy7!n)^uFD5t!R6SJ`3cz{E&s'
            'Q<!DWPVW^&@cnwiNVHx=ZHLqIX~)@K5e(b&u4V7RJC<zJh6&4{?c!t_gi%@^NaiGrs^8xwU*{!hh=3@3!CHh5YL-qbv}KL6h4RSu'
            '6>)GRn<-?nmLRIX0m)!pWWyvpIReO1_Z%+SMhQElvwa0eiz62~Pm|(#VyG%ostwU|<52Yr%~9v$zkAH*9_jdOx_?RAx$5&t?mEou'
            'IFK-DYe(83YPU!$G*gj=_<2_v?fhbPPVt6XAW=Qc7k7k|RO)}1)Ml}6Cu4-4{A(qIkuVAHJKh|u{RlNZAKeTH2d7g_<+j?Ev806<'
            'm&IxsO%iPJ?sFJ-!cJe9?No<4)zxnh<%pu~1ONa'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

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
                     name: None | uavcan.register.Name_1_0 = None) -> None:
            """
            uavcan.register.List.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param name: uavcan.register.Name.1.0 name
            """
            self._name: uavcan.register.Name_1_0

            if name is None:
                self.name = uavcan.register.Name_1_0()
            elif isinstance(name, uavcan.register.Name_1_0):
                self.name = name
            else:
                raise ValueError(f'name: expected uavcan.register.Name_1_0 '
                                 f'got {type(name).__name__}')

        @property
        def name(self) -> uavcan.register.Name_1_0:
            """
            uavcan.register.Name.1.0 name
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._name

        @name.setter
        def name(self, x: uavcan.register.Name_1_0) -> None:
            if isinstance(x, uavcan.register.Name_1_0):
                self._name = x
            else:
                raise ValueError(f'name: expected uavcan.register.Name_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.name._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 2048, \
                'Bad serialization of uavcan.register.List.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> List_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f1_ holds the value of "name"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.register.Name_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = List_1_0.Response(
                name=_f1_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 2048, \
                'Bad deserialization of uavcan.register.List.Response.1.0'
            assert isinstance(self, List_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'name=%s' % self.name,
            ])
            return f'uavcan.register.List.Response.1.0({_o_0_})'

        _FIXED_PORT_ID_ = 385
        _EXTENT_BYTES_ = 256

        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8eui~o0{?YXZEqVz5OzuuyKj_`LM0GzLKPU)9#nv+Kp;w>0=Y3!`ofE-wtKe|&(gcy)9#+-1A*EPphjAWN?HCZ-(c2fH*r(@'
            'gYRx<cIKI9=9vep|6Ez`On?53su5NcDYIZCFXXR0D<EaLE-P)NgW%8Jbf(T-ZQxc@K{yESJPf~wzF%XCmt=pf=Hr~J)WAqu2PVBi'
            'k8~GorIjUnkBz}tsa3#^@7|fcAB4fmpz~LF82o9*oij449oTR;EQ9pKDfqSP5(;q$<rEX#apodEJkcKFnm_+EvS9>_T|7C@jc4u#'
            'd|`HB)4#eTvoX90{=ywjr*v`y)X3qrc)Cc*Sq24^pj-=OStXT`rF3#k9-Ft7l_Le>TjgK`W-;DrmPyBoX}U1zQJp!rj+I(a8E^WR'
            'cjkfOwRDSY+tEbacK!^z!JlW=aV5ABM*}^oGk=mIRXmrj34{Oqi!&43i@eTwyf~xf?LiOw`0ijOhQ!P9_A1K?8~j`I@(zPjrS9qP'
            ';Lm(1T}#?c`ka;LpJTcTK3NvTHf5#@nG;FdP--I2(cpYnf#FV@Lz326j*_MUKlLwdX_a#a>Y1*w=;&!c(U|qg|J<-H3T~QXp6hJP'
            'iyFe;p+D$7wi$jlBjXFYbzzsQ5$r+*PA-FVpOt(<)Y64-riVC~$C~n2N<~eIFXXoUZ`XHYSL=e4>tH3ib{<>mH%uz7rh*yP84!@~'
            'sT)6RcY65a5l8%)tT8eT{c5YqRVFl1*9mpT{pJycv8-u@OPCnGVrj?(R0bk%BJBI;X$U4DSf!0)QiP%3U{=>A2Qn1EDo!KhyYW%T'
            'j7Z&~Ju%sdrw3H}%6pU>b%b!DlEI(aYAWQ#SJc5k`l>VPC?i2qsg&<fw=_=ctz2ni%mqu!CrUQGlD?nDAqg%{^(I4Z35SV7BV~<c'
            '4q+ef`PZ+h<o2!WS1*IgNe3dC$4O$rX}}Nh<F*-}EHw1o4i`eI(XmF7^>f-^Rcj^%){6}|&O4#_>Fcs`%`{~q6=7%>VNwEhGI7Wq'
            '{Y8_2Ng{2cYnSM~B-6DL_EI8KNG~Nq+FaA#Y@)}WRMH}dG&U16%KHE}EQ)=EA?~5<<1ct03oKEg#>#JeaP^~h3oj6d?h)QY{%jV0'
            'd-68HKb9Ao{tx-j9rQc~000'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    def __repr__(self) -> str:
        return 'uavcan.register.List.1.0()'


    _FIXED_PORT_ID_ = 385
    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8eui~o0{?|pU2hvj6m=kJ9JdK6Nn22%9RvgeVcSv)6(FHDv;y3ikS|r0%4&9Z>^ovTv&_soaivJ)0hCB1QIz3<7k&XM;@|OB'
        '?(Eu$lO{AT9?zY7?#H?JI6sa49!yk<KYKarB|1riP&378${*1vWkDFrP9`-s%-Pc`Om%t8R(lz9d+yzBx8>?~GF0rxoM{spe-9Nq'
        'xnfivn_L}vITi}qL7dle+Ks6Q6l-&Bm<sOUN3dL?I9m<7OldBK#~NSnpZ8p2q*3|BZDSrGHAe9$H%z;S?xf83A2~aAm$NiE$fOn~'
        ')X*~FliV}KJKXRtzL;4Pnzsc@z7~eHnL1q7=`i9ZOqpmKaE)mMk12MeBNOb#tM>fT0LZ%q3us&PCM>A(vs-p{Hq?fSgsNm1XeW=L'
        'X2-Zl*rv0iVIpH^D=v?yof)b>jCy5Pw;a3;=QU=NuuQR-8kV?SI~BJ0CQHIhDiiX=HSO6@%Us0_4JivVim~jt|44b{?8Fk1y}9IX'
        '_pr8+D;OK3XYGZIJ6l`mWkAy}Sw}j1G0UTr$H;#>Pkp?Du4-pbl`JEl1D>5dd;R8(lI?53)xdY%8Q+4L5U9pn6cfhN;HS*(z})@C'
        'kxFG1xF-EeLeo@kXkvho7|%=*BT2$_EW7@U*S;H?$d-Rf2B9^fUCL9>ERmvk=MkBzMLmMUt*GImUECKPCoMlPq@`qsJYq_cTo|4b'
        'DhTUjrdI?Zn3iHV<~SHZt+tB3QYAP;2!!E1)<Jj;WjY<o1&O8blpC@E$iYxH1!OJ+LIj5a(IBKD?VKufWGwM@_u+C80~Kw&+W<CP'
        '9J(a^G%=n+h5|oIQHu1;4W|BJ=CJeT=yzw&+~($9@qGoq_NU&y7|P69auSH{bs~wgfz&SItl&-=T;gvt-)N~0cIQ+WV+#@o3-+ZY'
        'nj~22GmqdaZ*AsjN>%Tu6%o2L&6)ev)f>}~b%gSfl|Zgh%_A(g!-Zc<JkU*l8277*1M9tOA=}KTC={ldM>;}}DI92>Aw{gOXyg4n'
        'YWDRLl&gI1;0#Q|*@q6!^*vr0@|`{E+w^OTE>i<xJM4<<b-b)8MSIR(Sf_Z4HzhZ>{OwU;W-06VjVjBy*hjw9sKRA<6W&6Ju@fj('
        '8I8H=xyDob@_@u*{Ezi}qcP%DtMG=;;fulux8cqZS?3m{@B$=`W!=a0q~o%qde@;@LVV{LtRjPlpe`)?$zEm|GyJ3x`k`d@DLNd*'
        '!W>r{6<AyRcO2HY@F&C@DvveXN4A;v)+$;n)n~1RbIpzx>I!r44oWZ75&So3X?SlJ-fzM@T&crVxCS4>b@&Kwz{hsd(|TCm;L}~0'
        'vzKlOvbK8n<_Ao~xR%MjI22+MxZ|7o&HiZ<R{TI8%J{fM?Snf*5+%rBm`R7>prblaGo*7U4l*}huOgX?M9&i*uwZ^)QhWYIiwmy7'
        'tH+=Rf5P`C_W(XAtKRWldtO<8Jg2PL<5q5e)9OR3R>jxj{r^S!gbi6AptY*@H?=S`UrQaHz+dnW{GAsCEpCtePf185e3nPSe**?)'
        'Q#lC$00'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)