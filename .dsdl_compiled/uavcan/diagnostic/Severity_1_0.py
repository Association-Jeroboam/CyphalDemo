# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/diagnostic/Severity.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:30.198506 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.diagnostic.Severity
# Version:       1.0
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


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Severity_1_0:
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
    TRACE:    int = 0
    DEBUG:    int = 1
    INFO:     int = 2
    NOTICE:   int = 3
    WARNING:  int = 4
    ERROR:    int = 5
    CRITICAL: int = 6
    ALERT:    int = 7

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.diagnostic.Severity.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint3 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint3 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 7:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 7]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 7), 0), 3)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.diagnostic.Severity.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Severity_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(3)
        self = Severity_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.diagnostic.Severity.1.0'
        assert isinstance(self, Severity_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.diagnostic.Severity.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8!mxy50{^vE-)|f>5Kc(*qt{YYrK&^`)JT95wJa?K`p~B|O{yr(C0tYJ18C*lojY6d+AG_8$$=`-2aqaR0;%Si7ydZ@3}!a>'
        'BWW7a2sJP9tvxf}H#7EpznuGX_Tp6Y7p_->!WAk>9azbg{E24@k~BAEWt{X7!@G~Yt#e;n*d0_5U&iI<@mX97v#I7K?q92UKj%6r'
        'B=2eCyv&ow&_{265W_->D<_SPVk*pkH(bAro70<9zs2V<Tu8b1R%W#a7k@;zCjc6sieYwLf+{9JT4}*OPd%YK$-J_%lwS7n#Nrd}'
        'WKTn}p*{4#9%XeQ&7@Bi=$;pGa|WH~-1)RL1w?TrT-_NtBC})__qJ#Y8BP5fJ26~Io#(pXwm9tQMV*P+Fx%&<Mg-^5!sPMkKhslF'
        'y8@USW{W9YC}z3tN!?>zYf5&DdBg7BWP1WEFlF{w<HIovl?4ad)5p)pE|zL7v2qqM_+?gtbG!%cCPPRqA$#JuIek53{~GIrHTC3*'
        'l^RN;W$swlSmuvmcZ^$T70{KKUX}quOIRE8(`+za^rgcMq=aD<loa38zN$UzO6AcL@-874TuWCHY=ti9V~yo>WavOa?pqYQl*koP'
        'jWG}?!0LF6F#>;Yyke$1giIdr2<D_=5B3<1J*iYH16I|Ul1@O;WblY91a{bvERZpCbw!yanoEUrIW__m%SprrxD*yvji&bS<9-v1'
        ';_7hq{^pFhCO#6^ht0CvSy^3+;^WZYI>JD@NmRUd6tt#rMymlU>L!N;(J&PyIB8*z4VV*{OQww<pO>0(OgmmBGOn<|9`7dQbKpFb'
        'Nepx8uwg$OT`Jgb$l<voS8Aa%v>ovhH^TX@<vD$IxW7JJ<9?XF73rq93~7FHY8D=>-GB0svY^IU@Phk>IhPF!Zw;0SoG`{C`J{Dn'
        'zNm=9!U<C=>QRPOqBjE9m_F$8TKNPCh-An_+zHdS&j9({Mtgmm5c`Lqn`<LAc4j$B?<-BjMmH{pw}Jf2Ga#R9Z|`m#^jv*9_U1Wx'
        'yWsDf0sQ>;E1mX6yXlpm$58N{Lws~4c&3Sn!j`4y2oddZt7#`Ux{yt$p2lJHT8v46K9$2)XX*B}PG`H*^v-J-RMudy@&G(oi?7|='
        'h5q#!pf9X;Hn4eC9-Wkbn#ZPgM_J^EPv+QI|APoudwk$Ve2$U$<}CSNd9>EqB?iyh_?C1LT7!v@6gZZ_5`$dYye?hS^~2YwfReDu'
        'vILYt9zo#{(q#Kzbl#Z5-7yCUi-!bLnhg#_7;$0ZvRD?MihJU&SQq!jw_;2DAfAez$b}VJJQIT&<xN48A9+C$UxZ6(SMEcRQjt<w'
        '#CEuxI#b&ma6>^_aTG6Mp8hGB#c+NHMdAJqeSL{yY5EHkGs2Jxe5aBzv{nZd&Y1_O5@PtE8J>A+p;s%4H<4*L66Ow6Bic-KV+@x^'
        '$}zc}+)8NXL{F+}F%{e)8jDFKW!INE#1~knrRJTI`RHYuBzLTEni3|Yx-x}<KO4=mi9AD({?*?xT)Z#+qvrQx7!T|)lbR|9c9Ih}'
        'C^Mso%HkGg0p%w}-)^R>u@jj&m*zsEh!uZ@_jY(u;0-x;Nc>H^?OG{r2e0mm8^6b;&6z)3h8nv%@DMi_>I`|JFv2A*_&zP>NxotY'
        '2!D%aIM<B~Z`T?1RPrw^3tlA<3;+N'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
