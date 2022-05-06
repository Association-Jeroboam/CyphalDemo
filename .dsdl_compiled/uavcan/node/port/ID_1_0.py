# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/port/ID.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.203388 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.ID
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node.port


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ID_1_0:
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
    def __init__(self, *,
                 subject_id: None | uavcan.node.port.SubjectID_1_0 = None,
                 service_id: None | uavcan.node.port.ServiceID_1_0 = None) -> None:
        """
        uavcan.node.port.ID.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        If no parameters are provided, the first field will be default-initialized and selected.
        If one parameter is provided, it will be used to initialize and select the field under the same name.
        If more than one parameter is provided, a ValueError will be raised.
        :param subject_id: uavcan.node.port.SubjectID.1.0 subject_id
        :param service_id: uavcan.node.port.ServiceID.1.0 service_id
        """
        self._subject_id: None | uavcan.node.port.SubjectID_1_0 = None
        self._service_id: None | uavcan.node.port.ServiceID_1_0 = None
        _init_cnt_: int = 0

        if subject_id is not None:
            _init_cnt_ += 1
            self.subject_id = subject_id  # type: ignore

        if service_id is not None:
            _init_cnt_ += 1
            self.service_id = service_id  # type: ignore

        if _init_cnt_ == 0:
            self.subject_id = uavcan.node.port.SubjectID_1_0()  # Default initialization
        elif _init_cnt_ == 1:
            pass  # A value is already assigned, nothing to do
        else:
            raise ValueError(f'Union cannot hold values of more than one field')

    @property
    def subject_id(self) -> None | uavcan.node.port.SubjectID_1_0:
        """
        uavcan.node.port.SubjectID.1.0 subject_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, x: uavcan.node.port.SubjectID_1_0) -> None:
        if isinstance(x, uavcan.node.port.SubjectID_1_0):
            self._subject_id = x
        else:
            raise ValueError(f'subject_id: expected uavcan.node.port.SubjectID_1_0 got {type(x).__name__}')
        self._service_id = None

    @property
    def service_id(self) -> None | uavcan.node.port.ServiceID_1_0:
        """
        uavcan.node.port.ServiceID.1.0 service_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._service_id

    @service_id.setter
    def service_id(self, x: uavcan.node.port.ServiceID_1_0) -> None:
        if isinstance(x, uavcan.node.port.ServiceID_1_0):
            self._service_id = x
        else:
            raise ValueError(f'service_id: expected uavcan.node.port.ServiceID_1_0 got {type(x).__name__}')
        self._subject_id = None

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if self.subject_id is not None:  # Union tag 0
            _ser_.add_aligned_u8(0)
            _ser_.pad_to_alignment(8)
            self.subject_id._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        elif self.service_id is not None:  # Union tag 1
            _ser_.add_aligned_u8(1)
            _ser_.pad_to_alignment(8)
            self.service_id._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        else:
            raise RuntimeError('Malformed union uavcan.node.port.ID.1.0')
        _ser_.pad_to_alignment(8)
        assert 24 <= (_ser_.current_bit_length - _base_offset_) <= 24, \
            'Bad serialization of uavcan.node.port.ID.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> ID_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        _tag0_ = _des_.fetch_aligned_u8()
        if _tag0_ == 0:
            _des_.pad_to_alignment(8)
            _uni0_ = uavcan.node.port.SubjectID_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = ID_1_0(subject_id=_uni0_)
        elif _tag0_ == 1:
            _des_.pad_to_alignment(8)
            _uni1_ = uavcan.node.port.ServiceID_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = ID_1_0(service_id=_uni1_)
        else:
            raise _des_.FormatError(f'uavcan.node.port.ID.1.0: Union tag value {_tag0_} is invalid')
        _des_.pad_to_alignment(8)
        assert 24 <= (_des_.consumed_bit_length - _base_offset_) <= 24, \
            'Bad deserialization of uavcan.node.port.ID.1.0'
        assert isinstance(self, ID_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = '(MALFORMED UNION)'
        if self.subject_id is not None:
            _o_0_ = 'subject_id=%s' % self.subject_id
        if self.service_id is not None:
            _o_0_ = 'service_id=%s' % self.service_id
        return f'uavcan.node.port.ID.1.0({_o_0_})'

    _EXTENT_BYTES_ = 3

    _MODEL_: _pydsdl_.UnionType = _restore_constant(
        'ABzY8QiOG40{`unTW=gS6o5C)Z8w)TZQ4?L9cU>@FVm(?X$u8P6BWWVY1AeaNL0o%<Lq&nof*w|LKX>$K7fd1iIr*|`4JU7@&FI~'
        '0e%t3yJv6dO}uxd)o1(6IX<?}Ira}jzsiYH^QTXw^)L@3m*papJd)pWKN2nrl3JSNQVF9g>#<DYwR$Sd6EpkRd~as-FpGH&Wzz-U'
        '40!CuNhsVj$&|aaXmpuviY!MZ10_BBfZ9)tH{g|iGLMZOXI!aF`h^m?d5HF2;6>*vqla%x5rth3##qP|XUe*TvrOJsSrMor6Mc@t'
        'us-~Zi}wrvkq8ue3ZqbII|UQy2uzXQ^ov|dGg*^LZra7K$GNP=B3z1<sEVwAi^iER6^le%RbaeHbU5I-Vl{Nbz;S(WwQb0%xeF*;'
        'wj$i6(vRkz(fe7hcpUO9>@~Dq__(IwO&%5K!4M0R!03{}(cQYdki=F;b(cR44z*5tlW+=VV76spaQTxj44j2?dW4a&W9<cttuzz4'
        'J+r>$mhW+eV?1h`hk0Gu$ar8!bClnvHp=zTwYlqa#x5lH3t#Bzo)c$&y%j#zuQPBIF2jWa_bU`QZ@`rZ&9>gnHsqEFnLRNkL$jjy'
        'vOFoWK%gKJEakWxdekD4K1S&(hU?a<9eskkKX3tkfW*e=h(dC7aIh+s(PIns6nL~KYKhTD(!!5qz%o%SB0F<8s!(C16*_3i1`onI'
        'WAwgG0J(GSMb~bcQTE8D8SorE%S5bf*lfx`m~A+#uaU-iRB_foI2n(tB6sjhClnhJW61IAjzUSEia>72pt;wsJz_sXS5CJNryC16'
        'gWB0Qdg7K;cbfhCq7w*ukR_?n&WnuX^_rjHKHw6TabGaj?d*3`k#Ut|-IyL>0Z7b3c&PWR@-UQf^_h>rx6+j&ig;GvDTVo8%#1hL'
        '$bBplY0HA~%7u^XtjXATQ?|jkY-7~s3Z9BJ>J3=EQp4Lt9JCy0ctg}5rv8ZKP{SLw+|}^PB(GSGHoP&*k%l*JIo$9j==({_!G^b+'
        '^!AXwDbn9-Io0s?5vPg!i3f-WiEj`O5#J;pCLSRkB_1OlC!QcW#J7lV6HgLP5#J%6CcaCYA<h!d5YH0N5ziA{;sxSG;vDf3@iK9q'
        'c!l^L@hb5e@jCH+;s?YV#1Dxd5kDs0Y_Y)diDik$&6|YAd|O(umW}1D?6PITmNXpflyNxlvWuXVqA$M)dMaq8w}Mg)rU~6wecma!'
        'Fb`KL7vP2-yfW8QCgG;l{0shsf8g%|Zf(QD3M|5>Gw>NK!RO$?9ax4HxC^UTh1%ZtS0PwyRh*Xe|5qG%0AIHJ`wCbmrNd4OdJ?&U'
        'i42j=U#NLg5aU02ovp946`nqmqOEZ3rYObw@38mLk%3YP{&+>Wk3T=oe_PKnl2zhlVnbw(kQmXK?Q@4Rz)9NuR+VtaY&ryx<RW$y'
        'uR1cs>lzaPv%{vtH!=>LWTV-(RpOj&#m#P9)bK4B@W@$O+^J?ib-u;vW!y1?*Y_TVQ{amQ->&pl?be4f)`!#HfX#lG{TcV^6`99+'
        'F4zP3*0WEg__;T=uCy*{e2CcRbzjbwZO-<Znry!Bcba%~2~Wl9ehvSMyf44u=?b1-bL<d~9qNpAN<sgyjRE&RFE>+-bPNCh'
    )
    assert isinstance(_MODEL_, _pydsdl_.UnionType)