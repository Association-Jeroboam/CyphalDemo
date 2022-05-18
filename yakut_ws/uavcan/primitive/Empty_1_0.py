# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/primitive/Empty.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:55.021326 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.Empty
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
class Empty_1_0:
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
    def __init__(self) -> None:
        """
        uavcan.primitive.Empty.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        """
        pass

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        assert 0 <= (_ser_.current_bit_length - _base_offset_) <= 0, \
            'Bad serialization of uavcan.primitive.Empty.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Empty_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        self = Empty_1_0(
                )
        _des_.pad_to_alignment(8)
        assert 0 <= (_des_.consumed_bit_length - _base_offset_) <= 0, \
            'Bad deserialization of uavcan.primitive.Empty.1.0'
        assert isinstance(self, Empty_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
        ])
        return f'uavcan.primitive.Empty.1.0({_o_0_})'

    _EXTENT_BYTES_ = 0

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8i?xJe0{?YVO^XyU5ba&Zopsd}5xjWNldK+k^)I-38XX5$yh)LC%IQG56Y|ka3k&W=5DFBgy!dNPX4Vf@%q3N+%FBE8@@ew@'
        '$8NP*bl;6CC{sf~uZ7Vcg)~@0V>@Sqj>vTLH2T!U<nit3kk|a^oX_}(u0k)mT)&&d(1^ZvUUxd`0qYl?izCxM4CsTlJ+~E2-(AFO'
        'p6$%4&wS2w9Yl;?%M>y2d!{>o<sio`{#of$=sY$eqT(-f2p{wc6*%i7XvK574Z$YgU@jO0Ct}MqEt}Dj>DnSISuM)xI`iH+W}39N'
        'P~UZ$>EL8^tuW8AvrP9~l14Y+ahXhc50r=kVpblQ_O?<p<ZrP|ha0)|)A~tWCdrZC6e+C;nTf|fmeCHn!AyMu$~H_@W&qM;#D~Ae'
        'FLeZi{W7+>Jzmb4ZamZR<t9JP>4gb&1*~Iw@IR0+cG6}!na`^%FPj^)1+N`?5v~7Y<sLMxHj3NFbZa4$(*5$EruMj0=gAo1$II1>'
        'FbI>7zw*(n`W9q1-)(_-wx48{+v%QXRSCqZ1XJj&$}=vv4**wA^qc=NPcq0P>z^*y=%A$n000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
