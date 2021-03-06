# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/node/Mode.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:57.273740 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.Mode
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
class Mode_1_0:
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
    OPERATIONAL:     int = 0
    INITIALIZATION:  int = 1
    MAINTENANCE:     int = 2
    SOFTWARE_UPDATE: int = 3

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.node.Mode.1.0
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
            'Bad serialization of uavcan.node.Mode.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Mode_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(3)
        self = Mode_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.node.Mode.1.0'
        assert isinstance(self, Mode_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.Mode.1.0({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jkSbg0{@j%-)kF35SHusN9@K)a4<Bb&9<~9A?_t<9{P|cMUg<rKC7~lLLn@BcYE4}yWL}VPmv0R<RJmWLJQvhznwYDb{u0$'
        '^dOCPW@o<ncD{Lg?cd&NtNHkQ)jYFV5mC#HWQF{bB?XUYs>@1S>3Hxr4xOn}R~tT_S3Det2k*jP;l5v?ik0BMRkLZzRHSsqqkZ@a'
        'ew|Lau~MrbT7K=-!afdzr9taMco+O8WzHFy)Q;Qm8j@WB<18xpm7e59c3ysiX3R0_5YtuHD<ezk<P;*dUn(mnif4W0_=KB_y=>A%'
        'I$CfwaUu+sA$iKIqa}7D?)aVIX(GH9b->p&3LUlHhf(l%sC7(b%w!)YI;s<~;#a1ur~$z>n&~w7R)EtjzuwUb@3=D%Vq5Gitgi;k'
        ';;#5s+&jszc`)pb+T;E~+};b~JHHcaQ?i2SiW}ynnh*pU1;0ucwZ1v!gU>3%Ez*C1jr9@S(~1?R)x|@9JvS`HQw#py!Un%zdK|Dx'
        'n*f*}{txR`KkkqF?Y;gV4Pb;D_Z5_FUIkMUX^B*%GJ1m0o)IVD1Uo<vhvzXoBeE=cCYj^KoUk0u2(V>bT}6OZL<`X3sb6~X8R$0m'
        '+x>XljoWdji_pIBMw4ilqyR244Z2-od6EANbLn;ocj={azkEiyn}-Lz@$c<Xm%bdnXpftcotVENR_E>wGyG95O^F7!o^X81LbD9|'
        '*9LguB+=S6Ck7)-trWyu!u0eE6ZhL6NsA`)6Oke|B5sQZ;z#jJ{3?3lx%f@&*D&}QhY3l6=qw!hEt<<2&uFEMqcRJzzfG;KP0GPh'
        'a9S}KYrlp+z*z9thp;4OLp(hO87)16F&7%Q!WWecexoz51S?+fQV0KaRVRf^so|5lz<TEbhKXA}*&=XXH7n!>3M_gOJ&tgYgF}^V'
        'Q^71?Ffb&j^r=jFI08=7F;I0;4MgXJk!B}tj5r1Zsf{`;JhuX}No{e?6v=B`Zp84ZM4?!`irm|Zr!tpmGZzsGI4J<>Pp8^CS2}=k'
        'pZ*X2%jeSVHUAI!nauq%)m8B1sw8$^CK_mhZufz<g=P+#-n2R2SgSM@68536{^pQn8T5TANX*b1*G0k1{8O)Z_;<KJSpLT*u&%3<'
        '3}LWdC(vgp6_{wS85(Q23E|NY{|4?9rkaf&*9i_?^dAN>xARd3000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
